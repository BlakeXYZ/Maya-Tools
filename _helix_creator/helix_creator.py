"""
Maya/QT UI template
Maya 2024
"""

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from functools import partial # optional, for passing args during signal function calls
import sys, os, math, string

class ValidationError(Exception):
    pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(387, 492)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 109, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(55, -1, 55, -1)
        self.label_sphereSpread = QLabel(self.centralwidget)
        self.label_sphereSpread.setObjectName(u"label_sphereSpread")
        self.label_sphereSpread.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.label_sphereSpread, 0, 0, 1, 1)

        self.spinBox_sphereSpread = QSpinBox(self.centralwidget)
        self.spinBox_sphereSpread.setObjectName(u"spinBox_sphereSpread")
        self.spinBox_sphereSpread.setMinimumSize(QSize(100, 0))
        self.spinBox_sphereSpread.setValue(2)

        self.gridLayout.addWidget(self.spinBox_sphereSpread, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox_helixRadius = QSpinBox(self.centralwidget)
        self.spinBox_helixRadius.setObjectName(u"spinBox_helixRadius")
        self.spinBox_helixRadius.setMinimumSize(QSize(100, 0))
        self.spinBox_helixRadius.setValue(10)

        self.gridLayout.addWidget(self.spinBox_helixRadius, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.spinBox_parentGroupSpeed = QSpinBox(self.centralwidget)
        self.spinBox_parentGroupSpeed.setObjectName(u"spinBox_parentGroupSpeed")
        self.spinBox_parentGroupSpeed.setMinimumSize(QSize(100, 0))
        self.spinBox_parentGroupSpeed.setMaximum(400)
        self.spinBox_parentGroupSpeed.setValue(55)

        self.gridLayout.addWidget(self.spinBox_parentGroupSpeed, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 3, 0, 1, 4)

        self.btn_help = QPushButton(self.centralwidget)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(75, 25))

        self.gridLayout_3.addWidget(self.btn_help, 6, 2, 1, 1)

        self.btn_closeWindow = QPushButton(self.centralwidget)
        self.btn_closeWindow.setObjectName(u"btn_closeWindow")
        self.btn_closeWindow.setMinimumSize(QSize(75, 25))

        self.gridLayout_3.addWidget(self.btn_closeWindow, 6, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 7, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(55, 15, 55, -1)
        self.btn_resetValues = QPushButton(self.centralwidget)
        self.btn_resetValues.setObjectName(u"btn_resetValues")
        self.btn_resetValues.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.btn_resetValues, 1, 0, 1, 1)

        self.btn_helix = QPushButton(self.centralwidget)
        self.btn_helix.setObjectName(u"btn_helix")
        self.btn_helix.setMinimumSize(QSize(0, 35))

        self.gridLayout_2.addWidget(self.btn_helix, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 4, 0, 1, 4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 4)

        self.verticalSpacer_3 = QSpacerItem(20, 109, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 5, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_sphereSpread.setText(QCoreApplication.translate("MainWindow", u"Sphere Spread", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Helix Radius", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Spin Speed", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_closeWindow.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.btn_resetValues.setText(QCoreApplication.translate("MainWindow", u"Reset to Default Values", None))
        self.btn_helix.setText(QCoreApplication.translate("MainWindow", u"Create Helix", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Helix Creator", None))
    # retranslateUi

class mayaQT_rainbow_helix(QtWidgets.QMainWindow):

    window = None
    
    def __init__(self, parent = None):
        """
        Initialize class.
        """
        super(mayaQT_rainbow_helix, self).__init__(parent = parent)

        # Set window flags to create a standalone window
        self.setWindowFlags(QtCore.Qt.Window)

        self.mainWidget = Ui_MainWindow()
        self.mainWidget.setupUi(self)  # Set up the UI within this widget
    

        # Set initial Window Size
        self.resize(340, 420)  # Set the size to match your .ui file dimensions

        ###
        ###
        # find interactive elements of UI
        self.spinBox_sphereSpread = self.findChild(QtWidgets.QSpinBox, 'spinBox_sphereSpread')
        self.spinBox_helixRadius = self.findChild(QtWidgets.QSpinBox, 'spinBox_helixRadius')
        self.spinBox_parentGroupSpeed = self.findChild(QtWidgets.QSpinBox, 'spinBox_parentGroupSpeed')

        self.btn_resetValues = self.findChild(QtWidgets.QPushButton, 'btn_resetValues')
        self.btn_helix = self.findChild(QtWidgets.QPushButton, 'btn_helix')

        self.btn_help = self.findChild(QtWidgets.QPushButton, 'btn_help')
        self.btn_closeWindow = self.findChild(QtWidgets.QPushButton, 'btn_closeWindow')

        ###
        ###
        # assign clicked handler to buttons
        self.btn_resetValues.clicked.connect(self.resetValues)
        self.btn_helix.clicked.connect(self.rainbowHelix)

        self.btn_help.clicked.connect(self.helpButton)
        self.btn_closeWindow.clicked.connect(self.closeWindow)

    def rainbowHelix(self):

        # Stop the time slider playback
        cmds.play(state=False)
        
        groupCount = 36
        sphereSpread = self.spinBox_sphereSpread.value()
        helixRadius = self.spinBox_helixRadius.value()
        parentGroupSpeed = self.spinBox_parentGroupSpeed.value()

        helixGroupPrefix = str(self.UTIL_helixGroupPrefix()) + '_'

        for currentGroup in range(groupCount):

            sphereA = str(helixGroupPrefix) + 'sphere_a_' + str(currentGroup)
            sphereB = str(helixGroupPrefix) + 'sphere_b_' + str(currentGroup)
            sphereC = str(helixGroupPrefix) + 'sphere_c_' + str(currentGroup)
            

            cmds.polySphere(name = sphereA)[0]
            cmds.move(sphereSpread,0,0)

            cmds.polySphere(name = sphereB, r=.75)[0]
            cmds.rotate(0,120,0, r=True, os=True)
            cmds.move(sphereSpread,0,0, r=True, os=True, wd=True)

            cmds.polySphere(name = sphereC, r=.5)[0]
            cmds.rotate(0,240,0, r=True, os=True)
            cmds.move(sphereSpread,0,0, r=True, os=True, wd=True)

            # Create Parent Group
            cmds.select(d=True)   
            parentGroupName = str(helixGroupPrefix) + 'group_' + str(currentGroup)
            cmds.group(name = parentGroupName, em=True)
            cmds.parent(sphereA, sphereB, sphereC, parentGroupName)

            # Rotate Parent Group
            cmds.select(parentGroupName)   
            cmds.rotate(0,(40 * currentGroup),0, r=True, ws=True)
            cmds.makeIdentity(apply=True, r=True)

            # Move Parent Group
            cmds.move(helixRadius,0,0, r=True, os=True, wd=True)

            # Animate Parent Group
            expressionString = f'{parentGroupName}.rotateY = time * {parentGroupSpeed};'
            cmds.expression(string=expressionString, object=parentGroupName, ae=True, uc='all')

            # Create Grandparent Group
            cmds.select(d=True)   
            grandparentGroupName = str(helixGroupPrefix) + 'grandgroup_' + str(currentGroup)
            cmds.group(name = grandparentGroupName, em=True)
            cmds.parent(parentGroupName, grandparentGroupName)

            # Rotate Grandparent Group
            cmds.select(grandparentGroupName)   
            cmds.rotate(0,0,(10 * currentGroup), r=True, ws=True)

            # Set RGB vertex color values
            cmds.select(d=True)   
            cmds.select(sphereA, sphereB, sphereC)
            redVal = math.sin(math.radians(currentGroup * 12 ))
            greenVal = math.sin(math.radians(currentGroup * 12 + 120))
            blueVal = math.sin(math.radians(currentGroup * 12  + 240))
            # Convert from -1,1 to 0,1 range
            redVal = (redVal + 1) / 2
            greenVal = (greenVal + 1) / 2
            blueVal = (blueVal + 1) / 2
            # Apply Poly Color
            cmds.polyColorPerVertex(rgb=(redVal,greenVal,blueVal), cdo = True)

        ### Leave Loop

        # Create Helix Master Group
        cmds.select(d=True)   
        helixMasterGroupName = str(helixGroupPrefix) + 'helix_Group'
        cmds.group(name = helixMasterGroupName, em=True)
        
        # Select All grand groups and parent
        prefix = str(helixGroupPrefix) + 'grandgroup_' 
        selected_groups = cmds.ls('*' + prefix + '*', type='transform')
        cmds.select(selected_groups)
        cmds.parent(selected_groups, helixMasterGroupName)
        cmds.select(d=True)   

    def resetValues(self):
        self.spinBox_sphereSpread.setValue(2)
        self.spinBox_helixRadius.setValue(10)
        self.spinBox_parentGroupSpeed.setValue(55)
 
    def helpButton(self):
        # Replace 'https://example.com' with the actual URL you want to open
        url = QtCore.QUrl('https://github.com/BlakeXYZ/Maya-Tools/tree/main/_helix_creator#readme')
        QtGui.QDesktopServices.openUrl(url)

    def UTIL_helixGroupPrefix(self):
        # Search for existing 'helix_Group' with a prefix
        existing_groups = cmds.ls('*' + 'helix_Group' + '*', type='transform')

        # Extract the existing prefixes
        existing_prefixes = [group.split('_')[0] for group in existing_groups]

        # If there are no existing groups, start with 'A' as the default
        if not existing_prefixes:
            helixGroupPrefix = 'A'
        else:
            # Sort the existing prefixes
            existing_prefixes.sort()

            # Find the first available letter in the sequence
            for letter in string.ascii_uppercase:
                if letter not in existing_prefixes:
                    helixGroupPrefix = letter
                    break
            else:
                # If all letters are taken, use the next letter after 'Z' ('AA', 'AB', etc.)
                last_prefix = existing_prefixes[-1]
                helixGroupPrefix = string.ascii_uppercase[(string.ascii_uppercase.index(last_prefix) + 1) % 26]

        return(helixGroupPrefix)
 
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
            if 'Helix Creator' in win.objectName(): # update this name to match name below
                win.destroy()

    #QtWidgets.QApplication(sys.argv)
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    mayaQT_rainbow_helix.window = mayaQT_rainbow_helix(parent = mayaMainWindow)
    mayaQT_rainbow_helix.window.setObjectName('Helix Creator') # code above uses this to ID any existing windows
    mayaQT_rainbow_helix.window.setWindowTitle('Helix Creator')
    mayaQT_rainbow_helix.window.show()
    
if __name__ == '__main__':
    openWindow()