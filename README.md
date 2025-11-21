# Project Catalog

Give prospects a 30-second tour of my automation, chatbot, scraping, and security demos.

## Portfolio Table
| Project | Category | Summary | Updated | Repo |
| --- | --- | --- | --- | --- |
| [n8n Sheet → Notion → GPT → Slack](catalog/n8n_sheet_automation.md) | Automation | AI-powered workflow monitors Sheets, enriches with GPT-4, creates Notion records, sends Slack alerts. | 2024-03-15 | [automation-templates](https://github.com/RazonIn4K/automation-templates) |
| [Driver Scoring Automation](catalog/driver_scoring.md) | Automation | Typeform intake scores compliance risk and syncs actions to Notion in <2 min. | 2024-06-20 | [automation-templates](https://github.com/RazonIn4K/automation-templates) |
| [N8N Messaging Agent Platform](catalog/n8n_messaging_agent.md) | Automation | AI-personalized SMS/email cadences that keep real-estate leads warm 24/7. | 2024-06-15 | [automation-templates](https://github.com/RazonIn4K/automation-templates) |
| [Scraping + Lead Gen Pipelines](catalog/scraping_lead_gen.md) | Scraping | Playwright scrapers + enrichment create CRM-ready lead lists automatically. | 2024-05-30 | [data-pipeline-starters](https://github.com/RazonIn4K/data-pipeline-starters) |
| [GHL Lead Capture & Slack Alert](index.md#ghl-lead-capture--slack-alert-n8n) | Automation | GoHighLevel forms drop leads into Sheets, trigger Slack alerts, and log activity. | 2024-04-15 | [automation-templates](https://github.com/RazonIn4K/automation-templates) |
| [FAQ Chatbot Template](index.md#faq-chatbot-template-coming-soon) | Chatbot | Multilingual FAQ bot powered by vector search for instant self-service answers. | 2024-05-10 | [chatbot-templates](https://github.com/RazonIn4K/chatbot-templates) |
| [ShopMatch Product Scraper & Enricher](index.md#shopmatch-product-scraper--enricher) | Scraping | CLI pipeline parses storefronts, enriches products, and drafts copy via LLM. | 2024-05-05 | [shopmatch-pro](https://github.com/RazonIn4K/shopmatch-pro) |
| [AI Integration & Security Audit Bundle](catalog/ai_security_bundle.md) | Security | Launch an AI workflow plus a guardrail audit so ops scale safely. | 2024-06-25 | [automation-templates](https://github.com/RazonIn4K/automation-templates) |

## Catalog Anatomy
- `catalog/` — High-signal one-pagers with problem, solution, stack, outcomes, and thumbnails.
- `index.md` — Long-form write-ups for each category plus setup instructions.
- `assets/screenshots/` — Lightweight thumbnail placeholders linked inside every entry.

## Categories
- **Automation** — Workflow automation, operations co-pilots, CRM syncs.
- **Chatbot** — Conversational AI, FAQ assistants, lead-qualification bots.
- **Scraping** — Data acquisition, enrichment, and outbound-ready datasets.
- **Security** — AI guardrails, prompt audits, secret scanning, and compliance-ready reporting.

## Add a New Project
1. Duplicate any file in `catalog/` and update the YAML front-matter (title, category, summary, date, thumbnail, repo/workflow links).
2. Keep the sections consistent: one-line summary, Problem, Solution, Tech Stack, and exactly three Key Outcome bullets.
3. Drop a PNG thumbnail into `assets/screenshots/` and reference it relatively (`../assets/screenshots/your-file.png`).
4. Update this README table with the quick link, category, one-line summary, date, and repo.
5. Link the new entry from `index.md` if you want the long-form narrative to include it.

## Usage
Every project includes a ready-to-clone workflow plus outcomes you can lift straight into Upwork proposals. Use the catalog during discovery calls to show proof, then send prospects the specific markdown entry that matches their scope.
