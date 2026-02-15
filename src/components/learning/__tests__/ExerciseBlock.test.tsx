import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import ExerciseBlock from '../ExerciseBlock';

describe('ExerciseBlock', () => {
  const defaultProps = {
    title: 'Build a Publisher Node',
    difficulty: 'beginner' as const,
    estimatedTime: 15,
    objectives: ['Create a publisher', 'Publish messages'],
  };

  it('renders exercise title and meta information', () => {
    render(<ExerciseBlock {...defaultProps} />);
    expect(screen.getByText(/Build a Publisher Node/)).toBeInTheDocument();
    expect(screen.getByText(/Beginner/)).toBeInTheDocument();
    expect(screen.getByText(/~15 min/)).toBeInTheDocument();
  });

  it('displays learning objectives as checkboxes', () => {
    render(<ExerciseBlock {...defaultProps} />);
    expect(screen.getByLabelText(/Create a publisher/)).toBeInTheDocument();
    expect(screen.getByLabelText(/Publish messages/)).toBeInTheDocument();
  });

  it('tracks objective completion', () => {
    render(<ExerciseBlock {...defaultProps} />);
    const firstCheckbox = screen.getByLabelText(/Create a publisher/);
    expect(firstCheckbox).not.toBeChecked();

    fireEvent.click(firstCheckbox);
    expect(firstCheckbox).toBeChecked();
  });

  it('shows progress percentage', () => {
    render(<ExerciseBlock {...defaultProps} />);
    expect(screen.getByText(/Progress: 0%/)).toBeInTheDocument();

    fireEvent.click(screen.getByLabelText(/Create a publisher/));
    expect(screen.getByText(/Progress: 50%/)).toBeInTheDocument();
  });

  it('expands hints when clicked', () => {
    const propsWithHints = {
      ...defaultProps,
      hints: ['Hint 1', 'Hint 2'],
    };

    render(<ExerciseBlock {...propsWithHints} />);
    expect(screen.queryByText(/Hint 1/)).not.toBeInTheDocument();

    fireEvent.click(screen.getByText(/View Hints/));
    expect(screen.getByText(/Hint 1/)).toBeInTheDocument();
    expect(screen.getByText(/Hint 2/)).toBeInTheDocument();
  });

  it('expands solution when clicked', () => {
    const propsWithSolution = {
      ...defaultProps,
      solutionCode: 'some/path/to/solution.py',
    };

    render(<ExerciseBlock {...propsWithSolution} />);
    expect(screen.queryByText(/Download complete solution/)).not.toBeInTheDocument();

    fireEvent.click(screen.getByText(/View Solution/));
    expect(screen.getByText(/Download complete solution/)).toBeInTheDocument();
  });

  it('has accessible labels', () => {
    render(<ExerciseBlock {...defaultProps} id="ex1" />);
    expect(screen.getByRole('complementary', { name: /Exercise: Build a Publisher Node/i })).toBeInTheDocument();
  });

  it('validates required props', () => {
    // Test that component handles missing required props gracefully
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

    // @ts-expect-error - intentionally missing required props for testing
    const { container } = render(<ExerciseBlock />);
    expect(container.firstChild).toBeNull();

    consoleSpy.mockRestore();
  });
});