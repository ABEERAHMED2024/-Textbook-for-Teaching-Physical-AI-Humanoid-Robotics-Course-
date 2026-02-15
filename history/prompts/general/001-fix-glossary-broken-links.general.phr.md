---
id: 001
title: Fix Glossary Broken Links
stage: general
date_iso: 2026-01-05
surface: agent
model: Antigravity
feature: none
branch: main
user: SARS
command: none
labels: ["bugfix", "docusaurus", "documentation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - d:\demo hackathon\Physical-AI-Humanoid-Robotics-Textbook\docs\references\glossary.md
tests_yaml:
  - build check
---

# Prompt History Record (PHR)

## Prompt Text
Compiled with problems:
×
ERROR in ./docs/references/glossary.md
Module build failed (from ./node_modules/@docusaurus/mdx-loader/lib/index.js):
Error: MDX compilation failed for file "D:\demo hackathon\Physical-AI-Humanoid-Robotics-Textbook\docs\references\glossary.md"
Cause: Markdown link with URL `../intro.md` in source file "docs/references/glossary.md" (18:14) couldn't be resolved.
...

## Response Text
I fixed the broken links in `docs/references/glossary.md` where `../intro.md` was referenced instead of the actual file `../intro.mdx`. I updated all 6 occurrences to ensure the Docusaurus build process can resolve the links correctly.

## Outcome/Evaluation
The MDX compilation error is resolved by matching the link destination to the actual file extension present in the documentation directory.
