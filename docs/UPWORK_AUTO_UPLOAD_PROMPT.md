# Prompt: Automate Upwork Portfolio Upload

**Goal:** Use an AI Browser Agent to upload 4 portfolio items to Upwork.

**Context:**
I have prepared 4 "Copy-Paste Ready" markdown files containing all the necessary text (Title, Description, Skills, Tags) and image paths for my Upwork portfolio. I need you to read these files and populate the Upwork Portfolio creation wizard for each one.

**Source Files:**

1.  `project-catalog/docs/upwork-entries/n8n-automation-entry.md`
2.  `project-catalog/docs/upwork-entries/crm-pipeline-entry.md`
3.  `project-catalog/docs/upwork-entries/saas-backend-entry.md`
4.  `project-catalog/docs/upwork-entries/rag-chatbot-entry.md`
5.  `project-catalog/docs/upwork-entries/security-audit-entry.md`

**Instructions for the Agent:**

1.  **Login Check:**

    - Navigate to `https://www.upwork.com/nx/find-work/`.
    - Verify I am logged in. If not, pause and ask me to login.

2.  **Navigate to Portfolio:**

    - Go to my Profile > Portfolio section.
    - Click "Add" or "Create New Project".

3.  **Process Item #1 (n8n Automation):**

    - Read `n8n-automation-entry.md`.
    - **Step 1 (Title):** Copy the "Title" from the file. Select "Development & IT" -> "AI & Machine Learning" (or as specified in "Project Details").
    - **Step 2 (Details):**
      - Select the "Skills" listed in the file.
      - Set "Project Role" to "Solo project" (or as specified).
      - Set "Client" to "Personal project" (or as specified).
    - **Step 3 (Description):**
      - Copy the text inside the `Description` code block.
      - Paste it into the "Project Description" field.
    - **Step 4 (Images):**
      - Look at the "Images to Upload" section.
      - Upload the corresponding images from the `project-catalog/assets/` or `automation-templates/` folders (paths are in the file).
      - Set the "Cover Image" to the first image listed.
    - **Step 5 (Tags):**
      - Add the "Tags" listed in the file.
    - **Step 6 (Review):**
      - Pause for my final review before clicking "Publish".

4.  **Repeat for Items #2, #3, #4, #5:**
    - Repeat the process for the remaining markdown files.

**Constraint:**

- Do NOT publish without my confirmation.
- If an image file is missing, skip it and note it in the chat.
