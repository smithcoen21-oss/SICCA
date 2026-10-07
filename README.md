
# SICCA

## Sistema Integrado de Casos Crímenes en Archivo

### In-Depth System, Methodology and Analytical Framework

---

# 1. System Overview

**SICCA** is an offline investigative intelligence platform designed to **manage, analyse, cross-reference, and prioritise criminal cases**.

The system integrates case management with advanced analytical modules, combining:

* Bayesian probability updating
* Exponential temporal decay
* Geographic relationship analysis
* NLP-based modus operandi (MO) similarity
* Confidence scoring
* Risk assessment
* Network analysis
* Case prioritisation
* Module-specific analytical functions

SICCA is designed to provide structured, probabilistic insights that can assist investigators in identifying relationships between cases, prioritising investigative resources, detecting patterns, and identifying potential investigative gaps.

The system is intended as **decision-support technology**. It does not replace investigators, investigative judgment, evidence, or lawful investigative procedures.

---

# 2. How SICCA Works

SICCA follows a structured analytical workflow beginning with case input and ending with analytical outputs and auditable reports.

## 2.1 Case Input

Users can:

* Create cases manually
* Upload cases using CSV files
* Link cases to establish relationships between them

Each case can include:

* Case ID
* Case name
* Location
* Description
* Case type
* Links to other cases

This structure allows individual cases to be analysed independently while also allowing relationships and patterns across multiple cases to be examined.

---

# 3. Database Storage

SICCA uses an **SQLite database** to store:

* Cases
* Users
* Case relationships/links
* Analysis results
* Relevant analytical outputs

Role-based permissions are incorporated to support controlled collaboration between authorised users.

The local database architecture allows sensitive investigative information to remain within the organisation's controlled environment.

---

# 4. Analysis Engine

The SICCA analysis engine combines several analytical methods.

## 4.1 Bayesian Probability Updating

The Bayesian component combines evidence-related signals including:

* Temporal relationships
* Geographic relationships
* Modus operandi similarity

These signals are used to calculate posterior probabilities representing the estimated likelihood of a relationship between cases or investigative entities based on the information currently available.

## 4.2 Confidence Scoring

Confidence scoring adjusts the analytical result according to factors including:

* Evidence strength
* Source reliability
* Temporal relevance
* Exponential time decay

This creates a distinction between a high analytical score and the degree of confidence that should be placed in that score.

## 4.3 Risk Assessment

SICCA uses logistic mapping to convert combined analytical signals into an operational risk score.

The purpose of the risk score is **prioritisation**, rather than establishing guilt or criminal responsibility.

## 4.4 NLP-Based MO Similarity

SICCA uses offline Natural Language Processing to compare case descriptions and identify similarities in:

* Modus operandi
* Behavioural descriptions
* Scene characteristics
* Relevant terminology
* Repeated textual patterns

The current implementation uses **TF-IDF and cosine similarity**.

## 4.5 Specialized Analytical Modules

SICCA includes specialised analytical modules for:

* Terrorist Network Analysis
* Missing Person Prediction
* Cold Case Gap Analysis
* Serial Killer Profiling

---

# 5. Outputs

SICCA produces several forms of analytical output.

### Dashboard Summaries

The dashboard provides structured summaries of case information and analytical results.

### CSV Exports

Analytical results can be exported in CSV format for external reporting and further analysis.

### Audit Logs

Relevant system actions and analytical updates can be recorded in audit logs, allowing reviewers to trace how results were generated and changed.

---

# 6. What SICCA Does

SICCA is designed to:

### Quantify Case Linkages

Calculate probability and confidence indicators for potential relationships between cases.

### Map Criminal Networks

Analyse networks to identify:

* Potential leaders
* Bridge nodes
* Structural relationships
* Potential vulnerabilities

### Prioritise Missing-Person Search Areas

Analyse available information to assist in prioritising potential search locations and allocating investigative resources.

### Identify Investigative Gaps in Cold Cases

Compare historical case information with analytical patterns and methods used in subsequently solved or better-developed cases.

### Support Serial-Killer Analysis

Identify potential similarities between cases and produce offender-profile indicators based on available information.

---

# 7. Analytical Outcomes

SICCA generates several categories of analytical outcome.

## 7.1 Probabilistic Scores

Posterior probabilities representing the estimated likelihood of a case linkage based on the evidence currently supplied to the system.

