---
title: "Assessment: ROS 2 Package Development Project"
description: Build a ROS 2 package that demonstrates publishers, subscribers, services, and URDF robot modeling
keywords: [ROS 2, package, publisher, subscriber, service, URDF, robotics, development]
sidebar_position: 1
sidebar_label: "ROS 2 Package Project"
estimated_time: 10
week: 5
module: 1
prerequisites: ["module-1-ros2"]
learning_objectives:
  - Create a complete ROS 2 package with proper structure and dependencies
  - Implement publishers and subscribers for sensor data streaming
  - Design and implement services for request/response communication
  - Model a robot using URDF and visualize in RViz2
  - Test and validate the package using ROS 2 tools
assessment_type: "project"
difficulty_level: "intermediate"
capstone_component: null
---

import LearningObjectives from '@site/src/components/LearningObjectives';
import Prerequisites from '@site/src/components/Prerequisites';
import AssessmentChecklist from '@site/src/components/learning/AssessmentChecklist';

# Assessment: ROS 2 Package Development Project

<LearningObjectives objectives={frontMatter.learning_objectives} />
<Prerequisites prereqs={frontMatter.prerequisites} estimatedTime={frontMatter.estimated_time} />

---

## Overview

In this assessment, you will build a complete ROS 2 package that demonstrates core communication patterns and robot modeling. You'll create a simulated robot system that includes publishers, subscribers, services, and a URDF model. This project will showcase your understanding of ROS 2 architecture and communication patterns.

## Learning Objectives Assessed

- [ ] Create a publisher node that publishes simulated sensor data
- [ ] Create a subscriber node that processes sensor data
- [ ] Implement a service server that responds to requests
- [ ] Create a client node that calls the service
- [ ] Define a robot model using URDF
- [ ] Visualize the robot in RViz2
- [ ] Launch the complete system using a launch file

## Scenario

You are developing a sensor monitoring system for a humanoid robot. The system must:
- Publish simulated sensor data (temperature, proximity, battery level)
- Subscribe to sensor data and log alerts when thresholds are exceeded
- Provide a diagnostic service that returns system health status
- Include a URDF model of the robot with at least 3 joints

## Requirements

### Functional Requirements

#### 1. Publisher Node (`sensor_publisher`)
- Publishes to `/sensors/temperature`, `/sensors/proximity`, and `/sensors/battery` topics
- Message types: `std_msgs/Float32` for all sensor data
- Publish rate: 1 Hz for temperature and battery, 10 Hz for proximity
- Simulate realistic sensor values with some random noise

#### 2. Subscriber Node (`sensor_subscriber`)
- Subscribes to all sensor topics
- Logs messages to console with timestamps
- Issues alerts when temperature > 80°C or battery < 20%
- Implements a simple moving average filter for noisy data

#### 3. Service Server (`diagnostic_server`)
- Provides `/diagnostics` service using `std_srvs/Trigger` type
- Returns system health status (OK, WARNING, ERROR)
- Checks all sensor values and returns appropriate status

#### 4. Service Client (`diagnostic_client`)
- Calls `/diagnostics` service every 5 seconds
- Logs health status to console
- Implements retry logic for failed service calls

#### 5. URDF Robot Model
- Create a simple humanoid robot model with at least 3 joints
- Include base_link, torso, and two limbs (arms or legs)
- Use appropriate visual and collision geometries
- Define joint limits and types appropriately

### Technical Requirements

- ROS 2 Humble Hawksbill
- Python 3.10+ with rclpy
- Package structure following ROS 2 conventions:
  ```
  ros2_sensor_package/
  ├── ros2_sensor_package/
  │   ├── sensor_publisher.py
  │   ├── sensor_subscriber.py
  │   ├── diagnostic_server.py
  │   ├── diagnostic_client.py
  │   └── __init__.py
  ├── urdf/
  │   └── simple_robot.urdf
  ├── launch/
  │   └── sensor_system_launch.py
  ├── test/
  │   └── test_nodes.py
  ├── CMakeLists.txt
  ├── package.xml
  └── setup.py
  ```
- Must include:
  - `package.xml` with dependencies (rclpy, std_msgs, std_srvs)
  - `setup.py` with entry points for nodes
  - `launch` file to start all nodes
  - `README.md` with usage instructions

## Assessment Rubric

| Criterion | Exemplary (100%) | Proficient (80%) | Developing (60%) | Beginning (40%) |
|-----------|------------------|------------------|------------------|-----------------|
| **Functionality** (40%) | All nodes work flawlessly, system meets all requirements, additional features implemented | Minor bugs, core features work, 1 requirement missing | Multiple features incomplete, significant bugs | Does not run or missing major functionality |
| **Code Quality** (30%) | Clean, well-documented, follows PEP 8, excellent error handling, comprehensive comments | Mostly clean, adequate docs, minor style issues, good error handling | Inconsistent style, limited docs, basic error handling | Hard to read, minimal docs, poor error handling |
| **ROS 2 Best Practices** (20%) | Proper QoS, node lifecycle, parameter usage, logging, appropriate message types | Good practices, minor issues (e.g., hardcoded values) | Some practices ignored, QoS defaults used without consideration | Poor practices, no consideration of ROS 2 patterns |
| **Documentation** (10%) | Comprehensive README, usage examples, troubleshooting, docstrings in all functions | Good README, basic usage, some docstrings | Minimal README, no usage examples, few docstrings | No README or documentation |

## Submission

1. Create a GitHub repository: `<your-username>-ros2-package-project`
2. Repository structure must match technical requirements above
3. Include a `REPORT.md` file that explains:
   - Design decisions you made
   - Challenges you faced and how you solved them
   - Testing approach you used
   - Possible improvements or extensions

## Self-Assessment Checklist

<AssessmentChecklist
  items={[
    "Package structure follows ROS 2 conventions",
    "All required nodes implemented and functional",
    "URDF model created with at least 3 joints",
    "Launch file starts all nodes correctly",
    "Service communication works as expected",
    "Code follows PEP 8 style guide",
    "Appropriate error handling implemented",
    "README.md includes usage instructions",
    "REPORT.md explains design decisions and challenges",
    "All dependencies properly declared in package.xml"
  ]}
/>

## Resources

- [Module 1: ROS 2](../module-1-ros2) - Core concepts and architecture
- [ROS 2 Humble Documentation](https://docs.ros.org/en/humble/) - Official ROS 2 documentation
- [URDF Tutorials](http://wiki.ros.org/urdf/Tutorials) - Robot modeling with URDF
- [ROS 2 Launch Files](https://docs.ros.org/en/humble/Tutorials/Launch-Files.html) - Creating launch files
- [ROS 2 Services](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html) - Service implementation

## Grading Notes

- **Late Submission**: -10% per day (max 3 days)
- **Partial Credit**: Available for incomplete but well-documented attempts
- **Code Quality**: Heavily weighted in evaluation
- **Testing**: Evidence of testing will positively impact your grade