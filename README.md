# MoveIt2 Tutorials — UR5 Arm Control

ROS2 Jazzy + MoveIt2 package for controlling a simulated UR5 robot arm using pymoveit2.
Built as part of a robotics software engineering learning path toward dual-arm origami folding research.

## Environment
- Ubuntu 24.04
- ROS2 Jazzy
- Gazebo Harmonic
- MoveIt2
- pymoveit2

## Nodes

### arm_mover.py
Commands the UR5 to joint angle configurations in radians using pymoveit2.

**Run:**
```bash
ros2 run moveit2_tutorials arm_mover
```

### pose_mover.py
Commands the UR5 to XYZ positions in 3D space with quaternion orientations.
Executes a choreographed 5-pose sequence demonstrating position and orientation control.

**Run:**
```bash
ros2 run moveit2_tutorials pose_mover
```

## Launch Simulation
```bash
ros2 launch ur_simulation_gz ur_sim_moveit.launch.py ur_type:=ur5
```

## Demo





## Key Concepts
- Joint space vs Cartesian space control
- Quaternion orientation (x, y, z, w) — unit quaternion rule: x² + y² + z² + w² = 1.0
- MoveIt2 pipeline: pymoveit2 → move_group → OMPL → ros2_control → Gazebo
