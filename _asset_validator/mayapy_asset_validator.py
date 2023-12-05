

"""
Maya/QT UI template
Maya 2024
"""
import sys
import os 
import inspect
import importlib     
import json 

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
from PySide2.QtCore import QUrl
from functools import partial # optional, for passing args during signal function calls

from utils import mayapy_asset_validator_utils
importlib.reload(mayapy_asset_validator_utils)           # Reloads imported .py file, without, edits to this imported file will not carry over

class ValidationError(Exception):
    pass

class AssetValidator(QtWidgets.QWidget):
    """
    Create a default tool window.
    """
    window = None
    
    def __init__(self, parent = None):
        """
        Initialize class.
        """
        super(AssetValidator, self).__init__(parent = parent)

        # Set window flags to create a standalone window
        self.setWindowFlags(QtCore.Qt.Window)

        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_dir = os.path.join(script_dir, 'mayapy_asset_validator.ui')
        #load the created UI widget
        self.mainWidget = QtUiTools.QUiLoader().load(ui_dir)
    
        #attach the widget to the instance of this class (aka self)
        self.mainWidget.setParent(self)

        # Set initial Window Size
        self.resize(577, 166)  # Set the size to match your .ui file dimensions
				# Set initial Window Size
        self.adjustSize()

        ####
        # find interactive elements of UI
        self.comboBox_LIST_attr_asset_type = self.mainWidget.findChild(QtWidgets.QComboBox, 'comboBox_LIST_attr_asset_type')

        self.btn_freeze_transforms = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_freeze_transforms')
        self.btn_reset_pivot = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_reset_pivot')
        self.btn_delete_construction_history = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_delete_construction_history')
        self.btn_delete_unused_shaders = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_delete_unused_shaders')

        self.btn_validate = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_validate')

        self.btn_closeWindow = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_closeWindow')
        self.btn_help_url = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_help_url')

        ####
        # assign clicked handler to buttons
        self.comboBox_LIST_attr_asset_type.activated.connect(self.validation_btns_state)

        self.btn_freeze_transforms.clicked.connect(self.freeze_transforms)
        self.btn_reset_pivot.clicked.connect(self.reset_pivot)
        self.btn_delete_construction_history.clicked.connect(self.delete_construction_history)
        self.btn_delete_unused_shaders.clicked.connect(self.delete_unused_shaders)

        self.btn_validate.clicked.connect(self.run_through_all_validations)

        self.btn_closeWindow.clicked.connect(self.closeWindow)
        self.btn_help_url.clicked.connect(self.help_url)

        ####
        # OUTPUT LOG 
        self.widget_toggle_output_log = self.mainWidget.findChild(QtWidgets.QWidget, 'widget_toggle_output_log')
        self.label_toggle_output_log = self.mainWidget.findChild(QtWidgets.QLabel, 'label_toggle_output_log')
        self.label_toggle_output_log_text = self.mainWidget.findChild(QtWidgets.QLabel, 'label_toggle_output_log_text')
        self.textEdit_output_log = self.mainWidget.findChild(QtWidgets.QTextEdit, 'textEdit_output_log')

        self.label_toggle_output_log_text.setStyleSheet("font-weight: bold;")
        self.label_toggle_output_log.setPixmap(QtGui.QPixmap(f':/teDownArrow.png').scaledToHeight(12))

        self.widget_toggle_output_log.installEventFilter(self)   # Install an event filter on the child widget

        ####
        # VALIDATION LABELS
        self.label_loaded_asset_name = self.mainWidget.findChild(QtWidgets.QLabel, 'label_loaded_asset_name')
        self.lineEdit_loaded_asset_name = self.mainWidget.findChild(QtWidgets.QLineEdit, 'lineEdit_loaded_asset_name')

        self.label_validate_is_single_asset_in_scene = self.mainWidget.findChild(QtWidgets.QLabel, 'label_validate_is_single_asset_in_scene')
        self.label_is_asset_name_valid = self.mainWidget.findChild(QtWidgets.QLabel, 'label_is_asset_name_valid')
        self.label_is_file_name_valid = self.mainWidget.findChild(QtWidgets.QLabel, 'label_is_file_name_valid')
        #-----
        self.label_is_transform_frozen = self.mainWidget.findChild(QtWidgets.QLabel, 'label_is_transform_frozen')
        self.label_is_pivot_worldspace_zero = self.mainWidget.findChild(QtWidgets.QLabel, 'label_is_pivot_worldspace_zero')
        self.label_is_construction_history_deleted = self.mainWidget.findChild(QtWidgets.QLabel, 'label_is_construction_history_deleted')
        self.label_are_shading_groups_all_assigned = self.mainWidget.findChild(QtWidgets.QLabel, 'label_are_shading_groups_all_assigned')

        ###
        ###
        # Initialize Global LISTS + DICTs + SWITCHes
        self.LIST_validation_labels = [
            self.label_validate_is_single_asset_in_scene,
            self.label_is_asset_name_valid,
            self.label_is_file_name_valid,
            #-----
            self.label_is_transform_frozen,
            self.label_is_pivot_worldspace_zero,
            self.label_is_construction_history_deleted,
            self.label_are_shading_groups_all_assigned,
        ]
        self.LIST_validation_btns = [
            self.btn_freeze_transforms,
            self.btn_reset_pivot,
            self.btn_delete_construction_history,
            self.btn_delete_unused_shaders,
            self.btn_validate
        ]

        ###
        ###
        # Init Logic Functions to Run
        self.run_through_all_validations()
        self.populate_comboBox_LIST_attr_asset_type()
        self.validation_btns_state()



    """
    Init Combo Box Function
    """
    # Populate Asset Type using custom JSON DataTable 
    def populate_comboBox_LIST_attr_asset_type(self):

        ###
        ###
        # Finding Paths
        # # Get the path of the current Python file
        # current_file_path = os.path.abspath(__file__)
        # print("current_file_path:", current_file_path)

        # Get Parent Folder Path
        script_directory_path = os.path.dirname(inspect.getfile(inspect.currentframe()))
        # Get Child Folder Path with JSON File
        asset_validator_DB_path = os.path.join(script_directory_path, 'data', 'mayapy_asset_validator_DB.json') # Add os.path.sep to have code be OS-agnostic (instead of hard coded backslash in path.join) --OR-- use os.path.join with individual components separated by commas
        #
        ###
        
        # Load JSON DB and store asset_types DB list into py LIST
        try:
            with open(asset_validator_DB_path, "r") as json_file:
                asset_validator_DB = json.load(json_file)
        except Exception as e:
            raise ValidationError(f'Error decoding JSON: {str(e)}')
        self.LIST_attr_asset_type = sorted(asset_validator_DB["asset_validator_DB"]["asset_types"]) # sort list alphabetically

        ###
        # push to GUI
        self.comboBox_LIST_attr_asset_type.clear()
        self.comboBox_LIST_attr_asset_type.addItem('-- Select Asset Type --')
        self.comboBox_LIST_attr_asset_type.addItems(self.LIST_attr_asset_type)
        #
        ###


    """
    BTN PRESS FUNCTIONS
    """

    # ENABLE UX if user has selected an ASSET TYPE
    def validation_btns_state(self):

        icon_locked = QtGui.QPixmap(f':/lock.png').scaledToHeight(32)

        # ENABLE UX if user has selected an ASSET TYPE
        # FLUSH/RESET UX LOGIC anytime user selects comboBox
        if self.comboBox_LIST_attr_asset_type.currentText() in self.LIST_attr_asset_type:
                for validation_btn in self.LIST_validation_btns:
                    validation_btn.setEnabled(True)

                self.UTILITY_set_attr_asset_type()
                self.run_through_all_validations()

        #DISABLE UX below comboBox if user has not selected ASSET TYPE
        else:
                for validation_btn in self.LIST_validation_btns:
                    validation_btn.setEnabled(False)
                # set validation label icons
                for validation_label in self.LIST_validation_labels:
                    validation_label.setPixmap(icon_locked)
                # Clear Log
                self.textEdit_output_log.setHtml(f'')

    # On BTN press, Run through all validations inside ValidationUtils Class -- self.btn_validate.clicked.connect(self.run_through_all_validations)
    def run_through_all_validations(self):
        current_outputLog =  self.textEdit_output_log.toHtml()
        self.textEdit_output_log.setHtml(f'{current_outputLog} ------------')

        self.lineEdit_loaded_asset_name.setText(self.UTILITY_get_asset_name())

        # If all Validation Checks PASS, print
        self.validations_all_passed = False

        # Build new Validation Instance based on get_asset_name function (grabs asset[0] in Maya Outliner)
        Validate = mayapy_asset_validator_utils.ValidationUtils(self.UTILITY_get_asset_name(), self.textEdit_output_log)

        # invoke methods and get return values to check if validaions have all passed
        bool_single_asset_in_scene = Validate.is_single_asset_in_scene(self.label_validate_is_single_asset_in_scene)
        bool_asset_name_is_valid = Validate.is_asset_name_valid(self.label_is_asset_name_valid)
        bool_file_name_is_valid = Validate.is_file_name_valid(self.label_is_file_name_valid)
        #-----
        bool_transform_is_frozen = Validate.is_transforms_frozen(self.label_is_transform_frozen)
        bool_pivot_is_worldspace_zero = Validate.is_pivot_worldspace_zero(self.label_is_pivot_worldspace_zero)
        bool_construction_history_deleted = Validate.is_construction_history_deleted(self.label_is_construction_history_deleted)
        bool_shading_groups_all_assigned = Validate.are_shading_groups_all_assigned(self.label_are_shading_groups_all_assigned)


        # Check if all boolean values are True
        self.validations_all_passed = all([
            bool_single_asset_in_scene,
            bool_asset_name_is_valid,
            bool_file_name_is_valid,
            #-----
            bool_transform_is_frozen,
            bool_pivot_is_worldspace_zero,
            bool_construction_history_deleted,
            bool_shading_groups_all_assigned
        ])

        # If all validations have passed, print to output log
        if self.validations_all_passed:
            text_input = 'ALL VALIDATIONS HAVE PASSED!'
            current_outputLog =  self.textEdit_output_log.toHtml()
            self.textEdit_output_log.setHtml(f'{current_outputLog} {text_input}')
            Validate.move_output_log_cursor_to_end()
        
    # On BTN press, Freeze transforms for the specified object -- self.btn_freeze_transforms.clicked.connect(self.freeze_transforms)
    def freeze_transforms(self):

        cmds.makeIdentity(self.UTILITY_get_asset_name(), apply=True, translate=True, rotate=True, scale=True)
        self.run_through_all_validations()

    # On BTN press, reset pivot -- self.btn_reset_pivot.clicked.connect(self.reset_pivot)
    def reset_pivot(self):

        ####
        # Store the original location
        original_location = cmds.xform(self.UTILITY_get_asset_name(), query=True, rotatePivot=True, worldSpace=True)
        # Move the object with the relative pivot point set to the origin
        cmds.move(0, 0, 0, self.UTILITY_get_asset_name(), rotatePivotRelative=True)
        # Freeze transforms for the specified object
        cmds.makeIdentity(self.UTILITY_get_asset_name(), apply=True, translate=True, rotate=True, scale=True)
        ####
        self.run_through_all_validations()

    def delete_construction_history(self):

        # Delete construction history for the specified object
        cmds.delete(self.UTILITY_get_asset_name(), constructionHistory=True, ch=True)
        self.run_through_all_validations()

    def delete_unused_shaders(self):

        # Delete Unused Nodes
        mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
        self.run_through_all_validations()

    def help_url(self):
            url = QUrl('https://github.com/BlakeXYZ/Maya-Tools/tree/main/_asset_validator#readme')  # Replace with the URL you want to open
            QtGui.QDesktopServices.openUrl(url)

    """
    UTILITY FUNCTIONS
    Called inside BTN PRESS FUNCTIONS
    """

    def UTILITY_get_asset_name(self):
        
        # List all geometry     
        list_geo = cmds.ls(geometry=True)
        mesh_info = list_geo[0]

        # Use listRelatives to get the parent of the object
        transform_info = cmds.listRelatives(mesh_info, parent=True)[0]
        asset_name = transform_info

        return asset_name
    

    # Set Asset Attribute for Asset when ComboBox selected
    # called inside validation_btns_state
    def UTILITY_set_attr_asset_type(self):

        asset_name = self.UTILITY_get_asset_name()
        # # Use listRelatives to get all shapes under the transform node
        # mesh_info = cmds.listRelatives(asset_name, shapes=True)[0]

        # Name of the string attribute
        attr_is_AssetType = "Asset_Type"
        # Value to set for the string attribute
        attr_value = self.comboBox_LIST_attr_asset_type.currentText()

        # Check if Attr exsists, if NOT, create one
        if not cmds.attributeQuery(attr_is_AssetType, node=asset_name, exists=True):
            try:
                # Add a custom float attribute named "Asset_Type"
                cmds.addAttr(asset_name, longName=attr_is_AssetType, dataType="string")
                print("Custom attribute 02 added successfully!")
            except Exception as e:
                print(f"Error adding custom attribute {attr_is_AssetType}: {str(e)}")
        # else:
            # print(f"{attr_name} already exists")

        # Set the value for the "Asset_Type" attr
        try:
            cmds.setAttr(f"{asset_name}.{attr_is_AssetType}", attr_value, type="string")
            print("setAttr added successfully!")
        except Exception as e:
            print(f"Error setting attribute {attr_is_AssetType} to : {str(e)}")


    """
    OUTPUT LOG FUNCTIONS
    """

    # GUI Press to toggle output log visibility
    def toggle_output_log(self):
        
        # Collapse Arrow GUI icons
        icon_collapsed = QtGui.QPixmap(f':/teRightArrow.png').scaledToHeight(12)
        icon_expanded = QtGui.QPixmap(f':/teDownArrow.png').scaledToHeight(12)

        # get isVisible bool and set to current visibility
        current_visibility = self.textEdit_output_log.isVisible()

        # set isVisible to opposite of current bool value
        self.textEdit_output_log.setVisible(not current_visibility)

        # set GUI icon based on bool value
        if current_visibility:
            self.label_toggle_output_log.setPixmap(icon_collapsed)
        else:
            self.label_toggle_output_log.setPixmap(icon_expanded)


    def eventFilter(self, obj, event):

        # if child widget_toggle_output_log widget clicked
        if obj == self.widget_toggle_output_log and event.type() == QtCore.QEvent.Type.MouseButtonRelease:
            self.toggle_output_log()

            return True  # Event handled
        return super().eventFilter(obj, event)


    """
    BASE FUNCTIONS
    """

    def resizeEvent(self, event):
        """
        Called on automatically generated resize event
        """
        self.mainWidget.resize(self.width(), self.height())
        
    def closeWindow(self):
        """
        Close window.
        """
        print ('closing window')
        self.destroy()
    
def openWindow():
    """
    ID Maya and attach tool window.
    """
    # Maya uses this so it should always return True
    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in (QtWidgets.QApplication.allWindows()):
            if 'myToolWindowName' in win.objectName(): # update this name to match name below
                win.destroy()

    #QtWidgets.QApplication(sys.argv)
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    AssetValidator.window = AssetValidator(parent = mayaMainWindow)
    AssetValidator.window.setObjectName('myToolWindowName') # code above uses this to ID any existing windows
    AssetValidator.window.setWindowTitle('Asset Validator')
    AssetValidator.window.show()
    
openWindow()



