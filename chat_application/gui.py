from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        verticalLayout = QVBoxLayout()
        label = QLabel("Welcome to Safe Chat")
        label.setAlignment(Qt.AlignCenter)
        label.setWordWrap(True)
        verticalLayout.addWidget(label)

        gridLayout = QGridLayout()
        pushButton = QPushButton("Information")
        pushButton_2 = QPushButton("Register")
        pushButton_4 = QPushButton("Login")
        pushButton_3 = QPushButton("Settings")
        gridLayout.addWidget(pushButton, 0, 0)
        gridLayout.addWidget(pushButton_2, 0, 1)
        gridLayout.addWidget(pushButton_3, 1, 0)
        gridLayout.addWidget(pushButton_4, 1, 1)
        verticalLayout.addLayout(gridLayout)
        self.setLayout(verticalLayout)

if __name__ == "__main__":
    app = QApplication([])
    ui = Ui_Form()
    ui.show()
    app.exec()