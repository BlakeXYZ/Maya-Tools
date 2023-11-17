

"""
Maya/QT UI template
Maya 2024
"""
import sys
import os 
import importlib     

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
from functools import partial # optional, for passing args during signal function calls

from utils import mayapy_asset_validator_utils
importlib.reload(mayapy_asset_validator_utils)           # Reloads imported .py file, without, edits to this imported file will not carry over

class ValidationError(Exception):
    pass

class my_Maya_QT_boilerplate(QtWidgets.QWidget):
    """
    Create a default tool window.
    """
    window = None
    
    def __init__(self, parent = None):
        """
        Initialize class.
        """
        super(my_Maya_QT_boilerplate, self).__init__(parent = parent)

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
        self.btn_validate = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_validate')
        self.btn_closeWindow = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_closeWindow')
        
        ####
        # assign clicked handler to buttons
        self.btn_validate.clicked.connect(self.run_through_validations)
        self.btn_closeWindow.clicked.connect(self.closeWindow)

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
        # VALIDATION calls
        self.label_loaded_asset_name = self.mainWidget.findChild(QtWidgets.QLabel, 'label_loaded_asset_name')
        self.label_validate_is_single_asset_in_scene = self.mainWidget.findChild(QtWidgets.QLabel, 'label_validate_is_single_asset_in_scene')
        self.label_is_transform_frozen = self.mainWidget.findChild(QtWidgets.QLabel, 'label_is_transform_frozen')

        self.run_through_validations()



    """
    Playground Code
    """
####
#####
####

    """
    Your code goes here
    """

    def run_through_validations(self):
        self.label_loaded_asset_name.setText(self.get_asset_name())

        # Build new Validation Instance based on get_asset_name function (grabs asset[0] in Maya Outliner)
        Validate = mayapy_asset_validator_utils.ValidationUtils(self.get_asset_name())

        Validate.is_single_asset_in_scene(self.label_validate_is_single_asset_in_scene)
        Validate.is_transform_frozen(self.label_is_transform_frozen)


    def get_asset_name(self):

        # List all geometry
        list_geo = cmds.ls(geometry=True)
        mesh_info = list_geo[0]

        # Use listRelatives to get the parent of the object
        transform_info = cmds.listRelatives(mesh_info, parent=True)[0]
        asset_name = transform_info

        return asset_name
 

#TODO: Setup UTILS.py and call in VALIDATIONs from there, help with code management


#TODO: VALIDATE Button, (refreshes asset) 

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

    # Handle QT textEdit panel view to always sit at latest log print
    def move_output_log_cursor_to_end(self):
        cursor = self.textEdit_output_log.textCursor()
        cursor.movePosition(cursor.End)
        self.textEdit_output_log.setTextCursor(cursor)
        self.textEdit_output_log.ensureCursorVisible()    


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
    my_Maya_QT_boilerplate.window = my_Maya_QT_boilerplate(parent = mayaMainWindow)
    my_Maya_QT_boilerplate.window.setObjectName('myToolWindowName') # code above uses this to ID any existing windows
    my_Maya_QT_boilerplate.window.setWindowTitle('My Maya QT boilerplatee')
    my_Maya_QT_boilerplate.window.show()
    
openWindow()

