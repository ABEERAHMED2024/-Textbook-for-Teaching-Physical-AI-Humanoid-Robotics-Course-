---
title: Glossary of Robotics Terms
description: Comprehensive glossary of robotics terms used throughout the Physical AI & Humanoid Robotics Textbook
keywords: [robotics, glossary, terminology, definitions]
sidebar_position: 1
sidebar_label: Glossary
---

<ChapterControls />

# Glossary of Robotics Terms

## A

### Actuator
**Definition**: A component of a robot that converts energy (electrical, hydraulic, or pneumatic) into mechanical motion$1 Common types include servo motors, stepper motors, and linear actuators$1

**Related Terms**: Motor, Joint, Control System

**Used In**: [Introduction](intro)
<!-- TODO: [Week 3: ROS 2 Architecture]($1$1/module-1-ros2/chapter-1-intro-ros2), [Week 4: Topics & Services]($1$1/module-1-ros2/chapter-2-nodes-topics) -->

### Artificial Intelligence (AI)
**Definition**: The simulation of human intelligence processes by machines, especially computer systems$1 In robotics, AI enables robots to perceive, reason, learn, and adapt to their environment$1

**Related Terms**: Machine Learning, Deep Learning, Cognitive Robotics

**Used In**: [Introduction](intro)
<!-- TODO: [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics) -->

### Autonomous System
**Definition**: A system that can operate independently without human intervention, making decisions based on its programming and environmental inputs$1

**Related Terms**: Autonomy, Control System, Perception

**Used In**: [Introduction](intro), [Module 4: VLA & Humanoids](module-4-vla-humanoids/index)

## B

### Behavior-Based Robotics
**Definition**: An approach to robotics that structures robot control systems as collections of individual behaviors that operate in parallel and compete for control of the robot$1

**Related Terms**: Control Architecture, Subsumption Architecture, Reactive Systems

**Used In**: <!-- TODO: [Week 4: Topics & Services]($1$1/module-1-ros2/chapter-2-nodes-topics) -->

### Bipedal Locomotion
**Definition**: The act of walking on two legs, a complex control problem in humanoid robotics that requires balance, coordination, and dynamic stability$1

**Related Terms**: Gait, Balance Control, Inverse Dynamics

**Used In**: [Module 4: VLA & Humanoids]($1$1/module-4-vla-humanoids/index$1mdx), [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation)

## C

### Cartesian Space
**Definition**: The 3D space defined by X, Y, and Z coordinates, as opposed to joint space which is defined by joint angles$1 In robotics, this is used to describe the position and orientation of an end-effector$1

**Related Terms**: Joint Space, End-Effector, Kinematics

**Used In**: [Week 5: URDF]($1$1/module-1-ros2/chapter-4-urdf-robot-modeling), [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics)

### Control System
**Definition**: A system that manages, commands, directs, or regulates the behavior of other devices or systems$1 In robotics, this typically refers to the algorithms and hardware that determine how a robot moves and responds to its environment$1

**Related Terms**: Actuator, Sensor, Feedback Control

**Used In**: [Week 3: ROS 2 Architecture]($1$1/module-1-ros2/chapter-1-intro-ros2), [Week 4: Topics & Services]($1$1/module-1-ros2/chapter-2-nodes-topics)

### Computer Vision
**Definition**: A field of artificial intelligence that trains computers to interpret and understand the visual world$1 Using digital images from cameras and videos and deep learning models, machines can accurately identify and classify objects and react accordingly$1

**Related Terms**: Perception, Image Processing, Object Recognition

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 9: Isaac ROS & VSLAM]($1$1/module-3-isaac/week-9-isaac-ros-vslam$1md)

## D

### Degrees of Freedom (DOF)
**Definition**: The number of independent movements a mechanical system can make$1 In robotics, this refers to the number of joints or independent movements a robot or robot arm can perform$1

**Related Terms**: Joint, Kinematics, Workspace

**Used In**: [Week 5: URDF]($1$1/module-1-ros2/chapter-4-urdf-robot-modeling), [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics)

### Differential Drive
**Definition**: A common drive mechanism used in mobile robotics that uses two wheels mounted on a common axis and a set of castor wheels for balance$1 The robot is turned by driving the wheels at different speeds$1

**Related Terms**: Mobile Robot, Wheel Odometry, Navigation

