from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
import webbrowser
import sys

class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        verticalLayout = QVBoxLayout()
        self.setFixedSize(400, 300)
        label = QLabel("Welcome to Safe Chat")
        label.setAlignment(Qt.AlignCenter)
        label.setWordWrap(True)
        verticalLayout.addWidget(label)

        gridLayout = QGridLayout()
        pushButton = QPushButton("Information")
        pushButton.setToolTip("Learn how to use the app")
        pushButton.clicked.connect(self.info_button_click)
        pushButton_2 = QPushButton("Chat")
        pushButton_4 = QPushButton("More From Us")
        pushButton_4.setToolTip("More projects from us")
        pushButton_4.clicked.connect(self.more_about_us_button_click)
        pushButton_3 = QPushButton("Exit")
        pushButton_3.setToolTip("Quit the application")
        pushButton_3.clicked.connect(self.close)
        gridLayout.addWidget(pushButton, 0, 0)
        gridLayout.addWidget(pushButton_2, 0, 1)
        gridLayout.addWidget(pushButton_3, 1, 0)
        gridLayout.addWidget(pushButton_4, 1, 1)
        verticalLayout.addLayout(gridLayout)
        self.setLayout(verticalLayout)

    @pyqtSlot()
    def info_button_click(self):
        webbrowser.open("https://github.com/rayzchen/paralax-code#readme")

    def more_about_us_button_click(self):
        webbrowser.open("https://github.com/rayzchen/paralax-code")

    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Message',
                        quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication([])
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())