# MoveIt2 Foundations — UR5 Arm Control

ROS2 Jazzy + MoveIt2 package for controlling a simulated UR5 robot arm using pymoveit2. Built as part of a robotics software engineering learning path toward dual-arm origami folding research.

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
```
ros2 run moveit2_tutorials arm_mover
```

### pose_mover.py

Commands the UR5 to XYZ positions in 3D space with quaternion orientations. Executes a choreographed 5-pose sequence demonstrating position and orientation control.

**Run:**
```
ros2 run moveit2_tutorials pose_mover
```

### cartesian_mover.py

Commands the UR5 to move in a guaranteed straight line between positions using Cartesian path planning. Instead of letting OMPL pick a random path through joint space, cartesian=True forces the end effector to travel linearly. Uses a max_step of 0.01m (1cm) for precise interpolation along the path.

**Run:**
```
ros2 run moveit2_tutorials cartesian_mover
```

### fold_point1.py
tf2 static broadcaster that injects a `fold_point_1` frame into the tf2 tree as a child of `paper_center`, positioned 5cm offset with no rotation. Built as a foundation node for origami fold point coordinate management in the dual UR5 project — not a standalone demo.

### listener_folding.py
tf2 listener that queries the transform between `paper_center` and `fold_point_1`, reporting the fold point's position in real time. Demonstrates reading spatial relationships directly from the tf2 tree using Buffer and TransformListener. Built as a foundation node for the dual UR5 origami project — not a standalone demo.



## Launch Simulation
```
ros2 launch ur_simulation_gz ur_sim_moveit.launch.py ur_type:=ur5
```



## Demo



### arm_mover.py demo 




https://github.com/user-attachments/assets/cdd9bd11-ce71-40ef-a7d9-7476a6f62166





### poser_mover.py demo
https://github.com/user-attachments/assets/7e2328d4-c468-473c-830e-42f12e2d8230

### cartesian_mover.py demo


https://github.com/user-attachments/assets/f7e4b5d3-ec5e-4e8f-b4e7-e1de3391542a



## Key Concepts

- Joint space vs Cartesian space control
- Quaternion orientation (x, y, z, w) — unit quaternion rule: x² + y² + z² + w² = 1.0
- MoveIt2 pipeline: pymoveit2 → move_group → OMPL → ros2_control → Gazebo
- Cartesian path planning: cartesian=True forces straight line end effector motion instead of unpredictable OMPL paths
- tf2 coordinate frames: every position is only meaningful relative to a reference frame
- Transform = translation (XYZ distance) + rotation (orientation difference) between two frames  
- tf2 tree: parent-child structure where updates flow downward from parent to children
- StaticTransformBroadcaster for fixed frames, TransformListener + Buffer for querying current transforms




