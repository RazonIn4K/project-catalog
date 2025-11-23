# Loom Script: AI Voice Agent Platform Demo

**Duration:** 3-4 Minutes
**Goal:** Showcase voice-agent builds, demonstrate call simulation, CRM handoff, and automation dashboards while connecting each capability to pricing tiers.

---

## 0:00 - Intro (Face)

"In this walkthrough, I'm going to show you our AI Voice Agent Platform—a complete solution I've built for clients who need intelligent phone automation. You'll see real call simulations, how leads flow into your CRM, and the dashboards that give you complete visibility. I'll also break down how each feature maps to our Starter, Standard, and Premium packages."

---

## 0:20 - Past Builds Overview (Screen: Portfolio/GitHub)

"First, let me show you some of the voice agent projects I've delivered. This architecture uses **ElevenLabs** for ultra-realistic voice synthesis—the same neural voices you hear in premium AI assistants. Combined with real-time speech recognition and GPT-4 for conversation intelligence, we get sub-second response times that feel genuinely human."

_(Action: Show ElevenLabs voice configuration panel)_

"Here's the ElevenLabs console where we configure voice personas. For a real estate client, we cloned their top agent's voice. For a healthcare intake system, we used a calm, professional preset. The voice is just the surface—underneath, we have intent detection, entity extraction, and conversation state management."

---

## 0:50 - Call Simulation Walkthrough (Screen: Live Demo)

"Now let's run a live call simulation. I'm triggering an inbound call to our demo line."

_(Action: Initiate test call via Twilio/Vonage dashboard)_

**Simulated Call Flow:**
1. **Greeting:** "Thank you for calling Apex Realty. I'm Maya, your virtual assistant. How can I help you today?"
2. **Intent Capture:** Caller says "I'm looking for a 3-bedroom in Austin under 500K"
3. **Qualification:** "Great! Are you pre-approved for financing, or would you like me to connect you with our mortgage partner?"
4. **Appointment Booking:** "I have availability Thursday at 2 PM or Friday at 10 AM. Which works better?"
5. **Handoff Trigger:** "Perfect. I'm transferring you to Sarah, one of our top agents who specializes in that area."

_(Action: Show real-time transcript appearing in dashboard)_

"Notice how every utterance is transcribed live. The AI extracts structured data—property type, budget, timeline—and stores it before the human agent ever picks up."

**Tier Connection:**
- **Starter:** Single-intent call handling (e.g., FAQ responses, basic scheduling)
- **Standard:** Multi-turn conversations with qualification logic and warm transfers
- **Premium:** Full conversation intelligence with sentiment analysis and escalation triggers

---

## 1:45 - CRM Handoff (Screen: HubSpot/Salesforce + n8n)

"Here's where the magic happens for your sales team. The moment that call ends—or even mid-call—the lead data syncs to your CRM."

_(Action: Switch to HubSpot/Salesforce contact record)_

"Look at this contact record. It was created 8 seconds after the call started. We have:
- Full transcript with timestamps
- Extracted entities: 3-bedroom, Austin, $500K budget, pre-approval status
- Lead score calculated from conversation signals
- Next action: 'Warm transfer requested to Sarah'
- Call recording linked for compliance"

_(Action: Show n8n workflow canvas)_

"Behind the scenes, this n8n workflow orchestrates everything. When a call ends, it:
1. Enriches the lead with ZoomInfo/Clearbit data
2. Creates or updates the CRM contact
3. Fires a Slack alert to the assigned agent with full context
4. Schedules follow-up sequences if no transfer occurred"

**Tier Connection:**
- **Starter ($800):** Basic CRM sync—contact creation with call transcript
- **Standard ($1,500):** Smart enrichment, lead scoring, Slack/Teams alerts, round-robin assignment
- **Premium ($3,000):** Bi-directional sync, custom field mapping, trigger-based sequences, compliance recording storage

---

## 2:30 - Automation Dashboards (Screen: Looker Studio / Metabase)

"Your voice agents are generating data 24/7. Let me show you the dashboards that turn that data into decisions."

_(Action: Navigate to main analytics dashboard)_

**Dashboard 1: Call Performance**
- "Total calls handled this week: 847"
- "Average handle time: 2 minutes 14 seconds"
- "First-call resolution rate: 73%"
- "Peak hours heatmap—you can see Tuesday 2-4 PM gets 3x volume"

_(Action: Switch to intent analytics)_

**Dashboard 2: Intent & Sentiment Analytics**
- "Top intents: Scheduling (34%), Pricing Questions (28%), Support Escalations (18%)"
- "Sentiment trend: 82% positive, 12% neutral, 6% frustrated"
- "Frustration spikes correlate with wait times over 90 seconds—actionable insight"

_(Action: Switch to conversion dashboard)_

**Dashboard 3: Conversion Funnel**
- "Calls to Qualified Leads: 62%"
- "Qualified to Appointments: 41%"
- "Appointments to Closed Deals: 18%"
- "Voice agent-assisted deals this month: $127K pipeline"

**Tier Connection:**
- **Starter:** Basic call volume metrics, simple daily reports via email
- **Standard:** Full performance dashboards, intent tracking, weekly automated reports
- **Premium:** Custom KPI dashboards, sentiment analysis, predictive insights, executive summaries

---

## 3:30 - Pricing Tier Summary (Face)

"Let me quickly summarize how these capabilities stack across our packages:"

| Feature | Starter ($800) | Standard ($1,500) | Premium ($3,000) |
|---------|----------------|-------------------|------------------|
| **Voice Engine** | ElevenLabs preset voices | Custom voice personas | Voice cloning + multilingual |
| **Call Handling** | Single-intent, FAQ-style | Multi-turn qualification | Full conversation AI |
| **CRM Integration** | Basic contact sync | Smart enrichment + Slack | Bi-directional + sequences |
| **Dashboards** | Email reports | Performance dashboards | Custom KPIs + sentiment |
| **Support** | 14 days | 30 days | 60 days + priority |

---

## 3:50 - Outro & CTA (Face)

"If you're spending hours on repetitive calls, or losing leads because your team can't answer fast enough, this platform pays for itself in the first month. Drop me a message with your use case—whether it's real estate, healthcare intake, appointment scheduling, or customer support—and I'll show you exactly how we'd configure this for your business."

"Thanks for watching. Let's build something that never sleeps."

---

## Production Notes

**Screen Recording Sequence:**
1. Portfolio/GitHub showing past voice agent repos
2. ElevenLabs voice configuration panel
3. Twilio/Vonage call dashboard (initiate test call)
4. Live transcript appearing in custom dashboard
5. HubSpot/Salesforce contact record with call data
6. n8n workflow canvas showing automation
7. Looker Studio / Metabase analytics dashboards
8. Pricing comparison table (can use Canva slide)

**B-Roll Suggestions:**
- Phone ringing animation
- Waveform visualizations during voice playback
- Data flowing into CRM (animated)
- Dashboard metrics incrementing

**Voiceover Tips:**
- Keep energy conversational, not salesy
- Pause briefly when showing new screens
- Emphasize "sub-second response" and "feels human"
- Let the dashboards speak for themselves during analytics section

---

## Related Assets

- **ElevenLabs Voice Library:** Used for neural voice synthesis
- **n8n Workflow Template:** [Voice Agent Integration](https://github.com/RazonIn4K/automation-templates/tree/main/voice-agent-crm)
- **Dashboard Template:** Looker Studio template for call analytics
- **CRM Field Mapping:** Standard schema for voice agent data sync
