import React from 'react';
import Link from '@docusaurus/Link';
import { useBaseUrl } from '@docusaurus/useBaseUrl';

import styles from './RecentUpdates.module.css';

const RecentUpdates: React.FC = () => {
  // In a real implementation, this would fetch from a blog or changelog
  const recentUpdates = [
    {
      id: '2025-11-25-week-3-content',
      title: 'Week 3: ROS 2 Architecture Content Added',
      date: '2025-11-25',
      excerpt: 'Added comprehensive content covering ROS 2 architecture, nodes, topics, and services.',
    },
    {
      id: '2025-11-20-setup-guides',
      title: 'Hardware Setup Guides Updated',
      date: '2025-11-20',
      excerpt: 'Updated setup guides for workstation, edge kit, and cloud configurations.',
    },
    {
      id: '2025-11-15-module-1-outline',
      title: 'Module 1 Outline Published',
      date: '2025-11-15',
      excerpt: 'Published detailed outline for Module 1: The Robotic Nervous System (ROS 2).',
    },
  ];

  return (
    <div className="col col--4">
      <div className="card">
        <div className="card__header">
          <h3>Recent Updates</h3>
        </div>
        <div className="card__body">
          <ul className={styles.recentUpdatesList}>
            {recentUpdates.map((update) => (
              <li key={update.id} className={styles.updateItem}>
                <h4>
                  <Link to={useBaseUrl(`/blog/${update.id}`)}>
                    {update.title}
                  </Link>
                </h4>
                <small className={styles.updateDate}>{update.date}</small>
                <p>{update.excerpt}</p>
              </li>
            ))}
          </ul>
        </div>
        <div className="card__footer">
          <Link
            className="button button--secondary button--block"
            to={useBaseUrl('/blog')}>
            View All Updates
          </Link>
        </div>
      </div>
    </div>
  );
};

export default RecentUpdates;