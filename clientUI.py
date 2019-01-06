# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientUI.ui'
#
# Created: Mon Dec 24 18:03:16 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(631, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 400, 511, 51))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 51, 611, 331))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 400, 91, 51))
#        font = QtWidgets.QFont()
#        font.setFamily(_fromUtf8("Aharoni"))
#        font.setPointSize(16)
#        font.setBold(True)
#        font.setWeight(75)
#        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 380, 611, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 20))
#        font = QtWidgets.QFont()
#        font.setFamily(_fromUtf8("Aharoni"))
#        font.setPointSize(16)
#        font.setBold(True)
#        font.setWeight(75)
#        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 71, 21))
#        font = QtWidgets.QFont()
#        font.setFamily(_fromUtf8("Aharoni"))
#        font.setPointSize(16)
#        font.setBold(True)
#        font.setWeight(75)
#        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(90, 9, 211, 31))
        self.username.setObjectName(_fromUtf8("username"))
        self.recvname = QtWidgets.QLineEdit(self.centralwidget)
        self.recvname.setGeometry(QtCore.QRect(410, 10, 211, 31))
        self.recvname.setObjectName(_fromUtf8("recvname"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "发  送", None))
        self.label.setText(_translate("MainWindow", "用户名", None))
        self.label_2.setText(_translate("MainWindow", "收信人", None))

