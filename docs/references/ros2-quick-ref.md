---
title: "Quick Reference: ROS 2 Commands and Concepts"
description: "Quick reference guide for ROS 2 commands, concepts, and best practices"
keywords: ["ROS 2", "reference", "commands", "cheatsheet", "robotics"]
sidebar_position: 3
sidebar_label: "ROS 2 Quick Reference"
estimated_time: 2
week: null
module: null
prerequisites: []
learning_objectives:
  - "Quickly reference common ROS 2 commands and concepts"
  - "Access best practices for ROS 2 development"
  - "Troubleshoot common ROS 2 issues efficiently"
assessment_type: null
difficulty_level: "beginner"
capstone_component: null
---

# Quick Reference: ROS 2 Commands and Concepts

## Essential Commands

### Workspace Management
```bash
# Create a new workspace
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

# Build the workspace
colcon build --packages-select <package_name>  # Build specific package
colcon build --symlink-install                 # Build with symlinks for easier development

# Source the workspace
source install/setup.bash

# Clean build artifacts
rm -rf build/ install/ log/
```

### Package Management
```bash
# Create a new package
ros2 pkg create --build-type ament_python <package_name>
ros2 pkg create --build-type ament_cmake <package_name>

# List all packages
ros2 pkg list

# Show package information
ros2 pkg info <package_name>
```

### Node Management
```bash
# List active nodes
ros2 node list

# Show node information
ros2 node info <node_name>

# Run a node
ros2 run <package_name> <executable_name>

# Get node parameters
ros2 param list <node_name>
ros2 param get <node_name> <param_name>
ros2 param set <node_name> <param_name> <value>
```

### Topic Management
```bash
# List active topics
ros2 topic list

# Show topic information
ros2 topic info <topic_name>

# Echo messages on a topic
ros2 topic echo <topic_name> <message_type>

# Publish a message to a topic
ros2 topic pub <topic_name> <message_type> <values>

# Show topic statistics
ros2 topic hz <topic_name>  # Message rate
ros2 topic bw <topic_name>  # Bandwidth usage
```

### Service Management
```bash
# List active services
ros2 service list

# Show service information
ros2 service info <service_name>

# Call a service
ros2 service call <service_name> <service_type> <request_values>
```

### Action Management
```bash
# List active actions
ros2 action list

# Show action information
ros2 action info <action_name>

# Send a goal to an action
ros2 action send_goal <action_name> <action_type> <goal_values>
```

## Message Types

### Common Message Types
- `std_msgs/msg/String` - Simple string messages
- `std_msgs/msg/Int32` - Integer values
- `std_msgs/msg/Float64` - Floating point values
- `geometry_msgs/msg/Twist` - Velocity commands (linear/angular)
- `geometry_msgs/msg/Pose` - Position and orientation
- `sensor_msgs/msg/JointState` - Joint positions, velocities, efforts
- `sensor_msgs/msg/Image` - Camera images
- `sensor_msgs/msg/LaserScan` - LIDAR data

### Creating Custom Messages
1. Create `msg/` directory in your package
2. Define message in `.msg` file:
   ```
   # MyCustomMessage.msg
   string name
   int32 id
   float64[] values
   geometry_msgs/Pose pose
   ```
3. Update `package.xml`:
   ```xml
   <build_depend>rosidl_default_generators</build_depend>
   <exec_depend>rosidl_default_runtime</exec_depend>
   <member_of_group>rosidl_interface_packages</member_of_group>
   ```
4. Update `CMakeLists.txt`:
   ```cmake
   find_package(rosidl_default_generators REQUIRED)
   rosidl_generate_interfaces(${PROJECT_NAME}
     "msg/MyCustomMessage.msg"
   )
   ```

## Launch Files

### Python Launch Files
```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_package',
            executable='my_node',
            name='my_node_name',
            parameters=[
                {'param1': 'value1'},
                {'param2': 42}
            ],
            remappings=[
                ('original_topic', 'new_topic')
            ]
        )
    ])
```

### Running Launch Files
```bash
# Run a launch file
ros2 launch <package_name> <launch_file>.py

# Run with arguments
ros2 launch <package_name> <launch_file>.py arg_name:=arg_value
```

## TF (Transforms)

### TF Commands
```bash
# View TF tree
ros2 run tf2_tools view_frames

# Echo transforms
ros2 run tf2_ros tf2_echo <source_frame> <target_frame>

# Check transform
ros2 run tf2_ros tf2_monitor <source_frame> <target_frame>
```

