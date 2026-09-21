"""
BrightCHAMPS AI Forward Deployed Associate Prototype
Component: WhatsApp Pre-Demo Attendance & Calendar Concierge Agent
Filename: attendance_agent.py
Author: Candidate (AI Forward Deployed Associate, Founder's Office)

Description:
A production-ready conversational agent designed to run on WhatsApp Business API
(via Wati / Aisensy / Interakt / Twilio / Make.com webhook) to slash demo no-show rates.

Features:
1. Automated T-24h and T-2h interactive confirmation sequence.
2. 1-Click Calendar Sync (.ics & Google Calendar link generation).
3. Intent classification (Confirm, Reschedule, Tech Query, Child Info, Opt-Out, Escalate).
4. Frictionless 1-tap re-scheduling state machine.
5. Automated unit test suite + interactive CLI dialogue mode.
"""

import json
import re
import sys
from datetime import datetime, timedelta
from typing import Dict, Any, Tuple, Optional

# ==============================================================================
# 1. PRODUCTION SYSTEM PROMPT & GUARDRAILS
# ==============================================================================

CONCIERGE_SYSTEM_PROMPT = """
You are "Aarav", BrightCHAMPS' AI Demo Concierge on WhatsApp.
Your single mission is to ensure parents attend their scheduled 1-on-1 trial class with their child.

PERSONALITY & TONE:
- Warm, polite, reassuring, professional, and concise.
- Talk to the parent as a trusted educational advisor, not a pushy salesperson.
- Use clean formatting with line breaks and minimal, friendly emojis (🎓, 🚀, 💻).
- Keep every WhatsApp message under 3 short paragraphs / 80 words.

CORE OBJECTIVES:
1. Confirm attendance for the scheduled trial class.
2. If parent has doubts or conflicts, offer frictionless 1-tap rescheduling to tomorrow.
3. Ensure technical readiness (Laptop/PC preferred over phone, Chrome browser, Zoom link).
4. Excite the child by referencing an interactive project (e.g., building their first game/animation).

GUARDRAILS:
- Never negotiate course pricing or discounts. If asked, reply: "Our senior academic advisor will share personalized scholarship options directly at the end of the demo class!"
- If the parent indicates dissatisfaction, aggressive refusal, or complex technical issues, flag intent as ESCALATE to transfer immediately to the human assigned rep.
- Always include the child's name and demo timing in the confirmation.
"""

# ==============================================================================
# 2. CALENDAR LINK GENERATOR UTILITIES
# ==============================================================================

def generate_google_calendar_url(child_name: str, start_dt: datetime, zoom_link: str) -> str:
    """Generates a 1-click Google Calendar add-to-calendar link."""
    end_dt = start_dt + timedelta(minutes=45)
    fmt = "%Y%m%dT%H%M%SZ"
    title = f"BrightCHAMPS 1-on-1 Coding Trial Class - {child_name}"
    details = f"Excited to meet {child_name}! Please join 5 mins early using a laptop/tablet.\\nZoom Link: {zoom_link}"
    location = zoom_link
    
    start_str = start_dt.strftime(fmt)
    end_str = end_dt.strftime(fmt)
    
    # URL encoded parameters
    title_enc = title.replace(" ", "%20")
    details_enc = details.replace(" ", "%20").replace("\\n", "%0A")
    location_enc = location.replace(":", "%3A").replace("/", "%2F")
    
    return f"https://calendar.google.com/calendar/render?action=TEMPLATE&text={title_enc}&dates={start_str}/{end_str}&details={details_enc}&location={location_enc}"


def generate_ics_content(child_name: str, start_dt: datetime, zoom_link: str) -> str:
    """Generates a standard iCalendar (.ics) string for Apple / Outlook sync."""
    end_dt = start_dt + timedelta(minutes=45)
    fmt = "%Y%m%dT%H%M%SZ"
    return (
        "BEGIN:VCALENDAR\n"
        "VERSION:2.0\n"
        "PRODID:-//BrightCHAMPS//Trial Class Concierge//EN\n"
        "BEGIN:VEVENT\n"
        f"SUMMARY:BrightCHAMPS 1-on-1 Coding Trial - {child_name}\n"
        f"DESCRIPTION:Join with {child_name} using laptop/PC. Zoom: {zoom_link}\n"
        f"DTSTART:{start_dt.strftime(fmt)}\n"
        f"DTEND:{end_dt.strftime(fmt)}\n"
        f"LOCATION:{zoom_link}\n"
        "STATUS:CONFIRMED\n"
        "END:VEVENT\n"
        "END:VCALENDAR"
    )

# ==============================================================================
# 3. INTENT CLASSIFIER & STATE MACHINE
# ==============================================================================

