"""
Render the SICCA source tree into a single PDF (for hand-off / audit).
Requires wkhtmltopdf on PATH. Falls back to HTML if unavailable.

Usage:
    python scripts/make_pdf.py
"""
import html
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "SICCA_v2_report.pdf"

SKIP_DIRS = {"__pycache__", ".git", "sicca_data", "static"}
SKIP_EXTS = {".db", ".key", ".log", ".joblib", ".pyc", ".pdf"}


def collect_files() -> list[Path]:
    out = []
    for p in sorted(ROOT.rglob("*")):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.is_file() and p.suffix not in SKIP_EXTS:
            out.append(p)
    return out


def build_html() -> str:
    parts = [
        "<!DOCTYPE html><html><head><meta charset='utf-8'>",
        "<style>",
        "body{font-family:DejaVu Sans,sans-serif;font-size:11px;margin:24px}",
        "h1,h2{color:#1d4ed8}",
        "pre{background:#0f172a;color:#e2e8f0;padding:12px;border-radius:6px;",
        "white-space:pre-wrap;word-wrap:break-word;font-size:9px;line-height:1.35}",
        "</style></head><body>",
        "<h1>SICCA v2.0 - Source Report</h1>",
        f"<p>Generated: {html.escape(datetime.utcnow().isoformat())}</p>",
    ]
    for f in collect_files():
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = f.relative_to(ROOT)
        parts.append(f"<h2>{html.escape(str(rel))}</h2>")
        parts.append(f"<pre>{html.escape(text)}</pre>")
    parts.append("</body></html>")
    return "".join(parts)


def main() -> int:
    doc = build_html()
    if shutil.which("wkhtmltopdf") is None:
        fallback = OUT.with_suffix(".html")
        fallback.write_text(doc, encoding="utf-8")
        print(f"wkhtmltopdf not found; wrote HTML instead: {fallback}")
        return 1
    try:
        import pdfkit
        pdfkit.from_string(doc, str(OUT), options={"quiet": None})
        print(f"Wrote {OUT}")
        return 0
    except Exception as exc:
        fallback = OUT.with_suffix(".html")
        fallback.write_text(doc, encoding="utf-8")
        print(f"pdfkit failed ({exc}); wrote HTML instead: {fallback}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
