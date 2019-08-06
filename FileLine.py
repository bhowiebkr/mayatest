from PySide2 import QtCore, QtWidgets

import os


class FileLine(QtWidgets.QWidget):
    pathChanged = QtCore.Signal()

    def __init__(self, parent=None):
        super(FileLine, self).__init__(parent)

        self.__path = None

        # Layout
        main_layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(main_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Widgets
        self.line = QtWidgets.QLineEdit()
        self.line.setReadOnly(True)
        self.btn = QtWidgets.QPushButton()
        self.btn.setFixedHeight(20)
        self.btn.setIcon(self.btn.style().standardIcon(
            QtWidgets.QStyle.SP_DirIcon))

        # Add Widgets
        main_layout.addWidget(self.line)
        main_layout.addWidget(self.btn)

        # Logic
        self.btn.clicked.connect(self.btn_clicked)

    @property
    def path(self):
        return self.get_path()

    @path.setter
    def path(self, path):
        self.set_path(path)

    def btn_clicked(self):
        """ The functionality of the button being clicked. 
            We launch a file dialog and get the result. We send the path to the 
            method that sets the rest if the widget and emits an update
        """

        # Get the starting directory. If the path already exists, we use that
        # if it doesn't exist we open in the home folder of the user
        if os.path.exists(self.line.text()):
            start_dir = self.line.text()
        else:
            start_dir = os.path.expanduser("~")

        path = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Set a Directory', start_dir, QtWidgets.QFileDialog.ShowDirsOnly)

        self.set_path(path)

    def get_path(self):
        """ Get the path
        """
        return self.line.text()

    def set_path(self, path):
        """ Set the path
        """
        path = os.path.abspath(path)
        if os.path.exists(path):
            self.line.setText(path)
            self.pathChanged.emit()