## 7.2 Confidence Levels

Confidence levels adjusted according to:

* Evidence strength
* Source reliability
* Time decay
* Quality of available information

## 7.3 Risk Scores

Logistic risk values designed to assist with investigative prioritisation.

## 7.4 Module-Specific Insights

### Terrorist Networks

Identification of:

* Structural relationships
* Potential vulnerabilities
* Network bridges
* Potentially important nodes

### Missing Persons

Support for:

* Search-area prioritisation
* Resource allocation
* Ranking of potential locations

### Cold Cases

Identification of:

* Investigative gaps
* Potentially applicable methodologies
* Recommendations for renewed analysis

### Serial Killers

Identification of:

* MO similarities
* Behavioural indicators
* Geographic relationships
* Potential offender-profile characteristics

---

# 8. Reliability of Outcomes

## Strengths

### Bayesian Updating

Bayesian updating provides a structured mechanism for combining multiple evidence signals.

### Exponential Temporal Decay

Exponential decay models the declining relevance of older information and prevents historical events from automatically receiving the same weight as recent events.

### NLP MO Similarity

NLP-based similarity analysis can identify nuanced textual and behavioural overlaps within case descriptions.

## Limitations

### Offline Operation

Because SICCA operates offline, it does not automatically provide live access to:

* GIS systems
* External intelligence feeds
* Live databases
* External information sources

### NLP Methodology

The current NLP implementation uses **TF-IDF**, which is heuristic and less sophisticated than modern deep-learning embedding approaches.

### Input Data Dependency

Reliability depends significantly on the quality of the information entered into the system, including:

* Case descriptions
* Case links
* Evidence information
* Source quality
* Completeness of the available data

## Overall Assessment

SICCA is intended to be reliable for **pattern detection and investigative prioritisation**, but its outputs should be treated as **decision-support information rather than sole evidence**.

Reliability is expected to be higher when input data is rich, accurate, and well documented, and lower when case descriptions are sparse or incomplete.

---

# 9. Illustrative Test Cases

The following examples illustrate how SICCA can be applied. These are **made-up illustrative cases** and are not presented as real criminal events.

---

## 9.1 Terrorist Network Analysis

### Case A

Bombing in Madrid, 2020.

### Case B

Safe house discovered in Valencia, 2021.

### Case C

Financing operation in Barcelona, 2022.

### SICCA Outcome

Bayesian analysis establishes a strong analytical relationship between Cases A and B based on:

* Temporal overlap
* Geographic relationship

Network analysis identifies **Case B as a bridge node** connecting Cases A and C.

The analysis identifies the safe house represented by Case B as a potential structural vulnerability within the network.

### Analytical Interpretation

Disrupting the bridge node could potentially have a significant effect on the connectivity of the network.

---

# 10. Missing Person Prediction

### Case D

A missing hiker in Sierra de Guadarrama, last seen in November 2025.

### SICCA Location Predictions

| Location       | Confidence |
| -------------- | ---------: |
| Trailhead      |       0.70 |
| River crossing |       0.60 |
| Mountain ridge |       0.40 |

### Outcome

Efficiency scoring ranks the **trailhead** as the highest-priority location.

### Recommended Resource Allocation

* 6 units → Trailhead
* 3 units → River crossing
* 1 unit → Mountain ridge

The purpose of this prioritisation is to improve resource allocation and potentially increase the efficiency of the search operation.

---

# 11. Cold Case Gap Analysis

### Case E

Unsolved homicide from 1995 in which limited forensic methods were available or used at the time.

SICCA compares the case with similar solved cases from 2005–2015 in which newer investigative technologies were available.

### Identified Investigative Gaps

* Advanced DNA analysis
* DNA genealogy
* Digital trace recovery
* Digital forensics

### Recommendation

Re-examine available evidence using:

* Genetic genealogy where legally and technically appropriate
* Modern DNA techniques
* Digital-forensic methodologies
* Digital trace recovery

### Analytical Confidence

**0.70**, based on the similarity between the historical case and the subsequently solved comparison cases.

---

# 12. Serial-Killer Profiling

### Case F

Victim found in Toledo.

Characteristics:

* Strangulation
* Body posing

### Case G

Victim found in Ciudad Real.

Characteristics:

* Strangulation
* Ritualistic staging

### SICCA Analysis

