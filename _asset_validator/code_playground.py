import maya.cmds as cmds
import maya.mel as mel
import os


print('hello world')


# List all geometry
list_geo = cmds.ls(geometry=True)
mesh_info = list_geo[0]

# Use listRelatives to get the parent of the object
transform_info = cmds.listRelatives(mesh_info, parent=True)[0]
asset_name = transform_info

#################

# print(transform_info)

# # List all attributes of 'myCubeShape'
# attributes = cmds.listAttr(transform_info)
# print(attributes)

# object_type = cmds.objectType(mesh_info)
# print('Object Type:', object_type)

# print(cmds.getAttr(myGeo + '.visibility'))

# cmds.setAttr(myGeo + '.visibility', True)


# #################
# ## Validate - Correct File/Asset Name

# ## All need to MATCH:       Folder Name         > File Name              > Asset Name
# ##                          CharacterABC_Skin01 > CharacterABC_Skin01.ma > CharacterABC_Skin01.fbx

# # Get the current scene name
# file_path = cmds.file(q=True, sceneName=True)
# if not file_path:
#     file_path = 'Unsaved Maya Scene!'

# print(f'File Path: {file_path}')

# folder_name = file_path.rsplit('/', 2)[-2]
# file_name_w_extension = file_path.rsplit('/', 2)[-1]
# file_name, file_extension = os.path.splitext(file_name_w_extension)

# print(f'Folder Name: {folder_name}')
# print(f'File Name w Extension: {file_name_w_extension}')
# print(f'File Name: {file_name} -- File Extension: {file_extension}')
# print(f'Asset Name: {asset_name}')


# #################
# ## Validate - Freeze Transforms


# def is_transform_frozen(asset_name): # Freeze Transforms VALIDATION FUNCTION

#     # Save the original transform values
#     translate_value = cmds.getAttr(asset_name + '.translate')[0]
#     rotate_value = cmds.getAttr(asset_name + '.rotate')[0]
#     scale_value = cmds.getAttr(asset_name + '.scale')[0]

#     # Check if transforms are zeroed out
#     if all(value == 0 for value in translate_value) and all(value == 0 for value in rotate_value) and all(value == 1 for value in scale_value):
#         return True
#     else:
#         return False



# print(f'is_transform_frozen: {is_transform_frozen(asset_name)}')

# ######
# # Freeze transforms for the specified object
# cmds.makeIdentity(asset_name, apply=True, translate=True, rotate=True, scale=True)
# ######

# print(f'# Freeze transforms for {asset_name}')
# print(f'is_transform_frozen: {is_transform_frozen(asset_name)}')


# #################
# ## Validate - Center PIVOT/ORIGIN and ASSET to 0,0,0 World Space

# #### # Center the pivot of the object at the origin ## DESTRUCTIVE ORIGIN ADJUST
# #### cmds.xform(asset_name, centerPivots=True)


# def is_pivot_worldspace_zero(asset_name): # pivot world space VALIDATION FUNCTION

#     # check pivot location
#     pivot_location = cmds.xform(asset_name, query=True, rotatePivot=True, worldSpace=True)

#     # Check if transforms are zeroed out
#     if all(value == 0 for value in pivot_location):
#         return True
#     else:
#         return False
    

# print(f'is_pivot_worldspace_zero: {is_pivot_worldspace_zero(asset_name)}')


# ######
# # Store the original location
# original_location = cmds.xform(asset_name, query=True, rotatePivot=True, worldSpace=True)

# # Move the object with the relative pivot point set to the origin
# cmds.move(0, 0, 0, asset_name, rotatePivotRelative=True)

# # Freeze transforms for the specified object
# cmds.makeIdentity(asset_name, apply=True, translate=True, rotate=True, scale=True)

# print("Object moved back to the centered origin.")

# # Query the new location
# new_location = cmds.xform(asset_name, query=True, rotatePivot=True, worldSpace=True)

# # Print the original and new locations
# print('Original Location:', original_location)
# print('New Location:', new_location)
# #
# ######

# print(f'is_pivot_worldspace_zero: {is_pivot_worldspace_zero(asset_name)}')


#################
## Validate - Construction History Deleted

