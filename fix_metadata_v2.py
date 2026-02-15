import os
import re

# This script standardizes the metadata for the newly created weekly chapters 
# to ensure they pass the 'npm run validate-metadata' check.

def fix_metadata():
    files = {
        'docs/week-1-foundations.mdx': {
            'title': "Week 1: Foundations of Physical AI & Humanoid Robotics",
            'description': "Understand the core principles of Physical AI, embodied intelligence, and how robots interact with the physical laws of nature.",
            'keywords': ["Physical AI", "Embodied Intelligence", "Robotics Foundations", "Artificial Intelligence", "Humanoid Robotics"],
            'estimated_time': 240,
            'content_type': "concept",
            'difficulty': "beginner",
            'learning_objectives': [
                "Understand the definition of Physical AI and how it differs from traditional AI",
                "Analyze the concept of embodied intelligence in robotics",
                "Evaluate the role of physics in robotic decision making",
                "Understand the history and future of humanoid robotics"
            ]
        },
        'docs/week-2-sensors.mdx': {
            'title': "Week 2: Sensor Systems & Perception in Physical AI",
            'description': "Explore the 'eyes and ears' of robots: LiDAR, depth cameras, IMUs, and force sensors for environmental perception.",
            'keywords': ["Sensors", "LiDAR", "IMU", "Camera", "Perception", "Robotics", "Computer Vision"],
            'estimated_time': 300,
            'content_type': "concept",
            'difficulty': "beginner",
            'learning_objectives': [
                "Understand different types of robotic sensors and their specific use cases",
                "Analyze the difference between active and passive sensing systems",
                "Understand the role of IMUs in robot balance",
                "Analyze camera data for depth and distance estimation"
            ]
        },
        'docs/module-2-digital-twin/week-6-gazebo.mdx': {
            'title': "Week 6: Physics-Accurate Simulation with Gazebo",
            'description': "Learn to build physics-accurate simulations using Gazebo and ROS 2 for testing humanoid robot behaviors.",
            'keywords': ["Gazebo", "Simulation", "ROS 2", "Physics Engine", "URDF", "Robotics"],
            'estimated_time': 480,
            'content_type': "tutorial",
            'difficulty': "intermediate",
            'learning_objectives': [
                "Build Gazebo setup with ROS 2 integration for simulation",
                "Design physics-accurate worlds using SDF (Simulation Description Format)",
                "Create URDF models and spawn them into a simulated environment",
                "Demonstrate how to control a simulated robot using ROS 2 topics"
            ]
        },
        'docs/module-2-digital-twin/week-7-unity-sensors.mdx': {
            'title': "Week 7: Unity for Photorealistic Sensor Simulation",
            'description': "Leverage Game Engines for high-fidelity sensor simulation, computer vision, and synthetic data generation.",
            'keywords': ["Unity", "Simulation", "Robotics", "Computer Vision", "Synthetic Data", "VLA"],
            'estimated_time': 480,
            'content_type': "tutorial",
            'difficulty': "intermediate",
            'learning_objectives': [
                "Understand why Unity is used for computer vision in robotics research",
                "Build URDF importers to bring ROS models into Unity GameObjects",
                "Analyze photorealistic camera data with realistic environmental noise",
                "Implement a ROS-TCP Connector to bridge Unity and ROS 2"
            ]
        },
        'docs/module-3-isaac/week-8-isaac-sim.mdx': {
            'title': "Week 8: NVIDIA Isaac Sim & Omniverse Ecosystem",
            'description': "Master GPU-accelerated simulation with NVIDIA Isaac Sim for wide-scale robotic AI training.",
            'keywords': ["Isaac Sim", "Omniverse", "NVIDIA", "GPU Simulation", "Digital Twin", "Reinforcement Learning"],
            'estimated_time': 600,
            'content_type': "concept",
            'difficulty': "intermediate",
            'learning_objectives': [
                "Understand the installation and configuration of Isaac Sim workstations",
                "Analyze the Omniverse ecosystem and USD (Universal Scene Description)",
                "Demonstrate high-speed physics simulation on the GPU",
                "Build simple locomotion policies using Isaac Gym"
            ]
        },
        'docs/module-3-isaac/week-9-isaac-ros-vslam.mdx': {
            'title': "Week 9: Isaac ROS & Visual SLAM Acceleration",
            'description': "Deploy hardware-accelerated perception pipelines with Isaac ROS for real-time humanoid localization.",
            'keywords': ["Isaac ROS", "VSLAM", "Visual Odometry", "Perception", "NVIDIA Jetson", "GPU acceleration"],
            'estimated_time': 480,
            'content_type': "tutorial",
            'difficulty': "advanced",
            'learning_objectives': [
                "Build NVIDIA Isaac ROS GEMs for hardware acceleration",
                "Implement Visual SLAM (VSLAM) for robot localization in complex maps",
                "Design perception pipelines optimized for edge devices like Jetson Orin",
                "Analyze visual odometry integration with legged robot state estimation"
            ]
        },
        'docs/module-3-isaac/week-10-nav2-rl.mdx': {
            'title': "Week 10: Nav2 Navigation & Reinforcement Learning",
            'description': "Implement autonomous navigation and learn the foundations of Reinforcement Learning for robot control.",
            'keywords': ["Navigation", "Nav2", "Reinforcement Learning", "RL", "Motion Planning", "Robotics"],
            'estimated_time': 600,
            'content_type': "tutorial",
            'difficulty': "advanced",
            'learning_objectives': [
                "Build the ROS 2 Navigation Stack (Nav2) for humanoid platforms",
                "Understand costmaps, planners, and behavior tree controllers",
                "Create a simple locomotion policy using Reinforcement Learning in Isaac",
                "Analyze the tradeoffs between classical navigation and RL-based control"
            ]
        },
        'docs/module-4-vla-humanoids/week-11-kinematics.mdx': {
            'title': "Week 11: Humanoid Kinematics, Balance & Control",
            'description': "Master the mathematics of humanoid movement, forward/inverse kinematics, and ZMP stability.",
            'keywords': ["Kinematics", "Inverse Kinematics", "Balance", "Center of Mass", "ZMP", "Humanoids"],
            'estimated_time': 600,
            'content_type': "concept",
            'difficulty': "advanced",
            'learning_objectives': [
                "Build Forward and Inverse Kinematics solvers for humanoid limbs",
                "Understand the Zero Moment Point (ZMP) algorithm for dynamic balance",
                "Design controllers for the Center of Mass (CoM) to maintain stability",
                "Implement basic bipedal walking gates for a virtual humanoid"
            ]
        },
        'docs/module-4-vla-humanoids/week-12-manipulation.mdx': {
            'title': "Week 12: Dexterous Manipulation & Human-Robot Interaction",
            'description': "Enable your humanoid to interact with objects and humans using vision, touch, and force control.",
            'keywords': ["Manipulation", "Grasping", "HRI", "Human-Robot Interaction", "Force Control", "Tactile perception"],
            'estimated_time': 600,
            'content_type': "tutorial",
            'difficulty': "advanced",
            'learning_objectives': [
                "Implement grasping strategies for various complex object shapes",
                "Build force and impedance control loops for safe human interaction",
                "Design human-aware behaviors for collaborative robotics tasks",
                "Demonstrate Teleoperation for data collection and imitation learning"
            ]
        },
        'docs/module-4-vla-humanoids/week-13-conversational-vla.mdx': {
            'title': "Week 13: Vision-Language-Action (VLA) Foundational Models",
            'description': "The cutting edge of Physical AI: Conversational robots that understand natural language and execute complex tasks.",
            'keywords': ["VLA", "Foundational Models", "RT-2", "Conversational Robotics", "LLM", "Generative AI"],
            'estimated_time': 720,
            'content_type': "concept",
            'difficulty': "advanced",
            'learning_objectives': [
                "Understand the architecture of modern Vision-Language-Action (VLA) models",
                "Implement Large Language Models (LLMs) for high-level robotic reasoning",
                "Build voice-agent triggers to initiate complex robotic actions",
                "Create an end-to-end Voice-to-Action pipeline for the capstone project"
            ]
        }
    }

    for path, meta in files.items():
        if not os.path.exists(path):
            print(f"Skipping {path} - does not exist")
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace frontmatter
        new_meta = f"""---
title: "{meta['title']}"
description: "{meta['description']}"
keywords: {meta['keywords']}
sidebar_position: {meta.get('sidebar_position', 2)}
learning_objectives:
"""
        for obj in meta['learning_objectives']:
            new_meta += f"  - \"{obj}\"\n"
            
        new_meta += f"""prerequisites: []
estimated_time: {meta['estimated_time']}
content_type: "{meta['content_type']}"
difficulty: "{meta['difficulty']}"
---"""

        # Using regex to replace the frontmatter
        updated_content = re.sub(r'---.*?---', new_meta, content, flags=re.DOTALL)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Updated {path}")

if __name__ == "__main__":
    fix_metadata()
