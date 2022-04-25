from tkinter import *
from zhiqian import database as find
import tkinter as tk

class Find:
    def __init__(self):
        root = Tk()
        root.title('查询学生')
        Label(root, text='学号/姓名:').grid(row=0)
        id = Entry(root, textvariable=StringVar())
        id.grid(row=0, column=1, padx=10, pady=10)

        def queryid():
            text.delete('1.0', 'end')  # 从第一行开始，全部删除
            number = 0
            list = ['学号:', '姓名:', '年龄:', '性别:', '班级:', '电话:', '地址:']
            result = Find()
            print(result)
            if result:
                for index, item in enumerate(result):
                    message = list[index] + str(item) + '  '
                    text.insert(INSERT, message)
                    number += 1
                    if number == 7:
                        text.insert(INSERT, '\n')
                        number = 0
                tk.messagebox.showinfo('提示', '显示成功!')
            else:
                print("查无此人")
                tk.messagebox.showwarning('提示', '未查询到该学生!')
        def queryname():
            text.delete('1.0', 'end')  # 从第一行开始，全部删除
            number = 0
            list = ['学号:','姓名:','年龄:','性别:','班级:','电话:','地址:']
            result = Find2()
            print(result)
            if result:
                for index,item in enumerate(result):
                    message=list[index]+str(item)+'  '
                    text.insert(INSERT,message)
                    number+=1
                    if number==7:
                        text.insert(INSERT,'\n')
                        number=0
                tk.messagebox.showinfo('提示', '显示成功!')
            else:
                print("查无此人")
                tk.messagebox.showwarning('提示', '未查询到该学生!')

        def Find():
            sid = int(id.get())
            #print(sid)
            result =find.Query(sid)
            print(result)
            return result
            id.delete(0,END)

        def Find2():
            sname = str(id.get())
            # print(sname)
            result = find.Queryname(sname)
            print(result)
            return result
            id.delete(0,END)

        Button(root, text='ID查询', width=10, command=queryid).grid(row=7, column=0, sticky=W, padx=10, pady=5)
        Button(root, text='姓名查询', width=10, command=queryname).grid(row=7, column=2, sticky=W, padx=10, pady=5)
        Button(root, text='取消', width=10,command=root.quit).grid(row=7, column=3, sticky=E, padx=10, pady=5)
        text = tk.Text()
        text.grid(row=3, column=1)
        mainloop()


if __name__ == '__main__':
    Find()