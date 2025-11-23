# Case Study: Premium Product Launch Splash Page

> How we built a high-converting landing page with 3D visuals, real-time reservation system, and pixel-perfect responsive design.

---

## Project Overview

**Client:** Luxury consumer electronics brand launching a limited-edition smart speaker
**Timeline:** 4 weeks from concept to launch
**Role:** Lead Developer & Technical Architect

---

## The Goal

Create a premium digital experience that:

1. **Builds anticipation** for a limited-edition product drop
2. **Captures reservations** with a $50 refundable deposit
3. **Showcases the product** using interactive 3D visualization
4. **Performs flawlessly** across all devices and connection speeds

**Success Metrics Target:**
- 10,000+ reservations in first 48 hours
- < 2% bounce rate on mobile
- 60+ Lighthouse performance score with 3D assets loaded

---

## The Concept

We designed a "reveal experience" that guided users through three phases:

| Phase | User Experience | Technical Feature |
|-------|----------------|-------------------|
| **Teaser** | Ambient particle animation with countdown | WebGL canvas + serverless timer sync |
| **Reveal** | 3D product emerges from particles | Three.js morph animation |
| **Reserve** | Smooth scroll to deposit form | Stripe Elements + real-time inventory |

The visual language combined dark gradients, metallic accents, and kinetic typography to match the brand's premium positioning.

---

## Layout Architecture

```
┌─────────────────────────────────────────────────────────┐
│  HERO SECTION (100vh)                                   │
│  ┌─────────────────────────────────────────────────┐    │
│  │  3D Product Viewer (Three.js Canvas)            │    │
│  │  - Auto-rotate on load                          │    │
│  │  - Drag to explore                              │    │
│  │  - Scroll-triggered zoom                        │    │
│  └─────────────────────────────────────────────────┘    │
│  [ RESERVE NOW ]  ←  Sticky CTA                         │
├─────────────────────────────────────────────────────────┤
│  FEATURES SECTION                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Feature  │  │ Feature  │  │ Feature  │              │
│  │ Card 1   │  │ Card 2   │  │ Card 3   │              │
│  └──────────┘  └──────────┘  └──────────┘              │
│  (Intersection Observer fade-in animations)             │
├─────────────────────────────────────────────────────────┤
│  RESERVATION FORM                                       │
│  ┌─────────────────────────────────────────────────┐    │
│  │  Email · Color Select · Stripe Card Element     │    │
│  │  [ Complete $50 Reservation ]                   │    │
│  │  Live inventory counter: "847 of 1,000 left"    │    │
│  └─────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────┤
│  FOOTER · Social Links · Legal                          │
└─────────────────────────────────────────────────────────┘
```

---

## Tech Stack

| Layer | Technology | Why |
|-------|------------|-----|
| **Framework** | Next.js 14 (App Router) | SSR for SEO, React Server Components for performance |
| **3D Engine** | Three.js + React Three Fiber | Declarative 3D, easy integration with React state |
| **3D Assets** | glTF 2.0 + Draco compression | 85% smaller file size vs. uncompressed |
| **Styling** | Tailwind CSS + Framer Motion | Rapid iteration, physics-based animations |
| **Payments** | Stripe Elements + Webhooks | PCI-compliant deposit capture |
| **Backend** | Vercel Edge Functions | Low-latency inventory checks globally |
| **Database** | Supabase (Postgres) | Real-time subscriptions for live inventory |
| **CDN** | Cloudflare R2 | Cost-effective 3D asset delivery |
| **Analytics** | Mixpanel + Vercel Analytics | Funnel tracking + Core Web Vitals |

---

## Deep Dive: 3D Asset Pipeline

### Challenge
The client's product model was a 45MB CAD export—unusable for web.

### Solution

```
Original CAD (45MB)
       ↓
Blender Decimate (preserve edges)
       ↓
glTF Export + Draco Compression
       ↓
Optimized Model (1.2MB)
       ↓
Progressive Loading with Suspense
```

**Key Optimizations:**
- **LOD (Level of Detail):** Three mesh versions (high/med/low) swapped based on device GPU
- **Texture Atlasing:** Combined 8 PBR textures into 2 atlas sheets
- **Lazy Hydration:** 3D canvas loads after critical content via `next/dynamic`

