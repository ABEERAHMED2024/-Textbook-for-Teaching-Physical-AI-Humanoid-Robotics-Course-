# Data Model: Book Master Plan - Physical AI & Humanoid Robotics Textbook

**Feature**: Book Master Plan | **Date**: 2025-11-29 | **Spec**: [spec.md](../001-book-master-plan/spec.md)

## Overview

This document defines the data model for the Physical AI & Humanoid Robotics textbook. It outlines the key entities, their attributes, relationships, and validation rules derived from the feature specification.

## Entities

### Module
Represents a major course section (4 total: ROS 2, Digital Twin, Isaac, VLA). Contains learning outcomes, week ranges, chapters, and integration points with capstone.

**Attributes**:
- `id`: string (e.g., "module-1-ros2") - Required, unique identifier
- `title`: string (e.g., "Module 1: The Robotic Nervous System (ROS 2)") - Required
- `weekRange`: string (e.g., "Weeks 3-5") - Required, follows format "Weeks X-Y"
- `description`: string (module overview) - Required, minimum 20 characters
- `learningOutcomes`: array of strings - Required, minimum 3 outcomes
- `chapters`: array of Chapter references - Required, minimum 1 chapter
- `capstoneIntegration`: string (how module contributes to capstone) - Optional

**Validation Rules**:
- `id` must be unique across all modules
- `weekRange` must follow the format "Weeks X-Y" where X and Y are integers
- `weekRange` values must be within the course duration (1-13 weeks)
- `learningOutcomes` must have at least 3 items
- `chapters` must reference valid chapter IDs

### Chapter
Represents a single topic within a module. Metadata includes estimated time, week number, module number, prerequisites, learning objectives, and optional assessment type, difficulty level, and capstone component. Contains content sections, code examples, exercises, and references. Maps to 1-2 weeks of course content.

**Attributes** (as Markdown frontmatter):
- `title`: string (full chapter title) - Required, minimum 5 characters
- `description`: string (brief summary for SEO and TOC) - Required, 20-160 characters
- `keywords`: array of strings (SEO keywords) - Required, 3-10 items
- `sidebar_position`: number (ordering within parent category) - Required, positive integer
- `sidebar_label`: string (optional override for long titles) - Optional, max 40 characters
- `estimated_time`: number (hours of reading/lab work) - Required, 0.5-20 hours
- `week`: number (1-13) - Required, within course duration
- `module`: number (1-4) - Required, references valid module
- `prerequisites`: array of strings (chapter slugs or "none") - Optional
- `learning_objectives`: array of strings (measurable objectives) - Required, 3-8 items
- `assessment_type`: string | null ("project", "quiz", "capstone", null) - Optional
- `difficulty_level`: string | null ("beginner", "intermediate", "advanced", null) - Optional
- `capstone_component`: string | null ("voice", "plan", "navigate", "perceive", "manipulate", null) - Optional

**Validation Rules**:
- `title` must be unique across all chapters
- `estimated_time` must be between 0.5 and 20 hours
- `week` must be between 1 and 13
- `module` must be between 1 and 4
- `prerequisites` must reference valid chapter IDs or be "none"
- `learning_objectives` must have 3-8 items
- `assessment_type` must be one of the allowed values or null
- `difficulty_level` must be one of the allowed values or null
- `capstone_component` must be one of the allowed values or null

### Part
High-level grouping of content. Parts include: Introduction, Foundational Setup, Modules 1-4, Capstone Guide, Assessments, References.

**Attributes**:
- `id`: string (unique identifier) - Required
- `title`: string (display title) - Required
- `description`: string (overview of content) - Required
- `sections`: array of strings (references to child sections) - Required

**Validation Rules**:
- `id` must be unique across all parts
- `sections` must reference valid section IDs

### Hardware Configuration
Represents one of three setup paths. Contains hardware requirements, software installation steps, cost estimates, and limitations.

