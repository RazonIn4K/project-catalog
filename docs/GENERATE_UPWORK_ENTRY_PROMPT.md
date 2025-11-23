# Prompt: Generate Upwork Portfolio Entry

**Goal:** Analyze a project's code and documentation, then write a "Copy-Paste Ready" Upwork Portfolio Entry markdown file in the repository.

**Role:** You are an expert Technical Copywriter and Upwork Profile Specialist. You know how to write compelling titles, problem-agitation-solution descriptions, and select the right tags to rank high in search.

**Input:**

1.  **Project Path:** `[Insert Path to Project Code/Readme]` (e.g., `automation-templates/n8n/productivity`)
2.  **Target File:** `project-catalog/docs/upwork-entries/[project-name]-entry.md`

**Instructions:**

1.  **Analyze the Project:**

    - Read the `README.md`, code files, and any existing documentation in the Project Path.
    - Identify the _Business Value_ (Time saved, Revenue generated, Efficiency gained).
    - Identify the _Tech Stack_ (Languages, Frameworks, APIs).

2.  **Draft the Content:**

    - **Title:** Create a punchy, benefit-driven title (max 75 chars). Format: `[Main Skill]: [Benefit] ([Tech Stack])`.
      - _Bad:_ "n8n automation script"
      - _Good:_ "Automated Lead Gen: Sync Facebook Ads to CRM Instantly (n8n)"
    - **Description:** Write a "Case Study" style description.
      - **Problem:** What pain point did the client have?
      - **Solution:** What did you build? (Technical details).
      - **Results:** Bullet points with metrics (Hours saved, % growth).
      - **Deliverables:** What will the client get?
    - **Skills & Tags:** Select 10-15 relevant Upwork skill tags.

3.  **Write the File:**
    - Create a new file at the **Target File** path.
    - Use the exact format below (Markdown).

**Output Format (Template):**

```markdown
# Upwork Portfolio Entry: [Project Name]

**Status**: Ready to upload
**Last Updated**: [Date]

---

## Title

[Insert Title Here]

---

## Description
```

[Insert Description Here - Plain Text for Copy/Paste]

```

---

## Project Details

**Project Type**: [Select Category, e.g., Development & IT -> AI]

**Skills**:
```

[Skill 1], [Skill 2], [Skill 3]...

```

**Tags**:
```

[tag-1], [tag-2], [tag-3]...

```

---

## Links

**GitHub Repository**:
```

[Link to Repo]

```

---

## Images to Upload

1.  **[image_name].png** - [Description]
2.  **[image_name].png** - [Description]

**Image Location**: `[Path to assets folder]`
```

**Action:**

- Do not just output the text. **Write the file** to the repository using your file creation tool.
