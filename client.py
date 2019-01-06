#coding:utf-8
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
#from PyQt5.QtCore import pyqtSignature
from PyQt5.QtCore import QTextCodec
import socket
import time
from clientUI import Ui_MainWindow
from gongJu import callMethodInMainThread
import sys
#import importlib,sys
#importlib.reload(sys)
#reload(sys)
#sys.setdefaultencoding('utf-8')
#global myMSG
class Thread(QtCore.QThread):
    trigger=QtCore.pyqtSignal(str)
    def __init__(self,tcpCliSock):
        super(Thread,self).__init__()
        self.tcpCliSock=tcpCliSock
        self.message=""

    def run(self):
        while 1:
            msg=self.tcpCliSock.recv(1024)
            if len(msg) !=0 and msg!="":
                #self.myMSG=msg.decode('utf-8','ignore')
                #print(self.myMSG)
                print("&&&&&&&&&&&&")
                #Ui_MainWindow.textBrowser.append(self.myMSG)
                self.message=msg
                print(msg.decode('utf-8','ignore'))
                #callMethodInMainThread(self.textBrowser.append, msg)
                self.trigger.emit(msg.decode('utf-8','ignore'))
            else:
                self.message=self.message

class client(QMainWindow,Ui_MainWindow):
    #global myMSG,textBrowser # global声明
    def __init__(self,parent=None):

        QMainWindow.__init__(self,parent)
        self.setupUi(self)

        self.Host="127.0.0.1"
        self.Port=8022#9999
        self.tcpCliSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcpCliSock.connect((self.Host,self.Port))

        self.th=Thread(self.tcpCliSock)
        self.th.trigger.connect(self.display)
        self.th.start()
        #global  myMSG
        #self.myMSG = self.th.message
        #QtCore.QQbject.connect(self.th,QtCore.SIGNAL('trigger()'),self.display)
#       self.textBrowser.append((self.th.message).decode('utf-8'))
        #self.textBrowser.append(self.th.message)#12-25

        #self.display()
        self.pushButton.clicked.connect(self.sendMsg)

        #self.timer = QTimer(self)  # 初始化一个定时器
        #self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
        #self.timer.start(500)  # 设置计时间隔并启动
    #def operate(self):# 具体操作
        #global myMSG
        #print(self.myMSG)
        #if   self.myMSG is not None and len(self.myMSG) !=0:#self.myMSG != ''
            #self.textBrowser.append(self.myMSG)
        #self.cursor = self.textBrowser.textCursor()
        #self.textBrowser.moveCursor(self.cursor.End)
    def sendMsg(self):
        text=self.textEdit.toPlainText()
        #ch=str(text).decode('utf-8')
        #name=self.username.text()+"    ".decode('utf-8')
        #nowtime=time.strftime('%H:%M:%S')
        #header=name+nowtime+'\n'
        #text=header+ch+'\n'
        data = self.recvname.text() + ":" + text
        self.textBrowser.setStyleSheet("color: rgb(126, 210, 120);")
        self.textBrowser.append(data)
        #self.tcpCliSock.send("%s|%s|%s"%(self.username.text(),self.recvname.text(),text))

        self.tcpCliSock.send(data.encode("utf-8"))
        self.textEdit.setText("")

    def display(self, message):
        self.textBrowser.append(self.th.message.decode('utf-8','ignore'))




if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    windows=client()
    windows.show()
    sys.exit(app.exec_())