**Used In**: [Module 2: Digital Twin]($1$1/module-2-digital-twin/index$1md), [Week 6: Gazebo]($1$1/module-2-digital-twin/week-6-gazebo$1md)

### Direct Kinematics
**Definition**: The process of calculating the position and orientation of the end-effector of a robot arm given the joint angles$1 Also known as forward kinematics$1

**Related Terms**: Forward Kinematics, Inverse Kinematics, Joint Space

**Used In**: [Week 5: URDF]($1$1/module-1-ros2/chapter-4-urdf-robot-modeling), [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics)

## E

### End-Effector
**Definition**: The device at the end of a robotic arm that interacts with the environment$1 This can be a gripper, tool, or sensor depending on the robot's intended function$1

**Related Terms**: Manipulator, Tool Center Point, Gripper

**Used In**: [Week 5: URDF]($1$1/module-1-ros2/week-5-urdf$1md), [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation$1md)

### Embodiment
**Definition**: The physical form of a robot, including its shape, size, and sensory-motor capabilities$1 The concept that intelligence emerges from the interaction between an agent and its environment$1

**Related Terms**: Morphology, Sensorimotor Loop, Situated Cognition

**Used In**: [Introduction]($1$1/intro$1mdx), [Module 4: VLA & Humanoids]($1$1/module-4-vla-humanoids/index$1md)

## F

### Feedback Control
**Definition**: A control system that uses sensors to monitor the output of a system and adjusts the input to achieve the desired output$1 Essential for stable robot control$1

**Related Terms**: PID Controller, Sensor, Actuator

**Used In**: [Week 3: ROS 2 Architecture]($1$1/module-1-ros2/week-3-architecture$1md), [Week 10: Nav2 & Reinforcement Learning]($1$1/module-3-isaac/week-10-nav2-rl$1md)

### Forward Kinematics
**Definition**: The process of calculating the position and orientation of the end-effector of a robot arm given the joint angles$1 Also known as direct kinematics$1

**Related Terms**: Direct Kinematics, Inverse Kinematics, Joint Space

**Used In**: [Week 5: URDF]($1$1/module-1-ros2/chapter-4-urdf-robot-modeling), [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics)

### Force Control
**Definition**: A control strategy that regulates the forces applied by a robot to its environment, often used in tasks requiring precise interaction with objects$1

**Related Terms**: Impedance Control, Compliance, Haptic Feedback

**Used In**: [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation$1md)

## G

### Gazebo
**Definition**: A 3D simulation environment for robotics that provides realistic physics simulation, high-quality graphics, and convenient programmatic interfaces$1 Commonly used with ROS$1

**Related Terms**: Simulation, Physics Engine, Robot Simulation

**Used In**: [Module 2: Digital Twin]($1$1/module-2-digital-twin/index$1md), [Week 6: Gazebo]($1$1/module-2-digital-twin/week-6-gazebo$1md)

### General-Purpose Robot
**Definition**: A robot designed to perform a variety of tasks rather than being specialized for a single function$1 These robots typically have more degrees of freedom and flexible programming$1

**Related Terms**: Specialized Robot, Manipulator, Task Flexibility

**Used In**: [Introduction]($1$1/intro$1mdx), [Module 4: VLA & Humanoids]($1$1/module-4-vla-humanoids/index$1md)

### Gripper
**Definition**: An end-effector designed to grasp and hold objects$1 Can be mechanical (with fingers), vacuum-based, or magnetic depending on the application$1

**Related Terms**: End-Effector, Manipulator, Grasping

**Used In**: [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation$1md)

## H

### Hardware-in-the-Loop (HIL)
**Definition**: A testing technique that involves connecting physical hardware components to a simulation environment to validate system behavior under realistic conditions$1

**Related Terms**: Simulation, Testing, Validation

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 8: Isaac Sim]($1$1/module-3-isaac/week-8-isaac-sim$1md)

### Haptic Feedback
**Definition**: The use of touch and motion to communicate with the user, often implemented in robotic systems to provide tactile information about the environment$1

**Related Terms**: Force Control, Tactile Sensors, Teleoperation

**Used In**: [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation$1md)

### Humanoid Robot
**Definition**: A robot with a human-like body structure, typically featuring a head, torso, two arms, and two legs$1 Designed to operate in human environments$1

