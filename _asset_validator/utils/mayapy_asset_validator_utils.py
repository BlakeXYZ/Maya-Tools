import os

import maya.cmds as cmds
import maya.mel as mel
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets




class ValidationError(Exception):
    pass




class ValidationUtils:

    def __init__(self, asset_name): #constructor
        # pass in current asset in scene to instance of validation asset 
        self.asset_name = asset_name

    ####
    # Is called inside each Validation Function: Sets and Toggles GUI Label based on Functions Bool Value
    def validation_label_toggle(ui_label_object, validation_check):

        # Valid Label GUI icons
        icon_confirm = QtGui.QPixmap(f':/confirm.png').scaledToHeight(32)
        icon_error = QtGui.QPixmap(f':/error.png').scaledToHeight(32)

        # Toggle Label based on arg: validation_check bool value
        if validation_check == True:
            ui_label_object.setPixmap(icon_confirm)
        elif validation_check == False:
            ui_label_object.setPixmap(icon_error)
        else:
            ui_label_object.setStyleSheet('background-color: black')
    ####
    

    ####
    def is_single_asset_in_scene(self, ui_label_object):
        # IF VALIDATION passes, allow to continue with rest of Tool Use
        # Init Bool check to False
        single_asset_in_scene = False

        # List all geometry
        list_geo = cmds.ls(geometry=True)

        # check if single asset is inside scene VALIDATION FUNCTION - conditional expressions yay
        single_asset_in_scene = False if len(list_geo) != 1 else True

        # Set GUI Label for Validation Func
        ValidationUtils.validation_label_toggle(ui_label_object, single_asset_in_scene)
    ####


    ####
    # Freeze Transforms VALIDATION FUNCTION
    def is_transform_frozen(self, ui_label_object): 

        transform_is_frozen = False
        # Save the original transform values
        translate_value = cmds.getAttr(self.asset_name + '.translate')[0]
        rotate_value = cmds.getAttr(self.asset_name + '.rotate')[0]
        scale_value = cmds.getAttr(self.asset_name + '.scale')[0]

        # Check if all transforms are zeroed out
        if all(value == 0 for value in translate_value) and all(value == 0 for value in rotate_value) and all(value == 1 for value in scale_value):
            transform_is_frozen = True
        else:
            transform_is_frozen = False
        
        # Set GUI Label for Validation Func
        ValidationUtils.validation_label_toggle(ui_label_object, transform_is_frozen)
        
    # Freeze transforms for the specified object
    def freeze_transform(self):
        cmds.makeIdentity(self.asset_name, apply=True, translate=True, rotate=True, scale=True)
    ####




### RAISE VALIDATION example
# # CHECK if number of selected assets is ONE
# if len(selected_assets) != 1:
#     raise ValidationError(f'Please select only 1 Master Material in Content Browser')


#################
#################

def test_function():

    print('--- hello world ---')


# List all geometry
list_geo = cmds.ls(geometry=True)
mesh_info = list_geo[0]

# Use listRelatives to get the parent of the object
transform_info = cmds.listRelatives(mesh_info, parent=True)[0]
asset_name = transform_info

# print(asset_name)

################
##                                                                                                        Validation - Missing Asset in Scene

# IF VALIDATION passes, allow to continue with rest of Tool Use

# List all geometry
list_geo = cmds.ls(geometry=True)


def is_asset_in_scene(list_geo): # check if single asset is inside scene VALIDATION FUNCTION

    print(f'list_geo length {len(list_geo)}')

    if len(list_geo) == 1:
        return True
    else:
        return False

# print(is_asset_in_scene(list_geo))





# #################
# ##                                                                                                        Validate - Correct File/Asset Name

# ## All need to MATCH:       Folder Name         > File Name              > Asset Name
# ##                          CharacterABC_Skin01 > CharacterABC_Skin01.ma > CharacterABC_Skin01.fbx

# def validate_is_asset_name_valid():
#     # Get the current scene name
#     file_path = cmds.file(q=True, sceneName=True)
#     if not file_path:
#         file_path = 'Unsaved Maya Scene!'

#     folder_name = file_path.rsplit('/', 2)[-2]
#     file_name_w_extension = file_path.rsplit('/', 2)[-1]
#     file_name, file_extension = os.path.splitext(file_name_w_extension)

