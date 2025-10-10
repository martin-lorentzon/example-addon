import bpy


# self.report() - rapporterar viktig information till användaren
# poll() - bestämmer när en operator eller panel är tillgänglig

# Mer nischade (då de enbart har effekt i panelen, men kan anvädas)
# layout.enabled - bestämmer när en (sub)layout är tillgänglig
# layout.active - samma som ovan men du kan interagera med den ändå
# layout.alert - målar (sub)layouts i röd färg, för att varna användaren


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
        
        # Rename active object-knapp  
        row = layout.row()
        
        # Kollar om vi har ett aktivt objekt likt vår poll-metod
        # row.enabled = context.object is not None
        
        row.operator("object.rename_active")
        

# ——————————————————————————————————————————————————————————————————————
# MARK: OPERATORS
# ——————————————————————————————————————————————————————————————————————


class RenameActiveObjectOP(bpy.types.Operator):
    bl_idname = "object.rename_active"
    bl_label = "Rename Object"
    bl_options = {"REGISTER", "UNDO"}
    
    new_name: bpy.props.StringProperty(name="New Name")
    
    
    @classmethod
    def poll(cls, context):     # Returnerar sant eller falskt beroende
                                # på när operatorn ska kunna köras.
        return context.object   # I detta fall om vi har ett aktivt object
        
    
    def execute(self, context):
        
        context.object.name = self.new_name

        return {"FINISHED"}

