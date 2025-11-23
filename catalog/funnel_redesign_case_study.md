---
title: "Long-Form Funnel Redesign: B2B Coaching Program"
category: Funnel Optimization / CRO
date: 2024-11-23
summary: "Complete sales funnel overhaul that increased conversion rates by 340% and reduced cost-per-acquisition by 62% for a B2B executive coaching program."
thumbnail: ../assets/screenshots/funnel-redesign.png
---

> A deep-dive case study on transforming an underperforming 7-page sales funnel into a high-converting system using data-driven redesign, A/B testing, and strategic automation.

---

## The Client

**Business:** Executive coaching program for mid-level managers transitioning to C-suite roles
**Offer:** $4,997 12-week intensive coaching program
**Traffic Source:** LinkedIn Ads + Organic content
**Monthly Ad Spend:** $8,000

---

## The Problem: Before State

The client had an existing funnel that was "leaking" prospects at every stage. Despite consistent traffic, conversions were disappointing and CAC was unsustainable.

### Original Funnel Structure

```
LinkedIn Ad → Landing Page → VSL (45 min) → Application Form →
Booking Page → Sales Call → Checkout
```

### Before Metrics (Baseline - 90 Days)

| Metric | Value | Industry Benchmark |
|--------|-------|-------------------|
| Landing Page Conversion | 12% | 25-35% |
| VSL Completion Rate | 8% | 25-40% |
| Application Submission | 18% of VSL viewers | 40-50% |
| Call Booking Rate | 35% of applicants | 60-70% |
| Sales Call Show Rate | 52% | 75-85% |
| Close Rate | 15% | 25-35% |
| **Overall Funnel Conversion** | **0.04%** | 0.3-0.5% |
| **Cost Per Acquisition** | **$4,200** | $1,500-2,500 |
| **ROAS** | **1.19x** | 3-5x |

### Identified Problems

1. **Landing Page Issues**
   - 6.2s page load time (mobile)
   - No social proof above the fold
   - Generic headline ("Transform Your Leadership")
   - Single CTA buried below the fold
   - No exit intent capture

2. **VSL Drop-Off Analysis**
   - 45-minute video with no engagement hooks
   - No chapter markers or skip options
   - Static thumbnail, no animation
   - 73% dropped off within first 3 minutes

3. **Application Friction**
   - 18-field application form
   - No progress indicator
   - Required LinkedIn URL (caused abandonment)
   - No conditional logic

4. **Booking/Show Rate Issues**
   - Generic Calendly page with no pre-frame
   - Single reminder email (24hr before)
   - No SMS confirmation
   - No pre-call video or materials

---

## The Solution: Redesign Strategy

### Phase 1: Landing Page Overhaul (Week 1-2)

**Technical Optimizations:**
- Migrated from WordPress to Webflow (1.8s load time)
- Implemented lazy loading for images
- Compressed hero video to WebM format
- Added CDN (Cloudflare) for global delivery

**Conversion Optimizations:**
- Rewrote headline using PAS framework: "Stuck in Middle Management? The C-Suite Playbook That Helped 127 Directors Get Promoted in 90 Days"
- Added video testimonial carousel above fold
- Implemented sticky CTA bar on scroll
- Added exit-intent popup with micro-commitment ("Get the Free Promotion Roadmap")
- Social proof ticker: "Sarah J. from Microsoft just registered"

### Phase 2: VSL Restructuring (Week 2-3)

**Before:** Single 45-minute video
**After:** Segmented experience with engagement gates

```
┌─────────────────────────────────────────────────────────────────┐
│                    NEW VSL STRUCTURE                            │
├─────────────────────────────────────────────────────────────────┤
│  Hook Video (90 sec) → "Want to see how?" micro-CTA            │
│            ↓                                                    │
│  Problem Agitation (4 min) → Quiz: "Which barrier is yours?"   │
│            ↓                                                    │
│  Solution Framework (8 min) → Personalized based on quiz       │
│            ↓                                                    │
│  Case Studies (6 min) → Industry-matched testimonials          │
│            ↓                                                    │
│  Offer + CTA (3 min) → "Apply Now" with urgency element        │
└─────────────────────────────────────────────────────────────────┘

Total: ~22 minutes (segmented) vs 45 minutes (monolithic)
```

