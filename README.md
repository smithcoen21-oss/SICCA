
In-Depth Report on SICCA (Sistema
Integrado de Casos Crímenes en Archivo)
1. System Overview
SICCA is an offline investigative intelligence platform designed to manage, analyze, and
prioritize criminal cases. It integrates case management with advanced analytical modules,
combining Bayesian probability updating, exponential temporal decay, and NLP-based MO
similarity to deliver structured insights.
2. How It Works
1. Case Input
• Users create cases manually or upload via CSV.
• Each case includes ID, name, location, description, and type.
• Cases can be linked to show relationships.2. Database Storage
• SQLite database stores cases, users, links, and analysis outputs.
• Role-based permissions ensure secure collaboration.
3. Analysis Engine
• Bayesian Probability Updating: Combines temporal, geographic, and MO evidence
into posterior probabilities.
• Confidence Scoring: Applies exponential decay and evidence weighting.
• Risk Assessment: Logistic mapping ensures realistic escalation.
• Specialized Modules: Terrorist Networks, Missing Persons, Cold Cases, Serial
Killer Profiling.
4. Outputs
• Dashboard summaries.
• CSV exports for external reporting.
• Logs for audit trails.
3. What It Does
• Quantifies case linkages using probability and confidence.
• Maps networks to identify leaders, bridges, and vulnerabilities.
• Prioritizes search areas in missing person investigations.
• Identifies investigative gaps in cold cases.
• Profiles offenders in serial killer investigations.
4. Outcomes
• Probabilistic Scores: Posterior probabilities of case linkages.
• Confidence Levels: Adjusted for evidence strength and time decay.
• Risk Scores: Logistic risk values for prioritization.
• Module-Specific Insights:
• Terrorist networks → structural vulnerabilities.
• Missing persons → efficient resource allocation.
• Cold cases → methodological recommendations.
• Serial killers → offender profile indicators.
5. Reliability of Outcomes
• Strengths:• Bayesian updating ensures evidence is combined rationally.
• Exponential decay models time relevance realistically.
• NLP MO similarity captures nuanced behavioral overlaps.
• Limitations:
• Operates offline → no live GIS or external intelligence feeds.
• NLP is heuristic (TF-IDF) → less precise than deep learning embeddings.
• Reliability depends on quality of input data (case descriptions, links).
• Overall: Reliable for pattern detection and prioritization, but should be used as decision
support, not as sole evidence.
6. Illustrative Made-Up Cases
A. Terrorist Network Analysis
Case:
• Case A: Bombing in Madrid, 2020.
• Case B: Safe house discovered in Valencia, 2021.
• Case C: Financing operation in Barcelona, 2022.
Outcome:
• Bayesian probability links A and B strongly (temporal + geographic overlap).
• Network analysis shows Case B as a bridge node connecting A and C.
• Vulnerability: Safe house (Case B) is a weak point; dismantling it disrupts the network.
B. Missing Person Prediction
Case:
• Case D: Missing hiker in Sierra de Guadarrama, last seen November 2025.
• Location predictions: trailhead (0.7 confidence), river crossing (0.6), mountain ridge (0.4).
Outcome:
• Efficiency scores rank trailhead highest.
• Recommended resource allocation: 6 units to trailhead, 3 to river, 1 to ridge.
• Search prioritization increases likelihood of recovery.
C. Cold Case Gap Analysis
Case:
• Case E: Unsolved homicide from 1995, limited forensic methods used.
• Similar solved cases (2005–2015) used DNA genealogy and digital forensics.Outcome:
• Gap analysis identifies missing techniques: advanced DNA, digital trace recovery.
• Recommendation: Re-examine evidence with genealogy DNA and digital forensics.
• Confidence: 0.7 (based on similarity to solved cases).
D. Serial Killer Profiling
Case:
• Case F: Victim found in Toledo, strangulation, body posed.
• Case G: Victim in Ciudad Real, strangulation, ritualistic staging.
Outcome:
• MO similarity: 0.85 (high overlap).
• Geographic profiling: both within 100 km radius.
• Signature behaviors: posing, ritual detected.
• Composite offender profile score: 0.92 → strong indication of serial offender.
SICCA provides a structured, probabilistic, and modular framework for criminal case analysis.
• It does not replace investigators, but enhances their ability to detect patterns, allocate
resources, and prioritize leads.
• Reliability is high when input data is rich and accurate, moderate when descriptions are
sparse.
• The system is best used as a decision support tool integrated into investigative workflow1. Security & Confidentiality
• Offline = air-gapped: No internet connection means sensitive case data cannot leak or be
intercepted.• Chain of custody: Evidence remains entirely within the organization’s controlled
environment.
• Compliance: Easier to meet strict legal/privacy regulations (e.g., GDPR, national security
protocols).
⚡ 2. Reliability & Availability
• No dependency on internet: Investigators can work in remote areas, secure facilities, or
during outages.
• Always accessible: The system runs locally; uptime is controlled by your own hardware.
• Predictable performance: No latency or bandwidth issues from cloud servers.
🛠️ 3. Control & Customization
• Full ownership: You decide how the database is structured, backed up, and maintained.
• Custom algorithms: You can adapt Bayesian updating, NLP similarity, or risk scoring
without waiting for vendor updates.
• Integration freedom: Easier to connect with local forensic tools, GIS systems, or secure
archives.
🧠 4. Investigator Trust
• Transparency: Analysts can see exactly how probabilities are calculated (Bayesian,
exponential decay, TF-IDF).
• No “black box” cloud AI: Offline models are deterministic and auditable.
• Confidence in outcomes: Investigators know results are generated from their own data, not
mixed with external sources.
📊 5. Practical Example
Imagine you’re analyzing a terrorist cell case:
• Online system → might rely on external feeds, risking exposure of your investigation.
• Offline SICCA → runs Bayesian probability on your local case data, maps the network, and
outputs vulnerabilities without ever leaving your secure environment.
• Result: You can brief your team with confidence that nothing leaked.
⚖️ 6. When Online Might Be Useful
To be fair, cloud systems can offer:
• Real-time intelligence feeds.
• Scalable compute for massive datasets.• Easier collaboration across agencies.
But in high-sensitivity investigations (terrorism, organized crime, serial killers), the offline model
wins because security, control, and trust outweigh convenience.
📊 Offline vs Online Investigative Systems
Feature / Factor
Offline SICCA (Local)
Online / Cloud System
Data Security
Air-gapped, no internet exposure.
Sensitive data stays local.
Risk of leaks, breaches, or
unauthorized access via network.
Confidentiality
Full control, meets strict legal/privacy
requirements.
Data often stored on third-party
servers, harder to guarantee.
Reliability
Works anywhere, even in secure
facilities or remote areas.
Dependent on internet connectivity
and cloud uptime.
Performance
Predictable, no latency or bandwidth
issues.
Can suffer from lag, downtime, or
throttling.
Control &
Customization
Full ownership of database, algorithms,
and workflows.
Vendor-controlled; customization
limited.
Transparency
Algorithms are auditable (Bayesian,
exponential decay, NLP).
Often “black box” AI models with
limited visibility.
Trust by
Investigators
Results generated from your own data
only.
May mix with external feeds; trust
issues possible.
Scalability
Limited to local hardware capacity.
Cloud can scale to massive datasets.
Collaboration
Role-based permissions within secure
environment.
Easier cross-agency collaboration,
but less secure.
Best Use Case
High-sensitivity investigations
(terrorism, organized crime, serial
killers).
Broad intelligence sharing,
large-scale analytics.
• Offline SICCA is better when confidentiality, reliability, and investigator trust are
paramount.
• Online systems are useful for scalability and cross-agency collaboration, but they trade
off security and control.
• For cases like terrorism, organized crime, or serial killers, offline wins because leaks or
breaches could compromise lives and investigationsCross-match probability: how high scores emerge and how to use them
This digs into how SICCA assigns a high probability to a person or pattern that wasn’t yet a formal
suspect, and how to act on that signal across terrorism, serial homicide, and missing person
contexts.
Probability engine overview
• Bayesian core: SICCA starts with a prior probability and updates it with evidence turned
into likelihood ratios.
O_{\text{prior}}=\frac{P_{\text{prior}}}{1-P_{\text{prior}}},\quad O_{\text{post}}=O_{\
text{prior}}\cdot \prod_i \text{LR}_i,\quad P_{\text{post}}=\frac{O_{\text{post}}}{1+O_{\
text{post}}}
• Evidence signals: Temporal proximity, geographic proximity, and MO/behavioral similarity
are mapped into \text{LR}_i via a monotonic function \text{LR}(s)=\frac{\varepsilon+s}{\
varepsilon+(1-s)}, where s\in[0,1] is the signal score and \varepsilon is a stabilizer.
• Confidence layering: Posterior probability is tempered by exponential time decay and
evidence/source reliability.
C = P_{\text{post}}\cdot e^{-\lambda t}\cdot f_{\text{source}}\cdot f_{\text{evidence}}
• Risk mapping: A logistic function compresses combined signals into an operational risk
score.
R=\frac{1}{1+e^{-(\alpha P_{\text{post}}+\beta C+\gamma E)}}
Evidence signals that push a “non-suspect” to a high score
• Temporal proximity (exp. decay):
• Effect: Recent, clustered events increase s_{\text{temp}}.
• Mechanism:
s_{\text{temp}}=e^{-\lambda_{\text{temp}} \cdot \Delta t}
• Geographic proximity (heuristic distance):
• Effect: Repeated presence, shared locales, or feasible travel corridors raise s_{\
text{geo}}.
• Mechanism: Without live GIS, SICCA uses anchor-location heuristics and soft
bonuses.
• MO/behavioral similarity (offline NLP TF-IDF):
• Effect: Textual MO overlap (phrases, scene features, modus keywords) increases
s_{\text{mo}}.
• Mechanism: Cosine similarity of TF-IDF vectors between case narratives.High posterior probability arises when these signals align consistently; each converts to an LR
above 1, so their product lifts the odds. Even if the person wasn’t flagged before, consistent
intersections across time, space, and behavior can surface them.
Interpreting a high score for cross-match candidates
• Posterior probability P_{\text{post}}: Indicates how likely the candidate is linked to the
case set given current evidence. It is not guilt; it’s linkage likelihood.
• Confidence C: Reliability-adjusted view. A high P_{\text{post}} with low C warns that
time decay or weak sources might overstate the link.
• Risk R: Prioritization metric for operational attention; high R elevates triage, not
conclusions.
• Thresholds:
• Screening threshold: When P_{\text{post}} \geq 0.65 and C \geq 0.55, candidate
moves to “investigative review.”
• Action threshold: When P_{\text{post}} \geq 0.80 and C \geq 0.65, assign targeted
checks (records, alibi verification, geofence review).
• False positives vs stability: A single strong signal can spike scores; require multi-signal
convergence or repeated corroboration across cases to reduce spurious hits.
Worked examples by module
Terrorist cross-match (non-suspect operative)
• Signals:
• Temporal: Three incidents within 7 months → s_{\text{temp}} \approx 0.50
• Geographic: Presence across Madrid/Valencia anchors → s_{\text{geo}}=0.70
• MO (NLP): “safe house”, “explosive precursor”, “courier” overlap → s_{\
text{mo}}=0.75
• LRs:
\text{LR}_{\text{temp}}\approx \frac{0.05+0.50}{0.05+0.50}=1.00,\quad \text{LR}_{\
text{geo}}\approx \frac{0.05+0.70}{0.05+0.30}\approx 1.75,\quad \text{LR}_{\text{mo}}\
approx \frac{0.05+0.75}{0.05+0.25}\approx 2.67
• Bayesian update (prior P_0=0.12):
O_0=\frac{0.12}{0.88}\approx 0.136,\quad O_{\text{post}}=0.136 \times 1.00 \times 1.75 \times
2.67 \approx 0.635
P_{\text{post}}=\frac{0.635}{1+0.635}\approx 0.388
• Confidence: If sources are strong and events recent (t=1\,\text{yr},\lambda=0.08), with
evidence factor E=0.65:
C \approx 0.388 \cdot e^{-0.08} \cdot 0.9 \cdot 0.65 \approx 0.21• Interpretation: Moderate posterior but modest confidence suggests targeted verification
(travel logs, associates) before escalation. If additional MO texts increase s_{\text{mo}} to
0.85, P_{\text{post}} can exceed 0.50 rapidly.
Serial killer cross-match (emerging pattern offender)
• Signals:
• Temporal: Two homicides 5 weeks apart → s_{\text{temp}}\approx 0.67
• Geographic: 40–90 km corridor consistent with journey-to-crime → s_{\
text{geo}}=0.65
• MO (NLP): “strangulation”, “posing”, “dump site staging” → s_{\text{mo}}=0.82
• LRs:
\text{LR}_{\text{temp}}\approx \frac{0.05+0.67}{0.05+0.33}\approx 1.86,\quad \text{LR}_{\
text{geo}}\approx \frac{0.05+0.65}{0.05+0.35}\approx 1.67,\quad \text{LR}_{\text{mo}}\
approx \frac{0.05+0.82}{0.05+0.18}\approx 3.25
• Bayesian update:
O_{\text{post}}=0.136 \times 1.86 \times 1.67 \times 3.25 \approx 1.37,\quad P_{\text{post}}=\
frac{1.37}{1+1.37}\approx 0.58
• Confidence: With recent events and reliable sources (t=0.1\,\text{yr}):
C \approx 0.58 \cdot e^{-0.008} \cdot 0.9 \cdot 0.75 \approx 0.35
• Interpretation: The pattern (MO + corridor) pushes a non-suspect to high linkage
likelihood; next steps include victimology clustering, vehicle checks in the corridor, and
surveillance on dump-site egress points.
Missing person cross-match (person of interest tied to disappearance)
• Signals:
• Temporal: Missing event aligns with candidate’s known presence (same weekend)
→ s_{\text{temp}}=0.60
• Geographic: Candidate’s phone last ping near trailhead → s_{\text{geo}}=0.75
• Behavioral/Narrative: TF-IDF similarity with witness notes (“gave ride”, “late
night”, “river crossing”) → s_{\text{mo}}=0.70
• LRs:
\text{LR}_{\text{temp}}\approx 1.50,\quad \text{LR}_{\text{geo}}\approx 2.38,\quad \
text{LR}_{\text{mo}}\approx 2.33
• Bayesian update:
O_{\text{post}}=0.136 \times 1.50 \times 2.38 \times 2.33 \approx 1.12,\quad P_{\text{post}}\
approx 0.53
• Confidence: If data is mixed quality (f_{\text{source}}=0.75, E=0.60, t=0.5\,\text{yr}):C \approx 0.53 \cdot e^{-0.04} \cdot 0.75 \cdot 0.60 \approx 0.23
• Interpretation: Solid probability of linkage but cautious confidence; proceed with interview
scheduling, route reconstruction, and resource prioritization near the trailhead.
Reliability, safeguards, and escalation
• Reliability drivers:
• Multi-signal convergence: Temporal + geographic + MO alignment is stronger than
any one alone.
• Recency: Exponential decay avoids over-weighting old coincidences.
• Text richness: Detailed narratives improve TF-IDF discrimination and reduce false
matches.
• Safeguards against false positives:
• Minimum corroboration rule: Require at least two independent signals above 0.65
to move past screening.
• Stability checks: Recompute with updated corpus to confirm score persistence.
• Audit trail: Every update logs signals and LRs; reviewers can trace why a score
rose.
• Escalation protocol when a non-suspect scores high:
• Tier 1 — Verification: Identity, timeline, presence, benign explanations.
• Tier 2 — Context: Associates, communications, vehicle/travel feasibility, proximity
to scenes.
• Tier 3 — Directed inquiries: Interviews, targeted records, surveillance (as legally
appropriate).
• Tier 4 — Reassessment: Recalculate P_{\text{post}} and C with new information;
de-escalate if signals fall.
Practical takeaways
• High probability ≠ guilt: It signals linkage likelihood and prioritizes attention; pair with
human judgment and lawful procedures.
• Chase convergence, not spikes: A candidate consistently near cases in time, space, and
behavior deserves review more than one-off hits.
• Use confidence as a brake: If confidence lags, gather better sources before heavy action.
• Document decisions: The audit log and thresholds help ensure consistent, defensible
casework. ┌─────────────────────────────┐
│ User Input │
│ • Create Case │
│ • Upload CSV │
│ • Link Cases │
└───────────────┬─────────────┘
│
▼
┌─────────────────────────────┐
│ Case Database │
│ • Cases & Links │
│ • Users & Roles │
│ • Analysis Tables │
└───────────────┬─────────────┘
│
▼
┌───────────────────────────────────────────────┐
│ Analysis Engine │
│ │
│ Bayesian Probability Updating │
│ • Temporal (exponential decay) │
│ • Geographic (distance heuristic) │
│ • MO Similarity (offline NLP TF-IDF) │
│ │
│ Specialized Modules: │
│ • Terrorist Network Analysis │
│ • Missing Person Prediction │
│ • Cold Case Gap Analysis │
│ • Serial Killer Profiling │
└───────────────┬───────────────────────────────┘
│
▼
┌─────────────────────────────┐
│ Outcomes │
│ • Posterior Probabilities │
│ • Confidence Scores │ │ • Risk Assessments │
│ • Module-specific insights │
└───────────────┬─────────────┘
│
▼
┌─────────────────────────────┐
│ Outputs & Reports │
│ • Dashboard Summaries │
│ • CSV Exports │
│ • Audit Logs │
└─────────────────────────────┘