#     print(f'Folder Name: {folder_name}')
#     print(f'File Name w Extension: {file_name_w_extension}')
#     print(f'File Name: {file_name} -- File Extension: {file_extension}')
#     print(f'Asset Name: {asset_name}')


# #################
# ##                                                                                                        Validate - Freeze Transforms


# def is_transform_frozen(asset_name): # Freeze Transforms VALIDATION FUNCTION

#     # Save the original transform values
#     translate_value = cmds.getAttr(asset_name + '.translate')[0]
#     rotate_value = cmds.getAttr(asset_name + '.rotate')[0]
#     scale_value = cmds.getAttr(asset_name + '.scale')[0]

#     # Check if all transforms are zeroed out
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
# ##                                                                                                        Validate - Center PIVOT/ORIGIN and ASSET to 0,0,0 World Space

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


# ####
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
# ####

# print(f'is_pivot_worldspace_zero: {is_pivot_worldspace_zero(asset_name)}')

# #################
# ##                                                                                                        Validate - Construction History Deleted

# def is_construction_history_deleted(asset_name): # construction history VALIDATION FUNCTION

#     my_history = cmds.listHistory(asset_name)

#    # Check if the object has a construction history
#     if len(my_history) == 1:
#         return True
#     else:
#         return False
    
# print(f'is_construction_history_deleted for {asset_name}: {is_construction_history_deleted(asset_name)}')

# # Delete construction history for the specified object
# cmds.delete(asset_name, constructionHistory=True)

# #################
# ##                                                                                                        Validation - Find Unused Materials



# def is_any_shading_group_unused(): 

#     ##### Detective work guide for exploring MEL Commands and how they work: https://groups.google.com/g/python_inside_maya/c/N1_wASF3SH4
#     ### // mel
#     ### whatIs hyperShadePanelMenuCommand
#     ### // path to a mel script

#     ### If you look through that mel script for the usage of "deleteUnusedNodes", it will bring you to a command like:
#     ### MLdeleteUnused

#     ### // mel
#     ### whatIs MLdeleteUnused
#     ### // path to another mel script

#     ### If you read that script, you will see that the process of finding unused nodes is multiple stages. It looks at shading groups, and connections, and texture nodes
#     ### Then converted mel function to py cmds
#     #####

#     ## List all shading groups in the scene
#     shading_groups = cmds.ls(type='shadingEngine')
#     # print(f'shading_groups: {shading_groups}')

#     for shading_group in shading_groups:

#         if not cmds.objExists(shading_group):
#             return False

#         if cmds.sets(shading_group, q=True, renderable=True):
#             if shading_group not in ["initialShadingGroup", "initialParticleSE", "defaultLightSet", "defaultObjectSet"]:
#                 # connection to dag objects
#                 objs = cmds.sets(shading_group, q=True)

#                 # connection to render layers
#                 layers = cmds.listConnections(shading_group, type="renderLayer") or []
#                 material_templates = cmds.listConnections(shading_group, type="materialTemplate") or []
#                 shapes = cmds.listConnections(shading_group, type="shape", p=1, d=1, s=0) or []

#                 if not objs and not layers and not material_templates and not shapes:
#                     # empty shading group
#                     return True
#                 else:
#                     # check to make sure at least one shader is connected to the group
#                     connected = False

#                     # Check Maya shader connections
#                     attributes = [".surfaceShader", ".volumeShader", ".displacementShader"]
#                     for attr in attributes:
#                         if cmds.listConnections(shading_group + attr):
#                             connected = True
#                             break

#                     # Check custom shader connections
#                     if not connected:
#                         custom_shaders_array = cmds.callbacks(executionHI="allConnectedShaders", hook="allConnectedShaders", sh=shading_group) or []
#                         for shader in custom_shaders_array:
#                             if shader:
#                                 connected = True
#                                 break

#                     if not connected:
#                         return True

#         return False


# print(f'is_any_shading_group_unused: {is_any_shading_group_unused()}')

# if is_any_shading_group_unused():
#     print('Found unused Shading Groups...do something')
#     # Delete Unused Nodes
#     mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

# else:
#     print('No unused Shading Groups found... do something else')


# #################
# ##                                                                                                        Validation - Choose Asset Type (JSON storage)


# ASSET TYPE assignment for:
#   UE Import Material Attachment
#   UE Import Initial Folder Hierarchy Setup
#   UE Import LOD Tag