**Result:** First Contentful Paint < 1.2s even with 3D hero on 4G connections.

---

## Deep Dive: Reservation Flow

### Architecture

```
User clicks "Reserve"
       ↓
1. Client: Validate email + color selection
       ↓
2. Edge Function: Check real-time inventory (Supabase)
       ↓
3. Client: Render Stripe Payment Element
       ↓
4. Stripe: Create PaymentIntent ($50 hold)
       ↓
5. Webhook: Decrement inventory + send confirmation
       ↓
6. Supabase Realtime: Push updated count to all clients
```

### Race Condition Handling

With 1,000 limited units and thousands of concurrent users, we implemented:

- **Optimistic Locking:** `UPDATE inventory SET count = count - 1 WHERE count > 0 RETURNING count`
- **Idempotency Keys:** Prevent duplicate charges on network retry
- **Graceful Degradation:** "Sold Out" state with waitlist fallback

### Security Measures

- Rate limiting: 10 requests/minute per IP
- Bot detection: hCaptcha on suspicious patterns
- Webhook signature verification: Stripe-Signature header validation

---

## Deep Dive: Responsive Polish

### Breakpoint Strategy

| Breakpoint | Layout Adjustments |
|------------|-------------------|
| **< 640px (Mobile)** | 3D viewer at 60% height, stacked feature cards, bottom-sheet reservation form |
| **640-1024px (Tablet)** | 2-column features, side-by-side form fields |
| **> 1024px (Desktop)** | Full 3D experience, 3-column features, inline form |

### Performance by Device

We detected GPU capability via `renderer.capabilities` and adjusted:

```javascript
const gpuTier = detectGPU();

const qualitySettings = {
  low:  { shadows: false, particles: 500,  antialias: false },
  mid:  { shadows: true,  particles: 2000, antialias: false },
  high: { shadows: true,  particles: 5000, antialias: true  }
};
```

### Touch Optimizations

- 3D rotation: Replaced drag with two-finger gesture on mobile
- CTA button: Minimum 48px tap target, haptic feedback on supported devices
- Form inputs: `inputmode="email"` and `autocomplete` for faster entry

### Accessibility

- 3D scene: `aria-label` description + static fallback image for screen readers
- Reduced motion: `prefers-reduced-motion` disables animations, shows static product shot
- Color contrast: All text passes WCAG AA against gradient backgrounds

---

## Results

| Metric | Target | Actual |
|--------|--------|--------|
| Reservations (48h) | 10,000 | **12,847** |
| Mobile Bounce Rate | < 2% | **1.3%** |
| Lighthouse Performance | 60+ | **74** (with 3D) |
| Largest Contentful Paint | < 2.5s | **1.8s** |
| Conversion Rate | — | **8.2%** (visitor → reservation) |
| Payment Failures | — | **0.4%** (retry success: 92%) |

### Qualitative Wins

- Featured in **Awwwards Honorable Mention**
- Client reported **3x social shares** vs. previous launches
- Zero downtime during peak traffic (Vercel auto-scaling)

---

## Lessons Learned

1. **Compress 3D assets early.** We wasted a week debugging "slow load" before realizing the model was 45MB.

2. **Test payments under load.** Our staging Stripe keys had lower rate limits than production—caught this 2 days before launch.

3. **Real-time inventory is worth the complexity.** Showing "23 left" created urgency that static copy couldn't match.

4. **Mobile-first 3D is possible.** With proper GPU detection and progressive enhancement, even budget Android devices handled the experience.

---

## Tech Highlights for Portfolio

```
✓ Three.js / React Three Fiber – Interactive 3D product visualization
✓ Stripe Elements + Webhooks – Secure reservation payment flow
✓ Supabase Realtime – Live inventory updates across all clients
✓ Next.js 14 App Router – Hybrid SSR/CSR for optimal performance
✓ Framer Motion – Physics-based scroll and reveal animations
✓ GPU-adaptive rendering – Quality scaling based on device capability
```

---

## Want This for Your Launch?

I specialize in high-converting product launch experiences that combine:

- **Interactive 3D visualization** (Three.js, WebGL, Spline)
- **Reservation/waitlist systems** (Stripe, Supabase, custom backends)
- **Performance-obsessed responsive design** (Core Web Vitals optimization)

[Let's discuss your launch →](#contact)