**MO similarity:** 0.85

**Geographic relationship:** Both cases occur within a 100 km radius.

**Signature behaviours:** Posing and ritualistic staging detected.

### Composite Offender Profile Score

**0.92**

This produces a strong analytical indication of a potential serial-offender pattern.

Again, the output represents an analytical indicator and does not independently establish that the cases were committed by the same offender.

---

# 13. Overall SICCA Framework

SICCA provides a **structured, probabilistic, and modular framework for criminal case analysis**.

Its purpose is to enhance investigators' ability to:

* Detect patterns
* Identify potential relationships
* Allocate resources
* Prioritise leads
* Identify investigative gaps
* Examine networks
* Compare cases

SICCA does not replace investigators.

It is designed to enhance human analytical capability by providing structured decision-support information.

### Reliability

Reliability is expected to be:

**High** when input data is rich, accurate, and well structured.

**Moderate** when descriptions and available information are sparse.

The system is therefore best used as a **decision-support tool integrated into the investigative workflow**.

---

# 14. Security & Confidentiality

## Offline Architecture

SICCA's offline architecture means that the core system can operate without an internet connection.

This provides an important security advantage for sensitive investigations because case information does not need to be transmitted to external cloud services for the core analytical workflow.

### Data Containment

Sensitive case data can remain within the organisation's controlled environment.

### Chain of Custody

Evidence and case information can remain within the organisation's own infrastructure and security controls.

### Compliance Considerations

Local operation can make it easier for organisations to implement strict legal and privacy requirements, including requirements relating to:

* GDPR
* National security procedures
* Internal data-protection policies
* Investigative confidentiality

Offline operation does not itself guarantee compliance. Organisations remain responsible for implementing appropriate security, access-control, retention, and legal procedures.

---

# 15. Reliability & Availability

## No Internet Dependency

Investigators can operate SICCA in:

* Remote locations
* Secure facilities
* Restricted environments
* Situations involving network outages

## Local Availability

The system operates locally, meaning availability is primarily dependent on the organisation's own hardware and infrastructure.

## Predictable Performance

Local processing avoids dependency on:

* Internet bandwidth
* Cloud latency
* External service availability
* Cloud-server throttling

---

# 16. Control & Customisation

## Full Ownership

The organisation determines how its:

* Database
* Backups
* Maintenance
* Case-management procedures

are structured and controlled.

## Custom Algorithms

The SICCA analytical framework can be adapted, including:

* Bayesian updating
* NLP similarity
* Risk scoring

without depending on external vendor update cycles.

## Integration Freedom

The local architecture can facilitate integration with:

* Forensic tools
* GIS systems
* Secure archives
* Other locally controlled investigative systems

subject to the technical and security requirements of the deployment environment.

---

# 17. Investigator Trust

## Transparency

Analysts can inspect how analytical scores are generated through mechanisms including:

* Bayesian calculations
* Exponential temporal decay
* TF-IDF similarity

## No External Cloud Black Box

The offline architecture means the core analytical workflow does not require external cloud AI services.

The analytical process can therefore be examined within the local environment.

## Confidence in Data Provenance

Results are generated from the case information supplied to SICCA rather than automatically combining that information with unknown external sources.

This allows investigators to maintain greater control over the information being analysed.

---

# 18. Practical Example — Terrorist Network Analysis

Imagine an investigation involving a suspected terrorist network.

### Online System

An online system may rely on external services or feeds.

This can create additional considerations regarding:

* Data exposure
* Network security
* Third-party infrastructure
* Confidentiality

### Offline SICCA

SICCA can operate on locally controlled case information.

It can:

1. Apply Bayesian probability analysis.
2. Examine temporal relationships.
3. Examine geographic relationships.
4. Analyse MO similarities.
5. Map the network.
6. Identify potential vulnerabilities.
7. Produce analytical outputs without transmitting the core case data externally.

### Result

Investigators can brief their team using results generated within their controlled environment.

---

# 19. When Online Systems May Be Useful

A balanced comparison is important.

Cloud-based systems can provide advantages including:

* Real-time intelligence feeds
* Scalable computing resources
* Processing of extremely large datasets
* Easier cross-agency collaboration

These capabilities can be valuable in appropriate environments.

However, for highly sensitive investigations, including:

* Terrorism
* Organised crime
* Serial homicide

