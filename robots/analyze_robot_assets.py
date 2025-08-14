#!/usr/bin/env python3
"""
简单的机器人资产文件分析脚本

使用方法：
cd roboverse_data/robots/
python analyze_robot_assets.py --urdf
python analyze_robot_assets.py --urdf --mjcf
python analyze_robot_assets.py --urdf --mjcf --usd --compare
"""

import argparse
import os
import xml.etree.ElementTree as ET
from typing import List, Dict

# =============================================================================
# 配置区域 - 请根据你的机器人文件结构填写路径
# =============================================================================
# 当前分析的机器人文件路径（请手动修改）
ROBOT_FILES = {
    "urdf": "Universal_Robots_UR5e/urdf/ur_description/urdf/ur5e.urdf",
    "mjcf": "Universal_Robots_UR5e/mjcf/ur5e.xml",
    "usd": "Universal_Robots_UR5e/usd/ur5e.usd"  # 如果有的话
}

def extract_urdf_info(file_path: str) -> Dict[str, List[str]]:
    """提取URDF文件的关节和执行器信息"""
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return {"joints": [], "actuators": []}
    
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    joints = []
    actuators = []
    
    # 获取所有关节名称
    for joint in root.findall('.//joint'):
        joint_name = joint.get('name', '')
        joint_type = joint.get('type', '')
        if joint_name:
            joints.append(joint_name)
            # 可动关节作为执行器
            if joint_type in ['revolute', 'prismatic', 'continuous']:
                actuators.append(joint_name)
    
    return {"joints": joints, "actuators": actuators}

def extract_mjcf_info(file_path: str) -> Dict[str, List[str]]:
    """提取MJCF文件的关节和执行器信息"""
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return {"joints": [], "actuators": []}
    
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    joints = []
    actuators = []
    
    # 获取所有关节名称
    for joint in root.findall('.//joint'):
        joint_name = joint.get('name', '')
        if joint_name:
            joints.append(joint_name)
    
    # 获取执行器（从actuator标签）
    for actuator in root.findall('.//actuator/*'):
        actuator_name = actuator.get('name', '')
        joint_name = actuator.get('joint', '')
        if actuator_name:
            actuators.append(actuator_name)
        elif joint_name:
            actuators.append(joint_name)
    
    # 如果没有显式执行器，使用关节名
    if not actuators:
        actuators = joints.copy()
    
    return {"joints": joints, "actuators": actuators}

def extract_usd_info(file_path: str) -> Dict[str, List[str]]:
    """提取USD文件的关节和执行器信息"""
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return {"joints": [], "actuators": []}
    
    try:
        from pxr import Usd, UsdPhysics, UsdGeom
    except ImportError:
        print("警告: 无法导入USD库，请安装: pip install usd-core")
        return {"joints": [], "actuators": []}
    
    try:
        # 禁用警告信息
        import pxr.Tf as Tf
        # 临时禁用USD的警告输出
        Tf.Debug.SetDebugSymbolsByName("USD_PARSER_*", False)
        
        stage = Usd.Stage.Open(file_path)
        if not stage:
            print("无法打开USD文件，可能格式有问题")
            return {"joints": [], "actuators": []}
        
        joints = []
        actuators = []
        
        # 遍历所有prims，寻找关节和执行器
        for prim in stage.Traverse():
            prim_name = prim.GetName()
            prim_type = prim.GetTypeName()
            
            # 检查是否是物理关节
            if prim.IsA(UsdPhysics.Joint):
                joints.append(prim_name)
                actuators.append(prim_name)
            # 检查是否是旋转关节
            elif prim.IsA(UsdPhysics.RevoluteJoint):
                joints.append(prim_name)
                actuators.append(prim_name)
            # 检查是否是棱柱关节
            elif prim.IsA(UsdPhysics.PrismaticJoint):
                joints.append(prim_name)
                actuators.append(prim_name)
            # 检查名称中包含joint的prim
            elif "joint" in prim_name.lower() and prim_type:
                joints.append(prim_name)
                # 如果不是固定关节，添加到执行器
                if "fixed" not in prim_name.lower():
                    actuators.append(prim_name)
            # 检查关节属性
            elif prim.HasAttribute("physics:jointEnabled"):
                joints.append(prim_name)
                actuators.append(prim_name)
        
        # 如果还是没找到，尝试寻找包含"joint"的属性或元数据
        if not joints:
            for prim in stage.Traverse():
                for attr in prim.GetAttributes():
                    attr_name = attr.GetName()
                    if "joint" in attr_name.lower():
                        prim_name = prim.GetName()
                        if prim_name not in joints:
                            joints.append(prim_name)
                            if "fixed" not in prim_name.lower():
                                actuators.append(prim_name)
        
        return {"joints": joints, "actuators": actuators}
        
    except Exception as e:
        print(f"USD文件解析出错: {e}")
        return {"joints": [], "actuators": []}

