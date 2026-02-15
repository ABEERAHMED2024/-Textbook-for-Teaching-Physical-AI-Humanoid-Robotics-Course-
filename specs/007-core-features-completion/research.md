# Research: Core Features Completion - Physical AI & Humanoid Robotics Textbook

**Feature**: Core Features Completion | **Date**: 2026-02-15 | **Spec**: [spec.md](../007-core-features-completion/spec.md)

## Objective

Research the technical requirements and implementation approaches for completing the missing core features: personalization backend, Urdu translation backend, Claude Code subagents, and remaining textbook content.

## Current State Analysis

### Personalization Feature Status
- **Current Implementation**: UI-only mock implementation exists
- **Location**: Likely in `src/components/` directory
- **Issue**: Missing real backend logic to adapt content based on user background
- **Requirements**: Need to implement backend that dynamically adapts content without duplicating textbook content

### Urdu Translation Feature Status
- **Current Implementation**: UI-only mock implementation exists
- **Location**: Likely in `src/components/` directory
- **Issue**: Missing real backend logic for translation
- **Requirements**: Need to implement backend that provides real translation without altering source markdown files

### Claude Code Subagents Status
- **Current Implementation**: Not implemented
- **Issue**: No reusable agents for content generation, QA/validation, or maintenance
- **Requirements**: Define and implement subagents that follow spec lifecycle and don't create files autonomously

### Textbook Content Status
- **Current Implementation**: Partial content exists
- **Issue**: Missing chapters as defined in Hackathon PDF
- **Requirements**: Complete missing content without rewriting existing chapters

## Technical Approaches

### Personalization Backend Implementation

#### Approach 1: Dynamic Content Rendering
- **Description**: Use conditional rendering in MDX components based on user profile
- **Pros**: 
  - No content duplication
  - Real-time adaptation
  - Maintains single source of truth
- **Cons**: 
  - More complex MDX components
  - Potential performance impact
- **Implementation**: Add conditional blocks in MDX files that render differently based on user background

#### Approach 2: Server-Side Content Adaptation
- **Description**: Adapt content on the server based on user profile before sending to client
- **Pros**:
  - Cleaner client-side code
  - Potentially better performance
- **Cons**:
  - More complex backend logic
  - Caching considerations
- **Implementation**: Create API endpoints that serve personalized content based on user profile

#### Recommended Approach: Dynamic Content Rendering
This approach aligns with the requirement to not duplicate content while maintaining a single source of truth.

### Urdu Translation Backend Implementation

#### Approach 1: On-Demand Translation API Call
- **Description**: Call translation service when user requests translation
- **Pros**:
  - No storage of translated content
  - Always up-to-date translations
  - Doesn't alter source files
- **Cons**:
  - Dependency on external service
  - Potential latency
- **Implementation**: Create API endpoint that calls translation service and returns translated content

#### Approach 2: Cached Translation
- **Description**: Cache translations after first request
- **Pros**:
  - Better performance for repeated requests
  - Reduced API calls
- **Cons**:
  - Storage requirements
  - Cache invalidation complexity
- **Implementation**: Add caching layer to Approach 1

#### Recommended Approach: On-Demand Translation with Optional Caching
Start with on-demand approach and add caching later if needed for performance.

### Claude Code Subagents Implementation

#### Approach 1: CLI-Based Subagents
- **Description**: Create CLI commands following the /sp.* pattern
- **Pros**:
  - Consistent with existing workflow
  - Easy to integrate with current processes
  - Clear task approval process
- **Cons**:
  - Requires command-line usage
- **Implementation**: Create commands like /sp.generate, /sp.validate, /sp.maintain

#### Approach 2: UI-Integrated Subagents
- **Description**: Integrate subagents into the Docusaurus UI
- **Pros**:
  - More user-friendly
  - Visual feedback
- **Cons**:
  - More complex implementation
  - Potential security concerns
- **Implementation**: Add UI controls that trigger subagent functionality

#### Recommended Approach: CLI-Based Subagents
This approach is consistent with the existing Spec-Kit Plus workflow and ensures proper task approval.

### Textbook Content Completion

#### Approach 1: Manual Content Creation
- **Description**: Manually create missing content based on Hackathon PDF
- **Pros**:
  - High quality control
  - Accurate to source material
- **Cons**:
  - Time-consuming
  - Requires subject matter expertise
- **Implementation**: Follow existing chapter template structure

#### Approach 2: AI-Assisted Content Creation
- **Description**: Use Claude Code to assist in content creation
- **Pros**:
  - Faster creation
  - Consistent formatting
- **Cons**:
  - Requires careful oversight
  - Must follow constitution principles
- **Implementation**: Use Claude Code subagents (once implemented) to assist with content creation

#### Recommended Approach: Manual Creation with AI Assistance
Manually create content following the template, with AI assistance where appropriate but with careful oversight.

## Technical Dependencies

### Backend Technologies
- **API Framework**: Likely FastAPI (based on existing architecture)
- **Authentication**: JWT-based system already in place
- **Translation Service**: External API (e.g., Google Translate API, Microsoft Translator)

### Frontend Technologies
- **Framework**: React (part of Docusaurus)
- **State Management**: Likely React Context or similar
- **Internationalization**: Need to implement i18n support for Urdu

### AI/LLM Technologies
- **Platform**: Claude Code
- **Integration**: CLI-based commands following /sp.* pattern
- **Safety**: Implement safeguards to prevent unauthorized file creation

## Risk Assessment

### High Risks
1. **Translation Quality**: Technical robotics terminology may not translate accurately
2. **Content Duplication**: Risk of accidentally creating duplicate content despite requirements
3. **Constitution Compliance**: Risk of violating non-hallucination principle during content creation

### Medium Risks
1. **Performance**: Dynamic personalization may impact page load times
2. **External Dependencies**: Reliance on translation API may cause availability issues
3. **Maintainability**: Complex conditional rendering may be difficult to maintain

### Mitigation Strategies
1. **Translation Quality**: Implement review process for translated content, maintain glossary of technical terms
2. **Content Duplication**: Implement automated checks for duplicate content
3. **Constitution Compliance**: Strict review process and adherence to spec lifecycle
4. **Performance**: Optimize conditional rendering and implement caching where appropriate
5. **External Dependencies**: Implement graceful degradation when translation service is unavailable

## Implementation Phases

### Phase 1: Backend Infrastructure
- Set up API endpoints for personalization
- Set up API endpoints for translation
- Implement Claude Code subagent framework

### Phase 2: Core Feature Implementation
- Implement personalization logic
- Implement translation service integration
- Create initial Claude Code subagents

### Phase 3: Content Completion
- Identify missing content from Hackathon PDF
- Create missing chapters following template
- Integrate new content with personalization and translation features

### Phase 4: Quality Assurance
- Test all features thoroughly
- Verify no content duplication
- Ensure constitution compliance
- Performance optimization

## Conclusion

The research indicates that implementing the missing core features is technically feasible with the existing technology stack. The key challenges are ensuring no content duplication while implementing personalization and translation, and creating Claude Code subagents that follow the required lifecycle. The recommended approach focuses on dynamic content rendering, on-demand translation, CLI-based subagents, and manual content creation with AI assistance.