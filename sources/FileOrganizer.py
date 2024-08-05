import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QTextEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FileOrganizer")

        screen = QDesktopWidget().screenGeometry()
        self.setMinimumSize(screen.width() // 2, screen.height() // 2)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.list_directory_contents()

        self.show()

    def list_directory_contents(self):
        directory = os.getcwd()
        contents = os.listdir(directory)
        self.text_edit.append(f"Contents of directory '{directory}':\n")
        for item in contents:
            self.text_edit.append(item)


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()