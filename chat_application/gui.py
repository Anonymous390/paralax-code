from PyQt5.QtWidgets import *

class App(QApplication):
    def __init__(self):
        super(App, self).__init__([])
        self.window = Window()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton(text="Hello"))
        self.window.addLayout(layout)
        self.window.setLayout(0)
        self.window.show()
    
    def run(self):
        self.exec()

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.layouts = []
    
    def addLayout(self, layout):
        self.layouts.append(layout)
    
    def setLayout(self, num):
        super(Window, self).setLayout(self.layouts[num])

if __name__ == "__main__":
    app = App()
    app.run()