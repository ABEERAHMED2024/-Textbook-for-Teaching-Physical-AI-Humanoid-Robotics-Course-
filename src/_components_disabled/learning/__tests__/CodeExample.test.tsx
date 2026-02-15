import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import CodeExample from '../CodeExample';

describe('CodeExample', () => {
  const defaultProps = {
    language: 'python' as const,
    children: 'print("Hello World")',
  };

  it('renders code with syntax highlighting', () => {
    render(<CodeExample {...defaultProps} />);
    expect(screen.getByText(/print/)).toBeInTheDocument();
  });

  it('shows solution toggle when solutionCode provided', () => {
    render(
      <CodeExample
        {...defaultProps}
        solutionCode={`print("Complete solution")`}
      />
    );
    expect(screen.getByRole('button', { name: /view solution/i })).toBeInTheDocument();
  });

  it('toggles between skeleton and solution', () => {
    render(
      <CodeExample
        {...defaultProps}
        solutionCode={`print("Solution")`}
      >
        {`# TODO: Implement`}
      </CodeExample>
    );
    const toggleButton = screen.getByRole('button', { name: /view solution/i });
    fireEvent.click(toggleButton);
    expect(screen.getByText(/Solution/)).toBeInTheDocument();
    expect(screen.queryByText(/TODO/)).not.toBeInTheDocument();
  });

  it('copies code to clipboard', async () => {
    Object.assign(navigator, {
      clipboard: {
        writeText: jest.fn().mockResolvedValue(undefined),
      },
    });

    render(
      <CodeExample {...defaultProps}>
        {`print("Test")`}
      </CodeExample>
    );
    const copyButton = screen.getByRole('button', { name: /copy/i });
    fireEvent.click(copyButton);

    await waitFor(() => {
      expect(navigator.clipboard.writeText).toHaveBeenCalledWith(`print("Test")`);
    });
  });

  it('displays difficulty and time badges', () => {
    render(
      <CodeExample
        {...defaultProps}
        difficulty="beginner"
        estimatedTime={15}
      >
        {`print("Test")`}
      </CodeExample>
    );
    expect(screen.getByText(/Beginner/)).toBeInTheDocument();
    expect(screen.getByText(/~15 min/)).toBeInTheDocument();
  });

  it('has accessible labels', () => {
    render(
      <CodeExample {...defaultProps} filename="test.py">
        {`print("Test")`}
      </CodeExample>
    );
    expect(screen.getByRole('region', { name: /code example: test\.py/i })).toBeInTheDocument();
  });

  it('supports keyboard navigation', () => {
    render(
      <CodeExample
        {...defaultProps}
        solutionCode={`print("Solution")`}
      >
        {`# TODO`}
      </CodeExample>
    );
    const copyButton = screen.getByRole('button', { name: /copy/i });
    copyButton.focus();
    expect(document.activeElement).toBe(copyButton);

    fireEvent.keyDown(copyButton, { key: 'Tab' });
    const toggleButton = screen.getByRole('button', { name: /view solution/i });
    expect(document.activeElement).toBe(toggleButton);
  });
});