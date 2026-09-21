# BrightCHAMPS — AI Forward Deployed Associate Case Study

> **Founder's Office Initiative**: Slashing Trial Class No-Show Rates with AI & Zero-Engineering Automation  
> **Target Metric**: Trial Demo Show Rate (Baseline: 63.80% → Target: 78.00%)  
> **Net Financial Impact**: **+₹24.12 Lakhs / month** (**₹2.89 Crores / year run-rate**; 68.9x ROI)  
> **Candidate**: Bharanee

---

## 📌 Executive Summary

BrightCHAMPS sells premium 1-on-1 coding and STEM learning pathways for kids aged 6–16 at an average revenue of **₹60,000 per converted student**. Because parents require high trust before purchasing, the business model hinges entirely on getting parents and children to attend a **Free 45-Minute Trial Class (Demo)** over Zoom.

Analyzing 5,000 anonymised leads across June–July 2026 revealed:
1. **The Primary Leak**: Out of 3,229 scheduled demos, 1,169 parents failed to attend (**584.5 no-shows/month; 36.20% no-show rate**).
2. **The Financial Ceiling**: At a 17.57% historical attendee conversion rate, this represents a gross theoretical pool of **₹61.62 Lakhs / month** in unrealized revenue.
3. **The Root Cause**: A **24-hour scheduling lag cliff**—leads scheduled within 24–48 hours achieve a **77.52% show rate**, but show rates collapse to **45.4%** when delayed past 48 hours.
4. **The Lever**: **Aarav — The AI WhatsApp Attendance Concierge**. Deployed in 14 days with zero engineering sprints using CRM webhooks, 1-click Google/Apple Calendar (.ics) injection, interactive T-24h confirmations, and T-10m Zoom launch alerts.
5. **Recoverable Impact**: Bridges the delayed-lead gap to the internal 77.52% speed-to-lead benchmark, recovering **229.3 attendees/month** and delivering **+40.2 net paid conversions/month (₹24.12 Lakhs / month)**.

---

## 🗂 Project Structure

```
├── memo/
│   ├── memo.pdf                       # Strictly 1-Page Executive Memo (Finance Signed-Off)
│   ├── memo.html                      # Source HTML template for PDF compilation
│   └── memo.md                        # Markdown version
├── build/
│   ├── index.html                     # Standalone Interactive Web Prototype
│   ├── attendance_agent.py            # Production Python Backend Engine (5/5 Unit Tests)
│   └── RUNBOOK.md                     # Operational Runbook (Named Owners, SOP, Fallbacks)
├── analysis/
│   ├── funnel_analysis.py             # Statistical analysis script (z-tests, p-values)
│   └── leak_quantification_report.md   # Full audit report
├── index.html                         # Root redirect for Render hosting
├── render.yaml                        # Render static site deployment config
├── SUBMISSION_EMAIL.md                # Ready-to-send response to Talent Acquisition
└── README.md                          # Repository documentation
```

---

## 🚀 Live Demo & Interactive Prototype

The prototype includes a **live WhatsApp chat simulator**, a **real-time ROI & what-if financial model**, and a **CRM telemetry inspector**.

### Option A: Open Locally (Zero Installation)
Simply double-click `build/index.html` in your file explorer to run it instantly in Chrome, Edge, Safari, or Firefox.

### Option B: Deploy to Render in 60 Seconds
1. Push this repository to GitHub.
2. In [Render Dashboard](https://dashboard.render.com/), click **New +** → **Static Site**.
3. Connect this repository. Render will automatically detect `render.yaml`.
4. Click **Deploy**. Your live prototype will be accessible at `https://<your-app>.onrender.com`.

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

- **Pre-Registered Baseline**: 63.80% Show Rate (584.5 monthly no-shows).
- **Target Threshold**: 78.00% Show Rate (anchored to the internal 24–48h fast-scheduled benchmark of 77.52%; $p < 0.01$).