**Related Terms**: Bipedal Locomotion, Anthropomorphic Design, Social Robotics

**Used In**: [Introduction]($1$1/intro$1mdx), [Module 4: VLA & Humanoids]($1$1/module-4-vla-humanoids/index$1md)

## I

### Inverse Dynamics
**Definition**: The calculation of the forces and torques required to generate a specific motion of a robot, taking into account the robot's mass, inertia, and external forces$1

**Related Terms**: Forward Dynamics, Kinematics, Force Control

**Used In**: [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics$1md), [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation$1md)

### Inverse Kinematics
**Definition**: The process of calculating the joint angles required to position the end-effector of a robot arm at a specific location and orientation$1

**Related Terms**: Forward Kinematics, Joint Space, Workspace

**Used In**: [Week 5: URDF]($1$1/module-1-ros2/chapter-4-urdf-robot-modeling), [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics)

### IMU (Inertial Measurement Unit)
**Definition**: A device that measures and reports a body's specific force, angular rate, and sometimes the magnetic field surrounding the body, using a combination of accelerometers, gyroscopes, and magnetometers$1

**Related Terms**: Sensor, Accelerometer, Gyroscope

**Used In**: [Week 7: Unity Sensors]($1$1/module-2-digital-twin/week-7-unity-sensors$1md)

## J

### Jacobian Matrix
**Definition**: A matrix that describes the relationship between the joint velocities of a robot and the linear and angular velocities of its end-effector$1

**Related Terms**: Kinematics, Velocity, Manipulator

**Used In**: [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics$1md)

### Joint
**Definition**: A connection between two or more links in a robot that allows relative motion between them$1 Joints can be revolute (rotary), prismatic (linear), or more complex$1

**Related Terms**: Link, Degrees of Freedom, Actuator

**Used In**: [Week 5: URDF]($1$1/module-1-ros2/chapter-4-urdf-robot-modeling), [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics)

## K

### Kinematics
**Definition**: The study of motion without considering the forces that cause the motion$1 In robotics, it refers to the relationship between joint positions and the position and orientation of the end-effector$1

**Related Terms**: Forward Kinematics, Inverse Kinematics, Jacobian

**Used In**: [Week 5: URDF]($1$1/module-1-ros2/chapter-4-urdf-robot-modeling), [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics)

### Kinesthetic Teaching
**Definition**: A method of programming a robot by physically guiding it through the desired motions, allowing the robot to learn and repeat the demonstrated behavior$1

**Related Terms**: Programming by Demonstration, Learning from Demonstration, Physical Human-Robot Interaction

**Used In**: [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation$1md)

## L

### LIDAR (Light Detection and Ranging)
**Definition**: A remote sensing method that uses light in the form of a pulsed laser to measure distances to objects, creating precise, three-dimensional information about the surrounding environment$1

**Related Terms**: Sensor, Range Finder, SLAM

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 9: Isaac ROS & VSLAM]($1$1/module-3-isaac/week-9-isaac-ros-vslam$1md)

### Localization
**Definition**: The process by which a robot determines its position and orientation in a given environment, often using sensors and maps$1

**Related Terms**: Mapping, SLAM, Navigation

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 10: Nav2 & Reinforcement Learning]($1$1/module-3-isaac/week-10-nav2-rl$1md)

### Learning from Demonstration
**Definition**: A technique in robotics where a robot learns a task by observing and imitating human demonstrations, reducing the need for explicit programming$1

**Related Terms**: Programming by Demonstration, Imitation Learning, Kinesthetic Teaching

**Used In**: [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation$1md)

## M

### Manipulator
**Definition**: A robot arm designed to manipulate objects in its environment, typically consisting of multiple links connected by joints and ending in an end-effector$1

**Related Terms**: End-Effector, Joint, Degrees of Freedom

**Used In**: [Week 5: URDF]($1$1/module-1-ros2/week-5-urdf$1md), [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation$1md)

### Mobile Robot
**Definition**: A robot that is capable of moving around in its environment, as opposed to being fixed in one location$1 Includes wheeled, legged, and tracked robots$1

**Related Terms**: Differential Drive, Navigation, Locomotion

**Used In**: [Module 2: Digital Twin]($1$1/module-2-digital-twin/index$1md), [Week 6: Gazebo]($1$1/module-2-digital-twin/week-6-gazebo$1md)

