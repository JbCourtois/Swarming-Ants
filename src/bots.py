import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QPoint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setStyleSheet("background-color:black;")
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;")
        self.child.resize(20, 20)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(400, 400))
        self.anim.setDuration(1500)
        print(self.anim.state())
        self.anim.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    app.exec_()
    print(MainWindow.anim.state())
