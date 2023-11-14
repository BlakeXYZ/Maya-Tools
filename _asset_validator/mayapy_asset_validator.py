

"""
Maya/QT UI template
Maya 2024
"""

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
from functools import partial # optional, for passing args during signal function calls
import sys, os

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


        ###
        ###
        # find interactive elements of UI

        self.label_loaded_asset_name = self.mainWidget.findChild(QtWidgets.QLabel, 'label_loaded_asset_name')
        self.label_validate_single_asset_in_scene = self.mainWidget.findChild(QtWidgets.QLabel, 'label_validate_single_asset_in_scene')

        self.btn_closeWindow = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_closeWindow')




        
        
        ###
        ###
        # assign clicked handler to buttons

        self.btn_closeWindow.clicked.connect(self.closeWindow)


        ###
        ### 
        
        self.label_loaded_asset_name.setText(self.get_asset_name())
        
        self.validate_single_asset_in_scene()





    
    """
    Your code goes here
    """

    def get_asset_name(self):

        # List all geometry
        list_geo = cmds.ls(geometry=True)
        mesh_info = list_geo[0]

        # Use listRelatives to get the parent of the object
        transform_info = cmds.listRelatives(mesh_info, parent=True)[0]
        asset_name = transform_info

        return asset_name
    
################
##                                                                                                        Validation - Missing Asset in Scene and/or too many assets in scene

    def validate_single_asset_in_scene(self):
        # IF VALIDATION passes, allow to continue with rest of Tool Use

        self.single_asset_in_scene = False

        # List all geometry
        list_geo = cmds.ls(geometry=True)

        # check if single asset is inside scene VALIDATION FUNCTION

        if len(list_geo) == 1:
            self.single_asset_in_scene = True
        elif len(list_geo) > 1:
            self.single_asset_in_scene = False
        else:
            self.single_asset_in_scene = False

        self.validation_StyleSheet('label_validate_single_asset_in_scene', self.single_asset_in_scene)

#TODO: Setup Output Log... find old code in repo that sets up Log to print at bottom and always keep log scrolled to bottom
#
#         def UTILITY_move_consoleLog_cursor_to_end(self): inside ue-tools > importTextures.py
#           

#TODO: Setup collapsible widget to show and hide output log

    def validation_StyleSheet(self, ui_name, validation_check):

        ui_widget = getattr(self, ui_name)

        icon_confirm = QtGui.QPixmap(f':/confirm.png').scaledToHeight(32)
        icon_error = QtGui.QPixmap(f':/error.png').scaledToHeight(32)


        if validation_check == True:
            ui_widget.setPixmap(icon_confirm)
        elif validation_check == False:
            ui_widget.setPixmap(icon_error)
        else:
            ui_widget.setStyleSheet('background-color: black')


            
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

