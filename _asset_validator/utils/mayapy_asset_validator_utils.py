import os

import maya.cmds as cmds
import maya.mel as mel
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets


class ValidationError(Exception):
    pass

class ValidationUtils:

    def __init__(self, asset_name, textEdit_output_log): #constructor
        self.asset_name = asset_name                        # pass in custom function self.get_asset_name() and it's retun value
        self.textEdit_output_log = textEdit_output_log      # pass in self.mainWidget.findChild(QtWidgets.QTextEdit, 'textEdit_output_log') inside class of QtWidgets.QWidget

    """
    HELPER FUNCTIONS
    Called inside each Validation Function
    """
#####
#TODO: Differentiate between ERROR WARNING and SUCCESS
#
#      Print to Maya Output Log and provide more context to Failed Validations
#####

    def print_to_output_log(self, bool_check, text_validation_name, text_validation_fail_reason=None):

        if text_validation_fail_reason is None:
            text_validation_fail_reason = ''
            
        if not bool_check:
            text_input = (f'{text_validation_name}: {bool_check} {text_validation_fail_reason}')
            current_outputLog =  self.textEdit_output_log.toHtml()
            self.textEdit_output_log.setHtml(f'{current_outputLog} {text_input}')

        self.move_output_log_cursor_to_end()

    # Handle QT textEdit panel view to always sit at latest log print
    def move_output_log_cursor_to_end(self):
        cursor = self.textEdit_output_log.textCursor()
        cursor.movePosition(cursor.End)
        self.textEdit_output_log.setTextCursor(cursor)
        self.textEdit_output_log.ensureCursorVisible()    

    # Is called inside each Validation Function: Sets and Toggles GUI Label based on Functions Bool Value
    def validation_label_toggle(self, ui_label_object, validation_check):

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


    """
    VALIDATION FUNCTIONS
    """

    ####
    # VALIDATE one asset inside scene
    def is_single_asset_in_scene(self, ui_label_object):
        # IF VALIDATION passes, allow to continue with rest of Tool Use
                
        text_validation_name = 'is_single_asset_in_scene'
        bool_single_asset_in_scene = False         # Init Bool check to False

        # List all geometry
        list_geo = cmds.ls(dag=True, long=True, type='transform', v=True) #dag=true flag limits the result to direct descendants of the DAG (Directed Acyclic Graph)

        # check if single asset is inside scene VALIDATION FUNCTION - conditional expressions yay
        bool_single_asset_in_scene = False if len(list_geo) != 1 else True

        # Set GUI Label for Validation Func
        self.validation_label_toggle(ui_label_object, bool_single_asset_in_scene)
        # Set Output Log Text
        self.print_to_output_log(bool_single_asset_in_scene, text_validation_name)

        return bool_single_asset_in_scene
    ####

    ####
    # VALIDATE Freeze Transforms
    def is_transforms_frozen(self, ui_label_object): 

        text_validation_name = 'is_transforms_frozen'
        bool_transform_is_frozen = False

        # Save the original transform values
        translate_value = cmds.getAttr(self.asset_name + '.translate')[0]
        rotate_value = cmds.getAttr(self.asset_name + '.rotate')[0]
        scale_value = cmds.getAttr(self.asset_name + '.scale')[0]

        # Check if all transforms are zeroed out
        if all(value == 0 for value in translate_value) and all(value == 0 for value in rotate_value) and all(value == 1 for value in scale_value):
            bool_transform_is_frozen = True
        else:
            bool_transform_is_frozen = False
        
        # Set GUI Label for Validation Func
        self.validation_label_toggle(ui_label_object, bool_transform_is_frozen)
        # Set Output Log Text
        self.print_to_output_log(bool_transform_is_frozen, text_validation_name)

        return bool_transform_is_frozen
    ####

    ####
    # VALIDATE Center PIVOT/ORIGIN and ASSET to 0,0,0 World Space
    def is_pivot_worldspace_zero(self, ui_label_object): 

        text_validation_name = 'is_pivot_worldspace_zero'
        bool_pivot_is_worldspace_zero = False

        # check pivot location
        pivot_location = cmds.xform(self.asset_name, query=True, rotatePivot=True, worldSpace=True)

        # Check if transforms are zeroed out
        if all(value == 0 for value in pivot_location):
            bool_pivot_is_worldspace_zero = True
        else:
            bool_pivot_is_worldspace_zero = False

        # Set GUI Label for Validation Func
        self.validation_label_toggle(ui_label_object, bool_pivot_is_worldspace_zero)
        # Set Output Log Text
        self.print_to_output_log(bool_pivot_is_worldspace_zero, text_validation_name)

        return bool_pivot_is_worldspace_zero
    ####

    ####
    # VALIDATE Correct Asset Name + File Name
    # compares against Folder Name using helper function: def get_folder_and_file_name()
    def is_asset_name_valid(self, ui_label_object):

        ## All need to MATCH:       Folder Name         > File Name              > Asset Name
        ##                          CharacterABC_Skin01 > CharacterABC_Skin01.ma > CharacterABC_Skin01.fbx
        text_validation_name = 'is_asset_name_valid'
        bool_asset_name_is_valid = False

        folder_name, file_name = self.get_folder_and_file_name()

        # compare stored variables
        if self.asset_name == folder_name:
            bool_asset_name_is_valid = True
        else:
            bool_asset_name_is_valid = False

        # Set GUI Label for Validation Func
        self.validation_label_toggle(ui_label_object, bool_asset_name_is_valid)
        # Set Output Log Text
        text_validation_fail_reason = (f'-- asset_name: "{self.asset_name}" does not match folder_name: "{folder_name}"')
        self.print_to_output_log(bool_asset_name_is_valid, text_validation_name, text_validation_fail_reason)

        return bool_asset_name_is_valid
    
    # Validates correct file name, compares against folder_name
    def is_file_name_valid(self, ui_label_object):

        text_validation_name = 'is_file_name_valid'
        bool_file_name_is_valid = False

        folder_name, file_name = self.get_folder_and_file_name()

        # compare stored variables and Validation for file_name 'unsaved scene'
        if file_name == folder_name and file_name is not None:
            bool_file_name_is_valid = True
        else:
            bool_file_name_is_valid = False

        # Set GUI Label for Validation Func
        self.validation_label_toggle(ui_label_object, bool_file_name_is_valid)
        # Set Output Log Text
        if file_name == None: #  Validation for file_name 'unsaved scene'
            text_validation_fail_reason = (f'-- Unsaved Maya Scene!')
        else:
            text_validation_fail_reason = (f'-- file_name: "{file_name}" does not match folder_name: "{folder_name}"')

        self.print_to_output_log(bool_file_name_is_valid, text_validation_name, text_validation_fail_reason)

        return bool_file_name_is_valid
    
    # helper function running inside VALIDATE Correct Asset Name + File Name functions
    def get_folder_and_file_name(self):

        # Get the current scene name
        file_path = cmds.file(q=True, sceneName=True)
        if not file_path:       # Validation for file_name 'unsaved scene'
            folder_name = None
            file_name = None
        else:
            # find and store folder, file and asset names to compare
            folder_name = file_path.rsplit('/', 2)[-2]
            file_name_w_extension = file_path.rsplit('/', 2)[-1]
            file_name, file_extension = os.path.splitext(file_name_w_extension)

        return folder_name, file_name
    ####

    ####
    # VALIDATE Construction History Deleted
    def is_construction_history_deleted(self, ui_label_object):

        text_validation_name = 'is_construction_history_deleted'
        bool_construction_history_deleted = False

        my_history = cmds.listHistory(self.asset_name)

        # Check if the object has a construction history
        if len(my_history) == 1:
            bool_construction_history_deleted = True
        else:
            bool_construction_history_deleted = False

        # Set GUI Label for Validation Func
        self.validation_label_toggle(ui_label_object, bool_construction_history_deleted)
        # Set Output Log Text
        self.print_to_output_log(bool_construction_history_deleted, text_validation_name)
        
        return bool_construction_history_deleted
    ####

    ####
    # VALIDATE All Shading Groups Assigned
    def are_shading_groups_all_assigned(self, ui_label_object): 

        text_validation_name = 'are_shading_groups_all_assigned'
        bool_shading_groups_all_assigned = False

        if self.is_any_shading_group_unused():
            bool_shading_groups_all_assigned = False
        else: 
            bool_shading_groups_all_assigned = True

        # Set GUI Label for Validation Func
        self.validation_label_toggle(ui_label_object, bool_shading_groups_all_assigned)
        # Set Output Log Text
        self.print_to_output_log(bool_shading_groups_all_assigned, text_validation_name)
        
        return bool_shading_groups_all_assigned
    

    def is_any_shading_group_unused(self):
        # List all shading groups in the scene
        shading_groups = cmds.ls(type='shadingEngine')

        for shading_group in shading_groups:

            if not cmds.objExists(shading_group):
                continue

            if cmds.sets(shading_group, q=True, renderable=True):
                if shading_group not in ["initialShadingGroup", "initialParticleSE", "defaultLightSet", "defaultObjectSet"]:
                    # Connection to dag objects
                    objs = cmds.sets(shading_group, q=True)

                    # Connection to render layers
                    layers = cmds.listConnections(shading_group, type="renderLayer") or []
                    material_templates = cmds.listConnections(shading_group, type="materialTemplate") or []
                    shapes = cmds.listConnections(shading_group, type="shape", p=True, d=True, s=False) or []

                    if not objs and not layers and not material_templates and not shapes:
                        # Empty shading group
                        return True
                    else:
                        # Check to make sure at least one shader is connected to the group
                        connected = False

                        # Check Maya shader connections
                        attributes = [".surfaceShader", ".volumeShader", ".displacementShader"]
                        for attr in attributes:
                            if cmds.listConnections(shading_group + attr):
                                connected = True
                                break

                        # Check custom shader connections
                        if not connected:
                            custom_shaders_array = cmds.callbacks(executionHI="allConnectedShaders", hook="allConnectedShaders", sh=shading_group) or []
                            for shader in custom_shaders_array:
                                if shader:
                                    connected = True
                                    break

                        if not connected:
                            return True

        # No unused shading group found
        return False




        ##### Detective work guide for exploring MEL Commands and how they work: https://groups.google.com/g/python_inside_maya/c/N1_wASF3SH4
        ### // mel
        ### whatIs hyperShadePanelMenuCommand
        ### // path to a mel script

        ### If you look through that mel script for the usage of "deleteUnusedNodes", it will bring you to a command like:
        ### MLdeleteUnused

        ### // mel
        ### whatIs MLdeleteUnused
        ### // path to another mel script

        ### If you read that script, you will see that the process of finding unused nodes is multiple stages. It looks at shading groups, and connections, and texture nodes
        ### Then converted mel function to py cmds
        #####


    """
    """


#################
#################
#################
#################
#################
#################



### RAISE VALIDATION example
# # CHECK if number of selected assets is ONE
# if len(selected_assets) != 1:
#     raise ValidationError(f'Please select only 1 Master Material in Content Browser')


#################
#################




# #################
# ##                                                                                                        Validation - Choose Asset Type (JSON storage)


# ASSET TYPE assignment for:
#   UE Import Material Attachment
#   UE Import Initial Folder Hierarchy Setup
#   UE Import LOD Tag




