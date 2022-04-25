import matplotlib.pyplot as plt
import numpy as np
import random
import math
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# 使用遗传算法找函数的最大值点
population_size=2000  #种群数量
generations=200  #迭代次数
#==========================================
chrom_length=16 #染色体长度，
#==========================================
pc=0.6  # 交配概率
pm=0.001 # 变异概率
genetic_population =[] # 种群的基因编码
population =[] # 种群对应的十进制数值
fitness =[] # 适应度
fitness_mean=[] # 平均适应度
optimum_solution =[] #每次迭代所获最优解
optimum_slt=[]  # 存储最优解对应的x,y值，元组形式
up=1 #上限
down=-1 #下限
precision=0.01 #精度

# 为染色体进行0，1编码，生成初始种群
def chrom_encoding():
    for i in range(population_size):
        a=random.randint(0,(up-down)/precision) #在允许范围内随机生成
        b=random.randint(0,(up-down)/precision) #在允许范围内随机生成
        aa=convert_b(a,chrom_length/2) #转为8位的str类型
        bb=convert_b(b,chrom_length/2)
        population_i=list(aa+bb) #两个染色体合并
        population_i=[int(x) for x in population_i] #各位转为int类型
        genetic_population.append(population_i) #元素是一个int列表，16位

#将数字a转为长度为n的二进制位，str类型
def convert_b(a:int,n:int):
    b = '{:b}'.format(a)
    while (len(b)<n): b='0'+b
    return b
#将数字a转为十进制，int类型
def convert_d(a:str):
    return int(a,2)
# convert_d('01110011')

def fmax(x,y):
    '''
    适合题目的适应度函数
    '''
    return 1+x*np.sin(np.pi*y)+y*np.sin(np.pi*x)

