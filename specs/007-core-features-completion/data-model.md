# Data Model: Core Features Completion - Physical AI & Humanoid Robotics Textbook

**Feature**: Core Features Completion | **Date**: 2026-02-15 | **Spec**: [spec.md](../007-core-features-completion/spec.md)

## Overview

This document defines the data structures and relationships needed to implement the missing core features: personalization backend, Urdu translation backend, Claude Code subagents, and remaining textbook content.

## Entity Relationships

```
User Profile
    ↓ (has)
User Background (software/hardware focus)
    ↓ (used by)
Personalization Engine
    ↓ (adapts)
Textbook Content (dynamic rendering)
    
Translation Request
    ↓ (processed by)
Translation Service (Urdu)
    ↓ (returns)
Translated Content (temporary/cache)
    
Subagent Task
    ↓ (executed by)
Claude Code Subagent
    ↓ (produces)
Validated Output
```

## Detailed Data Structures

### 1. User Profile Enhancement

```typescript
interface UserProfile {
  id: string;                // Unique user identifier (JWT subject)
  email: string;             // User's email address
  createdAt: Date;           // Account creation timestamp
  background: UserBackground; // Software/hardware focus information
  preferences: UserPreferences;
}

interface UserBackground {
  primaryFocus: 'software' | 'hardware' | 'both';  // Primary area of expertise
  experienceLevel: 'beginner' | 'intermediate' | 'advanced';
  specificInterests?: string[];  // Specific areas of interest
}

interface UserPreferences {
  preferredLanguage: string;     // Default language preference
  personalizationEnabled: boolean; // Whether to show personalized content
  lastActive: Date;              // Last activity timestamp
}
```

### 2. Content Personalization

```typescript
interface ContentVariant {
  id: string;                    // Unique identifier for the variant
  originalContentId: string;     // Reference to the original content
  userId: string;               // User this variant is personalized for
  backgroundMatch: 'exact' | 'partial' | 'none'; // How well content matches user background
  adaptations: ContentAdaptation[];
  createdAt: Date;              // When this variant was created
  lastAccessed: Date;           // When this variant was last accessed
}

interface ContentAdaptation {
  type: 'example' | 'explanation' | 'exercise' | 'resource';
  originalText: string;         // Original content
  adaptedText: string;          // Adapted content for user background
  confidence: number;           // Confidence in adaptation quality (0-1)
  reason: string;               // Reason for this adaptation
}
```

### 3. Translation Service

```typescript
interface TranslationRequest {
  id: string;                   // Unique request identifier
  userId: string;              // User requesting translation
  contentId: string;           // ID of content to translate
  sourceLanguage: string;      // Source language (likely 'en')
  targetLanguage: string;      // Target language ('ur' for Urdu)
  contentText: string;         // Text to translate
  context: TranslationContext; // Context for better translation
  timestamp: Date;             // When request was made
}

interface TranslationContext {
  domain: 'robotics' | 'ai' | 'ros' | 'isaac' | 'gazebo' | 'other';
  technicalTerms: string[];    // Technical terms in the content
  previousTranslations?: string[]; // Previous translations for consistency
}

interface TranslationResult {
  id: string;                  // Matches request ID
  success: boolean;            // Whether translation succeeded
  translatedText?: string;     // Translated content (if successful)
  error?: string;              // Error message (if failed)
  sourceLanguage: string;      // Detected source language
  targetLanguage: string;      // Target language
  confidence: number;          // Translation quality confidence (0-1)
  timestamp: Date;             // When translation was completed
  cached: boolean;             // Whether result was from cache
}
```

### 4. Claude Code Subagents