**Attributes**:
- `id`: string ("workstation", "edge-kit", "cloud") - Required, unique
- `name`: string (display name) - Required
- `requirements`: array of strings (hardware/software specs) - Required
- `cost`: string (estimated cost range) - Required
- `setupSteps`: array of strings (installation instructions) - Required
- `limitations`: array of strings (what doesn't work) - Optional

**Validation Rules**:
- `id` must be one of the allowed values
- `setupSteps` must have at least one item

### Assessment
Represents a project or evaluation point. Contains requirements, rubrics, evaluation criteria, and submission guidelines.

**Attributes**:
- `id`: string ("ros2-package", "gazebo-simulation", "isaac-perception", "capstone") - Required, unique
- `title`: string - Required
- `modules`: array of numbers (which modules assessed) - Required
- `rubric`: array of RubricLevel objects - Required
- `requirements`: string (what needs to be submitted) - Required
- `submissionGuidelines`: string (how to submit) - Required

**RubricLevel Object**:
- `level`: string ("needs improvement", "proficient", "excellent") - Required
- `criteria`: array of strings - Required
- `points`: number - Required

**Validation Rules**:
- `id` must be one of the allowed values
- `modules` must contain valid module numbers (1-4)
- `rubric` must have at least one RubricLevel object
- Each RubricLevel must have valid `level` value
- `criteria` in each RubricLevel must have at least one item

### Glossary Entry
Contains robotics terminology with definitions and cross-references.

**Attributes**:
- `term`: string (canonical term) - Required, unique
- `definition`: string (concise explanation) - Required
- `relatedTerms`: array of strings (cross-references) - Optional
- `chapters`: array of strings (where term is used) - Optional

**Validation Rules**:
- `term` must be unique across all glossary entries
- `definition` must be at least 10 characters
- `relatedTerms` must reference valid glossary terms

### Reference Material
Includes glossary entries, notation definitions, quick reference commands, troubleshooting solutions, and external resources.

**Attributes**:
- `id`: string (unique identifier) - Required
- `title`: string (display title) - Required
- `type`: string ("glossary", "notation", "quick-reference", "troubleshooting", "external-resource") - Required
- `content`: string (the actual reference material) - Required
- `relatedChapters`: array of strings (relevant chapter IDs) - Optional

**Validation Rules**:
- `id` must be unique across all reference materials
- `type` must be one of the allowed values
- `content` must be at least 10 characters

## Relationships

### Module → Chapter
- One-to-many relationship
- Module "has many" Chapters
- Each Chapter "belongs to" one Module

### Chapter → Module
- Many-to-one relationship
- Each Chapter "references" one Module via `module` attribute
- Module "contains" many Chapters

### Chapter → Chapter (Prerequisites)
- Many-to-many relationship (self-referencing)
- Chapter "has prerequisites" (other Chapters)
- Implemented via `prerequisites` array in Chapter

### Chapter → Glossary Entry
- Many-to-many relationship
- Chapter "references" many Glossary Entries
- Implemented via inline links in Chapter content

### Assessment → Module
- Many-to-many relationship
- Assessment "assesses" many Modules
- Implemented via `modules` array in Assessment

## State Transitions

None (static content, no workflow states)

## Validation Rules Summary

1. **Module Validation**:
   - Unique ID requirement
   - Valid week range format and values
   - Minimum learning outcomes count
   - Valid chapter references

2. **Chapter Validation**:
   - Unique title requirement
   - Valid time estimate range
   - Valid week and module numbers
   - Valid prerequisite references
   - Required learning objectives count
   - Valid optional field values

3. **Hardware Configuration Validation**:
   - Valid ID values
   - Required setup steps

4. **Assessment Validation**:
   - Valid ID values
   - Valid module references
   - Required rubric structure

5. **Glossary Entry Validation**:
   - Unique term requirement
   - Valid definition length

6. **Reference Material Validation**:
   - Unique ID requirement
   - Valid type values
   - Valid content length

## Implementation Notes

- All validation rules should be implemented using JSON Schema for automatic validation
- Custom validation functions may be needed for complex relationships
- Validation should occur during the build process and as part of the CI/CD pipeline
- Validation errors should prevent deployment to ensure data integrity