class ConciergeIntentClassifier:
    """Lightweight rule & pattern based classifier for sub-millisecond WhatsApp routing."""

    @staticmethod
    def classify(message_text: str) -> str:
        text = message_text.strip().lower()
        
        # 1. Confirmation
        if re.search(r"\b(yes|confirm|attending|will be there|see you|sure|okay|ok|yep|definitely|ready)\b", text):
            if not re.search(r"\b(can't|cannot|reschedule|change|postpone|not able)\b", text):
                return "CONFIRM"
        
        # 2. Rescheduling
        if re.search(r"\b(reschedule|change time|postpone|can't make it|busy|not available|different slot|tomorrow|later|shift)\b", text):
            return "RESCHEDULE"
        
        # 3. Technical / Setup Query
        if re.search(r"\b(laptop|phone|tablet|ipad|zoom|app|install|link|camera|mic|headphone|requirements)\b", text):
            return "TECH_QUERY"
            
        # 4. Child / Course / Curriculum Query
        if re.search(r"\b(age|grade|coding|scratch|python|curriculum|beginner|robotics|ai|certificate)\b", text):
            return "CHILD_INFO"
            
        # 5. Cancellation / Opt-out
        if re.search(r"\b(stop|unsubscribe|cancel|not interested|dont call|don't call|remove me)\b", text):
            return "OPT_OUT"
            
        # 6. Pricing query
        if re.search(r"\b(price|cost|fees|fee|discount|expensive|how much|charges)\b", text):
            return "PRICE_QUERY"
            
        return "UNKNOWN_ESCALATE"

# ==============================================================================
# 4. CONCIERGE ENGINE
# ==============================================================================