**Engagement Features Added:**
- Wistia player with chapter markers
- "Click to reveal" bonus content gates
- Real-time viewer count display
- Personalized video CTAs based on quiz responses

### Phase 3: Application Form Redesign (Week 3)

**Before:** 18 fields, single page
**After:** 6-step conditional flow with progress bar

| Step | Fields | Purpose |
|------|--------|---------|
| 1 | Current role + company size | Qualification |
| 2 | Biggest challenge (multiple choice) | Segmentation |
| 3 | Timeline for promotion goal | Urgency scoring |
| 4 | Investment readiness (scale) | Lead scoring |
| 5 | Name + Email + Phone | Contact capture |
| 6 | Preferred call time (embedded calendar) | Immediate booking |

**Key Changes:**
- Removed LinkedIn URL requirement (optional on step 5)
- Added "Why we ask" tooltips for sensitive questions
- Progress bar with encouraging micro-copy
- Conditional skip logic (qualified leads skip step 4)

### Phase 4: Booking & Show Rate Optimization (Week 4)

**New Confirmation Sequence:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    SHOW RATE SYSTEM                             │
├─────────────────────────────────────────────────────────────────┤
│  Booking Confirmed                                              │
│      ↓                                                          │
│  Immediate: SMS + Email confirmation with calendar invite       │
│      ↓                                                          │
│  +2 hours: "Prep Video" email (3-min video from coach)         │
│      ↓                                                          │
│  +24 hours: Case study PDF delivery                            │
│      ↓                                                          │
│  -24 hours: Email reminder + "Reply to confirm"                │
│      ↓                                                          │
│  -2 hours: SMS reminder with Zoom link                         │
│      ↓                                                          │
│  -15 minutes: Final SMS "We're ready for you!"                 │
│      ↓                                                          │
│  No-show: Immediate voicemail drop + rebooking sequence        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tools & Tech Stack

| Category | Tool | Purpose |
|----------|------|---------|
| **Landing Page** | Webflow | Page builder + hosting |
| **Video Hosting** | Wistia | VSL with analytics + CTAs |
| **Forms** | Typeform | Multi-step application |
| **Scheduling** | SavvyCal | Booking with pre-frame page |
| **Automation** | n8n (self-hosted) | Workflow orchestration |
| **SMS** | Twilio | Confirmation + reminders |
| **Email** | ConvertKit | Sequences + broadcasts |
| **Analytics** | Mixpanel + GA4 | Funnel tracking + attribution |
| **Heatmaps** | Hotjar | UX analysis + recordings |
| **A/B Testing** | VWO | Landing page variants |
| **CRM** | HubSpot | Pipeline + lead scoring |
| **Payments** | Stripe + ThriveCart | Checkout + payment plans |

---

## Results: After State (90 Days Post-Launch)

### After Metrics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Landing Page Conversion | 12% | 38% | **+217%** |
| VSL Completion Rate | 8% | 34% | **+325%** |
| Application Submission | 18% | 52% | **+189%** |
| Call Booking Rate | 35% | 78% | **+123%** |
| Sales Call Show Rate | 52% | 89% | **+71%** |
| Close Rate | 15% | 28% | **+87%** |
| **Overall Funnel Conversion** | 0.04% | 0.18% | **+340%** |
| **Cost Per Acquisition** | $4,200 | $1,580 | **-62%** |
| **ROAS** | 1.19x | 3.16x | **+166%** |

### Revenue Impact

| Period | Revenue | Ad Spend | Net Profit |
|--------|---------|----------|------------|
| Before (90 days) | $59,964 | $24,000 | $35,964 |
| After (90 days) | $149,910 | $24,000 | $125,910 |
| **Improvement** | **+$89,946** | — | **+$89,946** |

### Funnel Visualization: Before vs After