```typescript
interface SubagentDefinition {
  id: string;                  // Unique identifier (e.g., 'content-generator')
  name: string;                // Human-readable name
  description: string;         // What the subagent does
  capabilities: SubagentCapability[];
  configSchema: object;        // JSON schema for configuration
  requiredPermissions: SubagentPermission[];
}

interface SubagentTask {
  id: string;                  // Unique task identifier
  subagentId: string;          // Which subagent to use
  userId: string;              // User who initiated task
  parameters: object;          // Task-specific parameters
  status: 'pending' | 'in-progress' | 'completed' | 'failed';
  createdAt: Date;             // When task was created
  startedAt?: Date;            // When task execution began
  completedAt?: Date;          // When task was completed
  result?: SubagentResult;     // Result of task execution
  error?: string;              // Error if task failed
}

interface SubagentResult {
  taskId: string;              // Associated task ID
  outputs: SubagentOutput[];   // Generated outputs
  metrics: SubagentMetrics;    // Performance metrics
  validationReport: ValidationResult; // Quality validation
}

interface SubagentOutput {
  type: 'content' | 'code' | 'metadata' | 'report';
  content: string;             // The actual output
  format: 'markdown' | 'json' | 'yaml' | 'other';
  validated: boolean;          // Whether output passed validation
}

interface SubagentMetrics {
  tokensUsed: number;          // Number of tokens consumed
  executionTimeMs: number;     // Time taken to execute
  qualityScore: number;        // Quality score (0-1)
  complianceScore: number;     // Constitution compliance score (0-1)
}
```

### 5. Textbook Content Structure

```typescript
interface TextbookChapter {
  id: string;                  // Unique chapter identifier
  title: string;               // Chapter title
  module: string;              // Module this chapter belongs to
  week: number;                // Week number in the course
  estimatedTimeHours: number;  // Estimated time to complete
  prerequisites: string[];     // IDs of prerequisite chapters
  learningObjectives: string[]; // What students will learn
  content: string;             // Main content in Markdown/MDX
  metadata: ChapterMetadata;   // Additional metadata
  createdAt: Date;             // When chapter was created
  updatedAt: Date;             // When chapter was last updated
  authors: string[];           // Authors/contributors
}

interface ChapterMetadata {
  difficultyLevel: 'beginner' | 'intermediate' | 'advanced';
  assessmentType?: 'quiz' | 'project' | 'peer-review';
  capstoneComponent?: string;  // Connection to capstone project
  technicalTopics: string[];   // Technical topics covered
  hardwareRequirements?: string[]; // Hardware needed for examples
}
```

## API Endpoints

### Personalization Endpoints

```
GET /api/personalization/content/{contentId}
  Query: userId, backgroundPreference
  Response: PersonalizedContent

POST /api/personalization/profile/{userId}
  Body: UserProfileUpdate
  Response: Updated UserProfile
```

### Translation Endpoints

```
POST /api/translate
  Body: TranslationRequest
  Response: TranslationResult

GET /api/translate/cache/{requestId}
  Response: TranslationResult (if cached)
```

### Subagent Endpoints

```
GET /api/subagents
  Response: SubagentDefinition[]

POST /api/subagents/{subagentId}/execute
  Body: SubagentTaskParameters
  Response: SubagentTask (with ID for polling)

GET /api/subagents/task/{taskId}
  Response: SubagentTask (to check status)
```

## Database Schema Considerations

### User Profile Extension
- Extend existing user profile table with background information
- Add indexes on background fields for efficient querying

### Content Variants
- Store content adaptations separately from original content
- Use efficient indexing for content lookup by user and original content ID

### Translation Cache
- Implement TTL-based caching for translation results
- Consider external cache (Redis) for better performance

### Task Management
- Track subagent tasks for monitoring and debugging
- Implement cleanup for completed tasks after retention period

## Validation Rules

### Personalization Validation
- Ensure adaptations don't change technical accuracy
- Verify that personalized content still meets learning objectives
- Prevent content duplication in storage

### Translation Validation
- Verify translated content maintains technical accuracy
- Check that code examples remain valid after translation
- Ensure cultural appropriateness of translated content

### Subagent Validation
- Validate all outputs against constitution principles
- Ensure no unauthorized file creation
- Verify compliance with spec lifecycle requirements

## Performance Considerations

### Caching Strategy
- Cache personalized content variants for frequent users
- Cache translation results with appropriate TTL
- Cache subagent outputs where appropriate

### Indexing
- Index user profiles by background for quick personalization
- Index content by module and week for efficient retrieval
- Index translation requests by content ID and language pair

### Load Balancing
- Distribute translation requests across multiple service instances
- Scale subagent execution based on demand
- Consider CDN for static personalized content