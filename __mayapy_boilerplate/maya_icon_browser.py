"""
# paste this .py file into your scripts directory and run this in a python tab to show the UI
import maya_icon_browser
browser = maya_icon_browser.Window()
browser.show()
"""
__author__ = 'Tyler Thornock'
__doc__ = 'UI to show the possible built-in maya icons that can be used.'
# Tyler Thornock Website - https://charactersetup.com/?p=335

import logging
import shiboken2
from maya import OpenMayaUI, cmds
from PySide2 import QtWidgets, QtGui, QtCore

log = logging.getLogger(__name__)


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        """
        Create a UI that shows all the possible maya icons that can be used.
        """
        if parent is None:
            maya_pointer = OpenMayaUI.MQtUtil.mainWindow()
            parent = shiboken2.wrapInstance(int(maya_pointer), QtWidgets.QMainWindow)
        super(Window, self).__init__(parent)

        # create widgets/actions
        self.setWindowTitle('Maya Icon Browser')
        self.main_frame = QtWidgets.QFrame(self)
        self.main_layout = QtWidgets.QVBoxLayout(self.main_frame)
        self.label = QtWidgets.QLabel('Built-in maya icons, double click to send the name to clipboard, '
                                      'right click for options.', self)
        self.filter_lineedit = QtWidgets.QLineEdit(self.main_frame)
        self.icon_listwidget = QtWidgets.QListWidget(self.main_frame)
        self.scale_to_fit_action = QtWidgets.QAction('Scale to Fit', self, checkable=True, checked=True)
        self.to_clipboard_action = QtWidgets.QAction('Copy to Clipboard', self)

        # add to the window/layouts
        self.setCentralWidget(self.main_frame)
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.filter_lineedit)
        self.main_layout.addWidget(self.icon_listwidget)

        # setup widgets/connections
        self.label.setWordWrap(True)
        self.filter_lineedit.setPlaceholderText('Filter...')
        self.filter_lineedit.editingFinished.connect(self.filter_changed)

        self.to_clipboard_action.triggered.connect(self.copy_to_clipboard)
        self.scale_to_fit_action.triggered.connect(self.populate)

        self.icon_listwidget.setCursor(QtCore.Qt.WhatsThisCursor)
        self.icon_listwidget.setViewMode(self.icon_listwidget.ListMode)
        self.icon_listwidget.setFlow(self.icon_listwidget.LeftToRight)
        self.icon_listwidget.setWrapping(True)
        self.icon_listwidget.setIconSize(QtCore.QSize(32, 32))
        self.icon_listwidget.setResizeMode(QtWidgets.QListWidget.Adjust)
        self.icon_listwidget.setSelectionMode(self.icon_listwidget.ExtendedSelection)
        self.icon_listwidget.itemDoubleClicked.connect(self.copy_to_clipboard)
        self.icon_listwidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.icon_listwidget.customContextMenuRequested.connect(self.icon_context)

    def showEvent(self, *args, **kwargs):
        """
        Populate the UI after showing it.
        """
        self.populate()
        super().showEvent(*args, **kwargs)

    def icon_context(self):
        """
        Show the context for the asset list.
        """
        pos = QtGui.QCursor().pos()
        menu = QtWidgets.QMenu(self)

        menu.addAction(self.to_clipboard_action)
        menu.addSeparator()
        menu.addAction(self.scale_to_fit_action)

        menu.exec_(pos)

    def populate(self):
        """
        Add maya's built-in icons to the UI.
        """
        scale_to_fit = self.scale_to_fit_action.isChecked()
        self.icon_listwidget.clear()
        resources = cmds.resourceManager(nameFilter='*')
        for resource in resources:
            item = QtWidgets.QListWidgetItem(self.icon_listwidget)

            if scale_to_fit:
                icon = QtGui.QIcon(QtGui.QPixmap(f':/{resource}').scaledToHeight(32))
            else:
                icon = QtGui.QIcon(QtGui.QPixmap(f':/{resource}'))
            item.setIcon(icon)
            item.setData(QtCore.Qt.UserRole, resource)

        self.filter_changed()

    def filter_changed(self):
        """
        Filter the icons by their resource name.
        """
        text = self.filter_lineedit.text().lower()
        if text:
            self.filter_lineedit.setStyleSheet('background_color: rgb(80, 60, 40)')
        else:
            self.filter_lineedit.setStyleSheet('')

        items = [self.icon_listwidget.item(idx) for idx in range(self.icon_listwidget.count())]
        each_text = text.split(' ')
        for item in items:
            if not text or not each_text:
                item.setHidden(False)

            hidden = True
            resource = item.data(QtCore.Qt.UserRole).lower()
            for each in each_text:
                if each in resource:
                    hidden = False
                    break
            item.setHidden(hidden)

    def copy_to_clipboard(self, item=None):
        """
        Copy the resource name(s) to the clipboard.  If multiple resources are specified, a list will be copied.

        :param QtWidgets.QListWidgetItem or None item: specific item to copy, if None uses all selected items.
        """
        if item is None or isinstance(item, bool):
            items = self.icon_listwidget.selectedItems()
            if not items:
                return
            resources = [item.data(QtCore.Qt.UserRole) for item in items]
        else:
            resources = [item.data(QtCore.Qt.UserRole)]

        if len(resources) > 1:
            QtWidgets.QApplication.instance().clipboard().setText(str(resources))
            log.info(f'Copied resource names to clipboard: {resources}')
        else:
            QtWidgets.QApplication.instance().clipboard().setText(resources[0])
            log.info(f'Copied resource name to clipboard: {resources[0]}')