```
BEFORE FUNNEL (Per 1,000 visitors)
═══════════════════════════════════════════════════════════════
Landing Page    ████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░  120 (12%)
VSL Complete    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   10 (8%)
Application     ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    2 (18%)
Booked Call     █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    1 (35%)
Showed Up       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    0.5 (52%)
Closed          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    0.08 (15%)

AFTER FUNNEL (Per 1,000 visitors)
═══════════════════════════════════════════════════════════════
Landing Page    ███████████████████████████████████████░  380 (38%)
VSL Complete    █████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░  129 (34%)
Application     ███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   67 (52%)
Booked Call     █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   52 (78%)
Showed Up       ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   46 (89%)
Closed          █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   13 (28%)
```

---

## Key Learnings

### What Moved the Needle Most

1. **Page Speed** (+8% conversion from load time alone)
   - Mobile users converted 3x better after optimization

2. **VSL Segmentation** (+26% completion rate)
   - Interactive elements prevented passive viewing drop-off

3. **SMS Reminders** (+37% show rate improvement)
   - The -15 minute "We're ready!" text had 94% open rate

4. **Conditional Form Logic** (+34% completion)
   - Removing friction for qualified leads accelerated booking

5. **Social Proof Placement** (+12% landing page conversion)
   - Video testimonials outperformed text by 3:1

### What Didn't Work

- Exit-intent popup on mobile (caused UX issues, removed)
- Chatbot on application page (distracted from form completion)
- Calendar embed on landing page (too early in funnel, reduced VSL views)

---

## Screenshots & Documentation

### Landing Page Before/After
- **Before:** [Screenshot - Original WordPress page](../assets/screenshots/funnel-before-landing.png)
- **After:** [Screenshot - Redesigned Webflow page](../assets/screenshots/funnel-after-landing.png)

### Funnel Flow Diagram
- [Miro Board - Complete Funnel Architecture](../assets/screenshots/funnel-flow-diagram.png)

### Analytics Dashboard
- [Mixpanel Funnel View](../assets/screenshots/funnel-analytics-dashboard.png)

### Video Walkthrough
- [Loom: Full Funnel Teardown (12 min)](https://loom.com/share/funnel-redesign-walkthrough) *(placeholder)*

---

## Implementation Packages

| Package | Timeline | Includes | Investment |
|---------|----------|----------|------------|
| **Audit Only** | 3 days | Full funnel audit + Loom walkthrough + Prioritized recommendations doc | $750 |
| **Landing Page Redesign** | 7 days | New landing page (Webflow/Framer) + A/B test setup + Speed optimization + Analytics integration | $2,000 |
| **Full Funnel Overhaul** | 3 weeks | Complete redesign: Landing + VSL strategy + Application flow + Booking system + Email/SMS sequences + 30-day optimization | $5,500 |
| **Funnel + Ongoing CRO** | 3 weeks + monthly | Full overhaul + Monthly A/B testing + Conversion optimization + Reporting dashboard | $5,500 + $1,500/mo |

---

## Talking Points for Sales Calls

- "We turned a 1.19x ROAS into 3.16x without increasing ad spend - pure funnel optimization"
- "The biggest win was the VSL restructure - completion rate jumped from 8% to 34% by making it interactive"
- "Show rates went from 52% to 89% with a proper reminder sequence - that's free money on existing leads"
- "Most funnels don't have a traffic problem, they have a conversion problem at each stage"
- "We document everything in Notion so you own the playbook after we're done"

---

## Loom Script Outline

1. **Hook (30 sec):** Show the before/after revenue numbers side by side
2. **Problem overview (1 min):** Walk through original funnel metrics, highlight the "leaks"
3. **Landing page tour (2 min):** Before screenshot → After live page, point out specific changes
4. **VSL demo (2 min):** Show segmented video flow, quiz integration, personalized paths
5. **Application walkthrough (1 min):** Multi-step form with conditional logic in action
6. **Booking system (1 min):** SavvyCal pre-frame page + SMS/email reminder sequence in n8n
7. **Results dashboard (2 min):** Mixpanel funnel view, show the conversion lift at each stage
8. **ROI calculation (1 min):** $89K additional revenue from same ad spend
9. **CTA (30 sec):** "Want me to audit your funnel? Book a free 15-minute review"

---

*Case Study v1.0 | B2B High-Ticket Funnel Redesign | November 2024*
