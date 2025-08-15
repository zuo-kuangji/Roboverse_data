# Roboverse_data — Robots & Assets (with demo videos)

本表记录了 Roboverse_data 中已有的机械臂模型、资产文件，以及对应不同仿真器的随机动作演示视频。

- **URDF** → PyBullet
- **MJCF** → MuJoCo
- **USD** → Isaac Lab

---

| Model | URDF | MJCF | USD | DoFs | Manufacturer | License | PyBullet (URDF) | MuJoCo (MJCF) | Isaac Lab (USD) |
|---|---:|---:|---:|---:|---|---|---|---|---|
| **ARX L5** | ❌ | ✅ | ❌ | 7 | ARX Robotics | BSD-3-Clause |  |  |  |
| **PiPER** | ❌ | ✅ | ❌ | 7 | AgileX | MIT |  |  |  |
| **iiwa14** | ✅ | ✅ | ✅ | 7 | KUKA | BSD-3-Clause | [查看视频](outputs/random_action_iiwa14_pybullet.mp4) | [查看视频](outputs/random_action_iiwa14_mujoco.mp4) | [查看视频](outputs/random_action_iiwa14_isaaclab.mp4) |
| **Lite6** | ❌ | ✅ | ❌ | 6 | UFACTORY | BSD-3-Clause |  |  |  |
| **Franka Emika Panda** | ✅ | ✅ | ✅ | 7 | Franka Robotics | BSD-3-Clause |  |  | [查看视频](outputs/random_action_franka_isaaclab.mp4) |
| **Sawyer** | ✅ | ✅ | ✅ | 7 | Rethink Robotics | Apache-2.0 | [查看视频](outputs/random_action_sawyer_pybullet.mp4) | [查看视频](outputs/random_action_sawyer_mujoco.mp4) | [查看视频](outputs/random_action_sawyer_isaaclab.mp4) |
| **Unitree Z1** | ✅ | ✅ | ✅ | 6 | Unitree Robotics | BSD-3-Clause | [查看视频](outputs/random_action_z1_pybullet.mp4) | [查看视频](outputs/random_action_z1_mujoco.mp4) | [查看视频](outputs/random_action_z1_isaaclab.mp4) |
| **UR5e** | ✅ | ✅ | ✅ | 6 | Universal Robots | BSD-3-Clause | [查看视频](outputs/random_action_ur5e_pybullet.mp4) | [查看视频](outputs/random_action_ur5e_mujoco.mp4) | [查看视频](outputs/random_action_ur5e_isaaclab.mp4) |
| **UR10e** | ✅ | ✅ | ✅ | 6 | Universal Robots | BSD-3-Clause | [查看视频](outputs/random_action_ur10e_pybullet.mp4) | [查看视频](outputs/random_action_ur10e_mujoco.mp4) | [查看视频](outputs/random_action_ur10e_isaaclab.mp4) |
| **ViperX 300** | ❌ | ✅ | ❌ | 8 | Trossen Robotics | BSD-3-Clause |  |  |  |
| **WidowX 250** | ❌ | ✅ | ❌ | 8 | Trossen Robotics | BSD-3-Clause |  |  |  |
| **xArm7** | ❌ | ✅ | ❌ | 7 | UFACTORY | BSD-3-Clause |  |  |  |
| **Gen3** | ✅ | ✅ | ✅ | 7 | Kinova Robotics | BSD-3-Clause | [查看视频](outputs/random_action_gen3_pybullet.mp4) | [查看视频](outputs/random_action_gen3_mujoco.mp4) | [查看视频](outputs/random_action_gen3_isaaclab.mp4) |
| **SO-ARM100** | ❌ | ✅ | ❌ | 5 | The Robot Studio | Apache-2.0 |  |  |  |
| **Koch v1.1 Low-Cost Robot** | ❌ | ✅ | ❌ | 5 | Hugging Face | Apache-2.0 |  |  |  |
| **YAM** | ❌ | ✅ | ❌ | 7 | I2RT Robotics | MIT |  |  |  |

---

### 使用说明
1. 确保 `.md` 文件与 `outputs/` 目录在同一层级。
2. 在 GitHub 页面点击“查看视频”链接，即可在浏览器打开或下载视频文件。
3. 本地使用 VSCode、Typora 等 Markdown 编辑器，也可直接点击播放视频。
