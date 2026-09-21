# BrightCHAMPS — AI Forward Deployed Associate Case Study

> **Founder's Office Initiative**: Slashing Trial Class No-Show Rates with AI & Zero-Engineering Automation  
> **Target Metric**: Trial Demo Show Rate (Baseline: 63.80% → Target: 78.00%)  
> **Net Financial Impact**: **+₹24.12 Lakhs / month** (**₹2.89 Crores / year run-rate**; 68.9x ROI)  
> **Candidate**: Bharanee B  
> **Contact**: [+91 7708221675](tel:+917708221675) | [LinkedIn Profile](https://www.linkedin.com/in/bharanee-b-a387902b5/)

---

## ⚡ Quick Deliverables & Links

| Deliverable | Access Link | Description |
| :--- | :--- | :--- |
| 🌐 **Live Prototype** | [brightchamps-ai-solutions.onrender.com](https://brightchamps-ai-solutions.onrender.com) | Standalone interactive web app (2-way WhatsApp simulator, ROI model, CRM telemetry) |
| 🎬 **Video Walkthrough** | [Google Drive Video (2 Mins)](https://drive.google.com/file/d/1iS3d0MqnzJDR8UH8YxLr6K6lg6v23bkZ/view?usp=sharing) | 2-minute executive walkthrough of the prototype, runbook, and findings |
| 📄 **Executive Memo** | [`memo/memo.pdf`](memo/memo.pdf) | Strictly 1-page executive memorandum (Finance signed-off format) |
| 📘 **Word Memo** | [`memo/memo.docx`](memo/memo.docx) | Fully styled single-page Microsoft Word deliverable |
| 💻 **GitHub Repository** | [github.com/Totto1403/brightchamps-ai-solutions](https://github.com/Totto1403/brightchamps-ai-solutions) | Complete auditable source code, tests, and analysis engine |

---

## 📌 Executive Summary

BrightCHAMPS sells premium 1-on-1 coding and STEM learning pathways for kids aged 6–16 at an average revenue of **₹60,000 per converted student**. Because parents require high trust before purchasing, the business model hinges entirely on getting parents and children to attend a **Free 45-Minute Trial Class (Demo)** over Zoom.

Analyzing 5,000 anonymised leads across June–July 2026 revealed:
1. **The Primary Leak**: Out of 3,229 scheduled demos, 1,169 parents failed to attend (**584.5 no-shows/month; 36.20% no-show rate**).
2. **The Financial Ceiling**: At a 17.57% historical attendee conversion rate, this represents a gross theoretical pool of **₹61.62 Lakhs / month** in unrealized revenue.
3. **The Root Cause**: A **24-hour scheduling lag cliff**—leads scheduled within 24–48 hours achieve a **77.52% show rate**, but show rates collapse to **45.4%** when delayed past 48 hours.
4. **The Lever**: **Totto — The AI WhatsApp Attendance Concierge**. Deployed in 14 days with zero engineering sprints using CRM webhooks, 1-click Google/Apple Calendar (.ics) injection, interactive T-24h confirmations, and T-10m Zoom launch alerts.
5. **Recoverable Impact**: Bridges the delayed-lead gap to the internal 77.52% speed-to-lead benchmark, recovering **229.3 attendees/month** and delivering **+40.2 net paid conversions/month (₹24.12 Lakhs / month)**.

---

## 🗂 Project Structure

```
├── memo/
│   ├── memo.pdf                       # Strictly 1-Page Executive Memo (Finance Signed-Off)
│   ├── memo.docx                      # Strictly 1-Page Word Version
│   └── memo.md                        # Markdown version
├── build/
│   ├── index.html                     # Standalone Interactive Web Prototype (HTML/CSS/JS)
│   ├── attendance_agent.py            # Production Python Backend Engine (5/5 Unit Tests Passing)
│   └── RUNBOOK.md                     # Operational Runbook (Named Owners, Rep SOP, Fallbacks)
├── analysis/
│   ├── funnel_analysis.py             # Reproducible statistical engine (two-proportion z-tests)
│   └── leak_quantification_report.md   # Full audit report & TAM vs. Recoverable breakdown
├── index.html                         # Root redirect for Render cloud hosting
├── render.yaml                        # Render static site deployment configuration
└── README.md                          # Repository documentation
```

---

## 🚀 Interactive Prototype (Zero Installation)

The prototype includes a **live WhatsApp chat simulator**, a **real-time ROI & what-if financial model**, and a **CRM telemetry inspector**.

- **Option A (Live Cloud)**: Open [brightchamps-ai-solutions.onrender.com](https://brightchamps-ai-solutions.onrender.com) in any browser (runs immediately without any setup).
- **Option B (Local Offline)**: Simply double-click `build/index.html` in your file explorer to run it instantly in Chrome, Edge, Safari, or Firefox.

---

## 🧪 Automated Testing & Verification

The Python concierge backend includes an automated test suite validating all core user journeys:

```bash
# Run unit tests
python build/attendance_agent.py

# Expected Output:
# =================================================================
# RUNNING AUTOMATED TESTS: BrightChampsConciergeAgent
# =================================================================
#   [PASS] Test 1: Webhook Registration & Booking Confirmation generated
#   [PASS] Test 2: Inbound Confirmation Intent & State Transition
#   [PASS] Test 3: Tech Query Handling & Device Advisory
#   [PASS] Test 4: Frictionless Rescheduling & Next-Day Slot Offer
#   [PASS] Test 5: Pricing Guardrail & Counselor Protection
# -----------------------------------------------------------------
# ALL 5/5 UNIT TESTS PASSED SUCCESSFULLY.
```

To run the reproducible statistical funnel analysis:
```bash
python analysis/funnel_analysis.py
```

---

## 📊 Finance Reconciliation Formula

$$\Delta \text{Attendees} = N_{\text{scheduled, month}} \times \left( \text{Show Rate}_{\text{Variant}} - \text{Show Rate}_{\text{Control Baseline}} \right)$$

$$\Delta \text{Conversions} = \Delta \text{Attendees} \times 17.57\% \text{ (Historical Join-to-Paid)}$$

$$\text{Verified Revenue} = \Delta \text{Conversions} \times ₹60,000$$

- **Pre-Registered Baseline**: 63.80% Show Rate across 1,614.5 monthly scheduled leads.
- **Target Threshold**: 78.00% Show Rate (anchored to the internal 24–48h fast-scheduled benchmark of 77.52%; $p < 0.01$).
- **Net Run-Rate Contribution**: ₹24,12,000 / month against ₹35,000 / month tooling costs (**68.9x ROI**).
