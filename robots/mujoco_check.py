import os
import mujoco
import mujoco.viewer
print(os.getcwd())
model = mujoco.MjModel.from_xml_path("roboverse_data/robots/Franka_Emika_Panda_Arm/mjcf/panda.xml")  # 模型路径
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
