from tkinter import  *
from zhiqian import database as add


class AddStudent:
    def __init__(self):
        #新建窗口
        root=Tk()
        root.title('新增学生')
        #设置7行的label
        Label(root, text='学号:').grid(row=0)
        Label(root, text='姓名:').grid(row=1)
        Label(root, text='年龄:').grid(row=2)
        Label(root, text='性别:').grid(row=3)
        Label(root, text='班级:').grid(row=4)
        Label(root, text='电话:').grid(row=5)
        Label(root, text='地址:').grid(row=6)

        #创建对应7个文本框
        id=Entry(root,textvariable=StringVar())
        name=Entry(root,textvariable=StringVar())
        age=Entry(root,textvariable=StringVar())
        gender = Entry(root, textvariable=StringVar())
        cla = Entry(root, textvariable=StringVar())
        phone = Entry(root, textvariable=StringVar())
        address = Entry(root, textvariable=StringVar())

        #吧文本框对应行的第二列
        id.grid(row=0, column=1, padx=10, pady=10)
        name.grid(row=1, column=1, padx=20, pady=5)
        age.grid(row=2, column=1, padx=10, pady=5)
        gender.grid(row=3, column=1, padx=10, pady=5)
        cla.grid(row=4, column=1, padx=10, pady=5)
        phone.grid(row=5, column=1, padx=10, pady=5)
        address.grid(row=6, column=1, padx=10, pady=5)


        def adds():
            '''
            从文本框中读取文本并加入数据库中
            '''
            sid=int(id.get())
            sname=name.get()
            sage=int(age.get())
            sgender = gender.get()
            scla = cla.get()
            sphone = int(phone.get())
            saddress = address.get()

            #加入数据库中
            add.Add(sid, sname, sage, sgender, scla, sphone, saddress)

            #清空数据库
            id.delete(0, END)
            name.delete(0, END)
            age.delete(0, END)
            gender.delete(0, END)
            cla.delete(0, END)
            phone.delete(0, END)
            address.delete(0, END)

        Button(root,text='添加',width=10,command=adds).grid(row=7,column=0,sticky=W,padx=10,pady=5)
        Button(root,text='取消',width=10,command=root.quit).grid(row=7,column=1,sticky=E,padx=10,pady=5)
        mainloop()
if __name__=='__main__':
    AddStudent()
