# Loom Script: GHL Sandbox Demo

**Goal:** Show a live, working GHL setup to prove competence in < 4 minutes.
**Time:** 3–4 minutes.

---

## 1. Hook (0:00–0:15)

**Action:** Face camera or screen share of GHL Dashboard.
**Script:**
"Hi! This is a quick walkthrough of my GoHighLevel sandbox. I want to show you exactly how I set up automations—from form submission to tagging to pipeline updates—so you can see the logic in action."

## 2. The Flow (0:15–2:45)

### Step A: The Funnel

**Action:** Show the Funnel Builder (Form → Thank You Page).
**Script:**
"Here’s a simple lead capture funnel. I’ve got a custom form here..."
_(Fill out the form with test data: 'Test Lead', 'test@example.com')_
"...and when I hit submit, it redirects instantly to the Thank You page."

### Step B: The Backend Logic

**Action:** Switch to 'Contacts' tab, search for 'Test Lead'.
**Script:**
"Now, let's look at what happened in the background.

1. **Tagging:** You can see the `new-lead` tag was applied automatically.
2. **Pipeline:** The contact was created and moved to the 'New Lead' stage in the 'Main Sales Pipeline'."

### Step C: The Workflow

**Action:** Open 'Automation' > 'Workflows' > 'New Lead Sequence'. Show 'Execution History'.
**Script:**
"Inside the workflow, you can see the trigger fired. It sent this welcome email..." _(Click to show email preview)_ "...and waited 2 minutes before the SMS step. I always check the Execution Logs to ensure nothing misfired."

### Step D: QA & Debugging (The Flex)

**Action:** Briefly show a LambdaTest tab or Requestly window (optional).
**Script:**
"I also spot-check all my pages on mobile and Safari using LambdaTest to ensure they look perfect on every device. If a webhook ever fails, I use Requestly to debug the API call directly."

## 3. Close (2:45–3:15)

**Action:** Back to camera or GHL Dashboard.
**Script:**
"This is the exact pattern I deliver: simple, testable, and extensible. We can swap in your copy and offer in under a day, and you’ll have a system that just works. Thanks for watching!"
