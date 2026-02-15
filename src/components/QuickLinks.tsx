import React from 'react';
import Link from '@docusaurus/Link';
import GlossarySearch from './GlossarySearch';

// Import glossary data - in a real implementation this would come from a JSON file
// For now, we'll define a minimal set of entries for the search component to work
const glossaryData = [
  { id: 'robot', term: 'Robot', definition: 'A machine capable of carrying out complex actions automatically.' },
  { id: 'ai', term: 'Artificial Intelligence', definition: 'The simulation of human intelligence processes by machines.' },
  { id: 'ros', term: 'ROS', definition: 'Robot Operating System - a flexible framework for writing robot software.' },
  { id: 'actuator', term: 'Actuator', definition: 'A component of a robot that converts energy into mechanical motion.' },
  { id: 'sensor', term: 'Sensor', definition: 'A device that detects and responds to some type of input from the physical environment.' }
];

export default function QuickLinks(): JSX.Element {
  const links = [
    { title: 'Workstation Setup', to: '/docs/setup/workstation' },
    { title: 'Edge Kit Setup', to: '/docs/setup/edge-kit' },
    { title: 'Cloud Setup', to: '/docs/setup/cloud' },
    { title: 'Glossary', to: '/docs/references/glossary' },
    { title: 'Module 1: ROS 2', to: '/docs/module-1-ros2' },
    { title: 'Module 2: Digital Twin', to: '/docs/module-2-digital-twin' },
    { title: 'Module 3: Isaac Sim', to: '/docs/module-3-isaac' },
    { title: 'Module 4: VLA & Humanoids', to: '/docs/module-4-vla-humanoids' },
  ];

  return (
    <div className="quick-links-sidebar">
      <h3>Quick Links</h3>
      <ul>
        {links.map((link, index) => (
          <li key={index}>
            <Link to={link.to}>{link.title}</Link>
          </li>
        ))}
      </ul>
      <div className="glossary-search-section">
        <h3>Search Glossary</h3>
        <GlossarySearch glossaryData={glossaryData} />
      </div>
    </div>
  );
}
