bl_info = {
    "name": "Example Add-on",
    "description": "Add-on containing example functionality",
    "author": "Martin Lorentzon",
    "version": (1, 0, 0),
    "blender": (4, 5, 0),
    "location": "3D Viewport > N Panel > Examples",
    # "doc_url": "https://github.com/{username}/{repo-name}",
    # "tracker_url": "https://github.com/{username}/{repo-name}/issues",
    "support": "COMMUNITY",
    "category": "Education",
}


# ——————————————————————————————————————————————————————————————————————
# MARK: IMPORTS
# ——————————————————————————————————————————————————————————————————————


# fmt: off
if "bpy" in locals():
    from importlib import reload

    # Modules to reload during development go here
    reload(example_module)
else:
    # ...and here
    from . import example_module

# ...but not here
import bpy
# fmt: on


# ——————————————————————————————————————————————————————————————————————
# MARK: REGISTRATION
# ——————————————————————————————————————————————————————————————————————


classes = [
    example_module.ExamplePanel,
    example_module.LoadSomeDataOP
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
