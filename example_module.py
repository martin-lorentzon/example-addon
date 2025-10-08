import bpy
import addon_utils
from pathlib import Path


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
        layout.operator("wm.load_data")


# ——————————————————————————————————————————————————————————————————————
# MARK: OPERATORS
# ——————————————————————————————————————————————————————————————————————


class LoadSomeDataOP(bpy.types.Operator):
    bl_idname = "wm.load_data"
    bl_label  = "Load Data"
    
    def execute(self, context):
        filepath = None
        
        # Hittar filvägen till verktygets add-on-mapp (och blend-filen)
        for mod in addon_utils.modules():
            if mod.bl_info["name"] == "Example Add-on":
                filepath = Path(mod.__file__).parent / ("Stylized_Fire.blend")
        
        # Laddar blend-filen som ett blend-bibliotek och dess innehåll som vi specifierar
        with bpy.data.libraries.load(str(filepath)) as (data_from, data_to):
            data_to.objects = data_from.objects
            # Eller mer selektivt:
            # data_to.objects = ["Stylized Fire"]
            
        # Länkar in objekten i den aktiva scenen
        for obj in data_to.objects:
            context.scene.collection.objects.link(obj)
            
            # Ändrar en parameter i Geometry Nodes-modifieraren (exempel om sådan finns)
            obj.modifiers["GeometryNodes"]["Socket_2"] = 6
        
        return {"FINISHED"}