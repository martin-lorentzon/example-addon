import bpy


# ——————————————————————————————————————————————————————————————————————
# MARK: PROPERTIES
# ——————————————————————————————————————————————————————————————————————





# ——————————————————————————————————————————————————————————————————————
# MARK: INTERFACE
# ——————————————————————————————————————————————————————————————————————


class ConfiguratorPanel(bpy.types.Panel):
    bl_label = "Configurator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Examples"

    def draw(self, context):
        layout = self.layout
        
        scene_collection = context.scene.collection
        
        for col in scene_collection.children:
            if col.color_tag == "COLOR_05":
                box = layout.box()
                box.label(text=col.name)
                
                row = box.row(align=True)
                
                op = row.operator("collection.cycle_items", 
                    text="", icon="PLAY_REVERSE")
                op.collection_name = col.name
                op.go_back = True
                
                # Synliga objektet
                obj = next(o for o in col.objects if o.hide_get() == False)
                
                op = row.operator("collection.cycle_items",
                    text=obj.name)
                op.collection_name = col.name
                
                op = row.operator("collection.cycle_items",
                    text="", icon="PLAY")
                op.collection_name = col.name


# ——————————————————————————————————————————————————————————————————————
# MARK: OPERATORS
# ——————————————————————————————————————————————————————————————————————


class CycleItemsOP(bpy.types.Operator):
    bl_idname = "collection.cycle_items"
    bl_label  = "Cycle Items"
    
    collection_name: bpy.props.StringProperty()
    go_back: bpy.props.BoolProperty(default=False)
    
    def execute(self, context):
        
        collection = bpy.data.collections.get(self.collection_name)
        
        # Hittar det synliga indexet
        visible_idx = 0
        for i, obj in enumerate(collection.objects):
            if obj.hide_get() == False:
                visible_idx = i
                obj.hide_set(True)
                break
        
        # Bestäm vilket håll
        if self.go_back:
            visible_idx -= 1
        else:
            visible_idx += 1
        
        # Indexet går runt (över max -> min osv...)
        max_idx = len(collection.objects)-1
        
        if visible_idx > max_idx:
            visible_idx = 0
        elif visible_idx < 0:
            visible_idx = max_idx
            
        print(visible_idx)
        
        # Visar objektet
        collection.objects[visible_idx].hide_set(False)
        
        return {"FINISHED"}