import logging

import bpy

from urmoco.blender.constants import (
    ARMATURE_MODEL,
    CONSTRAINT_IK,
    CONSTRAINT_COPY_LOCATION,
    CONSTRAINT_COPY_ROTATION,
)
from urmoco.blender.rig import select_bones, BONES
from urmoco.blender.state import set_status_text
from urmoco.config import Config
from urmoco.scheduler import Scheduler

logger = logging.getLogger(__name__)


# TODO: reflect this switch in the action groups
# TODO: use ensures
def get_operators(_config: Config, _scheduler: Scheduler):
    class UseIkRigOperator(bpy.types.Operator):
        bl_idname = "urmoco.use_ik_rig"
        bl_label = "Use IK"

        def execute(self, _context):
            shoulder_pan_select_prev = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone"]
                .bone.select
            )
            shoulder_lift_select_prev = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone.002"]
                .bone.select
            )
            elbow_select_prev = (
                bpy.data.objects[ARMATURE_MODEL].pose.bones["Bone.003"].bone.select
            )
            wrist_joint_1_select_prev = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone.006"]
                .bone.select
            )
            wrist_joint_2_select_prev = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone.004"]
                .bone.select
            )
            wrist_joint_3_select_prev = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone.005"]
                .bone.select
            )
            ik_control_select_prev = (
                bpy.data.objects[ARMATURE_MODEL].pose.bones["IK Control"].bone.select
            )

            select_bones(ARMATURE_MODEL, BONES)

            bpy.ops.pose.visual_transform_apply()

            bpy.data.objects[ARMATURE_MODEL].pose.bones["IK Control"].constraints[
                CONSTRAINT_COPY_LOCATION
            ].enabled = False
            bpy.data.objects[ARMATURE_MODEL].pose.bones["IK Control"].constraints[
                CONSTRAINT_COPY_ROTATION
            ].enabled = False
            bpy.data.objects[ARMATURE_MODEL].pose.bones["Bone.005"].constraints[
                CONSTRAINT_IK
            ].enabled = True
            set_status_text("Using IK rig for robot")

            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone"
            ].bone.select = shoulder_pan_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone.002"
            ].bone.select = shoulder_lift_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone.003"
            ].bone.select = elbow_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone.006"
            ].bone.select = wrist_joint_1_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone.004"
            ].bone.select = wrist_joint_2_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone.005"
            ].bone.select = wrist_joint_3_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "IK Control"
            ].bone.select = ik_control_select_prev
            return {"FINISHED"}

    class UseFkRigOperator(bpy.types.Operator):
        bl_idname = "urmoco.use_fk_rig"
        bl_label = "Use FK"

        def execute(self, _context):
            shoulder_pan_select_prev = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone"]
                .bone.select
            )
            shoulder_lift_select_prev = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone.002"]
                .bone.select
            )
            elbow_select_prev = (
                bpy.data.objects[ARMATURE_MODEL].pose.bones["Bone.003"].bone.select
            )
            wrist_joint_1_select_prev = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone.006"]
                .bone.select
            )
            wrist_joint_2_select_prev = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone.004"]
                .bone.select
            )
            wrist_joint_3_select_prev = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone.005"]
                .bone.select
            )
            ik_control_select_prev = (
                bpy.data.objects[ARMATURE_MODEL].pose.bones["IK Control"].bone.select
            )

            select_bones(ARMATURE_MODEL, BONES)

            bpy.ops.pose.visual_transform_apply()

            bpy.data.objects[ARMATURE_MODEL].pose.bones["IK Control"].constraints[
                CONSTRAINT_COPY_LOCATION
            ].enabled = True
            bpy.data.objects[ARMATURE_MODEL].pose.bones["IK Control"].constraints[
                CONSTRAINT_COPY_ROTATION
            ].enabled = True
            bpy.data.objects[ARMATURE_MODEL].pose.bones["Bone.005"].constraints[
                CONSTRAINT_IK
            ].enabled = False
            set_status_text("Using FK rig for robot")

            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone"
            ].bone.select = shoulder_pan_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone.002"
            ].bone.select = shoulder_lift_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone.003"
            ].bone.select = elbow_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone.006"
            ].bone.select = wrist_joint_1_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone.004"
            ].bone.select = wrist_joint_2_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "Bone.005"
            ].bone.select = wrist_joint_3_select_prev
            bpy.data.objects[ARMATURE_MODEL].pose.bones[
                "IK Control"
            ].bone.select = ik_control_select_prev

            return {"FINISHED"}

    return [UseIkRigOperator, UseFkRigOperator]