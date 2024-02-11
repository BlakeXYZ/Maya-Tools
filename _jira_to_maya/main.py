from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
import sys, os
import logging
import importlib
from pprint import pprint

import testFetch_jira_lib



class ValidationError(Exception):
    pass

class jira_maya_livelink(QtWidgets.QMainWindow):

    """
    Create a default tool window.
    """
    window = None

    def __init__(self, parent = None):
        """
        Initialize class.
        """
        super(jira_maya_livelink, self).__init__(parent = parent)

        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_dir = os.path.join(script_dir, 'main.ui')

        #load the created UI widget
        self.mainWidget = QtUiTools.QUiLoader().load(ui_dir)

        #attach the widget to the instance of this class (aka self)
        self.mainWidget.setParent(self)

        # Set the initial size of the main window to match the size of the loaded .ui file
        self.resize(self.mainWidget.size())

        ###
        ###
        # find interactive elements of UI
        self.btn_refresh = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_refresh')

        self.text_issueFieldsInfo = self.mainWidget.findChild(QtWidgets.QTextEdit, 'text_issueFieldsInfo')
        self.comboBox_transitions = self.mainWidget.findChild(QtWidgets.QComboBox, 'comboBox_transitions')

        self.btn_01 = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_01')
        self.btn_closeWindow = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_closeWindow')



        ###
        ###
        # assign clicked handler to buttons
        self.btn_refresh.clicked.connect(self.refresh_jira_connection)

        self.comboBox_transitions.activated.connect(self.handle_comboBox_selection)

        self.btn_01.clicked.connect(self.print_to_log)
        self.btn_closeWindow.clicked.connect(self.closeWindow)


        #Initial Data Setup
        self.initialize_data()


    def initialize_data(self):
        self.set_text_issueFieldsInfo()
        self.set_comboBox_transitions()

    def set_text_issueFieldsInfo(self):
        # Iterate through the dictionary items and print them to QTextEdit
        formatted_output = '\n'.join([f"{key}: {value}" for key, value in testFetch_jira_lib.DICT_issue_fields_info.items()])
        self.text_issueFieldsInfo.setPlainText(formatted_output)

    def set_comboBox_transitions(self):
        # Iterate through the dictionary and add names to QComboBox
        # and store transition_id data inside each index, can later be retrieved (see handleComboBoxSelection)
        self.comboBox_transitions.clear()
        for transition_id, transition_info in testFetch_jira_lib.DICT_issue_transitions_info.items():
            self.comboBox_transitions.addItem(transition_info['name'])

        # Set the current index if set_transition is True
            if transition_info['set_transition']:
                index = self.comboBox_transitions.findText(transition_info['name'])
                if index != -1:
                    self.comboBox_transitions.setCurrentIndex(index)

    def refresh_jira_connection(self):
         print('running refresh_jira_connection')
         importlib.reload(testFetch_jira_lib)
         self.initialize_data()

    # Function to handle QComboBox item selection
    def handle_comboBox_selection(self):
        print('running handleComboBoxSelection')

        comboBox_transition_name = self.comboBox_transitions.currentText()

        # Find DICT that matches currently selected ComboBox name
        # and set_transition to True and update jira
        for transition_id, transition_info in testFetch_jira_lib.DICT_issue_transitions_info.items():
            if comboBox_transition_name == transition_info['name']:
                transition_info['set_transition'] = True
                testFetch_jira_lib.push_transition_to_jira(transition_id)
            else:
                transition_info['set_transition'] = False

        pprint(testFetch_jira_lib.DICT_issue_transitions_info)  # Print after the update

        self.refresh_jira_connection()

       

        


 


############
            
        
    
    """
    Code goes here
    """

    def print_to_log(self):

        print('btn_01 pressed')


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
        self.close()  # Close the window
        QtWidgets.QApplication.quit()  # Quit the application

if __name__ == '__main__':
    print('\n ** \n *** \n Launching')
    app = QtWidgets.QApplication(sys.argv)
    window = jira_maya_livelink()
    window.show()
    sys.exit(app.exec_())
    