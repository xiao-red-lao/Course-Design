# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rengongzhineng.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys  # 导入sys模块
# import yichuan
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D






class Ui_MainWindow(object):

    def __init__(self):
        # 使用遗传算法找函数的最大值点
        self.population_size = 2000  # 种群数量
        self.generations = 200  # 迭代次数
        # ==========================================
        self.chrom_length = 16  # 染色体长度，
        # ==========================================
        self.pc = 0.6  # 交配概率
        self.pm = 0.001  # 变异概率
        self.genetic_population = []  # 种群的基因编码
        self.population = []  # 种群对应的十进制数值
        self.fitness = []  # 适应度
        self.fitness_mean = []  # 平均适应度
        self.optimum_solution = []  # 每次迭代所获最优解
        self.optimum_slt = []  # 存储最优解对应的x,y值，元组形式
        self.up = 1  # 上限
        self.down = -1  # 下限
        self.precision = 0.01  # 精度

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 4)
        self.gene = QtWidgets.QLineEdit(self.centralwidget)
        self.gene.setObjectName("gene")
        self.gridLayout.addWidget(self.gene, 1, 2, 1, 2)
        self.pc_ = QtWidgets.QLineEdit(self.centralwidget)
        self.pc_.setObjectName("pc_")
        self.gridLayout.addWidget(self.pc_, 2, 2, 1, 2)
        self.pm_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.pm_2.setObjectName("pm_2")
        self.gridLayout.addWidget(self.pm_2, 3, 2, 1, 2)
        self.pc = QtWidgets.QLabel(self.centralwidget)
        self.pc.setObjectName("pc")
        self.gridLayout.addWidget(self.pc, 2, 0, 1, 2)
        self.popu_size = QtWidgets.QLineEdit(self.centralwidget)
        self.popu_size.setObjectName("popu_size")
        self.gridLayout.addWidget(self.popu_size, 0, 2, 1, 2)
        self.generations = QtWidgets.QLabel(self.centralwidget)
        self.generations.setObjectName("generations")
        self.gridLayout.addWidget(self.generations, 1, 0, 1, 2)
        self.pm = QtWidgets.QLabel(self.centralwidget)
        self.pm.setObjectName("pm")
        self.gridLayout.addWidget(self.pm, 3, 0, 1, 2)
        self.population_size = QtWidgets.QLabel(self.centralwidget)
        self.population_size.setObjectName("population_size")
        self.gridLayout.addWidget(self.population_size, 0, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 2, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.shixian)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "实现"))
        self.gene.setText(_translate("MainWindow", "200"))
        self.pc_.setText(_translate("MainWindow", "0.6"))

        self.pm_2.setText(_translate("MainWindow", "0.001"))
        self.pc.setText(_translate("MainWindow", "交配概率"))
        self.popu_size.setText(_translate("MainWindow", "2000"))
        self.generations.setText(_translate("MainWindow", "迭代次数"))
        self.pm.setText(_translate("MainWindow", "变异概率"))
        self.population_size.setText(_translate("MainWindow", "种群数量"))
        self.lineEdit.setText(_translate("MainWindow", "max"))

    def shixian(self):
        #取参
        self.population_size=int(self.popu_size.text())
        self.generations= int(self.gene.text())
        self.pm=float(self.pm_2.text())
        self.pc=float(self.pc_.text())


        if self.lineEdit.text()=='max':
            max_v=self.maxv()
            self.printf("最大值{}\n".format(max_v))
            self.printf("理论值：2.1580221298556457\n")
            cha=(max_v-2.1580221298556457)/2.1580221298556457
            self.printf("误差为{:%}:\n".format(cha))
        else:
            min_v=self.minv()
            self.printf("最大值{}\n".format(min_v))
            self.printf("理论值：-0.15838175958346823\n")
            cha = (-min_v + (-0.15846021952652467)) / -0.15846021952652467
            self.printf("误差为{:%}:\n".format(cha))


    def printf(self, mypstr):
        '''
        在文本框内打印
        自定义类print函数, 借用c语言
        printf
        Mypstr：是待显示的字符串
        '''
        self.textBrowser.append(str(mypstr))  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    # 为染色体进行0，1编码，生成初始种群
    def chrom_encoding(self):
        for i in range(self.population_size):
            a = random.randint(0, (self.up - self.down) / self.precision)  # 在允许范围内随机生成
            b = random.randint(0, (self.up - self.down) / self.precision)  # 在允许范围内随机生成
            aa = self.convert_b(a, self.chrom_length // 2)  # 转为8位的str类型
            bb = self.convert_b(b, self.chrom_length // 2)
            population_i = list(aa + bb)  # 两个染色体合并
            population_i = [int(x) for x in population_i]  # 各位转为int类型
            self.genetic_population.append(population_i)  # 元素是一个int列表，16位

    # 将数字a转为长度为n的二进制位，str类型
    def convert_b(self,a: int, n: int):
        b = '{:b}'.format(a)
        while (len(b) < n): b = '0' + b
        return b

    # 将数字a转为十进制，int类型
    def convert_d(self,a: str):
        return int(a, 2)

    # convert_d('01110011')

    def fmax(self,x, y):
        '''
        适合题目的适应度函数
        '''
        return 1 + x * np.sin(np.pi * y) + y * np.sin(np.pi * x)

    def chrom_decoding(self):
        '''
        对染色体进行解码，将二进制转化为十进制
        将得到的两个十进制作为元组传入 population 列表中
        '''
        self.population.clear()  # 清空
        for i in range(self.population_size):  # 对第i个染色体操作
            value = 0
            for j in range(0, self.chrom_length // 2):  # 对第一个个体操作
                value += self.genetic_population[i][j] * (2 ** (self.chrom_length / 2 - 1 - j))  # 染色体a值
            a = self.down + value * self.precision
            value = 0
            for j in range(self.chrom_length // 2, self.chrom_length):
                i = j - self.chrom_length // 2
                value += self.genetic_population[i][j] * (2 ** (self.chrom_length / 2 - 1 - i))  # 染色体b值
            b = self.down + value * self.precision
            self.population.append((a, b))

    def calculate_fitness(self):
        '''
        计算每个染色体的适应度,将适应度传入fitness列表中
        返回种群的平均适应度
        '''
        sum = 0.0
        self.fitness.clear()
        for i in range(self.population_size):
            #         1+x*np.sin(np.pi*y)+y*np.sin(np.pi*x)
            # ====================================================修改适应度函数
            function_value = self.fmax(self.population[i][0], self.population[i][1])
            #         function_value=1+population[i][0]*np.sin(np.pi*population[i][1])+population[i][1]*np.sin(np.pi*population[i][0])
            # ====================================================
            if function_value > 0.0:
                # 计算种群的适应度
                sum += function_value
                # 将适应度大于0的个体适应度添加至数组
                self.fitness.append(function_value)
            else:
                self.fitness.append(0.0)
        # 返回种群的平均适应度
        return sum / self.population_size

    def best_value(self):
        '''
        获取最大适应度的个体和对应的编号
        返回元组表示的十进制的x和y，最大适应度下标，对应最大适应度
        '''
        max_fitness = self.fitness[0]
        max_chrom = 0
        for i in range(self.population_size):
            if self.fitness[i] > max_fitness:
                max_fitness = self.fitness[i]
                max_chrom = i
        return self.population[max_chrom], max_chrom, max_fitness

    def selection(self):
        '''
        采用轮盘赌算法进行选择过程，重新选择与种群数量相等的新种群
        '''
        # 种群的适应度数组
        fitness_array = np.array(self.fitness)
        # 从指定的一维数组中生成随机数
        # para1:一维数组
        # para2:数组长度
        # para3:replace=TRUE 代表可以重复
        # para4:数组中数据出现的概率
        new_population_id = np.random.choice(np.arange(self.population_size), (self.population_size),
                                             replace=True, p=fitness_array / fitness_array.sum())
        new_genetic_population = []
        global genetic_population
        for i in range(self.population_size):
            new_genetic_population.append(self.genetic_population[new_population_id[i]])
        self.genetic_population = new_genetic_population

    def produce(self):
        a = random.randint(0, (self.up - self.down) / self.precision)  # 在允许范围内随机生成
        b = random.randint(0, (self.up - self.down) / self.precision)  # 在允许范围内随机生成
        aa = self.convert_b(a, self.chrom_length / 2)  # 转为8位的str类型
        bb = self.convert_b(b, self.chrom_length / 2)
        d = list(aa + bb)  # 两个染色体合并
        d = [int(x) for x in d]  # 各位转为int类型
        return d

    def check(self,intlist):
        a = 0
        b = 0
        for i in range(len(intlist) // 2):
            a = a * 2 + intlist[i]
            b = b * 2 + intlist[i + len(intlist) // 2]
        d = 200
        if a > d or b > d:
            return False
        else:
            return True

    # 进行交配过程
    def crossover(self):
        for i in range(0, self.population_size - 1, 2):
            # 如果小于交叉概率，执行交叉
            if random.random() < self.pc:
                # 随机选择交叉点，
                change_point = random.randint(0, self.chrom_length - 1)
                temp1 = []
                temp2 = []
                temp1.extend(self.genetic_population[i][0:change_point])  # 交叉点前是i
                temp1.extend(self.genetic_population[i + 1][change_point:])  # 交叉点后是i+1
                temp2.extend(self.genetic_population[i + 1][0:change_point])
                temp2.extend(self.genetic_population[i][change_point:])
                if self.check(temp1):
                    self.genetic_population[i] = temp1
                else:
                    self.genetic_population[i] = self.produce()
                if self.check(temp2):
                    self.genetic_population[i + 1] = temp2
                else:
                    self.genetic_population[i + 1] = self.produce()

    # 进行基因的变异
    def mutation(self):
        for i in range(self.population_size):  # 对每个染色体
            temp = self.genetic_population[i]
            for j in range(self.chrom_length):  # 的每个基因座
                if random.random() < self.pm:  # 如果小于变异概率，就变异
                    if temp[j] == 0:
                        temp[j] = 1
                    else:
                        temp[j] = 0
            if self.check(temp):
                self.genetic_population[i] = temp
            else:
                self.genetic_population[i] = self.produce()
        for i in range(self.population_size):
            if not self.check(self.genetic_population[i]):
                self.genetic_population[i] = self.produce()

    import time

    def maxv(self):
        # if __name__ == '__main__':
        self.genetic_population.clear()
        self.population.clear()
        self.fitness.clear()
        self.fitness_mean.clear()
        self.optimum_solution.clear()
        self.chrom_encoding()  # 编码，
        optimum_slt = []  # 存储最优解对应的x,y值，元组形式

        fig = plt.figure(0)
        plt.ion()
        ax = Axes3D(fig, auto_add_to_figure=False)
        fig.add_axes(ax)
        # 函数图像
        x = np.arange(-1, 1, 0.001)
        y = np.arange(-1, 1, 0.001)
        x, y = np.meshgrid(x, y)
        z = 1 + x * np.sin(np.pi * y) + y * np.sin(np.pi * x)
        ax.plot_surface(x, y, z, cmap='rainbow')
        plt.show()

        for step in range(self.generations):
            self.chrom_decoding()  # 解码，将各个染色体的两个十进制作为元组传入 population 列表中
            fit_mean = self.calculate_fitness()  # 计算每个染色体的适应度,将适应度传入fitness列表中，返回种群的平均适应度
            best_finess_var, best_id, best_finess = self.best_value()  # 适应度最高的个体的十进制编码、下标和适应度值
            self.optimum_solution.append(best_finess)  # 每次迭代的最佳适应度
            optimum_slt.append(best_finess_var)  # 每次迭代的最佳适应度对应的两个十进制值
            self.fitness_mean.append(fit_mean)  # 每次迭代的种群平均适应度

            if step%20==0:

                a,b=best_finess_var
                if 'scatt' in locals():
                    scatt.remove()
                scatt=ax.scatter(a, b, best_finess+0.05, c='b', marker='X')
                plt.show()
                plt.pause(0.1)


            self.selection()  # 选择
            self.crossover()  # 交叉
            self.mutation()  # 变异

        # fig = plt.figure(0)
        # ax = Axes3D(fig, auto_add_to_figure=False)
        # fig.add_axes(ax)
        # # 函数图像
        # x = np.arange(-1, 1, 0.001)
        # y = np.arange(-1, 1, 0.001)
        # x, y = np.meshgrid(x, y)
        # z = 1 + x * np.sin(np.pi * y) + y * np.sin(np.pi * x)
        # ax.plot_surface(x, y, z, cmap='rainbow')
        # # 画散点图
        # a, b = optimum_slt[-1]
        # ax.scatter(a, b, self.optimum_solution[-1], c='b', marker='o')
        # ax.view_init(20, 160)
        # plt.show()

        print(max(self.optimum_solution))
        # 最优解随迭代次数的变化

        fig1 = plt.figure(1)
        # range取不到最后一位
        plt.plot(range(1, self.generations + 1), self.optimum_solution)
        plt.xlabel('迭代次数', fontproperties='SimHei')
        plt.ylabel('最优解', fontproperties='SimHei')
        # 平均适应度随迭代次数的变化

        fig2 = plt.figure(2)
        plt.plot(range(1, self.generations + 1), self.fitness_mean)
        plt.xlabel('迭代次数', fontproperties='SimHei')
        plt.ylabel('平均适应度', fontproperties='SimHei')
        plt.show()
        print("======================================================")
        return max(self.optimum_solution)

    def calculate_fitness2(self):
        '''
        计算每个染色体的适应度,将适应度传入fitness列表中
        返回种群的平均适应度
        '''
        sum = 0.0
        self.fitness.clear()
        for i in range(self.population_size):
            #         1+x*np.sin(np.pi*y)+y*np.sin(np.pi*x)
            # ====================================================修改适应度函数
            function_value = -self.fmax(self.population[i][0], self.population[i][1]) + 5
            #         function_value=1+population[i][0]*np.sin(np.pi*population[i][1])+population[i][1]*np.sin(np.pi*population[i][0])
            # ====================================================
            if function_value > 0.0:
                # 计算种群的适应度
                sum += function_value
                # 将适应度大于0的个体适应度添加至数组
                self.fitness.append(function_value)
            else:
                self.fitness.append(0.0)
        # 返回种群的平均适应度
        return sum / self.population_size

    def minv(self):
        # if __name__ == '__main__':
        self.genetic_population.clear()
        self.population.clear()
        self.fitness.clear()
        self.fitness_mean.clear()
        self.optimum_solution.clear()
        self.chrom_encoding()  # 编码，
        optimum_slt = []  # 存储最优解对应的x,y值，元组形式

        fig = plt.figure(0)
        plt.ion()
        ax = Axes3D(fig, auto_add_to_figure=False)
        fig.add_axes(ax)
        # 函数图像
        x = np.arange(-1, 1, 0.001)
        y = np.arange(-1, 1, 0.001)
        x, y = np.meshgrid(x, y)
        z = 1 + x * np.sin(np.pi * y) + y * np.sin(np.pi * x)
        ax.plot_surface(x, y, z, cmap='rainbow',antialiased=True)
        # ax.scatter(x,y,z)
        # ax.plot_surface(x, y, z,cmap='theCM')
        plt.show()


        for step in range(self.generations):
            self.chrom_decoding()  # 解码，将各个染色体的两个十进制作为元组传入 population 列表中
            fit_mean = self.calculate_fitness2()  # 计算每个染色体的适应度,将适应度传入fitness列表中，返回种群的平均适应度
            best_finess_var, best_id, best_finess = self.best_value()  # 适应度最高的个体的十进制编码、下标和适应度值
            self.optimum_solution.append(best_finess)  # 每次迭代的最佳适应度
            optimum_slt.append(best_finess_var)  # 每次迭代的最佳适应度对应的两个十进制值
            self.fitness_mean.append(fit_mean)  # 每次迭代的种群平均适应度

            if step%20==0:

                a,b=best_finess_var
                if 'scatt' in locals():
                    scatt.remove()
                scatt=ax.scatter(a, b, -best_finess+5+0.1, c='r', marker='X')
                plt.show()
                plt.pause(0.1)

            self.selection()  # 选择
            self.crossover()  # 交叉
            self.mutation()  # 变异

        mina, minb, minv = 0, 0, 0
        for i in range(self.generations):
            if minv < self.optimum_solution[i]:
                mina, minb = optimum_slt[i]
                minv = self.optimum_solution[i]

        # fig = plt.figure(0)
        # ax = Axes3D(fig, auto_add_to_figure=False)
        # fig.add_axes(ax)
        # # 函数图像
        # x = np.arange(-1, 1, 0.001)
        # y = np.arange(-1, 1, 0.001)
        # x, y = np.meshgrid(x, y)
        # z = 1 + x * np.sin(np.pi * y) + y * np.sin(np.pi * x)
        # ax.plot_surface(x, y, z, cmap='rainbow')
        # # 画散点图
        # #     a,b=optimum_slt[-1]
        # #     print(optimum_slt)
        # #     print(maxa,maxb,5-maxv)
        # ax.scatter(mina, minb, 5 - minv, c='r', marker='o')
        # ax.view_init(45, 50)
            


        print(-max(self.optimum_solution) + 5)
        # 最优解随迭代次数的变化

        if 'scatt' in locals():
            scatt.remove()
        scatt = ax.scatter(mina, minb, -minv + 5 + 0.5, c='k', marker='X',s=100)
        print(mina,minb,-minv + 5)
        plt.show()
        plt.pause(0.1)


        fig1 = plt.figure(1)
        # range取不到最后一位
        plt.plot(range(1, self.generations + 1), self.optimum_solution)
        plt.xlabel('迭代次数', fontproperties='SimHei')
        plt.ylabel('最优解', fontproperties='SimHei')
        # 平均适应度随迭代次数的变化

        fig2 = plt.figure(2)
        plt.plot(range(1, self.generations + 1), self.fitness_mean)
        plt.xlabel('迭代次数', fontproperties='SimHei')
        plt.ylabel('平均适应度', fontproperties='SimHei')
        plt.show()
        print("======================================================")
        return -max(self.optimum_solution) + 5





# 主方法
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程