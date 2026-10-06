# SICCA v2.0

Secure Bayesian + Machine Learning case analysis.
Rewritten to address every issue in `Critical issues.txt`.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export SICCA_ADMIN_USER=admin
export SICCA_ADMIN_PASS='choose-a-strong-password'

python sicca_app.py
# open http://127.0.0.1:5000