def print_format_info(format_name: str, info: Dict[str, List[str]]):
    """打印格式信息"""
    print(f"\n{format_name.upper()} 文件信息:")
    print(f"  关节名称 ({len(info['joints'])} 个):")
    for joint in info['joints']:
        print(f"    - {joint}")
    
    print(f"  执行器名称 ({len(info['actuators'])} 个):")
    for actuator in info['actuators']:
        print(f"    - {actuator}")

def compare_formats(results: Dict[str, Dict[str, List[str]]]):
    """对比不同格式的信息"""
    print(f"\n{'='*50}")
    print("格式对比")
    print(f"{'='*50}")
    
    # 对比关节
    print("\n关节名称对比:")
    all_joints = set()
    for info in results.values():
        all_joints.update(info['joints'])
    
    for joint in sorted(all_joints):
        status = []
        for fmt, info in results.items():
            if joint in info['joints']:
                status.append(f"{fmt}:✓")
            else:
                status.append(f"{fmt}:✗")
        print(f"  {joint}: {' '.join(status)}")
    
    # 对比执行器
    print("\n执行器名称对比:")
    all_actuators = set()
    for info in results.values():
        all_actuators.update(info['actuators'])
    
    for actuator in sorted(all_actuators):
        status = []
        for fmt, info in results.items():
            if actuator in info['actuators']:
                status.append(f"{fmt}:✓")
            else:
                status.append(f"{fmt}:✗")
        print(f"  {actuator}: {' '.join(status)}")

def main():
    parser = argparse.ArgumentParser(description='机器人资产文件分析工具')
    parser.add_argument('--urdf', action='store_true', help='分析URDF文件')
    parser.add_argument('--mjcf', action='store_true', help='分析MJCF文件')
    parser.add_argument('--usd', action='store_true', help='分析USD文件')
    parser.add_argument('--compare', action='store_true', help='对比不同格式')
    
    args = parser.parse_args()
    
    # 检查至少选择一种格式
    if not (args.urdf or args.mjcf or args.usd):
        print("请至少选择一种格式: --urdf, --mjcf, 或 --usd")
        return
    
    print("机器人文件路径配置:")
    for fmt, path in ROBOT_FILES.items():
        print(f"  {fmt}: {path}")
    
    results = {}
    
    # 分析选中的格式
    if args.urdf:
        print(f"\n正在分析URDF文件...")
        results['urdf'] = extract_urdf_info(ROBOT_FILES['urdf'])
        print_format_info('urdf', results['urdf'])
    
    if args.mjcf:
        print(f"\n正在分析MJCF文件...")
        results['mjcf'] = extract_mjcf_info(ROBOT_FILES['mjcf'])
        print_format_info('mjcf', results['mjcf'])
    
    if args.usd:
        print(f"\n正在分析USD文件...")
        results['usd'] = extract_usd_info(ROBOT_FILES['usd'])
        print_format_info('usd', results['usd'])
    
    # 对比分析
    if args.compare and len(results) > 1:
        compare_formats(results)
    elif args.compare and len(results) == 1:
        print("\n需要至少两种格式才能进行对比")

if __name__ == "__main__":
    main()