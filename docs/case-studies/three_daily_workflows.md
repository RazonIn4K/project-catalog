# Three Automations I Use Daily to Run My One-Person Business

> How I save ~10 hours a week using n8n, Python, and ActiveCampaign.

Running a solo consultancy (or freelancing on Upwork) means you wear every hat: Sales, Marketing, Engineering, and Support. If you don't automate the boring stuff, you'll drown in admin work instead of billing hours.

Here are the three exact workflows I built to keep my sanity—and how you can build them too.

---

## 1. The "Instant Context" Lead Triage (n8n + GPT-4)

**The Problem:**
I used to get a "New Lead" email from my website form, read it, check their website, and then manually copy their details into Notion. If I was coding, I'd ignore it for hours.

**The Fix:**
I built an n8n workflow that triggers instantly when a form is submitted.

1. **Triggers** on new Google Sheet row (from the form).
2. **Scrapes** the lead's website (if provided) to see what they actually do.
3. **Asks GPT-4** to summarize their request and assign a "Priority Score" (1-5).
4. **Slacks me** only if Priority > 3. Otherwise, it just logs it to Notion.

**Result:**
I only get interrupted for high-value leads. Low-quality spam is silently filed away.

---

## 2. The "High-Speed" Data Fetcher (Python Async)

**The Problem:**
I often need to enrich data—like looking up 500 companies on an API or checking court records for a client. Doing this manually is impossible. Writing a simple Python script takes too long because APIs have rate limits (e.g., "60 requests per minute").

**The Fix:**
I wrote a reusable **Async Python Client** with a "Token Bucket" rate limiter.

- I feed it a CSV of 1,000 IDs.
- It fires off requests exactly at the API's limit (e.g., 99 req/min).
- It handles retries automatically if the server hiccups.

**Result:**
What used to be an overnight job now finishes in 10 minutes while I grab coffee.

---

## 3. The "Nurture Machine" (ActiveCampaign + Make)

**The Problem:**
Following up is where deals die. I'd have a great call, promise to send a proposal, and then forget to follow up 3 days later.

**The Fix:**
I set up a "Pipeline Automation" in ActiveCampaign.

- When I drag a deal to "Proposal Sent", it starts a timer.
- If I haven't moved it to "Won" or "Lost" in 3 days, it drafts a polite "Any questions?" email for me.
- It also pushes the deal value to a Google Sheet so I have a live "Forecast Dashboard" without doing any math.

**Result:**
My close rate went up ~20% simply because I stopped ghosting my own leads.

---

## Want to build these?

I've open-sourced the templates for the **n8n Lead Triage** and the **Python API Client**.
[Link to GitHub / Portfolio]
