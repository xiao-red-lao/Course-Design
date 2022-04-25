from tkinter import *
from zhiqian import database as find
import tkinter as tk

class Sexfind:
    def __init__(self):
        root = Tk()
        root.title('查询学生')
        Label(root, text='性别:').grid(row=0)
        gender = Entry(root, textvariable=StringVar())
        gender.grid(row=0, column=1, padx=10, pady=10)

        def querysex():
            text.delete('1.0', 'end')  # 从第一行开始，全部删除
            number = 0
            list = ['学号:', '姓名:', '年龄:', '性别:', '班级:', '电话:', '地址:']
            result = Find()
            print(result)
            if result:
                for items in result:
                    for index, item in enumerate(items):
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

        def Find():
            sgender = str(gender.get())
            result =find.findsex(sgender)
            #print(result)
            return result
            id.delete(0,END)

        Button(root, text='性别查询', width=10, command=querysex).grid(row=7, column=0, sticky=W, padx=10, pady=5)
        Button(root, text='取消', width=10,command=root.quit).grid(row=7, column=1, sticky=E, padx=10, pady=5)
        text = tk.Text()
        text.grid(row=4, column=0)
        mainloop()


if __name__ == '__main__':
    Sexfind()