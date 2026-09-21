# Operational Runbook: AI WhatsApp Pre-Demo Attendance Concierge

**Project**: BrightCHAMPS 1-on-1 Trial Attendance & No-Show Reduction  
**Target Metric**: Demo Show Rate (Baseline: 63.80% → Target: 78.00%)  
**Financial Impact**: +₹24.12 Lakhs / month (+₹2.89 Cr / year)  
**Named Owners**:
- **Business & Operational Owner**: Lead, Inside Sales Operations (`salesops.lead@brightchamps.com`)
- **Technical & AI Systems Owner**: AI Forward Deployed Associate, Founder's Office (`fda.ai@brightchamps.com`)
- **Frontline Rep Champions**: US Shift Lead (`us.shiftlead@brightchamps.com`) & IST Shift Lead (`ist.shiftlead@brightchamps.com`)
- **Finance Sign-Off Authority**: VP Finance / Head of FP&A (`finance@brightchamps.com`)

---

## 1. System Architecture (Zero-Engineering Stack)

The entire solution runs without a single software engineering sprint, leveraging existing B2C EdTech infrastructure:

```
[ CRM: LeadSquared / HubSpot / Salesforce ]
                    │
                    ▼ (Webhook: 'demo.scheduled')
          [ Make.com / n8n / Zapier ]
                    │
                    ▼
     [ Wati / Aisensy / Interakt WABA ]
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
 [Parent WhatsApp]     [Concierge Agent]
  (Interactive           (attendance_agent.py)
   Templates &            - State Machine
   Calendar Sync)         - Intent Classifier
        │                       │
        └───────────┬───────────┘
                    ▼
          [ CRM Status Update ]
       (CONFIRMED / RESCHEDULE)
```

---

## 2. 14-Day Zero-Engineering Rollout Schedule

### Phase 1: Configuration & Prerequisite (Days 1 to 3)
- **Day 1 (Operational Prerequisite)**: Deploy the **CRM Timezone-Shift Routing Rule** in LeadSquared/HubSpot:
  - America/New_York → US_SHIFT reps (`AD-01` to `AD-04`, `AD-12`)
  - Asia/Ho_Chi_Minh, Asia/Singapore, Australia/Sydney → SEA_SHIFT reps (`AD-10`, `AD-11`)
  - Asia/Riyadh, Asia/Dubai, Europe/London, Asia/Kolkata → IST_SHIFT reps (`AD-05` to `AD-09`)
- **Day 2**: Submit Meta WhatsApp Business Manager templates (Booking Confirmation, T-24h Nudge, T-10m Direct Link).
- **Day 3**: Configure CRM Webhook on `status == 'DEMO_SCHEDULED'` in Make.com / n8n pointing to WhatsApp sender.

### Phase 2: Pilot & Rep Shadowing (Days 4 to 7)
- **Days 4–5**: Route 10% of new US scheduled leads to Aarav Concierge. Shadow 3 reps live.
- **Days 6–7**: Rep training in 15-minute morning standup. Show reps where WhatsApp responses appear in CRM contact record.

### Phase 3: Randomized 50/50 A/B Test (Days 8 to 11)
- **Days 8–11**: Modulo split by `lead_id` (Even IDs: Concierge Agent; Odd IDs: Existing manual rep dial baseline).
- Daily automated telemetry in Google Sheets comparing Demo Join Rate between Control and Variant.

### Phase 4: Full 100% Rollout & Handoff (Days 12 to 14)
- **Day 12**: Review interim A/B results with VP Sales & Finance.
- **Day 13**: Switch router to 100% of scheduled demos across all 8 geographies.
- **Day 14**: Formal operational handoff to Inside Sales Operations Lead.

---

## 3. Daily Rep Standard Operating Procedure (SOP)

Every Academic Counselor / Sales Rep follows this 3-step morning checklist:

1. **Check CRM View: "Today's Demos - Attendance Status"**:
   - 🟢 **CONFIRMED** (Parent tapped Yes or confirmed on WhatsApp):
     - *Rep Action*: Do not cold call to confirm! Your slot is solid. Prepare child's tailored project 10 mins prior.
   - 🟡 **RESCHEDULE_PENDING** (Parent tapped Reschedule):
     - *Rep Action*: Open WhatsApp chat thread. Check parent's preferred time. Confirm new slot in 1 click or dial parent warmly within 15 minutes.
   - ⚪ **UNCONFIRMED** (No reply to T-24h nudge):
     - *Rep Action*: Priority dial 2 hours before demo with phone script: *"Hi [Parent], Aarav sent you Ethan's project link on WhatsApp—just making sure your laptop is all set for 5 PM!"*
   - 🔴 **CANCELLED / OPT_OUT**:
     - *Rep Action*: Do not call. Teacher calendar slot automatically freed up for reallocation.

---

## 4. Failure Modes & Fallback Runbook

| Failure Event | Detection Trigger | Fallback Protocol | SLA |
| :--- | :--- | :--- | :--- |
| **WhatsApp API Outage** | 3 consecutive webhook HTTP 5xx errors | Auto-failover to Twilio SMS with identical 1-click Google Calendar URL and Zoom link. | < 2 minutes |
| **Non-English Response** | Language detection != 'en' (e.g. Arabic, Vietnamese) | Auto-tag lead as `ESCALATE_LANGUAGE` and route immediately to native-language counselor on duty. | < 5 minutes |
| **Angry Parent / Opt-Out** | Inbound keywords: `stop`, `dont call`, `harassment` | Agent sends instant polite unsubscribe confirmation. CRM tags `DO_NOT_CONTACT`. Rep dialing disabled. | Instant (0s) |
| **Double Booking Conflict** | Calendar slot already taken in reschedule request | Agent offers next two available slots in parent's timezone and pings rep slack channel `#sales-hot-rebook`. | < 30 seconds |

---

## 5. Weekly Finance Reconciliation Protocol

To ensure Finance signs off on the ₹ number without debate, verified monthly impact is calculated using this locked formula:

$$\Delta \text{Attendees} = N_{\text{scheduled, month}} \times \left( \text{Show Rate}_{\text{Variant}} - \text{Show Rate}_{\text{Control Baseline}} \right)$$
$$\Delta \text{Conversions} = \Delta \text{Attendees} \times P(\text{Convert} \mid \text{Joined})_{\text{Historical 17.57\%}}$$
$$\text{Verified Incremental Revenue} = \Delta \text{Conversions} \times ₹60,000$$

- **Audit Trail**: Every conversion tagged with `lead_id` and attribution flag `whatsapp_attended_y`.
- **Review Cadence**: Every Monday at 10:00 AM between AI Solutions Associate, Sales Ops Lead, and FP&A Manager.

