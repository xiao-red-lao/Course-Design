from tkinter import *
from zhiqian import database as find
import tkinter as tk

class Sorsub:
    def __init__(self):
        root = Tk()
        root.title('成绩排序')
        Label(root, text='科目:').grid(row=0)
        sub = Entry(root, textvariable=StringVar())
        sub.grid(row=0, column=1, padx=10, pady=10)

        def querysub():
            text1.delete('1.0', 'end')  # 从第一行开始，全部删除
            number = 0
            list = ['学号:', '姓名:', 'C:', 'java:', 'python:']
            result = Find()
            print(result)
            if result:
                for items in result:
                    for index, item in enumerate(items):
                        message = list[index] + str(item) + '  '
                        text1.insert(INSERT, message)
                        number += 1
                        if number == 5:
                            text1.insert(INSERT, '\n')
                            number = 0
                tk.messagebox.showinfo('提示', '显示成功!')
            else:
                print("查无此人")
                tk.messagebox.showwarning('提示', '未查询到该科目!')
        def Find():
            ssub = str(sub.get())
            if(ssub=="python"):
                result =find.QueryAll4()
                #print(result)
            elif(ssub=="C"):
                result = find.QueryAll5()
            elif(ssub=="java"):
                result = find.QueryAll6()
            else:
                tk.messagebox.showwarning('提示', '未查询到该科目!')
            return result
            sub.delete(0,END)

        text1 = tk.Text(root)
        text1.grid(row=4, column=1)
        Button(root, text='开始排序', width=10, command=querysub).grid(row=7, column=0, sticky=W, padx=10, pady=5)
        Button(root, text='取消', width=10,command=root.quit).grid(row=7, column=1, sticky=E, padx=10, pady=5)


        mainloop()


if __name__ == '__main__':
    Sorsub()