---
id: "0002"
title: "Convert Tasks to GitHub Issues Summary"
stage: "tasks"
date: "2026-01-03"
surface: "agent"
model: "Qwen Code"
feature: "001-book-master-plan"
branch: "main"
user: "unknown"
command: "/sp.issues"
labels: ["tasks", "issues", "github", "001-book-master-plan"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "tasks_to_issues.md"
tests: []
---

# Prompt Record: Convert Tasks to GitHub Issues Summary

## Original Prompt

```
---
description: Convert existing tasks into actionable, dependency-ordered GitHub issues for the feature based on available design artifacts.
tools: ['github/github-mcp-server/issue_write']
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").
1. From the executed script, extract the path to **tasks**.
1. Get the Git remote by running:

```bash
git config --get remote.origin.url
```

> [!CAUTION]
> ONLY PROCEED TO NEXT STEPS IF THE REMOTE IS A GITHUB URL

1. For each task in the list, use the GitHub MCP server to create a new issue in the repository that is representative of the Git remote.

> [!CAUTION]
> UNDER NO CIRCUMSTANCES EVER CREATE ISSUES IN REPOSITORIES THAT DO NOT MATCH THE REMOTE URL
```

## Response Summary

I analyzed the tasks.md file for the 001-book-master-plan feature and identified all incomplete tasks that need to be converted to GitHub issues. Since I don't have write permissions to create issues directly in the repository, I created a summary document (tasks_to_issues.md) with all the required information for creating the issues manually.

## Outcome & Impact

Created a comprehensive summary of 39 tasks that need to be converted to GitHub issues, organized by user story and priority. This provides a clear roadmap for creating the actual GitHub issues.

## Tests Summary

none

## Files Summary

- tasks_to_issues.md: Contains detailed summary of all tasks that need to be converted to GitHub issues

## Next Prompts

none

## Reflection Note

The approach of creating a summary document when lacking direct write permissions was effective for ensuring the work is properly documented and actionable.

## Evaluation Notes

**Failure modes observed:** Lack of write permissions to create GitHub issues directly

**Next experiment to improve prompt quality:** Consider adding a fallback mechanism for when direct issue creation isn't possible