import maya.cmds as cmds
import maya.mel as mel
import os


class ValidationError(Exception):
    pass


### RAISE VALIDATION example
# # CHECK if number of selected assets is ONE
# if len(selected_assets) != 1:
#     raise ValidationError(f'Please select only 1 Master Material in Content Browser')





print('hello world')


# List all geometry
list_geo = cmds.ls(geometry=True)
mesh_info = list_geo[0]

# Use listRelatives to get the parent of the object
transform_info = cmds.listRelatives(mesh_info, parent=True)

print(transform_info)

# List all attributes of 'myCubeShape'
attributes = cmds.listAttr(transform_info)
print(attributes)

object_type = cmds.objectType(mesh_info)
print('Object Type:', object_type)


# print(cmds.getAttr(myGeo + '.visibility'))

# cmds.setAttr(myGeo + '.visibility', True)


# Get the current scene name
file_path = cmds.file(q=True, sceneName=True)
if not file_path:
    file_path = 'Unsaved Maya Scene!'

print(f'File Path: {file_path}')

file_name = file_path.rsplit('/', 1)[-1]

print(f'File Name: {file_name}')

print(os.path.splitext(file_name))