the advantages of offline operation may outweigh the convenience of cloud infrastructure where **security, control, confidentiality, and investigator trust are the primary requirements**.

---

# 20. Offline SICCA vs Online Investigative Systems

| Feature / Factor            | Offline SICCA — Local                                                                                               | Online / Cloud System                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Data Security**           | Local/air-gapped operation can minimise network exposure. Sensitive data remains within the controlled environment. | Network-connected infrastructure can introduce additional exposure to breaches or unauthorised access.            |
| **Confidentiality**         | Organisation maintains direct control over data storage and handling.                                               | Data may be stored or processed on third-party infrastructure.                                                    |
| **Reliability**             | Can operate without internet connectivity, including in secure or remote environments.                              | Dependent on internet connectivity and cloud-service availability.                                                |
| **Performance**             | Local processing provides predictable performance without internet latency or bandwidth limitations.                | Performance may be affected by network conditions, service availability, or throttling.                           |
| **Control & Customisation** | Organisation controls database structure, algorithms, workflows, and maintenance.                                   | Customisation may be constrained by the service provider.                                                         |
| **Transparency**            | Analytical components such as Bayesian scoring, exponential decay, and NLP methods can be inspected.                | Some cloud AI systems may provide less visibility into their underlying models.                                   |
| **Investigator Trust**      | Results can be generated exclusively from locally supplied data.                                                    | External services may introduce additional data sources or processing outside the investigator's environment.     |
| **Scalability**             | Limited by local hardware capacity.                                                                                 | Cloud infrastructure can scale to very large datasets.                                                            |
| **Collaboration**           | Role-based permissions can support controlled collaboration within the secure environment.                          | Cross-agency collaboration can be easier, although additional security considerations apply.                      |
| **Best Use Case**           | High-sensitivity investigations where confidentiality and local control are priorities.                             | Large-scale analytics, broad intelligence sharing, and environments where scalability is the primary requirement. |

### Summary

Offline SICCA is particularly suited to environments where:

* Confidentiality is critical
* Reliability is required without internet access
* Investigators need direct control
* Analytical transparency is important

Online systems remain useful where:

* Scalability is essential
* Real-time external intelligence is required
* Large-scale collaboration is necessary

For high-sensitivity investigations such as terrorism, organised crime, and serial-homicide analysis, an offline architecture can provide significant advantages where security and control are more important than convenience.

---

# 21. Cross-Match Probability

## How High Scores Emerge — and How to Use Them

Cross-match probability analysis examines how SICCA can assign a high analytical score to a person, case, location, or pattern that has not previously been identified as a formal suspect or established relationship.

The objective is to identify potentially meaningful intersections across:

* Time
* Geography
* Behaviour
* Modus operandi
* Case narratives

This section examines the process across three contexts:

* Terrorism
* Serial homicide
* Missing persons

A high score is an **analytical signal**, not a conclusion of guilt.

---

# 22. Probability Engine Overview

## 22.1 Bayesian Core

SICCA begins with a prior probability and updates it using evidence represented through likelihood ratios.

### Prior Odds

$$
O_{\text{prior}} =
\frac{P_{\text{prior}}}{1-P_{\text{prior}}}
$$

### Posterior Odds

$$
O_{\text{post}}
=
O_{\text{prior}}
\times
\prod_i LR_i
$$

### Posterior Probability

$$
P_{\text{post}}
=
\frac{O_{\text{post}}}
{1+O_{\text{post}}}
$$

---

# 23. Evidence Signals

SICCA converts several evidence signals into likelihood ratios.

These include:

* Temporal proximity
* Geographic proximity
* MO/behavioural similarity

The current mapping uses:

$$
LR(s)=
\frac{\varepsilon+s}
{\varepsilon+(1-s)}
$$

where:

* \(s \in [0,1]\) is the signal score
* \(\varepsilon\) is a stabilising factor

---

# 24. Confidence Layering

Posterior probability is tempered by factors including:

* Exponential time decay
* Source reliability
* Evidence reliability

The confidence calculation is represented as:

$$
C =
P_{\text{post}}
\times
e^{-\lambda t}
\times
f_{\text{source}}
\times
f_{\text{evidence}}
$$

This provides a distinction between:

**How strong the analytical linkage appears**

and

**How much confidence should be placed in that linkage.**

---

# 25. Risk Mapping

