# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buybook.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
sys.path.append("../")  # 返回上层路径
from service import service, myservice


class Ui_MainWindow(QMainWindow):
    # 构造方法
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        self.setupUi(self)  # 初始化窗体设置
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 421)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.editName = QtWidgets.QLineEdit(self.splitter_2)
        self.editName.setObjectName("editName")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cboxclass = QtWidgets.QComboBox(self.splitter_2)
        self.cboxclass.setObjectName("cboxclass")
        self.btnAdd = QtWidgets.QPushButton(self.splitter_2)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.tbStudent = QtWidgets.QTableWidget(self.centralwidget)
        self.tbStudent.setObjectName("tbStudent")
        self.tbStudent.setColumnCount(4)
        self.tbStudent.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tbStudent, 1, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        self.label_4.setObjectName("label_4")
        self.btnAdd_2 = QtWidgets.QPushButton(self.splitter)
        self.btnAdd_2.setObjectName("btnAdd_2")
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.bindclass()
        self.tbStudent.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.tbStudent.verticalHeader().setVisible(False)  # 隐藏垂直标题
        self.query()  # 窗体加载时显示所有数据
        self.tbStudent.itemClicked.connect(self.getItem)  # 获取选中的单元格数据
        self.btnAdd.clicked.connect(self.query)
        self.btnAdd_2.clicked.connect(self.buy)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "书城"))
        self.label_2.setText(_translate("MainWindow", "书名"))
        self.label_3.setText(_translate("MainWindow", "类型"))
        self.btnAdd.setText(_translate("MainWindow", "查找"))
        item = self.tbStudent.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "书名"))
        item = self.tbStudent.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "类型"))
        item = self.tbStudent.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "作者"))
        item = self.tbStudent.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "价格"))
        self.label.setText(_translate("MainWindow", "已选"))
        self.label_4.setText(_translate("MainWindow", "选择书本"))
        self.btnAdd_2.setText(_translate("MainWindow", "购买"))
    def bindclass(self):
        '''
        修改下拉栏
        '''
        self.cboxclass.addItem("所有")
        result = myservice.query2("select distinct Bclass from tb_book")
        for i in result:  # 遍历查询结果
            self.cboxclass.addItem(i[0])  # 在下拉列表中显示
    def query(self):
        self.tbStudent.setRowCount(0)  # 清空表格中的所有行
        t=self.editName.text()
        bclass = self.cboxclass.currentText()  # 记录选择的类型
        # 获取所有学生信息
        if bclass == "所有" and t=='':
            result = myservice.query2(
                "select Bname,Bclass,Bauthor,Bprice from tb_book where Bnum>0")
        elif bclass == "所有":
            result = myservice.query2(
                "select Bname,Bclass,Bauthor,Bprice from tb_book where Bname like '%{}%' and Bnum>0".format(t))
        elif t=='':
            result = myservice.query2(
                "select Bname,Bclass,Bauthor,Bprice from tb_book where Bclass='{}' and Bnum>0".format(bclass))
        else:
            result = myservice.query2(
                "select Bname,Bclass,Bauthor,Bprice from tb_book where Bname like '%{}%' and Bclass='{}' and Bnum>0".format(t,bclass))
        row = len(result)
        self.tbStudent.setRowCount(row)
        for i in range(row):  # 遍历行
            for j in range(self.tbStudent.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbStudent.setItem(i, j, data)  # 设置每个单元格的数据
#   获取选中的表格内容
    def getItem(self, item):
        if item.column() == 0:  # 如果单击的是第一列
            self.select = item.text()  # 获取单击的单元格文本
            self.label_4.setText(self.select)  # 显示在label中

    #购买
    def buy(self):
        t=self.label_4.text()
        # num=service.query2("select Bnum from tb_book where Bname='{}'".format(t))
        # if num[0][0]>0:

        # sql="update tb_book set Bnum = Bnum-1 where Bname= '{}' ;".format(t)
        # print(sql)
        # result=myservice.exec(sql)
        # print(t)
        # print(result)

        t=self.label_4.text()
        result=myservice.exec("update tb_book set Bnum= Bnum-1 where Bname = '{}'".format(t))

        QMessageBox.information(None, '提示', '购买成功！', QMessageBox.Ok)
        self.query()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程

    # t='龙族'
    # num = myservice.query2("select Bnum from tb_book where Bname='{}'".format(t))
    # print(num[0][0]>1)


    # t = '龙族'
    # sql = "update tb_book set Bname='123' where Bname='龙族'"
    # print(sql)
    # result = myservice.exec(sql)
    # num = myservice.query2("select Bnum from tb_book where Bname='{}'".format(t))
    # print(num)
    # print(t)
    # print(result)