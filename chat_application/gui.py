from PyQt5 import QtWidgets, QtGui 
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Safe Chat - Paralax')
        self.InitUI()

    def InitUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Welcome To Safe Chat')
        self.label.setFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold))
        self.label.adjustSize()
        self.label.move(90, 50)

        # self.t1 = QtWidgets.QLineEdit(self)
        # self.t1.move(200, 200)

        self.info = QtWidgets.QPushButton(self)
        self.info.setText("Info")
        self.info.setGeometry(80, 200, 110, 70)


        self.start = QtWidgets.QPushButton(self)
        self.start.setText("Start!")
        self.start.setGeometry(230, 200, 110, 70)
    
    def update(self):
        self.label.adjustSize()



def clik():
    print("Clicked")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()
