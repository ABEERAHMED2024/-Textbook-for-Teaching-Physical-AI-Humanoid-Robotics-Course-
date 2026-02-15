import React from 'react';
import Link from '@docusaurus/Link';
import { useBaseUrl } from '@docusaurus/useBaseUrl';
import clsx from 'clsx';

import styles from './ModuleCard.module.css';

interface ModuleCardProps {
  id: string;
  title: string;
  weeks: string;
  description: string;
  learningOutcomes: string[];
  capstoneIntegration: string;
  position: number;
}

const ModuleCard: React.FC<ModuleCardProps> = ({
  id,
  title,
  weeks,
  description,
  learningOutcomes,
  capstoneIntegration,
  position,
}) => {
  return (
    <div className={clsx('col col--3', styles.moduleCard)}>
      <div className="card">
        <div className="card__header">
          <h3>
            <Link to={useBaseUrl(`/docs/module-${position}-intro`)}>
              {title}
            </Link>
          </h3>
          <small>{weeks}</small>
        </div>
        <div className="card__body">
          <p>{description}</p>
          <h4>Learning Outcomes:</h4>
          <ul>
            {learningOutcomes.slice(0, 3).map((outcome, index) => (
              <li key={index}>{outcome}</li>
            ))}
          </ul>
          <p><strong>Capstone Integration:</strong> {capstoneIntegration}</p>
        </div>
        <div className="card__footer">
          <Link
            className="button button--secondary button--block"
            to={useBaseUrl(`/docs/module-${position}-intro`)}>
            Start Module
          </Link>
        </div>
      </div>
    </div>
  );
};

export default ModuleCard;