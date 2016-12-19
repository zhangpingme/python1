# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'huatu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np
from numpy.linalg import cholesky
import sys
import random
import matplotlib.pyplot as plt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(772, 510)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 331, 171))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 89, 16))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 90, 89, 16))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 140, 89, 16))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(220, 40, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(150, 40, 62, 22))
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(250, 40, 62, 22))
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(110, 90, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(150, 90, 161, 22))
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(150, 140, 62, 22))
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(250, 140, 62, 22))
        self.doubleSpinBox_7.setObjectName(_fromUtf8("doubleSpinBox_7"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(110, 140, 54, 12))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(220, 140, 54, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 210, 331, 171))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 40, 89, 16))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 90, 89, 16))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 140, 89, 16))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(120, 40, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(220, 40, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(150, 40, 62, 22))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(250, 40, 62, 22))
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(110, 90, 54, 12))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_8.setGeometry(QtCore.QRect(150, 90, 161, 22))
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.doubleSpinBox_9 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_9.setGeometry(QtCore.QRect(150, 140, 62, 22))
        self.doubleSpinBox_9.setObjectName(_fromUtf8("doubleSpinBox_9"))
        self.doubleSpinBox_10 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_10.setGeometry(QtCore.QRect(250, 140, 62, 22))
        self.doubleSpinBox_10.setObjectName(_fromUtf8("doubleSpinBox_10"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(110, 140, 54, 12))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(220, 140, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.radioButton_4.raise_()
        self.radioButton_5.raise_()
        self.radioButton_6.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.doubleSpinBox.raise_()
        self.doubleSpinBox_2.raise_()
        self.label_7.raise_()
        self.doubleSpinBox_8.raise_()
        self.doubleSpinBox_9.raise_()
        self.doubleSpinBox_10.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 400, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 440, 141, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 390, 111, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 440, 141, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 400, 54, 12))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(90, 390, 61, 31))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(360, 10, 371, 441))
        self.label_13.setAcceptDrops(False)
        self.label_13.setText(_fromUtf8(""))
        
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_3.clear)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_4.clear)
        QtCore.QObject.connect(self.radioButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox.clear)
        QtCore.QObject.connect(self.radioButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_2.clear)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_3.clear)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_4.clear)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_6.clear)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_7.clear)
        QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_3.clear)
        QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_4.clear)
        QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_5.clear)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_5.clear)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_6.clear)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_7.clear)
        QtCore.QObject.connect(self.radioButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_8.clear)
        QtCore.QObject.connect(self.radioButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_9.clear)
        QtCore.QObject.connect(self.radioButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_10.clear)
        QtCore.QObject.connect(self.radioButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox.clear)
        QtCore.QObject.connect(self.radioButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_2.clear)
        QtCore.QObject.connect(self.radioButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_9.clear)
        QtCore.QObject.connect(self.radioButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_10.clear)
        QtCore.QObject.connect(self.radioButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_2.clear)
        QtCore.QObject.connect(self.radioButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox.clear)
        QtCore.QObject.connect(self.radioButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_2.clear)
        QtCore.QObject.connect(self.radioButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_8.clear)
        QtCore.QObject.connect(self.radioButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_9.clear)
        QtCore.QObject.connect(self.radioButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doubleSpinBox_10.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.drawing)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self,MainWindow):
        n=(self.spinBox.value())
        
        a1=(self.doubleSpinBox.value())
        b1=(self.doubleSpinBox_2.value())
        a2=(self.doubleSpinBox_3.value())
        b2=(self.doubleSpinBox_4.value())

        c1=(self.doubleSpinBox_5.value())
        c2=(self.doubleSpinBox_8.value())

        d1=(self.doubleSpinBox_6.value())
        e1=(self.doubleSpinBox_7.value())
        d2=(self.doubleSpinBox_9.value())
        e2=(self.doubleSpinBox_10.value())
        
        if (bool(a1) and bool(b1)) and (not bool(c1))and (not bool(d1) and not bool(e1)):
            s = np.random.normal(a2,b2,n)
        elif (not bool(a1) and not bool(b1)) and (bool(c1))and (not bool(d1) and not bool(e1)):
            s = np.random.exponential(c1,n)
        elif (not bool(a1) and not bool(b1)) and (not bool(c1))and (bool(d1) and bool(e1)):
            s = np.random.normal(d1,e1,n)
        else:
            self.textBrowser.setPlainText('Wrong!!!!!!!!!!!')
            
        if (bool(a1) and bool(b1)) and (not bool(c1))and (not bool(d1) and not bool(e1)):
            t = np.random.normal(a1,b1,n)           
        elif (not bool(a1) and not bool(b1)) and (bool(c1))and (not bool(d1) and not bool(e1)):
            t = np.random.exponential(c2,n)           
        elif (not bool(a1) and not bool(b1)) and (not bool(c1))and (bool(d1) and bool(e1)):
            t = np.random.normal(d2,e2,n)          
        else:
            self.textBrowser.setPlainText('Wrong!!!!!!!!!!!')

        plt.figure(1)
        ax1 = plt.subplot(211)
        ax2 = plt.subplot(212)        

        plt.sca(ax1)
        plt.hist(s,bins=n/4,normed=True,color="blue", alpha=0.5)
        plt.hist(t,bins=n/4,normed=True,color="red", alpha=0.5)

        plt.sca(ax2)
        x1 = [j for j in range(1,n+1)]
        plt.plot(x1,s)
        plt.plot(x1,t)

        plt.savefig("C:/Users/panhao/Desktop/test.png", dpi=120)
        
        l=0
        for i in range(1,n,1):
            if s[i] > t[i]:
                l += 1
            elif s[i] == t[i]:
                l+=0.5
            else:
                continue

        m =float(l)/n
        m =str(m)
        self.textBrowser.setPlainText(m)  
        

    def drawing(self):
        
        
        self.label_13.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/panhao/Desktop/test.png")))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "可靠性", None))
        self.groupBox.setTitle(_translate("MainWindow", "强度分布", None))
        self.radioButton.setText(_translate("MainWindow", "正态分布", None))
        self.radioButton_2.setText(_translate("MainWindow", "指数分布", None))
        self.radioButton_3.setText(_translate("MainWindow", "威布尔分布", None))
        self.label_2.setText(_translate("MainWindow", "均值：", None))
        self.label_3.setText(_translate("MainWindow", "方差：", None))
        self.label_6.setText(_translate("MainWindow", "Lamda:", None))
        self.label_10.setText(_translate("MainWindow", "Alpha:", None))
        self.label_11.setText(_translate("MainWindow", "Beta:", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "应力分布", None))
        self.radioButton_4.setText(_translate("MainWindow", "正态分布", None))
        self.radioButton_5.setText(_translate("MainWindow", "指数分布", None))
        self.radioButton_6.setText(_translate("MainWindow", "威布尔分布", None))
        self.label_4.setText(_translate("MainWindow", "均值：", None))
        self.label_5.setText(_translate("MainWindow", "方差：", None))
        self.label_7.setText(_translate("MainWindow", "Lamda:", None))
        self.label_8.setText(_translate("MainWindow", "Alpha:", None))
        self.label_9.setText(_translate("MainWindow", "Beta:", None))
        self.label.setText(_translate("MainWindow", "可靠性：", None))
        self.pushButton.setText(_translate("MainWindow", "计算", None))
        self.pushButton_2.setText(_translate("MainWindow", "画图", None))
        self.label_12.setText(_translate("MainWindow", "仿行次数：", None))
        self.menu.setTitle(_translate("MainWindow", "可靠性计算", None))


def main():
    app = QtGui.QApplication(sys.argv)

  
    
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
            
            
if __name__ == "__main__" :
   main()


    