SICCA maps combined signals into an operational risk score using a logistic function:

$$
R =
\frac{1}
{1+e^{-(\alpha P_{\text{post}}
+\beta C
+\gamma E)}}
$$

The risk score is intended to support **operational prioritisation**, not to establish guilt.

---

# 26. Evidence Signals That Can Move a Non-Suspect to a Higher Score

## 26.1 Temporal Proximity

Recent and clustered events increase the temporal signal.

The mechanism is:

$$
s_{\text{temp}}
=
e^{-\lambda_{\text{temp}}\Delta t}
$$

The closer events are in time, the stronger the temporal relationship may become.

---

## 26.2 Geographic Proximity

Repeated presence, shared locations, or feasible travel corridors can increase the geographic signal.

SICCA's current offline implementation uses:

* Anchor locations
* Distance heuristics
* Soft geographic bonuses

It does not depend on live GIS data.

---

## 26.3 MO / Behavioural Similarity

Offline NLP compares case narratives using TF-IDF.

The system examines textual overlap involving:

* Modus operandi
* Scene characteristics
* Behavioural descriptions
* Relevant keywords

Similarity is calculated using the cosine similarity between TF-IDF vectors.

---

# 27. How High Posterior Probability Can Arise

High posterior probability can occur when several independent signals align consistently.

Each signal can generate a likelihood ratio above 1.

When these likelihood ratios are multiplied together, the combined odds can increase significantly.

Therefore, even where a person or entity was not previously flagged, consistent intersections across:

* Time
* Space
* Behaviour

can cause SICCA to surface that entity for investigative review.

The important principle is:

**The strength comes from convergence of signals rather than reliance on a single indicator.**

---

# 28. Interpreting a High Cross-Match Score

## Posterior Probability — \(P_{\text{post}}\)

Indicates the estimated likelihood that the candidate is linked to the relevant case set given the current evidence.

**It is not a probability of guilt.**

It represents **linkage likelihood** within the model.

## Confidence — \(C\)

Provides a reliability-adjusted view of the posterior probability.

For example:

A high \(P_{\text{post}}\) combined with a low \(C\) indicates that factors such as weak sources or temporal decay may reduce confidence in the apparent relationship.

## Risk — \(R\)

Provides an operational prioritisation measure.

A high risk score should elevate a candidate or pattern for **triage and review**, not produce an automatic conclusion.

---

# 29. Investigative Thresholds

The current SICCA framework defines the following illustrative thresholds.

## Screening Threshold

When:

$$
P_{\text{post}}\geq0.65
$$

and

$$
C\geq0.55
$$

the candidate moves to:

**Investigative Review**

## Action Threshold

When:

$$
P_{\text{post}}\geq0.80
$$

and

$$
C\geq0.65
$$

the candidate can be considered for:

* Targeted record checks
* Alibi verification
* Geofence review
* Other lawful investigative checks

These thresholds should be regarded as **methodological parameters subject to validation**, rather than universal investigative standards.

---

# 30. False Positives vs Stability

A single strong signal can cause an analytical score to increase sharply.

For that reason, SICCA should favour:

* Multi-signal convergence
* Repeated corroboration
* Stability across updated datasets
* Independent confirmation

rather than treating a single high-scoring signal as sufficient.

The objective is to reduce spurious hits and improve the stability of analytical results.

---

# 31. Worked Example — Terrorist Cross-Match

## Scenario

A previously unidentified operative is evaluated against several incidents.

### Signals

**Temporal**

Three incidents occur within seven months.

$$
s_{\text{temp}}\approx0.50
$$

**Geographic**

Presence across Madrid and Valencia anchor locations.

$$
s_{\text{geo}}=0.70
$$

**MO / NLP**

Overlap involving:

* Safe house
* Explosive precursor
* Courier

$$
s_{\text{mo}}=0.75
$$

---

## Likelihood Ratios

Using:

$$
LR(s)=
\frac{0.05+s}
{0.05+(1-s)}
$$

the illustrative values are:

$$
LR_{\text{temp}}
\approx1.00
$$

$$
LR_{\text{geo}}
\approx1.75
$$

$$
LR_{\text{mo}}
\approx2.67
$$

---

## Bayesian Update

Starting prior:

$$
P_0=0.12
$$

Prior odds:

$$
O_0=
\frac{0.12}{0.88}
\approx0.136
$$

