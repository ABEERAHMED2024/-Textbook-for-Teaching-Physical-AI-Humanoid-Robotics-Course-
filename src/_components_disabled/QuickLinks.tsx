import React from 'react';
import Link from '@docusaurus/Link';
import { useBaseUrl } from '@docusaurus/useBaseUrl';

import styles from './QuickLinks.module.css';

const QuickLinks: React.FC = () => {
  return (
    <div className="col col--3">
      <div className="card">
        <div className="card__header">
          <h3>Quick Access</h3>
        </div>
        <div className="card__body">
          <ul className={styles.quickLinksList}>
            <li>
              <Link to={useBaseUrl('/docs/setup/workstation')}>
                🖥️ Workstation Setup
              </Link>
            </li>
            <li>
              <Link to={useBaseUrl('/docs/setup/edge-kit')}>
                🤖 Edge Kit Setup
              </Link>
            </li>
            <li>
              <Link to={useBaseUrl('/docs/setup/cloud')}>
                ☁️ Cloud Setup
              </Link>
            </li>
            <li>
              <Link to={useBaseUrl('/docs/assessments')}>
                📝 Assessments
              </Link>
            </li>
            <li>
              <Link to={useBaseUrl('/docs/references/glossary')}>
                📖 Glossary
              </Link>
            </li>
            <li>
              <Link to={useBaseUrl('/docs/instructors/guide')}>
                👨‍🏫 Instructors
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default QuickLinks;