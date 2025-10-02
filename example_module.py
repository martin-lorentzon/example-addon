import bpy


# ——————————————————————————————————————————————————————————————————————
# MARK: PROPERTIES
# ——————————————————————————————————————————————————————————————————————





# ——————————————————————————————————————————————————————————————————————
# MARK: INTERFACE
# ——————————————————————————————————————————————————————————————————————


class ExamplePanel(bpy.types.Panel):
    bl_label = "Example Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Examples"

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Example Text")


# ——————————————————————————————————————————————————————————————————————
# MARK: OPERATORS
# ——————————————————————————————————————————————————————————————————————