### TF in Code
```python
# Python example
import rclpy
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class TFExample:
    def __init__(self):
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

    def lookup_transform(self, target_frame, source_frame, time):
        try:
            transform = self.tf_buffer.lookup_transform(
                target_frame,
                source_frame,
                time)
            return transform
        except TransformException as ex:
            self.get_logger().info(f'Could not transform {target_frame} to {source_frame}: {ex}')
            return None
```

## Quality of Service (QoS)

### Common QoS Profiles
```python
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

# Default profile
default_qos = QoSProfile(depth=10)

# Reliable, persistent
reliable_qos = QoSProfile(
    depth=10,
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.TRANSIENT_LOCAL
)

# Best effort, volatile
best_effort_qos = QoSProfile(
    depth=10,
    reliability=ReliabilityPolicy.BEST_EFFORT,
    durability=DurabilityPolicy.VOLATILE
)
```

## Lifecycle Nodes

### Lifecycle Node Commands
```bash
# List lifecycle nodes
ros2 lifecycle list <node_name>

# Change lifecycle state
ros2 lifecycle set <node_name> configure
ros2 lifecycle set <node_name> activate
ros2 lifecycle set <node_name> deactivate
ros2 lifecycle set <node_name> cleanup
ros2 lifecycle set <node_name> shutdown
```

## Common Issues and Solutions

### Network Issues
```bash
# Check if nodes can communicate
printenv | grep ROS

# Set ROS domain ID to avoid interference
export ROS_DOMAIN_ID=1

# Check multicast connectivity
ros2 topic list  # Should work across machines if configured correctly
```

### Permission Issues
```bash
# If getting permission errors with serial devices
sudo usermod -a -G dialout $USER
# Log out and back in for changes to take effect
```

### Build Issues
```bash
# Clean and rebuild
rm -rf build/ install/ log/
colcon build --symlink-install

# If getting import errors after build
source install/setup.bash
```

### Memory Issues
```bash
# Check memory usage
free -h

# If running out of memory during build
colcon build --parallel-workers 1  # Reduce parallel compilation
```

## Best Practices

### Package Structure
```
my_robot_package/
├── CMakeLists.txt
├── package.xml
├── src/
│   └── my_robot_package/
│       ├── __init__.py
│       └── my_node.py
├── launch/
│   └── robot.launch.py
├── config/
│   └── params.yaml
├── test/
│   └── test_my_node.py
└── README.md
```

### Node Development
- Use meaningful node and topic names
- Implement proper error handling
- Use parameters for configuration
- Follow ROS 2 style guides (PEP 8 for Python)
- Add logging for debugging
- Use QoS profiles appropriately

### Testing
```bash
# Run tests
colcon test
colcon test-result --verbose  # View test results

# Run specific tests
colcon test --packages-select <package_name>
```

## Debugging Tools

### Common Debugging Commands
```bash
# Monitor system resources
htop

# Check network connections
netstat -tulpn | grep :11311

# Monitor topics in real-time
rqt_plot

# Visualize robot state
rqt_robot_steering
rqt_topic

# Debug with GDB
gdb --args ros2 run <package> <node>
```

## Performance Optimization

### Profiling
```bash
# Use ros2doctor for system diagnostics
ros2 doctor

# Profile node performance
ros2 run tracetools_trace trace -a
```

### Memory Management
- Use shared pointers appropriately
- Avoid unnecessary copies of large messages
- Consider using intra-process communication for same-process nodes

## Security Considerations

### Authentication
- Use DDS security plugins for sensitive applications
- Implement proper access controls
- Encrypt sensitive data transmission

### Network Security
- Use VPN for remote operations
- Configure firewall rules appropriately
- Monitor network traffic for anomalies

## Troubleshooting Checklist

When facing issues:

1. **Check ROS environment**:
   ```bash
   printenv | grep ROS
   ```

2. **Verify nodes are running**:
   ```bash
   ros2 node list
   ```

3. **Check topic connections**:
   ```bash
   ros2 topic info <topic_name>
   ```

4. **Review logs**:
   ```bash
   ros2 launch <package> <launch_file> --non-interactive
   # Check ~/.ros/log/ for log files
   ```

5. **Test basic functionality**:
   ```bash
   ros2 topic pub /test std_msgs/msg/String "data: 'test'"
   ros2 topic echo /test
   ```

## Resources

- [ROS 2 Documentation](https://docs.ros.org/en/humble/)
- [ROS 2 Tutorials](https://docs.ros.org/en/humble/Tutorials.html)
- [ROS Answers](https://answers.ros.org/questions/)
- [ROS Discourse](https://discourse.ros.org/)

---

**Need more help?** Refer to the [Glossary](./glossary.md) for terminology or consult the ROS 2 community forums.