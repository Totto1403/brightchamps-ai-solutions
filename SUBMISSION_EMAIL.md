# Submission Email Draft for Manya Agarwal (Talent Acquisition, BrightCHAMPS)

**To:** Manya Agarwal (`manya.agarwal@brightchamps.com`)  
**Subject:** Re: AI Forward Deployed Associate — Take-Home Case Submission — Bharanee  
**Attachments:** 
1. `BrightCHAMPS_Submission/memo/memo.pdf` (One-page Executive Memo)
2. `BrightCHAMPS_Submission/build/index.html` (Interactive Zero-Install Prototype Application)
3. `BrightCHAMPS_Submission/build/RUNBOOK.md` (Operational Runbook)

---

### Email Body:

Hi Manya,

Thank you for the opportunity. Please find my complete submission for the **AI Forward Deployed Associate (Founder's Office)** take-home case below.

- 🌐 **Live Interactive Prototype (Cloud)**: [Paste your Render URL here]
- 📹 **Interactive Video Walkthrough (2 Mins)**: [Paste your Google Drive link here - make sure access is set to 'Anyone with the link can view']
- 🐙 **GitHub Repository**: [Paste your GitHub repo URL here]

As requested, I have focused on commercial judgment, statistical quantification, rapid two-week deployability, and concrete adoption mechanics. 

---

### 1. The Four Deliverables Summary

1. **The Leak**:
   - The funnel loses the most money at **Demo Scheduled → Demo Joined (The Pre-Demo No-Show Drop)**.
   - Out of 3,229 scheduled demos across the 2 months, 1,169 parents failed to attend (**584.5 no-shows/month; 36.20% no-show rate**).
   - At a 17.57% historical demo-to-paid conversion rate and ₹60,000 revenue per customer, each attending lead has an expected value of ₹10,544.
   - **Theoretical Maximum Pool (TAM of Leak)**: **₹61,62,786 / month (~₹61.62 Lakhs/mo or ₹7.40 Cr/year)**.
   - *Root Cause & Empirical Grounding*: Sizing requires distinguishing the theoretical ceiling from recoverable cash. Data reveals a **24-hour lag cliff**: leads scheduled within 24–48 hours **already achieve a 77.52% show rate** in this dataset, whereas leads delayed >48h collapse to **45.4%** show rate. Bringing delayed leads up to the internal 24–48h benchmark recovers **229.3 attendees/month**.

2. **The Lever**:
   - **Chosen Lever: The AI WhatsApp Pre-Demo Attendance & Calendar Concierge ("Aarav")**.
   - A 2-way WhatsApp agent triggered on booking via CRM webhook. Automatically delivers instant 1-click Google/Apple Calendar (.ics) holds, interactive T-24h/T-2h attendance confirmation buttons ("Confirm Spot" / "Reschedule to Tomorrow"), and a T-10m direct Zoom launch ping with laptop device checklist.
   - **Sized Recoverable Impact**: **+₹24,12,000 / month incremental revenue (₹2.89 Cr / year run-rate)** from +40.2 net conversions/mo at ₹35,000/mo tooling cost (**68.9x ROI**).
   - *Why chosen over rejected alternatives*:
     - *Rejected 1 (Outbound AI Voice Calling Bot)*: High consumer friction (>60% drop/hangup) and severe TCPA/DND regulatory compliance risks in US/UK.
     - *Rejected 2 (Timezone Routing Alone)*: Two-proportion $z$-tests prove *only the USA effect is statistically significant* ($z = 2.65, p = 0.008$, unlocking ₹11.31L/mo); other cells are sample noise. Even on `US_SHIFT`, US no-show is 30.4%. We deploy the USA routing rule on Day 1 as an operational quick-win, but focus the primary build on attendance.
     - *Rejected 3 (Post-Demo Pitch AI Copilot)*: Long coaching cycle (>6 weeks), subjective adoption, and leaves empty Zoom rooms unaddressed.

3. **The Build (Verified & Runs Instantly With Zero Installation)**:
   - **Interactive Browser Web App**: Open [`build/index.html`](file:///e:/Testing%20Ground/BrightCHAMPS/BrightCHAMPS_Submission/build/index.html) in any browser (Chrome/Edge/Safari). It contains a **live 2-way WhatsApp simulator**, a **real-time ROI & what-if financial model**, and a **lead telemetry inspector**.
   - **Production Python Engine**: [`build/attendance_agent.py`](file:///e:/Testing%20Ground/BrightCHAMPS/BrightCHAMPS_Submission/build/attendance_agent.py) features the complete production system prompt, intent classifier, calendar generator, and state machine (**all 5 automated unit tests executed and passing**).
   - **Operational Runbook**: [`build/RUNBOOK.md`](file:///e:/Testing%20Ground/BrightCHAMPS/BrightCHAMPS_Submission/build/RUNBOOK.md) outlines named owners (Inside Sales Ops Lead), a 14-day rollout schedule, rep morning SOPs, failure fallbacks, and the Finance sign-off formula.

4. **The Memo**:
   - Attached as **`memo.pdf`** (strictly 1 page, concise, finance signed-off format).
   - **The Rupee Number**: **₹24,12,000 / month incremental revenue** (₹2.89 Cr annual run-rate) by closing the no-show gap to the empirical 77.52% benchmark.
   - **Biggest Adoption Risk & Mitigation**: Rep workflow bypass (reps double-calling confirmed parents) and parent spam fatigue. Mitigated via bi-directional CRM status flags (`CONFIRMED` = green/no-call), child-personalized project teaser content, and instant "STOP" opt-out triggers.
   - **Measurement & Pre-Registered Baseline**: 14-day 50/50 randomized A/B test. Baseline registered at **63.80% Show Rate** across 1,614.5 scheduled demos/mo. Primary target: **$\ge$ 78.00% Show Rate** ($p < 0.01$).

---

### 2. Disclosure of AI Tools Used

In accordance with your instructions, here are the AI tools used and their specific applications:
1. **Google Antigravity / Gemini 3.8 Flash**:
   - Used for exploratory multi-variate hypothesis generation, evaluating trade-offs, and drafting initial copy for WhatsApp message templates and runbooks.
2. **Python 3.14 (Standard Library Data Engine)**:
   - Used to execute deterministic computations, calculate the 24-hour scheduling lag cliff, run two-proportion $z$-tests for geographic routing, size the financial leaks, and execute automated unit tests.
3. **Chromium Headless**:
   - Used to compile the pixel-perfect, single-page executive memorandum from HTML/CSS into A4 PDF format.

---

### 3. Submission Links & Files
- **Live Cloud Prototype (Render)**: [Paste your Render URL here]
- **Video Walkthrough (Google Drive)**: [Paste your Google Drive link here]
- **GitHub Repository**: [Paste your GitHub repo URL here]
- **One-Page Memo (PDF)**: Attached to this email (`memo.pdf`).
- **Interactive Build**: Attached as `index.html` (runs locally with zero install).
- **Code & Analysis Repository**: All reproducible Python scripts, raw data parsers, and runbooks are organized in the attached submission directory.

Looking forward to discussing this and moving numbers together at BrightCHAMPS!

Warm regards,  
**Bharanee**  
Candidate — AI Forward Deployed Associate  
Phone: +91-XXXXXXXXXX  
LinkedIn / Portfolio: [Your Link]