Posterior odds:

$$
O_{\text{post}}
=
0.136
\times1.00
\times1.75
\times2.67
\approx0.635
$$

Posterior probability:

$$
P_{\text{post}}
=
\frac{0.635}{1+0.635}
\approx0.388
$$

### Confidence

Assuming:

* Strong sources
* Recent events
* \(t=1\) year
* \(\lambda=0.08\)
* Evidence factor \(E=0.65\)

then:

$$
C
\approx
0.388
\times
e^{-0.08}
\times
0.9
\times
0.65
\approx0.21
$$

### Interpretation

The posterior probability is moderate, but confidence is comparatively modest.

The appropriate response is therefore **targeted verification**, such as:

* Travel-log examination
* Associate analysis
* Other lawful verification procedures

rather than immediate escalation.

If additional MO evidence increases:

$$
s_{\text{mo}}\rightarrow0.85
$$

the posterior probability can increase significantly.

---

# 32. Worked Example — Serial-Killer Cross-Match

## Scenario

Two homicides are examined for a potential emerging pattern.

### Signals

**Temporal**

Two homicides occur five weeks apart.

$$
s_{\text{temp}}\approx0.67
$$

**Geographic**

Cases fall within a 40–90 km corridor consistent with a journey-to-crime relationship.

$$
s_{\text{geo}}=0.65
$$

**MO / NLP**

Overlap includes:

* Strangulation
* Posing
* Dump-site staging

$$
s_{\text{mo}}=0.82
$$

---

## Likelihood Ratios

$$
LR_{\text{temp}}\approx1.86
$$

$$
LR_{\text{geo}}\approx1.67
$$

$$
LR_{\text{mo}}\approx3.25
$$

---

## Bayesian Update

Using:

$$
O_0=0.136
$$

the posterior odds are:

$$
O_{\text{post}}
=
0.136
\times1.86
\times1.67
\times3.25
\approx1.37
$$

Therefore:

$$
P_{\text{post}}
=
\frac{1.37}{1+1.37}
\approx0.58
$$

### Confidence

Using:

* Recent events
* Reliable sources
* \(t=0.1\) year

the illustrative confidence becomes:

$$
C
\approx
0.58
\times
e^{-0.008}
\times
0.9
\times
0.75
\approx0.35
$$

### Interpretation

The combination of MO similarity and geographic corridor produces a substantially stronger linkage signal.

Potential next investigative steps include:

* Victimology clustering
* Vehicle checks within the relevant corridor
* Examination of dump-site access and egress points
* Additional case comparison

These remain investigative leads requiring independent verification.

---

# 33. Worked Example — Missing Person Cross-Match

## Scenario

A person of interest is evaluated in relation to a disappearance.

### Signals

**Temporal**

The disappearance occurs during the same weekend as the candidate's known presence.

$$
s_{\text{temp}}=0.60
$$

**Geographic**

The candidate's phone is recorded near the trailhead.

$$
s_{\text{geo}}=0.75
$$

**Behavioural / Narrative**

TF-IDF similarity is identified between case narratives and witness descriptions involving:

* Giving a ride
* Late-night activity
* River crossing

$$
s_{\text{mo}}=0.70
$$

---

## Likelihood Ratios

$$
LR_{\text{temp}}\approx1.50
$$

$$
LR_{\text{geo}}\approx2.38
$$

$$
LR_{\text{mo}}\approx2.33
$$

---

## Bayesian Update

Starting with:

$$
O_0=0.136
$$

the posterior odds are:

$$
O_{\text{post}}
=
0.136
\times1.50
\times2.38
\times2.33
\approx1.12
$$

Therefore:

$$
P_{\text{post}}
\approx0.53
$$

### Confidence

With:

* Mixed-quality data
* \(f_{\text{source}}=0.75\)
* Evidence factor \(E=0.60\)
* \(t=0.5\) year

the illustrative confidence is:

$$
C
\approx
0.53
\times
e^{-0.04}
\times
0.75
\times
0.60
\approx0.23
$$

### Interpretation

The result indicates a meaningful probability of linkage, but confidence remains cautious.

Potential next steps include:

* Interview scheduling
* Route reconstruction
* Resource prioritisation around the trailhead
* Verification of the candidate's movements

---

# 34. Reliability, Safeguards & Escalation

## Reliability Drivers

### Multi-Signal Convergence

