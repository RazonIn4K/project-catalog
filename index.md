# Project Index

A comprehensive listing of all public demos and projects.

---

## 🤖 Automation

Workflow automation and process optimization projects.

### GHL Lead Capture & Slack Alert (n8n)

Demonstrates a simple automation where a lead from a GoHighLevel form flows into Google Sheets, triggers a Slack notification, and logs the data.

**Tech stack:** n8n, GoHighLevel Webhooks, Google Sheets, Slack API

**Who this is for:** Marketing agencies and sales teams using GoHighLevel who want instant notifications when new leads come in, with automatic logging to Google Sheets for tracking and reporting.

**How to try it:**
1. Check out the [automation-templates repository](https://github.com/RazonIn4K/automation-templates) and follow the README for setup instructions
2. Import the n8n workflow JSON into your n8n instance
3. Configure your GoHighLevel webhook URL, Google Sheets credentials, and Slack webhook
4. Watch the [demo video](TODO - add Loom URL) to see it in action

- **Repository**: [automation-templates](https://github.com/RazonIn4K/automation-templates)
- **Demo Video**: TODO (add URL)

---

## 💬 Chatbots

Conversational AI and bot implementations.

### FAQ Chatbot Template (coming soon)

A planned demo of a multilingual FAQ bot that uses a vector store to answer customer questions from uploaded docs.

**Tech stack:** OpenAI/Claude API, vector DB (Pinecone/Chroma), simple web UI

**Who this is for:** Customer support teams and businesses that want to automate FAQs and provide 24/7 answers from their existing documentation, help articles, or knowledge bases.

**How to try it:**
1. Repository coming soon at TODO (chatbot-templates repo)
2. Upload your FAQ documents (PDF, Markdown, or text files)
3. Run the setup script to create embeddings and deploy the chatbot
4. See the [demo video](TODO - add Loom URL) for a walkthrough

- **Repository**: TODO (chatbot-templates repo)
- **Demo Video**: TODO (add URL)

---

## 📊 Data Pipelines

Data processing, transformation, and ETL solutions.

### ShopMatch Product Scraper & Enricher

A CLI pipeline that reads sample product data, parses HTML to extract product info, and shows where an LLM could enrich descriptions.

**Tech stack:** Python, BeautifulSoup, CSV I/O, (optional) LLM API

**Who this is for:** E-commerce teams and data analysts who need to extract product information from websites, enrich product catalogs, or generate better product descriptions at scale.

**How to try it:**
1. Clone the [shopmatch-pro repository](https://github.com/RazonIn4K/shopmatch-pro)
2. Install dependencies: `pip install -r requirements.txt`
3. Run the scraper: `python scraper.py --input sample_products.csv`
4. Check the [demo video](TODO - add Loom URL) for examples of LLM-enhanced descriptions

- **Repository**: [shopmatch-pro](https://github.com/RazonIn4K/shopmatch-pro)
- **Demo Video**: TODO (add URL)

---

## Usage & Customization

These demos showcase real-world automation, AI chatbot, and data pipeline solutions that I use in client proposals and projects. Each demo is fully functional and can be customized to fit your specific use case:

- **For proposals:** Share relevant demos to show proof-of-concept capabilities
- **For customization:** All templates can be adapted to your tech stack, workflows, and business requirements
- **For integration:** Demos can be extended to connect with your existing CRM, databases, or APIs

Contact me to discuss how these solutions can be tailored to your needs.

---

## Adding New Projects

To add a new project to this catalog:

1. Choose the appropriate category (Automation, Chatbots, or Data Pipelines)
2. Add a new entry following the format:
   ```markdown
   ### Project Name
   *Brief description of the project.*

   - **Repository**: [Link to repo](repository-url)
   - **Demo Video**: [Watch on Loom](loom-url)
   ```
3. Update the entry with actual repository and Loom URLs when available
