# Lawpronation-Style Survey CSS for GoHighLevel

A professional, conversion-optimized survey design with smooth transitions, clean typography, and responsive layout.

---

## Quick Start

Copy the CSS below and inject it into your GHL survey builder using the **Custom CSS** field or **Code Injection** settings.

---

## Complete CSS Snippet

```css
/* ============================================
   LAWPRONATION-STYLE SURVEY CSS FOR GHL
   Professional Legal Survey Design System
   ============================================ */

/* === FONT IMPORTS === */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

/* === ROOT VARIABLES === */
:root {
  /* Primary Colors - Professional Legal Theme */
  --lp-primary: #1e3a5f;
  --lp-primary-dark: #0f2744;
  --lp-primary-light: #2d5a8a;
  --lp-accent: #c9a227;
  --lp-accent-hover: #ddb82f;

  /* Neutral Colors */
  --lp-white: #ffffff;
  --lp-off-white: #f8f9fa;
  --lp-light-gray: #e9ecef;
  --lp-medium-gray: #6c757d;
  --lp-dark-gray: #343a40;
  --lp-black: #212529;

  /* Feedback Colors */
  --lp-success: #28a745;
  --lp-error: #dc3545;

  /* Typography */
  --lp-font-primary: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --lp-font-display: 'Playfair Display', Georgia, serif;

  /* Spacing */
  --lp-spacing-xs: 0.5rem;
  --lp-spacing-sm: 1rem;
  --lp-spacing-md: 1.5rem;
  --lp-spacing-lg: 2rem;
  --lp-spacing-xl: 3rem;

  /* Transitions */
  --lp-transition-fast: 150ms ease;
  --lp-transition-normal: 250ms ease;
  --lp-transition-slow: 400ms cubic-bezier(0.4, 0, 0.2, 1);

  /* Shadows */
  --lp-shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
  --lp-shadow-md: 0 4px 12px rgba(0,0,0,0.1);
  --lp-shadow-lg: 0 8px 30px rgba(0,0,0,0.12);
  --lp-shadow-hover: 0 12px 40px rgba(30,58,95,0.15);

  /* Border Radius */
  --lp-radius-sm: 6px;
  --lp-radius-md: 10px;
  --lp-radius-lg: 16px;
}

/* === SURVEY CONTAINER === */
.survey-container,
.hl-form-container,
[class*="survey-wrapper"] {
  font-family: var(--lp-font-primary) !important;
  background: linear-gradient(135deg, var(--lp-off-white) 0%, var(--lp-white) 100%) !important;
  max-width: 720px !important;
  margin: 0 auto !important;
  padding: var(--lp-spacing-xl) var(--lp-spacing-lg) !important;
  border-radius: var(--lp-radius-lg) !important;
  box-shadow: var(--lp-shadow-lg) !important;
}

/* === SURVEY HEADER/TITLE === */
.survey-title,
.hl-form-title,
h1[class*="survey"],
.survey-header h1 {
  font-family: var(--lp-font-display) !important;
  font-size: clamp(1.75rem, 4vw, 2.5rem) !important;
  font-weight: 700 !important;
  color: var(--lp-primary) !important;
  text-align: center !important;
  margin-bottom: var(--lp-spacing-sm) !important;
  line-height: 1.2 !important;
  letter-spacing: -0.02em !important;
}

/* === SUBTITLE/DESCRIPTION === */
.survey-subtitle,
.survey-description,
.hl-form-subtitle {
  font-size: 1.1rem !important;
  color: var(--lp-medium-gray) !important;
  text-align: center !important;
  margin-bottom: var(--lp-spacing-lg) !important;
  line-height: 1.6 !important;
  max-width: 540px !important;
  margin-left: auto !important;
  margin-right: auto !important;
}

/* === PROGRESS BAR === */
.survey-progress,
.hl-progress-bar,
[class*="progress-container"] {
  background: var(--lp-light-gray) !important;
  height: 8px !important;
  border-radius: 100px !important;
  overflow: hidden !important;
  margin-bottom: var(--lp-spacing-lg) !important;
}

.survey-progress-fill,
.hl-progress-fill,
[class*="progress-bar-fill"] {
  background: linear-gradient(90deg, var(--lp-primary) 0%, var(--lp-primary-light) 100%) !important;
  height: 100% !important;
  border-radius: 100px !important;
  transition: width var(--lp-transition-slow) !important;
}

/* Progress Percentage Text */
.progress-text,
[class*="progress-percent"] {
  font-size: 0.875rem !important;
  font-weight: 600 !important;
  color: var(--lp-primary) !important;
  text-align: right !important;
  margin-top: var(--lp-spacing-xs) !important;
}

/* === QUESTION STYLING === */
.survey-question,
.hl-form-question,
[class*="question-container"] {
  margin-bottom: var(--lp-spacing-lg) !important;
  animation: fadeInUp 0.4s ease forwards !important;
}

.question-text,
.hl-question-text,
label[class*="question"] {
  font-size: 1.125rem !important;
  font-weight: 600 !important;
  color: var(--lp-dark-gray) !important;
  margin-bottom: var(--lp-spacing-sm) !important;
  display: block !important;
  line-height: 1.5 !important;
}

/* Question Number Badge */
.question-number {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 28px !important;
  height: 28px !important;
  background: var(--lp-primary) !important;
  color: var(--lp-white) !important;
  font-size: 0.875rem !important;
  font-weight: 600 !important;
  border-radius: 50% !important;
  margin-right: var(--lp-spacing-xs) !important;
}

/* === INPUT FIELDS === */
input[type="text"],
input[type="email"],
input[type="tel"],
input[type="number"],
input[type="url"],
textarea,
.hl-input,
[class*="survey-input"] {
  width: 100% !important;
  padding: 14px 18px !important;
  font-family: var(--lp-font-primary) !important;
  font-size: 1rem !important;
  color: var(--lp-dark-gray) !important;
  background: var(--lp-white) !important;
  border: 2px solid var(--lp-light-gray) !important;
  border-radius: var(--lp-radius-md) !important;
  transition: all var(--lp-transition-normal) !important;
  outline: none !important;
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="tel"]:focus,
input[type="number"]:focus,
input[type="url"]:focus,
textarea:focus,
.hl-input:focus {
  border-color: var(--lp-primary) !important;
  box-shadow: 0 0 0 4px rgba(30, 58, 95, 0.1) !important;
  transform: translateY(-1px) !important;
}

textarea {
  min-height: 120px !important;
  resize: vertical !important;
}

/* Placeholder Styling */
::placeholder {
  color: var(--lp-medium-gray) !important;
  opacity: 0.7 !important;
}

/* === RADIO & CHECKBOX OPTIONS === */
.survey-option,
.hl-option,
[class*="radio-option"],
[class*="checkbox-option"] {
  display: flex !important;
  align-items: center !important;
  padding: 16px 20px !important;
  margin-bottom: 12px !important;
  background: var(--lp-white) !important;
  border: 2px solid var(--lp-light-gray) !important;
  border-radius: var(--lp-radius-md) !important;
  cursor: pointer !important;
  transition: all var(--lp-transition-normal) !important;
  position: relative !important;
}

.survey-option:hover,
.hl-option:hover,
[class*="radio-option"]:hover,
[class*="checkbox-option"]:hover {
  border-color: var(--lp-primary-light) !important;
  background: rgba(30, 58, 95, 0.02) !important;
  transform: translateX(4px) !important;
  box-shadow: var(--lp-shadow-sm) !important;
}

/* Selected State */
.survey-option.selected,
.survey-option.active,
.hl-option.selected,
input[type="radio"]:checked + label,
input[type="checkbox"]:checked + label,
[class*="option-selected"] {
  border-color: var(--lp-primary) !important;
  background: rgba(30, 58, 95, 0.05) !important;
  box-shadow: var(--lp-shadow-md) !important;
}

/* Custom Radio Button */
input[type="radio"],
input[type="checkbox"] {
  appearance: none !important;
  -webkit-appearance: none !important;
  width: 22px !important;
  height: 22px !important;
  border: 2px solid var(--lp-medium-gray) !important;
  border-radius: 50% !important;
  margin-right: 14px !important;
  flex-shrink: 0 !important;
  transition: all var(--lp-transition-fast) !important;
  position: relative !important;
}

input[type="checkbox"] {
  border-radius: 6px !important;
}

input[type="radio"]:checked,
input[type="checkbox"]:checked {
  border-color: var(--lp-primary) !important;
  background: var(--lp-primary) !important;
}

input[type="radio"]:checked::after {
  content: '' !important;
  position: absolute !important;
  top: 50% !important;
  left: 50% !important;
  width: 8px !important;
  height: 8px !important;
  background: var(--lp-white) !important;
  border-radius: 50% !important;
  transform: translate(-50%, -50%) !important;
}

input[type="checkbox"]:checked::after {
  content: '✓' !important;
  position: absolute !important;
  top: 50% !important;
  left: 50% !important;
  transform: translate(-50%, -50%) !important;
  color: var(--lp-white) !important;
  font-size: 14px !important;
  font-weight: 700 !important;
}

/* === DROPDOWN/SELECT === */
select,
.hl-select,
[class*="survey-select"] {
  width: 100% !important;
  padding: 14px 18px !important;
  font-family: var(--lp-font-primary) !important;
  font-size: 1rem !important;
  color: var(--lp-dark-gray) !important;
  background: var(--lp-white) !important;
  border: 2px solid var(--lp-light-gray) !important;
  border-radius: var(--lp-radius-md) !important;
  cursor: pointer !important;
  transition: all var(--lp-transition-normal) !important;
  appearance: none !important;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%236c757d' d='M6 8L1 3h10z'/%3E%3C/svg%3E") !important;
  background-repeat: no-repeat !important;
  background-position: right 16px center !important;
  padding-right: 44px !important;
}

select:focus {
  border-color: var(--lp-primary) !important;
  box-shadow: 0 0 0 4px rgba(30, 58, 95, 0.1) !important;
}

/* === BUTTONS === */
.survey-button,
.hl-btn,
button[type="submit"],
[class*="next-btn"],
[class*="submit-btn"] {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 16px 40px !important;
  font-family: var(--lp-font-primary) !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
  color: var(--lp-white) !important;
  background: linear-gradient(135deg, var(--lp-primary) 0%, var(--lp-primary-dark) 100%) !important;
  border: none !important;
  border-radius: var(--lp-radius-md) !important;
  cursor: pointer !important;
  transition: all var(--lp-transition-normal) !important;
  box-shadow: var(--lp-shadow-md) !important;
  text-transform: none !important;
  letter-spacing: 0.02em !important;
  min-width: 180px !important;
}

.survey-button:hover,
.hl-btn:hover,
button[type="submit"]:hover {
  background: linear-gradient(135deg, var(--lp-primary-light) 0%, var(--lp-primary) 100%) !important;
  transform: translateY(-2px) !important;
  box-shadow: var(--lp-shadow-hover) !important;
}

.survey-button:active,
.hl-btn:active,
button[type="submit"]:active {
  transform: translateY(0) !important;
  box-shadow: var(--lp-shadow-sm) !important;
}

/* Secondary/Back Button */
.back-btn,
[class*="prev-btn"],
.survey-button-secondary {
  background: transparent !important;
  color: var(--lp-primary) !important;
  border: 2px solid var(--lp-primary) !important;
  box-shadow: none !important;
}

.back-btn:hover,
[class*="prev-btn"]:hover,
.survey-button-secondary:hover {
  background: var(--lp-primary) !important;
  color: var(--lp-white) !important;
}

/* CTA Accent Button (for final submit) */
.survey-button-accent,
[class*="cta-btn"] {
  background: linear-gradient(135deg, var(--lp-accent) 0%, var(--lp-accent-hover) 100%) !important;
  color: var(--lp-black) !important;
}

/* Button Container */
.button-container,
[class*="button-wrapper"],
.survey-navigation {
  display: flex !important;
  justify-content: space-between !important;
  gap: var(--lp-spacing-sm) !important;
  margin-top: var(--lp-spacing-lg) !important;
  padding-top: var(--lp-spacing-lg) !important;
  border-top: 1px solid var(--lp-light-gray) !important;
}

/* === STEP INDICATOR === */
.step-indicator,
[class*="step-dots"] {
  display: flex !important;
  justify-content: center !important;
  gap: 10px !important;
  margin-bottom: var(--lp-spacing-lg) !important;
}

.step-dot {
  width: 12px !important;
  height: 12px !important;
  border-radius: 50% !important;
  background: var(--lp-light-gray) !important;
  transition: all var(--lp-transition-normal) !important;
}

.step-dot.active,
.step-dot.current {
  background: var(--lp-primary) !important;
  transform: scale(1.2) !important;
}

.step-dot.completed {
  background: var(--lp-success) !important;
}

/* === ANIMATIONS === */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% {
    box-shadow: 0 0 0 0 rgba(30, 58, 95, 0.4);
  }
  50% {
    box-shadow: 0 0 0 10px rgba(30, 58, 95, 0);
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Animate questions on load */
.survey-question:nth-child(1) { animation-delay: 0ms !important; }
.survey-question:nth-child(2) { animation-delay: 100ms !important; }
.survey-question:nth-child(3) { animation-delay: 200ms !important; }
.survey-question:nth-child(4) { animation-delay: 300ms !important; }

/* === VALIDATION STATES === */
.input-error,
.hl-input-error,
[class*="has-error"] input,
[class*="has-error"] textarea {
  border-color: var(--lp-error) !important;
  box-shadow: 0 0 0 4px rgba(220, 53, 69, 0.1) !important;
}

.error-message,
.hl-error-text,
[class*="error-msg"] {
  color: var(--lp-error) !important;
  font-size: 0.875rem !important;
  margin-top: var(--lp-spacing-xs) !important;
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
}

.error-message::before {
  content: '⚠' !important;
}

.input-success,
[class*="has-success"] input {
  border-color: var(--lp-success) !important;
}

/* === THANK YOU / COMPLETION SCREEN === */
.survey-complete,
.thank-you-screen,
[class*="completion-screen"] {
  text-align: center !important;
  padding: var(--lp-spacing-xl) !important;
  animation: fadeInUp 0.5s ease forwards !important;
}

.survey-complete h2,
.thank-you-screen h2 {
  font-family: var(--lp-font-display) !important;
  font-size: 2rem !important;
  color: var(--lp-primary) !important;
  margin-bottom: var(--lp-spacing-sm) !important;
}

.survey-complete .checkmark {
  width: 80px !important;
  height: 80px !important;
  background: var(--lp-success) !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: 0 auto var(--lp-spacing-md) !important;
  animation: pulse 2s infinite !important;
}

.survey-complete .checkmark::after {
  content: '✓' !important;
  color: var(--lp-white) !important;
  font-size: 40px !important;
  font-weight: 700 !important;
}

/* === RESPONSIVE DESIGN === */

/* Tablet */
@media (max-width: 768px) {
  .survey-container,
  .hl-form-container {
    padding: var(--lp-spacing-lg) var(--lp-spacing-md) !important;
    margin: var(--lp-spacing-sm) !important;
    border-radius: var(--lp-radius-md) !important;
  }

  .survey-title,
  .hl-form-title {
    font-size: 1.75rem !important;
  }

  .question-text,
  .hl-question-text {
    font-size: 1rem !important;
  }

  .survey-button,
  .hl-btn {
    width: 100% !important;
    padding: 14px 24px !important;
  }

  .button-container,
  .survey-navigation {
    flex-direction: column-reverse !important;
    gap: var(--lp-spacing-sm) !important;
  }
}

/* Mobile */
@media (max-width: 480px) {
  :root {
    --lp-spacing-lg: 1.5rem;
    --lp-spacing-xl: 2rem;
  }

  .survey-container,
  .hl-form-container {
    padding: var(--lp-spacing-md) var(--lp-spacing-sm) !important;
    margin: 0 !important;
    border-radius: 0 !important;
    min-height: 100vh !important;
  }

  .survey-title,
  .hl-form-title {
    font-size: 1.5rem !important;
  }

  .survey-option,
  .hl-option {
    padding: 14px 16px !important;
  }

  input[type="text"],
  input[type="email"],
  textarea,
  select {
    padding: 12px 14px !important;
    font-size: 16px !important; /* Prevents iOS zoom */
  }

  .step-indicator {
    gap: 8px !important;
  }

  .step-dot {
    width: 10px !important;
    height: 10px !important;
  }
}

/* High contrast / Accessibility */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* Dark mode support (optional) */
@media (prefers-color-scheme: dark) {
  /* Uncomment to enable dark mode
  :root {
    --lp-white: #1a1a2e;
    --lp-off-white: #16213e;
    --lp-light-gray: #2d3748;
    --lp-dark-gray: #e2e8f0;
    --lp-black: #f7fafc;
  }
  */
}

/* === GHL-SPECIFIC OVERRIDES === */
/* These target specific GHL class patterns */

/* GHL Survey Wrapper */
.hl_page-creator__body,
[class*="hl-survey"] {
  background: transparent !important;
}

/* GHL Form Elements */
.hl-form-group {
  margin-bottom: var(--lp-spacing-md) !important;
}

/* GHL Modal/Popup Surveys */
.hl-modal .survey-container {
  max-height: 90vh !important;
  overflow-y: auto !important;
}

/* Hide GHL default branding (if permitted) */
.hl-powered-by,
[class*="powered-by-ghl"] {
  opacity: 0.5 !important;
  font-size: 0.75rem !important;
}
```

