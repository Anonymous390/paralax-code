from PyQt5.QtWidgets import *

class App(QApplication):
    def __init__(self):
        super(App, self).__init__([])
        self.window = Window()
        self.window.add_layout(Layout())
        self.window.set_layout(1)
        self.window.show()

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.layouts = []
    
    def add_layout(self, layout)
        self.layouts.append(layout)
    
    def set_layout(self, num):
        super(Window, self).set_layout(self.layouts[num])

class Layout(QVBoxLayout):
    def __init__(self):
        pass

if __name__ == "__main__":
    app = App()
    app.