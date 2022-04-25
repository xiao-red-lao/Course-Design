'''
连接数据库，给出一些普通的操作语句
'''
import pymysql
import tkinter as tk
import  tkinter.messagebox
# 打开数据库
db=pymysql.connect(host='localhost',user='root',password='111111',database='try')
# 使用cursor()方法获取操作游标
cursor=db.cursor()


def IsExists(id):
    '''
    查找是否存在某个学生
    '''
    sql="select * from students where id=%s"
    # 使用execute方法执行SQL语句
    cursor.execute(sql,id)
    result=cursor.rowcount
    if result:
        return True
    else:
        return False

def Add(id,name,age,gender,cla,phone,address):
    '''
    添加某个学生
    '''
    if(IsExists(id)==True):
        print('该学生已存在')
        tk.messagebox.showwarning('提示','该学生已存在')
    else:
        sql="insert into  students values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(id,name,age,gender,cla,phone,address))
        result=cursor.rowcount
        if result:
            print('添加成功')
            tk.messagebox.showinfo('提示','添加成功!')
        else:
            print('添加失败')
            tk.messagebox.showerror('提示','添加失败!')

def Delete(id):
    '''
    删除某个学生
    '''
    if(IsExists(id)==True):
        sql="delete from students where id=%s"
        cursor.execute(sql,id)
        result=cursor.rowcount
        if result:
            print('删除成功')
            tk.messagebox.showinfo('提示','删除成功!')
        else:
            print('删除失败')
            tk.messagebox.showerror('提示','删除失败!')
    else:
        print('该学生不存在')
        tk.messagebox.showwarning('提示','该学生不存在!')

def Update(id,name,age,gender,cla,phone,address):
    '''
    修改某个学生
    '''
    if(IsExists(id)==True):
        sql='update students set name=%s,age=%s,gender=%s,cla=%s,phone=%s,address=%s where id=%s'
        cursor.execute(sql,(name,age,gender,cla,phone,address,id))
        result=cursor.rowcount
        if result:
            print('修改成功')
            tk.messagebox.showinfo('提示','修改成功!')
        else:
            print('修改失败')
            tk.messagebox.showerror('提示','修改失败!')
    else:
        print('未查询到该学生')
        tk.messagebox.showwarning('提示','未查询到该学生!')



def Query(id):
    '''
    根据id搜索学生信息
    '''
    sql="select * from students where id =%s"
    cursor.execute(sql,id)
    #返回一条记录
    result=cursor.fetchone()
    # print(result)
    return result

def Queryname(name):
    '''
    根据姓名搜索学生信息
    '''
    sql="select * from students where name =%s"

    cursor.execute(sql,name)
    result=cursor.fetchone()
    # print(result)
    return result

def findsex(sex):
    '''
    根据性别查找学生
    '''
    sql="select * from students where gender =%s"
    cursor.execute(sql,sex)
    # 返回多条记录（二维元组）
    result=cursor.fetchall()
    # print(result)
    return result

def QueryAll():
    '''
    查找所有学生
    '''
    #list=['学号:','姓名:','年龄:'...:']
    sql="select * from students"
    cursor.execute(sql)
    #返回多条记录
    result=cursor.fetchall()
    #for items in result:
       # for index,item in enumerate(items):
      #      print(list[index],item,end='')
     #   print('\n')
    #print(result)
    return result

def QueryAll2():
    '''
    查找所有班级信息
    '''
    sql="select * from class"
    cursor.execute(sql)
    result=cursor.fetchall()
    return result

def QueryAll3():
    '''
    查找所有年级信息
    '''
    sql="select * from grade"
    cursor.execute(sql)
    result=cursor.fetchall()
    return result

def QueryAll4():
    '''
    根据python成绩来倒序排序
    '''
    sql="select * from grade order by python desc"
    cursor.execute(sql)
    result=cursor.fetchall()
    return result
def QueryAll5():
    '''
    根据C成绩来倒序排序
    '''
    sql="select * from grade order by C desc"
    cursor.execute(sql)
    result=cursor.fetchall()
    return result
def QueryAll6():
    '''
    根据JAVA成绩倒序排序
    '''
    sql="select * from grade order by java desc"
    cursor.execute(sql)
    result=cursor.fetchall()
    return result

QueryAll()