---

## How to Inject CSS in GHL Survey Builder

### Method 1: Custom CSS Field (Recommended)

1. **Open your survey** in GoHighLevel
2. Go to **Settings** → **Advanced** or **Styling**
3. Look for **"Custom CSS"** or **"Additional CSS"** field
4. Paste the entire CSS snippet above
5. Save and preview

### Method 2: Code Injection (Header/Footer)

1. Navigate to **Sites** → **Your Funnel/Website**
2. Click **Settings** → **Tracking Code** or **Code Injection**
3. In the **Header Code** section, wrap the CSS:

```html
<style>
  /* Paste the entire CSS here */
</style>
```

4. Save changes

### Method 3: Page-Level Custom Code

1. Edit the specific page containing your survey
2. Click **Settings** (gear icon) → **Custom Code**
3. Add the CSS wrapped in `<style>` tags in the **Head** section

### Method 4: External Stylesheet (Advanced)

1. Host the CSS file on your server or CDN
2. Add this to Header Code:

```html
<link rel="stylesheet" href="https://yourdomain.com/lawpronation-survey.css">
```

---

## Customization Guide

### Changing Brand Colors

Modify these variables at the top of the CSS:

```css
:root {
  --lp-primary: #1e3a5f;      /* Main brand color */
  --lp-primary-dark: #0f2744;  /* Darker shade */
  --lp-primary-light: #2d5a8a; /* Lighter shade */
  --lp-accent: #c9a227;        /* CTA/highlight color */
}
```

