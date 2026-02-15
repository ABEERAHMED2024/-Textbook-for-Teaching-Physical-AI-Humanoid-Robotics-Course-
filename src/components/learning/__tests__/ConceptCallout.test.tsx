import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import ConceptCallout from '../ConceptCallout';

describe('ConceptCallout', () => {
  it('renders concept callout with default title and icon', () => {
    render(
      <ConceptCallout type="concept">
        This is a concept explanation.
      </ConceptCallout>
    );
    expect(screen.getByText(/Concept/)).toBeInTheDocument();
    expect(screen.getByLabelText(/Concept/)).toBeInTheDocument();
  });

  it('renders with custom title', () => {
    render(
      <ConceptCallout type="definition" title="Custom Definition">
        This is a custom definition.
      </ConceptCallout>
    );
    expect(screen.getByText(/Custom Definition/)).toBeInTheDocument();
  });

  it('renders different types with appropriate icons', () => {
    const { rerender } = render(
      <ConceptCallout type="tip">Tip content</ConceptCallout>
    );
    expect(screen.getByText(/Tip/)).toBeInTheDocument();

    rerender(
      <ConceptCallout type="warning">Warning content</ConceptCallout>
    );
    expect(screen.getByText(/Warning/)).toBeInTheDocument();

    rerender(
      <ConceptCallout type="danger">Danger content</ConceptCallout>
    );
    expect(screen.getByText(/Danger/)).toBeInTheDocument();
  });

  it('has accessible labels', () => {
    render(
      <ConceptCallout type="definition" title="Test Definition">
        Test content
      </ConceptCallout>
    );
    expect(screen.getByRole('note', { name: /Test Definition/i })).toBeInTheDocument();
  });

  it('validates type prop', () => {
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

    // @ts-expect-error - intentionally using invalid type for testing
    const { container } = render(
      <ConceptCallout type="invalid">
        Invalid type content
      </ConceptCallout>
    );
    expect(container.firstChild).toBeNull();

    consoleSpy.mockRestore();
  });

  it('handles empty children gracefully', () => {
    const consoleSpy = jest.spyOn(console, 'warn').mockImplementation(() => {});

    const { container } = render(
      // @ts-expect-error - intentionally not providing children for testing
      <ConceptCallout type="concept" />
    );
    expect(container.firstChild).toBeNull();

    consoleSpy.mockRestore();
  });

  it('applies correct CSS classes based on type', () => {
    render(
      <ConceptCallout type="definition">
        Definition content
      </ConceptCallout>
    );
    const callout = screen.getByRole('note');
    expect(callout).toHaveClass('concept-callout--definition');
  });
});