# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mylogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import mymain
import main
from service import myservice
import base64
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 196)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 10, 321, 201))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.editName = QtWidgets.QLineEdit(self.widget)
        self.editName.setObjectName("editName")
        self.verticalLayout.addWidget(self.editName)
        self.editPwd = QtWidgets.QLineEdit(self.widget)
        self.editPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPwd.setObjectName("editPwd")
        self.verticalLayout.addWidget(self.editPwd)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnLogin = QtWidgets.QPushButton(self.widget)
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout_2.addWidget(self.btnLogin)
        self.btnExit = QtWidgets.QPushButton(self.widget)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout_2.addWidget(self.btnExit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnExit.clicked.connect(MainWindow.close) # ??????????????????
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # ?????????????????????????????????????????????
        self.editPwd.editingFinished.connect(self.openMain)
        # ??????????????????????????????????????????
        self.btnLogin.clicked.connect(self.openMain)

    # ???????????????
    def openMain(self):
        myservice.userName = self.editName.text()  # ??????????????????????????????
        t=self.editPwd.text()
        # self.userPwd=base64.b64encode(t.encode()) #base64???????????????????????????
        self.userPwd = self.editPwd.text()  # ??????????????????


        '''??????????????????'''
        self.userPwd=self.userPwd+'1'




        if myservice.userName != "" and self.userPwd != "":  # ?????????????????????????????????
            # ????????????????????????????????????
            result = myservice.query2("select * from tb_pwd where user = '{}' and password = '{}'".format(myservice.userName,self.userPwd))
            cl=myservice.query2("select Uclass from tb_user where Uuser = '{}'".format(myservice.userName))
            # print(cl)
            myservice.Uclass=cl[0][0]
            # print(result)
            if len(result) > 0:  # ????????????????????????0???????????????????????????????????????
                # myservice.Uclass=result #???????????????????????????????????????
                self.m = mymain.Ui_MainWindow()  # ?????????????????????
                self.m.show()  # ???????????????
                MainWindow.hide()  # ???????????????????????????
            else:
                self.editName.setText("")  # ?????????????????????
                self.editPwd.setText("")  # ?????????????????????
                QMessageBox.warning(None, '??????', '???????????????????????????????????????', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '??????', '??????????????????????????????', QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.label_3.setText(_translate("MainWindow", "???  ??????"))
        self.btnLogin.setText(_translate("MainWindow", "???  ???"))
        self.btnExit.setText(_translate("MainWindow", "???  ???"))
import img_rc



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # ??????????????????
    ui = Ui_MainWindow() # ??????PyQt5?????????????????????
    ui.setupUi(MainWindow) # ??????PyQt5???????????????????????????????????????????????????
    MainWindow.show() # ????????????
    sys.exit(app.exec_()) # ???????????????????????????

    # myservice.userName='1234@local'
    # userPwd=456
    # result = myservice.query2(
    #     "select * from tb_pwd where user = '{}' and password = '{}';".format(myservice.userName, userPwd))
    # print(result)