### Popular Color Schemes

**Classic Navy (Default)**
```css
--lp-primary: #1e3a5f;
--lp-accent: #c9a227;
```

**Modern Blue**
```css
--lp-primary: #2563eb;
--lp-accent: #f59e0b;
```

**Professional Green**
```css
--lp-primary: #065f46;
--lp-accent: #d97706;
```

**Elegant Purple**
```css
--lp-primary: #5b21b6;
--lp-accent: #ec4899;
```

### Changing Fonts

Replace the font import and variables:

```css
@import url('https://fonts.googleapis.com/css2?family=YOUR+FONT&display=swap');

:root {
  --lp-font-primary: 'Your Font', sans-serif;
  --lp-font-display: 'Your Display Font', serif;
}
```

---

## Responsive Breakpoints Reference

| Breakpoint | Target Devices | Key Changes |
|------------|----------------|-------------|
| > 768px | Desktop | Full layout, side-by-side buttons |
| 481-768px | Tablet | Reduced padding, stacked buttons |
| ≤ 480px | Mobile | Full-width, minimal padding, 16px inputs |

---

## Troubleshooting

### CSS Not Applying?

1. **Specificity Issues**: Add `!important` to overridden properties
2. **Cache**: Hard refresh (Ctrl+Shift+R) or clear browser cache
3. **Class Names**: Use browser DevTools to find exact GHL class names
4. **Load Order**: Ensure CSS loads after GHL's default styles

### Finding GHL Class Names

1. Open your survey in the browser
2. Right-click any element → **Inspect**
3. Note the class names (e.g., `.hl-form-input`, `.hl-btn`)
4. Add those specific selectors to the CSS

### Common GHL Classes to Target

```css
.hl-form-input { }
.hl-form-label { }
.hl-form-group { }
.hl-btn { }
.hl-btn-primary { }
.hl-survey-container { }
.hl-survey-question { }
.hl-progress-bar { }
```

---

## Performance Tips

1. **Minimize Font Loading**: Only import weights you use
2. **Remove Unused Sections**: Delete CSS for features you don't use
3. **Compress CSS**: Use a minifier for production
4. **Test on Mobile**: Always verify responsive behavior

---

## Version History

- **v1.0** - Initial Lawpronation-style survey CSS for GHL

---

*Created for GoHighLevel survey customization. Compatible with GHL survey builder and form elements.*
