from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import res
import webbrowser


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(381, 270)
        Dialog.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/lock_error_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(34, 11, 63);color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 381, 271))
        self.frame.setStyleSheet("QFrame#frame{border: 5px solid white;border-bottom: 6px solid white;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 191, 61))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
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
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(20, 70, 341, 141))
        self.label_15.setStyleSheet("background-color: #220B4D;border-radius: 5px;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.facebook = QtWidgets.QPushButton(self.frame, clicked=lambda: webbrowser.open('https://web.facebook.com/iamroyland/'))
        self.facebook.setGeometry(QtCore.QRect(20, 220, 31, 31))
        self.facebook.setFocusPolicy(QtCore.Qt.NoFocus)
        self.facebook.setStyleSheet("image: url(:/icons/icons/facebook_96px.png);background-color:transparent;")
        self.facebook.setText("")
        self.facebook.setObjectName("facebook")
        self.instagram = QtWidgets.QPushButton(self.frame, clicked=lambda: webbrowser.open('https://www.instagram.com/iamroyland/'))
        self.instagram.setGeometry(QtCore.QRect(50, 220, 31, 31))
        self.instagram.setFocusPolicy(QtCore.Qt.NoFocus)
        self.instagram.setStyleSheet("background-color:transparent;image: url(:/icons/icons/Instagram logo_96px.png);")
        self.instagram.setText("")
        self.instagram.setObjectName("instagram")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_5.setGeometry(QtCore.QRect(180, 220, 181, 31))
        self.textBrowser_5.setStyleSheet("background: transparent;border: 0;")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(40, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: #220B4D;")
        self.label_13.setObjectName("label_13")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(40, 110, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: transparent;border: 0;")
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.l = QtWidgets.QPushButton(self.frame)
        self.l.setGeometry(QtCore.QRect(100, 20, 41, 41))
        self.l.setStyleSheet("image: url(:/icons/icons/lock_error_48px.png);background:transparent;")
        self.l.setText("")
        self.l.setObjectName("l")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 16, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">Notice:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">    - This is version 1.0, expect a lot of bugs.</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "About"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Simple Password Generator</span><span style=\" font-size:7pt;\"> is a desktop application made to generate random and secure passwords in just a few clicks.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">SPG is made using </span><span style=\" font-size:7pt; text-decoration: underline;\">Python</span><span style=\" font-size:7pt;\"> and </span><span style=\" font-size:7pt; text-decoration: underline;\">PyQt framework</span><span style=\" font-size:7pt;\"> with the help of </span><span style=\" font-size:7pt; text-decoration: underline;\">Qt Designer</span><span style=\" font-size:7pt;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">© Royland Pepaño</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "PASSWORD GENERATOR"))
        self.label.setText(_translate("Dialog", "SIMPLE"))
