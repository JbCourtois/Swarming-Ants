from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.hits = 0
        self.max_hp = 500
        self.frame_count = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 740)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(90, 40, 581, 61))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.hitsBar = QtWidgets.QProgressBar(self.frame_2)
        self.hitsBar.setEnabled(True)
        self.hitsBar.setGeometry(QtCore.QRect(170, 0, 411, 31))
        self.hitsBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hitsBar.setAutoFillBackground(False)
        self.hitsBar.setMinimum(0)
        self.hitsBar.setMaximum(self.max_hp)
        self.hitsBar.setProperty("value", self.max_hp)
        self.hitsBar.setTextVisible(False)
        self.hitsBar.setObjectName("hitsBar")
        self.lcd_hits = QtWidgets.QLCDNumber(self.frame_2)
        self.lcd_hits.setGeometry(QtCore.QRect(210, 40, 81, 21))
        self.lcd_hits.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_hits.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_hits.setSmallDecimalPoint(False)
        self.lcd_hits.setDigitCount(6)
        self.lcd_hits.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcd_hits.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_hits.setProperty("value", 0.0)
        self.lcd_hits.setProperty("intValue", 0)
        self.lcd_hits.setObjectName("lcd_hits")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(170, 40, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(300, 40, 16, 16))
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.lcd_maxHP = QtWidgets.QLCDNumber(self.frame_2)
        self.lcd_maxHP.setGeometry(QtCore.QRect(310, 40, 81, 21))
        self.lcd_maxHP.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_maxHP.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_maxHP.setDigitCount(6)
        self.lcd_maxHP.setProperty("intValue", self.max_hp)
        self.lcd_maxHP.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_maxHP.setObjectName("lcd_maxHP")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lcd_frame = QtWidgets.QLCDNumber(self.frame_2)
        self.lcd_frame.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.lcd_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_frame.setSmallDecimalPoint(False)
        self.lcd_frame.setDigitCount(6)
        self.lcd_frame.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcd_frame.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_frame.setObjectName("lcd_frame")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.next_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.update()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Hits:"))
        self.label_2.setText(_translate("MainWindow", "/"))
        self.label_3.setText(_translate("MainWindow", "Frame"))
        self.pushButton.setText(_translate("MainWindow", "Next frame"))

    def update(self):
        self.lcd_frame.setProperty("intValue", self.frame_count)
        self.lcd_hits.setProperty("intValue", self.hits)
        self.hitsBar.setProperty("value", self.max_hp - self.hits)

    def next_frame(self):
        self.hits += 10
        self.frame_count += 1
        self.update()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
