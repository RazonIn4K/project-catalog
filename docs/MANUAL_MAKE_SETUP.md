# Manual Make.com Setup: CRM Pipeline

**Goal:** Create a 3-node scenario to verify the "ActiveCampaign -> Sheets -> Slack" flow.
**Time:** 2 minutes.

## 1. Open the Scenario

1.  Go to your new **"CRM Pipeline Demo"** scenario.
2.  If you see a big purple button in the middle, click it.

## 2. Add Node 1: ActiveCampaign

1.  Search for **"ActiveCampaign"**.
2.  Select **"Watch Deals"** (or "Watch Deal Updates").
3.  **Webhook:** Click "Add", name it "Demo Hook", and click Save.
4.  Click "OK".

## 3. Add Node 2: Google Sheets

1.  Hover over the right "ear" of the ActiveCampaign node to see the "Add another module" button.
2.  Search for **"Google Sheets"**.
3.  Select **"Add a Row"**.
4.  **Connection:** Connect your Google account.
5.  **Spreadsheet:** Select any sheet (or the "n8n Demo - Leads" one if visible).
6.  **Values:** Just type "Test" in the first column for now.
7.  Click "OK".

## 4. Add Node 3: Slack

1.  Add another module after Google Sheets.
2.  Search for **"Slack"**.
3.  Select **"Create a Message"**.
4.  **Connection:** Connect your Slack account (or skip if you don't want to auth).
5.  **Channel:** Select any channel (e.g. `#general`).
6.  **Text:** "New Deal: {{1.title}}" (You can map fields or just type text).
7.  Click "OK".

## 5. Save

1.  Click the **Save** icon (floppy disk) at the bottom.
2.  Click **"Run once"** to test (optional).

**That's it!** You now have the visual proof for the video.