### Motion Planning
**Definition**: The computational problem of finding a valid sequence of configurations to move a robot from a start state to a goal state while avoiding obstacles$1

**Related Terms**: Path Planning, Trajectory Generation, Collision Detection

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 10: Nav2 & Reinforcement Learning]($1$1/module-3-isaac/week-10-nav2-rl$1md)

## N

### Navigation
**Definition**: The ability of a robot to move through an environment to reach a desired destination, typically involving localization, mapping, and path planning$1

**Related Terms**: Localization, Mapping, SLAM, Path Planning

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 10: Nav2 & Reinforcement Learning]($1$1/module-3-isaac/week-10-nav2-rl$1md)

### Node
**Definition**: In ROS (Robot Operating System), a process that performs computation$1 Nodes are the fundamental building blocks of ROS applications and communicate with each other via topics, services, and actions$1

**Related Terms**: ROS, Topic, Service, Process

**Used In**: [Week 3: ROS 2 Architecture]($1$1/module-1-ros2/chapter-1-intro-ros2), [Week 4: Topics & Services]($1$1/module-1-ros2/chapter-2-nodes-topics)

## O

### Odometry
**Definition**: The use of data from motion sensors to estimate change in position over time$1 In robotics, it typically refers to estimating position based on wheel rotations or other motion sensors$1

**Related Terms**: Localization, Sensor Fusion, Differential Drive

**Used In**: [Module 2: Digital Twin]($1$1/module-2-digital-twin/index$1md), [Week 6: Gazebo]($1$1/module-2-digital-twin/week-6-gazebo$1md)

### Operational Space
**Definition**: The space in which the robot's end-effector operates, typically defined by Cartesian coordinates (position and orientation) rather than joint angles$1

**Related Terms**: Cartesian Space, Joint Space, Task Space

**Used In**: [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics$1md)

## P

### Path Planning
**Definition**: The computational process of determining a route from a starting point to a destination, considering obstacles and other constraints$1

**Related Terms**: Motion Planning, Navigation, Trajectory Generation

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 10: Nav2 & Reinforcement Learning]($1$1/module-3-isaac/week-10-nav2-rl$1md)

### Perception
**Definition**: The ability of a robot to interpret sensory information from its environment, including vision, touch, sound, and other modalities$1

**Related Terms**: Computer Vision, Sensor, SLAM

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 9: Isaac ROS & VSLAM]($1$1/module-3-isaac/week-9-isaac-ros-vslam$1md)

### PID Controller
**Definition**: A control loop feedback mechanism widely used in robotics and industrial control systems$1 It calculates an error value as the difference between a desired setpoint and a measured process variable and applies a correction based on proportional, integral, and derivative terms$1

**Related Terms**: Feedback Control, Control System, Tuning

**Used In**: [Week 3: ROS 2 Architecture]($1$1/module-1-ros2/week-3-architecture$1md), [Week 10: Nav2 & Reinforcement Learning]($1$1/module-3-isaac/week-10-nav2-rl$1md)

## R

### Range Finder
**Definition**: A sensor that measures the distance to objects in the environment, including technologies like LIDAR, sonar, and structured light systems$1

**Related Terms**: LIDAR, Sonar, Sensor, SLAM

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 9: Isaac ROS & VSLAM]($1$1/module-3-isaac/week-9-isaac-ros-vslam$1md)

### ROS (Robot Operating System)
**Definition**: A flexible framework for writing robot software that provides services designed for a heterogeneous computer cluster such as hardware abstraction, device drivers, libraries, visualizers, message-passing, package management, and more$1

**Related Terms**: Node, Topic, Service, Package

**Used In**: [Week 3: ROS 2 Architecture]($1$1/module-1-ros2/chapter-1-intro-ros2), [Week 4: Topics & Services]($1$1/module-1-ros2/chapter-2-nodes-topics)

### Robot Operating System (ROS)
**Definition**: See ROS (Robot Operating System)$1

**Related Terms**: ROS

**Used In**: [Week 3: ROS 2 Architecture]($1$1/module-1-ros2/week-3-architecture$1md)

## S

### SLAM (Simultaneous Localization and Mapping)
**Definition**: The computational problem of constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it$1

**Related Terms**: Localization, Mapping, Navigation, LIDAR

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 9: Isaac ROS & VSLAM]($1$1/module-3-isaac/week-9-isaac-ros-vslam$1md)

