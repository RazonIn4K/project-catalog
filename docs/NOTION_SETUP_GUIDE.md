# Notion Setup Guide: n8n Demo

**Goal:** Create the database that the n8n workflow will populate.

## 1. Create a New Page

1.  Go to [Notion](https://www.notion.so).
2.  Create a new page titled: **"n8n Demo - CRM"**.

## 2. Create the Database

1.  Type `/table` and select **"Table view"**.
2.  Select **"New database"**.

## 3. Configure Columns

Rename and configure the properties (columns) as follows:

| Property Name | Type   | Options (if applicable)                   |
| :------------ | :----- | :---------------------------------------- |
| **Name**      | Title  | -                                         |
| **Email**     | Email  | -                                         |
| **Company**   | Text   | -                                         |
| **Status**    | Select | `New`, `Contacted`, `Qualified`, `Closed` |
| **Summary**   | Text   | -                                         |

## 4. Add Dummy Data

Add one row so the table isn't empty:

- **Name:** John Doe
- **Email:** john@example.com
- **Company:** Acme Corp
- **Status:** New
- **Summary:** (Leave empty)

## 5. Get Database ID (Optional but helpful)

- Click the "..." menu at the top right of the database.
- Select "Copy link to view".
- The ID is the 32-character string between the `/` and the `?`.
