import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import AssessmentChecklist from '../AssessmentChecklist';

describe('AssessmentChecklist', () => {
  const defaultProps = {
    assessmentId: 'module-1-assessment-1',
    totalPoints: 10,
    items: [
      {
        category: 'Functionality',
        criteria: [
          {
            id: 'func-1',
            description: 'Node publishes messages correctly',
            points: 5,
          },
          {
            id: 'func-2',
            description: 'Node subscribes to topics correctly',
            points: 3,
          },
        ],
      },
      {
        category: 'Code Quality',
        criteria: [
          {
            id: 'cq-1',
            description: 'Code follows ROS 2 conventions',
            points: 2,
          },
        ],
      },
    ],
  };

  it('renders assessment checklist with title and progress', () => {
    render(<AssessmentChecklist {...defaultProps} />);
    expect(screen.getByText(/Assessment Checklist/)).toBeInTheDocument();
    expect(screen.getByText(/Progress: 0%/)).toBeInTheDocument();
    expect(screen.getByText(/0 \/ 10 points/)).toBeInTheDocument();
  });

  it('displays categories and criteria', () => {
    render(<AssessmentChecklist {...defaultProps} />);
    expect(screen.getByText(/Functionality/)).toBeInTheDocument();
    expect(screen.getByText(/Code Quality/)).toBeInTheDocument();
    expect(screen.getByText(/Node publishes messages correctly/)).toBeInTheDocument();
    expect(screen.getByText(/Code follows ROS 2 conventions/)).toBeInTheDocument();
  });

  it('shows points for each criterion', () => {
    render(<AssessmentChecklist {...defaultProps} />);
    expect(screen.getByText(/\(5 pts\)/)).toBeInTheDocument();
    expect(screen.getByText(/\(3 pts\)/)).toBeInTheDocument();
    expect(screen.getByText(/\(2 pts\)/)).toBeInTheDocument();
  });

  it('tracks completion of criteria', () => {
    render(<AssessmentChecklist {...defaultProps} />);
    const firstCheckbox = screen.getByLabelText(/Node publishes messages correctly \(5 points\)/);
    expect(firstCheckbox).not.toBeChecked();

    fireEvent.click(firstCheckbox);
    expect(firstCheckbox).toBeChecked();

    // Check that progress updates
    expect(screen.getByText(/Progress: 50%/)).toBeInTheDocument();
    expect(screen.getByText(/5 \/ 10 points/)).toBeInTheDocument();
  });

  it('updates total points when criteria are checked', () => {
    render(<AssessmentChecklist {...defaultProps} />);
    const checkboxes = screen.getAllByRole('checkbox');

    // Check the first two checkboxes (5 + 3 = 8 points)
    fireEvent.click(checkboxes[0]); // 5 points
    fireEvent.click(checkboxes[1]); // 3 points

    expect(screen.getByText(/8 \/ 10 points/)).toBeInTheDocument();
  });

  it('shows completion status when all criteria are met', () => {
    render(<AssessmentChecklist {...defaultProps} />);
    const checkboxes = screen.getAllByRole('checkbox');

    // Check all checkboxes
    checkboxes.forEach(checkbox => fireEvent.click(checkbox));

    expect(screen.getByText(/✅ Ready to Submit!/)).toBeInTheDocument();
    expect(screen.getByText(/All criteria met/)).toBeInTheDocument();
  });

  it('shows incomplete status when not all criteria are met', () => {
    render(<AssessmentChecklist {...defaultProps} />);
    expect(screen.getByText(/⚠️ Incomplete \(100% remaining\)/)).toBeInTheDocument();
  });

  it('has accessible labels for checkboxes', () => {
    render(<AssessmentChecklist {...defaultProps} />);
    const checkbox = screen.getByLabelText(/Node publishes messages correctly \(5 points\)/);
    expect(checkbox).toBeInTheDocument();
  });

  it('validates required props', () => {
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

    // @ts-expect-error - intentionally missing required props for testing
    const { container } = render(<AssessmentChecklist />);
    expect(container.firstChild).toBeNull();

    consoleSpy.mockRestore();
  });

  it('validates total points match criteria points', () => {
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

    render({
      ...defaultProps,
      totalPoints: 99, // Intentionally wrong total
    } as any);

    expect(consoleSpy).toHaveBeenCalledWith(
      expect.stringContaining('totalPoints (99) does not match sum of criteria points (10)')
    );

    consoleSpy.mockRestore();
  });

  it('has proper ARIA attributes', () => {
    render(<AssessmentChecklist {...defaultProps} />);
    expect(screen.getByRole('group', { name: /checklist-title/ })).toBeInTheDocument();
  });
});