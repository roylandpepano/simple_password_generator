from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from pass_about import Ui_Dialog
import random
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(422, 400)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint) # Removes the titlebar

        # Center window
        qtRectangle = MainWindow.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        MainWindow.move(qtRectangle.topLeft())
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        MainWindow.move(qtRectangle.topLeft())

        MainWindow.setMaximumSize(QtCore.QSize(16777215, 476))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/lock_error_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/lock_error_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(34, 11, 63);color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 421, 401))
        self.frame.setStyleSheet("QFrame#frame{border: 5px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));border-bottom: 6px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 191, 61))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.l = QtWidgets.QPushButton(self.frame_2)
        self.l.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.l.setStyleSheet("image: url(:/icons/icons/lock_error_48px.png);background:transparent;")
        self.l.setText("")
        self.l.setObjectName("l")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(60, 6, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(60, 30, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cat = QtWidgets.QLabel(self.frame)
        self.cat.setGeometry(QtCore.QRect(220, 0, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cat.setFont(font)
        self.cat.setStyleSheet("image: url(:/icons/icons/cat-1.png);background:transparent;")
        self.cat.setText("")
        self.cat.setObjectName("cat")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 151, 20))
        self.label_3.setObjectName("label_3")
        self.sb_manyPass = QtWidgets.QSpinBox(self.frame)
        self.sb_manyPass.setGeometry(QtCore.QRect(190, 120, 42, 22))
        self.sb_manyPass.setStyleSheet("")
        self.sb_manyPass.setObjectName("sb_manyPass")
        self.sb_manyPass.setValue(1)
        self.sb_manyPass.lineEdit().setReadOnly(True)
        self.sb_lengthPass = QtWidgets.QSpinBox(self.frame)
        self.sb_lengthPass.setEnabled(True)
        self.sb_lengthPass.setGeometry(QtCore.QRect(190, 90, 42, 21))
        self.sb_lengthPass.setObjectName("sb_lengthPass")
        self.sb_lengthPass.setValue(15)
        self.sb_lengthPass.lineEdit().setReadOnly(True)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 101, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(20, 160, 381, 221))
        self.groupBox.setObjectName("groupBox")
        self.tb_showPass = QtWidgets.QTextBrowser(self.groupBox)
        self.tb_showPass.setGeometry(QtCore.QRect(10, 20, 361, 191))
        self.tb_showPass.setStyleSheet("border:#220B3F;")
        self.tb_showPass.setObjectName("tb_showPass")
        self.about = QtWidgets.QPushButton(self.frame, clicked=lambda: self.btn_about())
        self.about.setGeometry(QtCore.QRect(320, 10, 31, 31))
        self.about.setStyleSheet("image: url(:/icons/icons/info_96px.png);")
        self.about.setText("")
        self.about.setObjectName("about")
        self.btn_close = QtWidgets.QPushButton(self.frame)
        self.btn_close.setGeometry(QtCore.QRect(380, 10, 31, 31))
        self.btn_close.setStyleSheet("image: url(:/icons/icons/close_window_96px.png);")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.minimize = QtWidgets.QPushButton(self.frame)
        self.minimize.setGeometry(QtCore.QRect(350, 10, 31, 31))
        self.minimize.setStyleSheet("image: url(:/icons/icons/minimize_window_96px.png);")
        self.minimize.setText("")
        self.minimize.setObjectName("minimize")
        self.btn_generate = QtWidgets.QPushButton(self.frame, clicked=lambda: self.generate())
        self.btn_generate.setGeometry(QtCore.QRect(250, 90, 141, 51))
        self.btn_generate.setStyleSheet("QPushButton#btn_generate {color: #fff;background-color: #06B4DB;border-radius: 3px;    }QPushButton#btn_generate:hover:!pressed {background-color: #05A3C7;}")
        self.btn_generate.setObjectName("btn_generate")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def generate(self):
        lengthPass = self.sb_lengthPass.value()
        manyPass = self.sb_manyPass.value()

        upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowerCaseLetter = upperCaseLetters.lower()
        digits = "0123456789"
        symbols = "~`!@#$%^&*()_-+={[}]|\\\:;""'<,>.?/"""

        upper, lower, digit, symbol = True, True, True, True
        all = ""

        if upper:
            all += upperCaseLetters
        if lower:
            all += lowerCaseLetter
        if digit:
            all += digits
        if symbol:
            all += symbols

        for i in range(manyPass):
            password = "".join(random.sample(all, lengthPass))
            self.tb_showPass.append("Password:   " + password)

    def btn_about(self):
        self.new = QtWidgets.QWidget() 
        self.about_dialog = Ui_Dialog()
        self.about_dialog.setupUi(self.new)
        self.new.show() 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple PG"))
        self.label.setText(_translate("MainWindow", "SIMPLE"))
        self.label_5.setText(_translate("MainWindow", "PASSWORD GENERATOR"))
        self.label_3.setText(_translate("MainWindow", "How many password to create?"))
        self.label_2.setText(_translate("MainWindow", "Length of password:"))
        self.groupBox.setTitle(_translate("MainWindow", "Generated Password"))
        self.tb_showPass.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_generate.setText(_translate("MainWindow", "GENERATE"))

# Main Window
class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.minimize.clicked.connect(self.showMinimized)
        self.btn_close.clicked.connect(self.close)
            
    def mousePressEvent(self, event):                                 
        self.dragPos = event.globalPos()
            
    def mouseMoveEvent(self, event):                                  
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())