def chrom_decoding():
    '''
    对染色体进行解码，将二进制转化为十进制
    将得到的两个十进制作为元组传入 population 列表中
    '''
    population.clear() #清空
    for i in range(population_size):#对第i个染色体操作
        value = 0
        for j in range(0,chrom_length//2): #对第一个个体操作
            value += genetic_population[i][j]*(2**(chrom_length/2-1-j)) #染色体a值
        a=down+value*precision
        value = 0
        for j in range(chrom_length//2,chrom_length):
            i=j-chrom_length//2
            value += genetic_population[i][j]*(2**(chrom_length/2-1-i)) #染色体b值
        b=down+value*precision
        population.append((a,b))

def calculate_fitness():
    '''
    计算每个染色体的适应度,将适应度传入fitness列表中
    返回种群的平均适应度
    '''
    sum=0.0
    fitness.clear()
    for i in range(population_size):
#         1+x*np.sin(np.pi*y)+y*np.sin(np.pi*x)
#====================================================修改适应度函数
        function_value=fmax(population[i][0],population[i][1])
#         function_value=1+population[i][0]*np.sin(np.pi*population[i][1])+population[i][1]*np.sin(np.pi*population[i][0])
#====================================================
        if function_value > 0.0:
            # 计算种群的适应度
            sum+=function_value
            # 将适应度大于0的个体适应度添加至数组
            fitness.append(function_value)
        else:
            fitness.append(0.0)
    # 返回种群的平均适应度
    return sum/population_size

def best_value():
    '''
    获取最大适应度的个体和对应的编号
    返回元组表示的十进制的x和y，最大适应度下标，对应最大适应度
    '''
    max_fitness=fitness[0]
    max_chrom=0
    for i in range(population_size):
        if fitness[i]>max_fitness:
            max_fitness=fitness[i]
            max_chrom=i
    return population[max_chrom],max_chrom,max_fitness

def selection():
    '''
    采用轮盘赌算法进行选择过程，重新选择与种群数量相等的新种群
    '''
    # 种群的适应度数组
    fitness_array = np.array(fitness)
    # 从指定的一维数组中生成随机数 para1:一维数组  para2:数组长度 para3:replace=TRUE 代表可以重复 para4:数组中数据出现的概率
    new_population_id = np.random.choice(np.arange(population_size), (population_size),
                                         replace=True, p=fitness_array/fitness_array.sum())
    new_genetic_population = []
    global genetic_population
    for i in range(population_size):
        new_genetic_population.append(genetic_population[new_population_id[i]])
    genetic_population = new_genetic_population

def produce():
    a=random.randint(0,(up-down)/precision) #在允许范围内随机生成
    b=random.randint(0,(up-down)/precision) #在允许范围内随机生成
    aa=convert_b(a,chrom_length/2) #转为8位的str类型
    bb=convert_b(b,chrom_length/2)
    d=list(aa+bb) #两个染色体合并
    d=[int(x) for x in d] #各位转为int类型
    return d

def check(intlist):
    a=0
    b=0
    for i in range(len(intlist)//2):
        a=a*2+intlist[i]
        b=b*2+intlist[i+len(intlist)//2]
    d=200
    if a>d or b>d:
        return False
    else:
        return True

# 进行交配过程
def crossover():
    for i in range(0,population_size-1,2):
        #如果小于交叉概率，执行交叉
        if random.random()<pc:
            # 随机选择交叉点，
            change_point=random.randint(0,chrom_length-1)
            temp1=[]
            temp2=[]
            temp1.extend(genetic_population[i][0:change_point]) #交叉点前是i
            temp1.extend(genetic_population[i+1][change_point:]) #交叉点后是i+1
            temp2.extend(genetic_population[i+1][0:change_point])
            temp2.extend(genetic_population[i][change_point:])
            if check(temp1):
                genetic_population[i]=temp1
            else:
                genetic_population[i]=produce()
            if check(temp2):
                genetic_population[i+1]=temp2
            else:
                genetic_population[i+1]=produce()

# 进行基因的变异
def mutation():
    for i in range(population_size): #对每个染色体
        temp=genetic_population[i]
        for j in range(chrom_length): #的每个基因座
            if random.random()<pm: #如果小于变异概率，就变异
                if temp[j]==0:
                    temp[j]=1
                else:
                    temp[j]=0
        if check(temp):
            genetic_population[i]=temp
        else:
            genetic_population[i]=produce()
    for i in range(population_size):
        if not check(genetic_population[i]):
            genetic_population[i]=produce()


import time


def maxv():
    # if __name__ == '__main__':
    genetic_population.clear()
    population.clear()
    fitness.clear()
    fitness_mean.clear()
    optimum_solution.clear()
    chrom_encoding()  # 编码，
    optimum_slt = []  # 存储最优解对应的x,y值，元组形式
    for step in range(generations):
        chrom_decoding()  # 解码，将各个染色体的两个十进制作为元组传入 population 列表中
        fit_mean = calculate_fitness()  # 计算每个染色体的适应度,将适应度传入fitness列表中，返回种群的平均适应度
        best_finess_var, best_id, best_finess = best_value()  # 适应度最高的个体的十进制编码、下标和适应度值
        optimum_solution.append(best_finess)  # 每次迭代的最佳适应度
        optimum_slt.append(best_finess_var)  # 每次迭代的最佳适应度对应的两个十进制值
        fitness_mean.append(fit_mean)  # 每次迭代的种群平均适应度
        selection()  # 选择
        crossover()  # 交叉
        mutation()  # 变异

    fig = plt.figure()
    ax = Axes3D(fig)
    # 函数图像
    x = np.arange(-1, 1, 0.001)
    y = np.arange(-1, 1, 0.001)
    x, y = np.meshgrid(x, y)
    z = 1 + x * np.sin(np.pi * y) + y * np.sin(np.pi * x)
    ax.plot_surface(x, y, z, cmap='rainbow')
    # 画散点图
    a, b = optimum_slt[-1]
    ax.scatter(a, b, optimum_solution[-1], c='b', marker='o')
    ax.view_init(20, 160)
    plt.show()

    print(max(optimum_solution))
    # 最优解随迭代次数的变化

    fig1 = plt.figure(1)
    # range取不到最后一位
    plt.plot(range(1, generations + 1), optimum_solution)
    plt.xlabel('迭代次数', fontproperties='SimHei')
    plt.ylabel('最优解', fontproperties='SimHei')
    # 平均适应度随迭代次数的变化

    fig2 = plt.figure(2)
    plt.plot(range(1, generations + 1), fitness_mean)
    plt.xlabel('迭代次数', fontproperties='SimHei')
    plt.ylabel('平均适应度', fontproperties='SimHei')
    plt.show()
    print("======================================================")
    return max(optimum_solution)

def calculate_fitness2():
    '''
    计算每个染色体的适应度,将适应度传入fitness列表中
    返回种群的平均适应度
    '''
    sum=0.0
    fitness.clear()
    for i in range(population_size):
#         1+x*np.sin(np.pi*y)+y*np.sin(np.pi*x)
#====================================================修改适应度函数
        function_value=-fmax(population[i][0],population[i][1])+5
#         function_value=1+population[i][0]*np.sin(np.pi*population[i][1])+population[i][1]*np.sin(np.pi*population[i][0])
#====================================================
        if function_value > 0.0:
            # 计算种群的适应度
            sum+=function_value
            # 将适应度大于0的个体适应度添加至数组
            fitness.append(function_value)
        else:
            fitness.append(0.0)
    # 返回种群的平均适应度
    return sum/population_size


def minv():
    # if __name__ == '__main__':
    genetic_population.clear()
    population.clear()
    fitness.clear()
    fitness_mean.clear()
    optimum_solution.clear()


    chrom_encoding()  # 编码，
    optimum_slt = []  # 存储最优解对应的x,y值，元组形式
    for step in range(generations):
        chrom_decoding()  # 解码，将各个染色体的两个十进制作为元组传入 population 列表中
        fit_mean = calculate_fitness2()  # 计算每个染色体的适应度,将适应度传入fitness列表中，返回种群的平均适应度
        best_finess_var, best_id, best_finess = best_value()  # 适应度最高的个体的十进制编码、下标和适应度值
        optimum_solution.append(best_finess)  # 每次迭代的最佳适应度
        optimum_slt.append(best_finess_var)  # 每次迭代的最佳适应度对应的两个十进制值
        fitness_mean.append(fit_mean)  # 每次迭代的种群平均适应度
        selection()  # 选择
        crossover()  # 交叉
        mutation()  # 变异

    mina,minb,minv=0,0,0
    for i in range(generations):
        if minv < optimum_solution[i]:
            mina, minb = optimum_slt[i]
            minv = optimum_solution[i]

    fig = plt.figure(0)
    ax = Axes3D(fig,auto_add_to_figure=False)
    fig.add_axes(ax)
    # 函数图像
    x = np.arange(-1, 1, 0.001)
    y = np.arange(-1, 1, 0.001)
    x, y = np.meshgrid(x, y)
    z = 1 + x * np.sin(np.pi * y) + y * np.sin(np.pi * x)
    ax.plot_surface(x, y, z, cmap='rainbow')
    # 画散点图
    #     a,b=optimum_slt[-1]
    #     print(optimum_slt)
    #     print(maxa,maxb,5-maxv)
    ax.scatter(mina, minb, 5 - minv, c='r', marker='o')
    ax.view_init(45, 50)


    print(-max(optimum_solution) + 5)
    # 最优解随迭代次数的变化

    fig1 = plt.figure(1)
    # range取不到最后一位
    plt.plot(range(1, generations + 1), optimum_solution)
    plt.xlabel('迭代次数', fontproperties='SimHei')
    plt.ylabel('最优解', fontproperties='SimHei')
    # 平均适应度随迭代次数的变化

    fig2 = plt.figure(2)
    plt.plot(range(1, generations + 1), fitness_mean)
    plt.xlabel('迭代次数', fontproperties='SimHei')
    plt.ylabel('平均适应度', fontproperties='SimHei')
    plt.show()
    print("======================================================")
    return -max(optimum_solution) + 5
if __name__ == '__main__':
    minv()