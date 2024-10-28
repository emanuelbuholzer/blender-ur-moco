import bpy

from urmoco.capabilities import CAP_BRAKE, CAP_FREEDRIVE, CAP_POWER, CAP_CALIBRATION
from urmoco.config import Config
from urmoco.blender.state import Mode, get_mode, get_status_text
from urmoco.blender.constants import (ARMATURE_MODEL, CONSTRAINT_IK)

def get_urmoco_panel(config: Config):
    class URMocoPanel(bpy.types.Panel):
        bl_label = "urmoco"
        bl_idname = "PANEL_PT_URMOCO"
        bl_space_type = "VIEW_3D"
        bl_region_type = "UI"
        bl_category = "Motion Control"

        def __init__(self):
            self.config = config
            self.robot_type = config.get("type")

        def draw_initialised(self, state: Mode):
            self.layout.label(text="Capturing:")
            row = self.layout.row()
            if state is Mode.SHOOTING:
                row.operator("urmoco.stop_capturing")
            else:
                row.operator("urmoco.start_capturing")
                row.enabled = state is Mode.ON

            if CAP_BRAKE in config.get(f"{self.robot_type}.capabilities"):
                self.layout.label(text="Movement:")
                row = self.layout.row()
                row.scale_y = 2
                row.enabled = state in {Mode.MOVING}
                row.operator("urmoco.emergency_stop")

            self.layout.label(text="Pose:")

            if CAP_FREEDRIVE in config.get(f"{self.robot_type}.capabilities"):
                row = self.layout.row()
                if state is Mode.FREEDRIVE:
                    row.operator("urmoco.stop_freedrive")
                else:
                    row.enabled = state is Mode.ON
                    row.operator("urmoco.start_freedrive")

            row = self.layout.row()
            row.enabled = state is Mode.ON
            row.operator("urmoco.transfer")
            row.operator("urmoco.sync")

            if CAP_POWER in config.get(f"{self.robot_type}.capabilities"):
                self.layout.label(text="Robot:")
                row = self.layout.row()
                row.operator("urmoco.power_off")

            if CAP_CALIBRATION in config.get(f"{self.robot_type}.capabilities"):
                row = self.layout.row()
                row.operator("urmoco.calibration")


        def draw_uninitialised(self, context):
            self.layout.operator("urmoco.startup")

        def draw(self, context):
            state = get_mode()

            if context.mode != "POSE":
                self.layout.label(icon="INFO", text="Please use urmoco in pose mode")
                return

            self.layout.label(icon="INFO", text=get_status_text())

            if state is Mode.UNINITIALIZED:
                self.draw_uninitialised(context)
                pass
            else:
                self.draw_initialised(state)

            self.layout.label(text="Animation:")
            row = self.layout.row()
            row.enabled = state is not Mode.AWAIT_RESPONSE
            ik_enabled = (
                bpy.data.objects[ARMATURE_MODEL]
                .pose.bones["Bone.005"]
                .constraints[CONSTRAINT_IK]
                .enabled
            )
            if ik_enabled:
                row.operator("urmoco.use_fk_rig")
            else:
                row.operator("urmoco.use_ik_rig")

    return URMocoPanel
