# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sssss.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!



from PyQt4 import QtCore, QtGui
import numpy as np
from numpy.linalg import cholesky

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
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 331, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 40, 89, 16))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 90, 89, 16))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 140, 89, 16))
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
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 190, 331, 161))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 40, 89, 16))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(30, 90, 89, 16))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(30, 140, 89, 16))
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
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(380, 20, 341, 191))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 400, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 370, 111, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 420, 331, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self,MainWindow):
        
       
        a1=(self.doubleSpinBox.value())
        b1=(self.doubleSpinBox_2.value())
        a2=(self.doubleSpinBox_3.value())
        b2=(self.doubleSpinBox_4.value())
        s = np.random.normal(a1,b1,1000)
        t = np.random.normal(a2,b2,1000)
       
        l=0
        for i in range(1,1000,1):
            if s[i]>t[i]:
                l+=1
            elif s[i]==t[i]:
                l+=0.5
            else:
                continue

        m =float(l)/1000
        m =str(m)
        self.textBrowser.setPlainText(m)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "可靠性", None))
        self.groupBox.setTitle(_translate("MainWindow", "强度分布", None))
        self.radioButton.setText(_translate("MainWindow", "正态分布", None))
        self.radioButton_2.setText(_translate("MainWindow", "指数分布", None))
        self.radioButton_3.setText(_translate("MainWindow", "威布尔分布", None))
        self.label_2.setText(_translate("MainWindow", "均值：", None))
        self.label_3.setText(_translate("MainWindow", "方差：", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "应力分布", None))
        self.radioButton_4.setText(_translate("MainWindow", "正态分布", None))
        self.radioButton_5.setText(_translate("MainWindow", "指数分布", None))
        self.radioButton_6.setText(_translate("MainWindow", "威布尔分布", None))
        self.label_4.setText(_translate("MainWindow", "均值：", None))
        self.label_5.setText(_translate("MainWindow", "方差：", None))
        self.label.setText(_translate("MainWindow", "可靠性：", None))
        self.pushButton.setText(_translate("MainWindow", "计算", None))
        self.menu.setTitle(_translate("MainWindow", "可靠性计算", None))
        


import sys

        
   
        
def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
            
            
if __name__ == "__main__" :
   main()
