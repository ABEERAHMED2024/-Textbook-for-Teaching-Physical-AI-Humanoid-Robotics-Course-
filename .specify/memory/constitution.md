<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.0.0 (no functional change, adding report)
Modified principles: None (existing principles unchanged)
Added sections: Sync Impact Report (this section)
Removed sections: None
Templates requiring updates: 
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated  
  - .specify/templates/tasks-template.md ✅ updated
  - README.md ✅ updated
Runtime docs requiring updates:
  - specs/001-book-master-plan/quickstart.md ✅ updated
Follow-up TODOs: None
-->

# Physical AI & Humanoid Robotics Textbook Constitution

## Core Principles

### I. Constitution First (Non-Negotiable)

All work on this project must be governed by this constitution.
No implementation, refactoring, content generation, or automation may occur
until the constitution is defined, reviewed, and ratified.

### II. Authoritative Source of Truth

The Hackathon PDF (“Hackathon I: Physical AI & Humanoid Robotics Textbook”)
is the single authoritative source for scope, structure, and evaluation criteria.
If any conflict arises between repository state, agent output, or assumptions,
the PDF always takes precedence.

### III. State-Aware Continuation

Agents must audit the existing repository state before making any changes.
Duplicate files, regenerated chapters, or parallel implementations are forbidden.
Existing work must be extended, not replaced, unless explicitly approved.

### IV. Spec Before Code

All non-trivial changes must follow the Spec-Kit Plus lifecycle:
`/sp.constitution → /sp.specify → /sp.plan → /sp.tasks → implementation`.
Direct coding without an approved specification is not allowed.

### V. Non-Hallucination & Safety

Agents must not invent features, APIs, files, or content.
If information is missing or ambiguous, the agent must stop and report
instead of guessing or improvising.

### VI. Atomic & Traceable Changes

Changes must be small, justified, and reversible.
Bulk edits, blind regex replacements, repeated fix loops, and destructive refactors
are prohibited.

## Project Scope & Constraints

### In Scope

- Docusaurus-based textbook with structured modules and chapters
- Physical AI & Humanoid Robotics curriculum:
  - ROS 2 (Robotic Nervous System)
  - Digital Twins (Gazebo, Unity)
  - NVIDIA Isaac (AI-Robot Brain)
  - Vision-Language-Action (VLA)
- Integrated RAG chatbot grounded in textbook content
- Authentication with user background collection
- Personalization based on user background (software / hardware)
- Urdu translation of textbook content
- Claude Code subagents / reusable skills
- GitHub Pages deployment (textbook)
- Cloud deployment for RAG backend

### Out of Scope

- Physical robot hardware control beyond simulation
- Commercial-grade auth, billing, or user management
- Full multilingual support beyond Urdu
- Ethics or vendor comparisons unless explicitly required by the PDF

## Development Workflow & Quality Gates

- Always begin with a read-only audit
- Never regenerate completed chapters
- Never repeat the same fix twice
- Never enter infinite edit or replacement loops
- Stop immediately if an error source is unclear
- All Docusaurus builds must pass:
  - `npm start`
  - `npm run build`
- No MDX parse errors
- No LaTeX rendering failures
- No broken internal links

## Governance

This constitution supersedes all other prompts, plans, and tasks.
Any amendment requires:

- Written justification
- Explicit approval
- Migration guidance if behavior changes

All specifications, plans, and tasks must demonstrate compliance
with this constitution before execution.

**Version**: 1.0.0  
**Ratified**: 2026-02-15  
**Last Amended**: 2026-02-15