### Sensor Fusion
**Definition**: The process of combining data from multiple sensors to improve the accuracy and reliability of information obtained from the environment$1

**Related Terms**: Perception, Sensor, Kalman Filter

**Used In**: [Week 7: Unity Sensors]($1$1/module-2-digital-twin/week-7-unity-sensors$1md)

### Servo Motor
**Definition**: A rotary actuator that allows for precise control of angular position, velocity, and acceleration$1 Consists of a motor coupled to a sensor for position feedback$1

**Related Terms**: Actuator, Motor, Feedback Control

**Used In**: [Week 3: ROS 2 Architecture]($1$1/module-1-ros2/week-3-architecture$1md)

## T

### Teleoperation
**Definition**: The remote operation of a robot by a human operator, often used for tasks that are too dangerous or difficult for direct human involvement$1

**Related Terms**: Human-Robot Interaction, Remote Control, Haptic Feedback

**Used In**: [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation$1md)

### Trajectory Generation
**Definition**: The process of creating a time-parameterized path that specifies the position, velocity, and acceleration of a robot over time$1

**Related Terms**: Path Planning, Motion Planning, Interpolation

**Used In**: [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics$1md)

### Topic
**Definition**: In ROS, a named bus over which nodes exchange messages$1 Topics implement a publish-subscribe communication pattern$1

**Related Terms**: ROS, Node, Message, Publish-Subscribe

**Used In**: [Week 4: Topics & Services]($1$1/module-1-ros2/week-4-topics-services$1md)

## U

### URDF (Unified Robot Description Format)
**Definition**: An XML format for representing a robot model in ROS, including physical properties, visual representation, and kinematic structure$1

**Related Terms**: Robot Model, XML, ROS, Kinematics

**Used In**: [Week 5: URDF]($1$1/module-1-ros2/week-5-urdf$1md)

### Underactuated System
**Definition**: A mechanical system with fewer actuators than degrees of freedom, making it challenging to control but often more energy-efficient$1

**Related Terms**: Degrees of Freedom, Actuator, Control

**Used In**: [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics$1md)

## V

### Visual Servoing
**Definition**: A technique in robotics that uses visual feedback to control the motion of a robot, typically to position an end-effector relative to objects in the environment$1

**Related Terms**: Computer Vision, Feedback Control, Manipulation

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 9: Isaac ROS & VSLAM]($1$1/module-3-isaac/week-9-isaac-ros-vslam$1md)

### VSLAM (Visual Simultaneous Localization and Mapping)
**Definition**: A variant of SLAM that uses visual sensors (cameras) instead of or in addition to other sensors like LIDAR for mapping and localization$1

**Related Terms**: SLAM, Computer Vision, Mapping

**Used In**: [Module 3: NVIDIA Isaac]($1$1/module-3-isaac/index$1md), [Week 9: Isaac ROS & VSLAM]($1$1/module-3-isaac/week-9-isaac-ros-vslam$1md)

## W

### Workspace
**Definition**: The volume of space that a robot's end-effector can reach$1 This can be classified as the reachable workspace (positions the end-effector can reach) or the dexterous workspace (positions with all orientations)$1

**Related Terms**: Kinematics, Reach, Manipulator

**Used In**: [Week 11: Kinematics]($1$1/module-4-vla-humanoids/week-11-kinematics$1md)

### Wheeled Mobile Robot
**Definition**: A mobile robot that uses wheels for locomotion, including configurations like differential drive, Ackermann steering, and omnidirectional wheels$1

**Related Terms**: Mobile Robot, Differential Drive, Locomotion

**Used In**: [Module 2: Digital Twin]($1$1/module-2-digital-twin/index$1md), [Week 6: Gazebo]($1$1/module-2-digital-twin/week-6-gazebo$1md)

## X, Y, Z

### Zero Moment Point (ZMP)
**Definition**: A concept used in bipedal robotics to describe the point on the ground where the sum of all moments of the ground reaction forces equals zero, important for balance control$1

**Related Terms**: Bipedal Locomotion, Balance Control, Stability

**Used In**: [Module 4: VLA & Humanoids]($1$1/module-4-vla-humanoids/index$1md), [Week 12: Manipulation]($1$1/module-4-vla-humanoids/week-12-manipulation$1md)