# Quickstart Guide: Core Features Completion - Physical AI & Humanoid Robotics Textbook

**Feature**: Core Features Completion | **Date**: 2026-02-15 | **Spec**: [spec.md](../007-core-features-completion/spec.md)

## Purpose

This guide enables developers to implement the missing core features: personalization backend, Urdu translation backend, Claude Code subagents, and remaining textbook content as defined in the Hackathon PDF.

## Prerequisites

- Node.js 18+ (LTS recommended)
- Git
- Text editor with Markdown support
- Basic command-line knowledge
- Access to translation API (for Urdu translation feature)
- Claude Code access (for subagent implementation)

## Implementation Steps

### 1. Set Up Development Environment

1. Navigate to the project directory:
   ```bash
   cd d:\demo hackathon\Physical-AI-Humanoid-Robotics-Textbook
   ```

2. Install dependencies if not already installed:
   ```bash
   npm install
   ```

### 2. Implement Personalization Backend

1. Review the current personalization UI in `src/components/` to understand the frontend implementation
2. Create backend endpoints for personalization logic in the API service
3. Connect user profile data (from authentication) to content adaptation logic
4. Ensure content adaptation happens dynamically without duplicating source files

### 3. Implement Urdu Translation Backend

1. Review the current translation UI in `src/components/` to understand the frontend implementation
2. Integrate with a translation service API for Urdu translation
3. Implement on-demand translation endpoint that doesn't alter source markdown files
4. Add optional caching mechanism for improved performance

### 4. Develop Claude Code Subagents

1. Create subagent definitions for content generation, QA/validation, and maintenance
2. Ensure subagents follow the spec lifecycle requirements
3. Implement CLI interfaces following the /sp.* command pattern
4. Add safeguards to prevent autonomous file creation without approved tasks

### 5. Complete Missing Textbook Content

1. Compare existing content with the Hackathon PDF to identify gaps
2. Create missing chapters following the established chapter template
3. Ensure all content integrates properly with Docusaurus and sidebar structure
4. Verify that existing content remains unchanged during this process

### 6. Quality Assurance

1. Run all quality checks:
   ```bash
   npm run build          # Ensures no build errors/warnings
   npm run check-links    # Validates internal/external links
   npm run lighthouse     # Runs performance/accessibility/SEO checks
   npm run validate-metadata  # Validates chapter frontmatter against schema
   ```

2. Test personalization and translation features end-to-end
3. Verify that subagents function as expected
4. Confirm all textbook content is complete per Hackathon PDF

## Testing the Features

### Personalization Testing
1. Register with different user backgrounds (software/hardware focus)
2. Log in and navigate to various chapters
3. Verify content adapts appropriately to user background
4. Test toggling personalization on/off

### Urdu Translation Testing
1. Access any chapter content
2. Trigger Urdu translation
3. Verify real translation occurs without altering source files
4. Test switching between English and Urdu

### Subagent Testing
1. Invoke each subagent with sample tasks
2. Verify they follow constitution and spec lifecycle
3. Confirm they don't create files autonomously
4. Test all subagent functions (content generation, QA/validation, maintenance)

## Troubleshooting

### Common Issues

1. **Personalization not working**
   - Check that user profile contains background information
   - Verify backend endpoint is properly connected to frontend
   - Confirm conditional rendering logic is functioning

2. **Translation service errors**
   - Verify API credentials for translation service
   - Check network connectivity to translation service
   - Confirm translation endpoint is properly implemented

3. **Subagent not following guidelines**
   - Review subagent configuration for constitution compliance
   - Verify subagent follows spec lifecycle requirements
   - Check that safeguards prevent unauthorized file creation

### Performance Tips

1. **Optimize translation performance** with optional caching
2. **Minimize content duplication** by using dynamic rendering
3. **Use efficient conditional logic** for personalization
4. **Implement proper error handling** for external service calls