from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
import sys, os

import testFetch_jira_lib
from pprint import pprint


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
        self.text_issueFieldsInfo = self.mainWidget.findChild(QtWidgets.QTextEdit, 'text_issueFieldsInfo')
        self.comboBox_transitions = self.mainWidget.findChild(QtWidgets.QComboBox, 'comboBox_transitions')

        self.btn_01 = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_01')
        self.btn_02 = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_02')



        ###
        ###
        # assign clicked handler to buttons
        self.comboBox_transitions.currentIndexChanged.connect(self.handleComboBoxSelection)

        self.btn_01.clicked.connect(self.print_to_log)
        self.btn_02.clicked.connect(self.closeWindow)


#TODO: Tidy Up Code below, make more accessible 
############
        # Iterate through the dictionary items and print them to QTextEdit
        formatted_output = '\n'.join([f"{key}: {value}" for key, value in testFetch_jira_lib.DICT_issue_fields_info.items()])

        self.text_issueFieldsInfo.setPlainText(formatted_output)

############
        # Iterate through the dictionary and add names to QComboBox
        # and store transition_id data inside each index, can later be retrieved (see handleComboBoxSelection)
        for transition_id, transition_info in testFetch_jira_lib.DICT_issue_transitions_info.items():
            name = transition_info['name']
            self.comboBox_transitions.addItem(name, userData=transition_id)

        # Set the current index if set_transition is True
            if transition_info['set_transition']:
                index = self.comboBox_transitions.findData(transition_id)
                if index != -1:
                    self.comboBox_transitions.setCurrentIndex(index)




    # Function to handle QComboBox item selection
    def handleComboBoxSelection(self, index):

        print('hello')

        # retrieve stored data inside current index
        selected_transition_id = self.comboBox_transitions.itemData(index)

        # Set all 'set_transition' values to False 
        for transition_id, transition_info in testFetch_jira_lib.DICT_issue_transitions_info.items():
            transition_info['set_transition'] = False

        # Set the selected transition to True
        # access Dict key that matches the currently selected_transition_id and set to True
        if selected_transition_id in testFetch_jira_lib.DICT_issue_transitions_info:
            testFetch_jira_lib.DICT_issue_transitions_info[selected_transition_id]['set_transition'] = True

        pprint(testFetch_jira_lib.DICT_issue_transitions_info)  # Print after the update

        testFetch_jira_lib.push_transition_to_jira(selected_transition_id)



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
    