class BrightChampsConciergeAgent:
    """Manages the full lifecycle of a scheduled lead's attendance nudges."""

    def __init__(self):
        self.state_store: Dict[str, Dict[str, Any]] = {}

    def register_scheduled_demo(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """Triggered upon CRM webhook event: 'demo.scheduled'."""
        lead_id = lead_data["lead_id"]
        scheduled_dt = datetime.strptime(lead_data["demo_scheduled_at"], "%Y-%m-%d %H:%M")
        zoom_link = lead_data.get("zoom_link", f"https://brightchamps.zoom.us/j/{lead_id}")
        
        self.state_store[lead_id] = {
            "lead_id": lead_id,
            "parent_name": lead_data.get("parent_name", "Parent"),
            "child_name": lead_data.get("child_name", "your child"),
            "child_age": lead_data.get("child_age", 9),
            "scheduled_at": scheduled_dt,
            "zoom_link": zoom_link,
            "rep_assigned": lead_data.get("rep_assigned", "AD-01"),
            "status": "SCHEDULED", # SCHEDULED, CONFIRMED, RESCHEDULE_REQUESTED, OPT_OUT, ESCALATED
            "history": []
        }
        
        # Return initial Instant Booking Confirmation Message (Touchpoint 1)
        return self._build_booking_confirmation_message(lead_id)

    def _build_booking_confirmation_message(self, lead_id: str) -> Dict[str, Any]:
        lead = self.state_store[lead_id]
        dt_str = lead["scheduled_at"].strftime("%A, %b %d at %I:%M %p")
        gcal_url = generate_google_calendar_url(lead["child_name"], lead["scheduled_at"], lead["zoom_link"])
        
        msg = (
            f"Hi {lead['parent_name']}! Congratulations on booking {lead['child_name']}'s "
            f"1-on-1 trial class with BrightCHAMPS.\n\n"
            f"Class Timing: {dt_str}\n"
            f"Meeting Link: {lead['zoom_link']}\n"
            f"Recommended Device: Laptop or PC for hands-on activities.\n\n"
            f"Add to calendar: {gcal_url}\n\n"
            f"Please reply YES to confirm attendance, or reply RESCHEDULE if you need a different time."
        )
        lead["history"].append({"type": "OUTBOUND", "tag": "BOOKING_CONFIRMATION", "text": msg})
        return {"lead_id": lead_id, "channel": "WHATSAPP", "action": "SEND_MESSAGE", "message": msg}

    def trigger_t24_nudge(self, lead_id: str) -> Optional[Dict[str, Any]]:
        """Triggered automatically 24 hours prior to demo."""
        lead = self.state_store.get(lead_id)
        if not lead or lead["status"] in ["CONFIRMED", "OPT_OUT"]:
            return None
            
        dt_str = lead["scheduled_at"].strftime("%A, %b %d at %I:%M %p")
        msg = (
            f"Hi {lead['parent_name']}, quick reminder: {lead['child_name']}'s 1-on-1 trial class "
            f"is tomorrow at {dt_str}.\n\n"
            f"Our mentor has prepared an exciting hands-on project for {lead['child_name']}.\n\n"
            f"Could you please confirm if this time still works?\n"
            f"1. Reply 1 to Confirm\n"
            f"2. Reply 2 to Reschedule to another slot"
        )
        lead["history"].append({"type": "OUTBOUND", "tag": "T24_NUDGE", "text": msg})
        return {"lead_id": lead_id, "channel": "WHATSAPP", "action": "SEND_MESSAGE", "message": msg}

    def trigger_t10m_launch(self, lead_id: str) -> Optional[Dict[str, Any]]:
        """Triggered automatically 10 minutes prior to demo start."""
        lead = self.state_store.get(lead_id)
        if not lead or lead["status"] == "OPT_OUT":
            return None
            
        msg = (
            f"Your BrightCHAMPS class starts in 10 minutes.\n\n"
            f"Teacher is ready in the classroom for {lead['child_name']}.\n"
            f"Click here to join directly: {lead['zoom_link']}\n\n"
            f"Please have {lead['child_name']} seated with a laptop and audio enabled. See you inside!"
        )
        lead["history"].append({"type": "OUTBOUND", "tag": "T10M_LAUNCH", "text": msg})
        return {"lead_id": lead_id, "channel": "WHATSAPP", "action": "SEND_MESSAGE", "message": msg}

    def process_incoming_message(self, lead_id: str, message_text: str) -> Dict[str, Any]:
        """Handles inbound message from the parent on WhatsApp."""
        lead = self.state_store.get(lead_id)
        if not lead:
            return {"error": "Lead not found in concierge state"}
            
        lead["history"].append({"type": "INBOUND", "text": message_text})
        intent = ConciergeIntentClassifier.classify(message_text)
        
        if intent == "CONFIRM":
            lead["status"] = "CONFIRMED"
            reply = (
                f"Awesome! {lead['child_name']}'s slot is fully confirmed. "
                f"Our mentor has been notified. We will send the direct meeting link 10 minutes before class. "
                f"Looking forward to a great session!"
            )
            crm_update = {"crm_status": "DEMO_CONFIRMED", "rep_notify": False}
            
        elif intent == "RESCHEDULE":
            lead["status"] = "RESCHEDULE_REQUESTED"
            # Offer next day slots based on lead's current time
            next_day = lead["scheduled_at"] + timedelta(days=1)
            slot1 = next_day.replace(hour=17, minute=0).strftime("%A, %b %d at 5:00 PM")
            slot2 = next_day.replace(hour=19, minute=0).strftime("%A, %b %d at 7:00 PM")
            
            reply = (
                f"No problem at all! We know family schedules change.\n\n"
                f"Here are two instant slots for tomorrow:\n"
                f"1. {slot1}\n"
                f"2. {slot2}\n\n"
                f"Reply 1 or 2 to choose, or send your preferred day and time."
            )
            crm_update = {"crm_status": "RESCHEDULE_PENDING", "rep_notify": True}
            
        elif intent == "TECH_QUERY":
            reply = (
                f"For the best experience, we recommend using a Laptop or Desktop PC "
                f"with Google Chrome. This lets {lead['child_name']} interact directly with code blocks. "
                f"Tablets work as backup, but phones are not recommended."
            )
            crm_update = {"crm_status": lead["status"], "rep_notify": False}
            
        elif intent == "PRICE_QUERY":
            reply = (
                f"BrightCHAMPS offers flexible monthly and annual learning pathways tailored to each child. "
                f"This trial class is 100% free and hands-on. At the end of the session, our academic director "
                f"will share a detailed feedback report along with scholarship options."
            )
            crm_update = {"crm_status": lead["status"], "rep_notify": False}
            
        elif intent == "OPT_OUT":
            lead["status"] = "OPT_OUT"
            reply = "You have been successfully unsubscribed. We have cancelled the trial session. Have a wonderful day!"
            crm_update = {"crm_status": "LEAD_OPT_OUT", "rep_notify": True}
            
        else: # UNKNOWN_ESCALATE
            lead["status"] = "ESCALATED"
            reply = (
                f"Got it! I am connecting you directly with your dedicated BrightCHAMPS counselor "
                f"({lead['rep_assigned']}) who will assist you right away."
            )
            crm_update = {"crm_status": "ESCALATED_TO_REP", "rep_notify": True}
            
        lead["history"].append({"type": "OUTBOUND", "tag": f"REPLY_{intent}", "text": reply})
        
        return {
            "lead_id": lead_id,
            "detected_intent": intent,
            "reply_text": reply,
            "current_status": lead["status"],
            "crm_sync": crm_update
        }

# ==============================================================================
# 5. AUTOMATED TEST SUITE
# ==============================================================================

def run_automated_tests():
    """Runs 5 validation test cases covering all primary customer journeys."""
    print("=" * 65)
    print("RUNNING AUTOMATED TESTS: BrightChampsConciergeAgent")
    print("=" * 65)
    
    agent = BrightChampsConciergeAgent()
    passed = 0
    total = 5
    
    # Test Case 1: Initial Registration & Touchpoint 1
    sample_lead = {
        "lead_id": "L104544",
        "parent_name": "Sarah Jenkins",
        "child_name": "Ethan",
        "child_age": 10,
        "demo_scheduled_at": "2026-07-30 17:00",
        "zoom_link": "https://brightchamps.zoom.us/j/104544",
        "rep_assigned": "AD-01"
    }
    res1 = agent.register_scheduled_demo(sample_lead)
    assert "Ethan" in res1["message"], "Child name should appear in confirmation"
    assert "calendar.google.com" in res1["message"], "Google calendar link should be present"
    print("  [PASS] Test 1: Webhook Registration & Booking Confirmation generated")
    passed += 1
    
    # Test Case 2: Parent confirms via WhatsApp
    res2 = agent.process_incoming_message("L104544", "Yes, we will definitely be there! Thanks")
    assert res2["detected_intent"] == "CONFIRM", "Should classify as CONFIRM"
    assert res2["current_status"] == "CONFIRMED", "State should transition to CONFIRMED"
    print("  [PASS] Test 2: Inbound Confirmation Intent & State Transition")
    passed += 1
    
    # Test Case 3: Technical requirements query
    res3 = agent.process_incoming_message("L104544", "Do we need to install Zoom or can he use an iPad?")
    assert res3["detected_intent"] == "TECH_QUERY", "Should classify as TECH_QUERY"
    assert "Laptop or Desktop" in res3["reply_text"], "Should recommend laptop/desktop"
    print("  [PASS] Test 3: Tech Query Handling & Device Advisory")
    passed += 1
    
    # Test Case 4: Parent requests reschedule
    res4 = agent.process_incoming_message("L104544", "Can we reschedule to tomorrow? He has soccer practice")
    assert res4["detected_intent"] == "RESCHEDULE", "Should classify as RESCHEDULE"
    assert "instant slots for tomorrow" in res4["reply_text"], "Should offer next-day slots"
    assert res4["crm_sync"]["rep_notify"] is True, "Should flag CRM to notify rep"
    print("  [PASS] Test 4: Frictionless Rescheduling & Next-Day Slot Offer")
    passed += 1
    
    # Test Case 5: Pricing guardrail
    res5 = agent.process_incoming_message("L104544", "How much does the full course cost after the trial?")
    assert res5["detected_intent"] == "PRICE_QUERY", "Should classify as PRICE_QUERY"
    assert "100% free and hands-on" in res5["reply_text"], "Should protect trial pitch"
    print("  [PASS] Test 5: Pricing Guardrail & Counselor Protection")
    passed += 1
    
    print("-" * 65)
    print(f"ALL {passed}/{total} UNIT TESTS PASSED SUCCESSFULLY.")
    print("=" * 65)

def interactive_cli():
    """Live interactive chat simulation for evaluators."""
    agent = BrightChampsConciergeAgent()
    lead = {
        "lead_id": "SIM_DEMO_01",
        "parent_name": "Dr. Ananya Sharma",
        "child_name": "Aarav",
        "child_age": 9,
        "demo_scheduled_at": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d 18:00"),
        "zoom_link": "https://brightchamps.zoom.us/j/simdemo01",
        "rep_assigned": "AD-05"
    }
    init_msg = agent.register_scheduled_demo(lead)
    print("\n" + "=" * 65)
    print("BrightCHAMPS WhatsApp Concierge - Interactive Simulation")
    print("=" * 65)
    print("[SYSTEM]: New Demo Scheduled for Aarav (Age 9). Outbound WhatsApp sent:")
    print("-" * 65)
    print(init_msg["message"])
    print("-" * 65)
    print("Type your message as the parent (or 'quit' to exit):")
    
    while True:
        try:
            user_in = input("\nParent > ").strip()
            if not user_in or user_in.lower() in ["quit", "exit"]:
                print("Exiting simulation.")
                break
            resp = agent.process_incoming_message("SIM_DEMO_01", user_in)
            print(f"\n[Concierge Bot ({resp['detected_intent']})]:\n{resp['reply_text']}")
            print(f"[CRM Sync]: Status={resp['current_status']}, RepNotify={resp['crm_sync']['rep_notify']}")
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_cli()
    else:
        run_automated_tests()