Temporal, geographic, and MO alignment is generally more informative than any one signal alone.

### Recency

Exponential decay prevents older coincidences from automatically receiving excessive weight.

### Text Richness

Detailed case narratives provide more information for TF-IDF comparison and can improve discrimination between similar and unrelated cases.

---

# 35. Safeguards Against False Positives

## Minimum Corroboration Rule

Require at least **two independent signals above 0.65** before moving beyond the initial screening stage.

## Stability Checks

Recalculate the result using an updated corpus to determine whether the score persists.

## Audit Trail

Record:

* Signals
* Likelihood ratios
* Updates
* Changes in scores

This allows reviewers to trace why an analytical score increased or decreased.

---

# 36. Escalation Protocol for High-Scoring Non-Suspects

A high score should trigger **structured verification**, not an automatic conclusion.

## Tier 1 — Verification

Verify:

* Identity
* Timeline
* Presence
* Plausible benign explanations

## Tier 2 — Context

Examine, where lawful and appropriate:

* Associates
* Communications
* Vehicle/travel feasibility
* Proximity to relevant scenes

## Tier 3 — Directed Inquiries

Potential actions may include:

* Interviews
* Targeted records checks
* Surveillance

All such activity must be legally authorised and conducted according to applicable investigative procedures.

## Tier 4 — Reassessment

New information should be entered into SICCA.

The system should then recalculate:

$$
P_{\text{post}}
$$

and

$$
C
$$

If the underlying signals weaken, the candidate should be **de-escalated** accordingly.

---

# 37. Practical Takeaways

## High Probability Does Not Mean Guilt

A high probability indicates **linkage likelihood within the analytical model**.

It prioritises attention; it does not establish guilt.

## Chase Convergence, Not Spikes

A candidate who repeatedly intersects with cases across:

* Time
* Geography
* Behaviour

deserves greater analytical attention than a candidate identified through a single isolated signal.

## Use Confidence as a Brake

If confidence is significantly lower than the posterior probability, additional and better-quality information should be gathered before significant investigative escalation.

## Document Decisions

Audit logs and defined thresholds help create a consistent and defensible analytical process.

---

# 38. SICCA System Architecture

The complete SICCA workflow can be represented as follows:

```text
┌──────────────────────────────────────┐
│              USER INPUT              │
│                                      │
│  • Create Case                       │
│  • Upload CSV                        │
│  • Link Cases                        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│            CASE DATABASE             │
│                                      │
│  • Cases & Links                     │
│  • Users & Roles                     │
│  • Analysis Tables                   │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│                ANALYSIS ENGINE                  │
│                                                 │
│  Bayesian Probability Updating                  │
│  • Temporal — exponential decay                 │
│  • Geographic — distance heuristic              │
│  • MO Similarity — offline NLP / TF-IDF         │
│                                                 │
│  Specialized Modules:                           │
│  • Terrorist Network Analysis                   │
│  • Missing Person Prediction                    │
│  • Cold Case Gap Analysis                       │
│  • Serial Killer Profiling                      │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────┐
│              OUTCOMES                │
│                                      │
│  • Posterior Probabilities           │
│  • Confidence Scores                 │
│  • Risk Assessments                  │
│  • Module-Specific Insights          │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│          OUTPUTS & REPORTS           │
│                                      │
│  • Dashboard Summaries               │
│  • CSV Exports                       │
│  • Audit Logs                        │
└──────────────────────────────────────┘
```

---

# 39. Final SICCA Position

SICCA is designed as a **structured, probabilistic, modular, and locally controlled investigative intelligence platform**.

Its analytical framework combines:

**Case Management**

*

**Bayesian Probability Updating**

*

**Temporal Decay**

*

**Geographic Analysis**

*

**Offline NLP / TF-IDF MO Similarity**

*

**Risk Assessment**

*

**Confidence Scoring**

*

**Specialised Investigative Modules**

*

**Auditability**

The system's purpose is to help investigators identify patterns, examine potential case relationships, prioritise resources, identify investigative gaps, and structure complex information.

The central principle remains:

> **SICCA does not replace the investigator. It gives the investigator a structured analytical framework with which to examine complex case information.**

The quality of SICCA's conclusions ultimately depends on the quality of the underlying data, the validity of its analytical assumptions, the suitability of its models, and the professional judgment applied to its outputs.


