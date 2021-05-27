from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(100, 100, 400, 800)
        self.setWindowTitle('Safe Chat - Paralax')
        self.InitUI()

    def InitUI(self):
        self.label = QLabel(self)
        self.label.setText('Welcome To Safe Chat')
        self.label.setFont(QtGui.QFont("Times", 19, QtGui.QFont.Bold))
        self.label.adjustSize()
        self.label.move(20, 50)

        # self.t1 = QtWidgets.QLineEdit(self)
        # self.t1.move(200, 200)

        self.info = QPushButton(self)
        self.info.setText("Info")
        self.info.setGeometry(60, 350, 110, 50)
        self.info.clicked.connect(self.Info_click)


        self.start = QPushButton(self)
        self.start.setText("Start!")
        self.start.setGeometry(230, 350, 110, 50)

        self.more_from_us = QPushButton(self)
        self.more_from_us.setText("More from us")
        self.more_from_us.setGeometry(60, 450, 110, 50)
        self.more_from_us.clicked.connect(self.more_from_us_click)

        self.exit = QPushButton(self)
        self.exit.setText("Exit")
        self.exit.setGeometry(230, 450, 110, 50)
        self.exit.clicked.connect(self.close)

    def update(self):
        self.label.adjustSize()

    def more_from_us_click(self, checked):
        self.w = MoreFromUs()
        self.w.show()

    def Info_click(self, checked):
        self.w = Info()
        self.w.show()

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

class MoreFromUs(QWidget):
    def __init__(self):
        super(MoreFromUs, self).__init__()

        self.setGeometry(150, 150, 500, 500)
        self.setWindowTitle('More From Us - Paralax')
        self.InitUI()

    def InitUI(self):
        self.ai_bot = QLabel(self)
        self.ai_bot.setOpenExternalLinks(True)
        self.ai_bot.setText('<a href="https://github.com/blankRiot96/paralax-code/tree/main/Ai_Bot"><font size=5 color=blue>Ai Bot</font></a>')
        self.ai_bot.move(20, 20)
        self.ai_bot_desc = QLabel(self)
        self.ai_bot_desc.setText("""It is basically an auto response bot, that can also 'learn'.
If there is a question that the bot is unaware of,
it will ask you to teach it instead of dismissing it with 'I don't know'.
The knowledge that you entered into the bot, will be stored,
so all you have to do is re-run the program to use it""")
        self.ai_bot_desc.setFont(QtGui.QFont("Times", 9))
        self.ai_bot_desc.move(45, 55)

        self.tetris = QLabel(self)
        self.tetris.setOpenExternalLinks(True)
        self.tetris.setText('<a href="https://github.com/rayzchen/paralax-code/tree/main/tetris"><font size=5 color=blue>Tetris</font></a>')
        self.tetris.move(20, 210)
        self.tetris_desc = QLabel(self)
        self.tetris_desc.setText("""It is basically an auto response bot, that can also 'learn'.
If there is a question that the bot is unaware of,
it will ask you to teach it instead of dismissing it with 'I don't know'.
The knowledge that you entered into the bot, will be stored,
so all you have to do is re-run the program to use it""")
        self.tetris_desc.setFont(QtGui.QFont("Times", 9))
        self.tetris_desc.move(45, 245)

class Info(QWidget):
    def __init__(self):
        super(Info, self).__init__()

        self.setGeometry(150, 150, 870, 420)
        self.setWindowTitle("Info - Paralax")
        self.InitUI()

    def InitUI(self):
        self.title = QLabel(self)
        self.title.setOpenExternalLinks(True)
        self.title.setText('<a href="https://github.com/blankRiot96/paralax-code/tree/main/chat_application"><font size=7 color=black>Welcome to Safe Chat App</font></a>')
        self.title.move(20, 20)

        self.desc = QLabel(self)
        self.desc.setText("""We call it a 'safe' chat application, because our idea is that
only people with the same wifi can connect, and chat inthis application. This is
highly inconvinient, and impractical, it cannot be actually sold, since no one,
is actually gonna onlywant to be able to message people in their house only. We
are using pyQt5 and sockets, again, the main people working on this, are,
blankRiot96 and 404ErrorNotFound. Me, working on the servers and clients, while he
works on the GUI.""")
        self.desc.setFont(QtGui.QFont("Times", 14))
        self.desc.move(35, 80)


def window():
    app = QApplication(sys.argv)
    w = MyWindow()

    w.show()
    sys.exit(app.exec_())

window()
