# Quickstart Guide: Book Master Plan - Physical AI & Humanoid Robotics Textbook

**Feature**: Book Master Plan | **Date**: 2025-11-29 | **Spec**: [spec.md](../001-book-master-plan/spec.md)

## Purpose

This guide enables developers to set up, run, and contribute to the Physical AI & Humanoid Robotics textbook project.

## Prerequisites

- Node.js 18+ (LTS recommended)
- Git
- Text editor with Markdown support
- Basic command-line knowledge

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ameen-alam/Physical-AI-Humanoid-Robotics-Textbook.git
   cd Physical-AI-Humanoid-Robotics-Textbook
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Development Server

Start the development server:
```bash
npm start
```

This opens the textbook at http://localhost:3000 with hot reloading enabled.

## Building & Deploying

### Local Build
Create a production-ready build:
```bash
npm run build
```

This creates a static site in the `build/` directory.

### Local Preview
Preview the production build locally:
```bash
npm run serve
```

This serves the built site at http://localhost:3000.

### Deployment
Deploy to GitHub Pages (main branch only):
```bash
npm run deploy
```

## Creating New Content

### New Chapter
To create a new chapter:

1. Copy the chapter template from `.specify/templates/chapter-template.md`
2. Fill in the frontmatter metadata (see schema in `contracts/chapter-metadata-schema.json`)
3. Place the file in the appropriate module directory (`docs/module-X-name/`)
4. Add the new chapter to `sidebars.js` in the correct category
5. Validate the metadata:
   ```bash
   npm run validate-metadata
   ```

### New Module
To create a new module:

1. Create a new directory in `docs/` (e.g., `docs/module-5-new-topic/`)
2. Create an `index.md` file for the module overview
3. Add the module to `sidebars.js`
4. Update the data model if needed

### New Assessment
To create a new assessment:

1. Create a new file in `docs/assessments/`
2. Follow the assessment template structure
3. Add to `sidebars.js` under assessments
4. Update the assessment data model if needed

## Quality Checks

Run all quality checks:
```bash
npm run build          # Ensures no build errors/warnings
npm run check-links    # Validates internal/external links
npm run lighthouse     # Runs performance/accessibility/SEO checks
npm run validate-metadata  # Validates chapter frontmatter against schema
npm run check-accessibility  # Verifies WCAG 2.1 AA compliance
```

### Individual Quality Checks

- Build validation: `npm run build`
- Link validation: `npm run check-links`
- Performance/accessibility/SEO: `npm run lighthouse`
- Metadata validation: `npm run validate-metadata`
- Accessibility compliance: `npm run check-accessibility`

## Updating Glossary

1. Edit `docs/references/glossary.md`
2. Rebuild the search index:
   ```bash
   npm run generate-glossary-index
   ```

## Working with Components

### Custom Components Location
All custom React components are in `src/components/`

### Creating New Components
1. Create a new `.tsx` file in `src/components/`
2. Follow the existing component patterns
3. Use TypeScript interfaces for props
4. Ensure accessibility compliance
5. Test in the development environment

### Homepage Components
The homepage is built with custom components in `src/pages/index.tsx`
- ModuleCard: Displays module information
- QuickLinks: Sidebar with common links
- RecentUpdates: Shows recent content changes
- GlossarySearch: Dedicated search for terminology

## Configuration Files

### Docusaurus Configuration
Main configuration is in `docusaurus.config.js`
- Site metadata (title, tagline, URL)
- Theme configuration
- Plugin configuration
- Algolia search settings
- Security headers
- Accessibility features

### Sidebar Configuration
Navigation structure is in `sidebars.js`
- Organized by modules and weeks
- Collapsible categories
- Cross-references for topics

### TypeScript Configuration
Settings in `tsconfig.json`
- Type checking rules
- Module resolution
- JSX compilation

## Environment-Specific Commands

### Development
- `npm start`: Start development server with hot reloading
- `npm run swizzle`: Customize Docusaurus themes/components

### Production
- `npm run build`: Create production build
- `npm run serve`: Serve production build locally
- `npm run deploy`: Deploy to GitHub Pages

### Testing & Validation
- `npm run check-links`: Check for broken links
- `npm run lighthouse`: Performance/accessibility/SEO audit
- `npm run validate-metadata`: Validate chapter metadata
- `npm run check-accessibility`: WCAG compliance check

## Troubleshooting

### Common Issues

1. **Build fails with errors**
   - Check that all frontmatter metadata is valid according to the schema
   - Ensure all required dependencies are installed
   - Verify that all links are valid

2. **Components not rendering properly**
   - Check browser console for JavaScript errors
   - Verify TypeScript interfaces match component props
   - Ensure accessibility attributes are properly set

3. **Search not working**
   - Verify Algolia configuration in `docusaurus.config.js`
   - Check that the glossary search index is properly generated
   - Ensure search selectors are correctly configured

### Performance Tips

1. **Optimize images** using the ideal-image plugin
2. **Minimize JavaScript bundle size** by code splitting large components
3. **Use lazy loading** for non-critical content
4. **Enable compression** in deployment configuration

## Contributing Guidelines

### Content Creation
- Follow the established chapter template
- Include all required metadata
- Write in clear, accessible language
- Use consistent terminology (refer to glossary)
- Include relevant code examples with proper syntax highlighting

### Code Contributions
- Write TypeScript for all custom components
- Follow accessibility best practices
- Include JSDoc comments for exported functions/components
- Ensure all tests pass before submitting PRs
- Follow the established code style

### Review Process
- All changes must pass quality checks
- PRs require at least one approval
- Changes to core functionality require additional review
- Documentation updates should accompany code changes