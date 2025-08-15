# Roboverse_data — Robots & Assets (with Demo Videos)

This table lists the robot arm models available in **Roboverse_data**, the asset formats provided, and demo videos showing random actions in different simulators.

- **URDF** → PyBullet
- **MJCF** → MuJoCo
- **USD** → Isaac Lab

---

| Model | URDF | MJCF | USD | DoFs | Manufacturer | License | PyBullet (URDF) | MuJoCo (MJCF) | Isaac Lab (USD) |
|---|---:|---:|---:|---:|---|---|---|---|---|
| **ARX L5** | ❌ | ✅ | ❌ | 7 | ARX Robotics | BSD-3-Clause |  |  |  |
| **PiPER** | ❌ | ✅ | ❌ | 7 | AgileX | MIT |  |  |  |
| **iiwa14** | ✅ | ✅ | ✅ | 7 | KUKA | BSD-3-Clause | [View Video](outputs/random_action_iiwa14_pybullet.mp4) | [View Video](outputs/random_action_iiwa14_mujoco.mp4) | [View Video](outputs/random_action_iiwa14_isaaclab.mp4) |
| **Lite6** | ❌ | ✅ | ❌ | 6 | UFACTORY | BSD-3-Clause |  |  |  |
| **Franka Emika Panda** | ✅ | ✅ | ✅ | 7 | Franka Robotics | BSD-3-Clause |  |  | [View Video](outputs/random_action_franka_isaaclab.mp4) |
| **Sawyer** | ✅ | ✅ | ✅ | 7 | Rethink Robotics | Apache-2.0 | [View Video](outputs/random_action_sawyer_pybullet.mp4) | [View Video](outputs/random_action_sawyer_mujoco.mp4) | [View Video](outputs/random_action_sawyer_isaaclab.mp4) |
| **Unitree Z1** | ✅ | ✅ | ✅ | 6 | Unitree Robotics | BSD-3-Clause | [View Video](outputs/random_action_z1_pybullet.mp4) | [View Video](outputs/random_action_z1_mujoco.mp4) | [View Video](outputs/random_action_z1_isaaclab.mp4) |
| **UR5e** | ✅ | ✅ | ✅ | 6 | Universal Robots | BSD-3-Clause | [View Video](outputs/random_action_ur5e_pybullet.mp4) | [View Video](outputs/random_action_ur5e_mujoco.mp4) | [View Video](outputs/random_action_ur5e_isaaclab.mp4) |
| **UR10e** | ✅ | ✅ | ✅ | 6 | Universal Robots | BSD-3-Clause | [View Video](outputs/random_action_ur10e_pybullet.mp4) | [View Video](outputs/random_action_ur10e_mujoco.mp4) | [View Video](outputs/random_action_ur10e_isaaclab.mp4) |
| **ViperX 300** | ❌ | ✅ | ❌ | 8 | Trossen Robotics | BSD-3-Clause |  |  |  |
| **WidowX 250** | ❌ | ✅ | ❌ | 8 | Trossen Robotics | BSD-3-Clause |  |  |  |
| **xArm7** | ❌ | ✅ | ❌ | 7 | UFACTORY | BSD-3-Clause |  |  |  |
| **Gen3** | ✅ | ✅ | ✅ | 7 | Kinova Robotics | BSD-3-Clause | [View Video](outputs/random_action_gen3_pybullet.mp4) | [View Video](outputs/random_action_gen3_mujoco.mp4) | [View Video](outputs/random_action_gen3_isaaclab.mp4) |
| **SO-ARM100** | ❌ | ✅ | ❌ | 5 | The Robot Studio | Apache-2.0 |  |  |  |
| **Koch v1.1 Low-Cost Robot** | ❌ | ✅ | ❌ | 5 | Hugging Face | Apache-2.0 |  |  |  |
| **YAM** | ❌ | ✅ | ❌ | 7 | I2RT Robotics | MIT |  |  |  |

---

## Verification Script — Random Action Video Generation

This repository includes a verification script that runs a **random joint action** test for a selected robot in a chosen simulator.
It helps confirm that the robot’s assets load correctly and that the simulation works as expected.

### Script Location
