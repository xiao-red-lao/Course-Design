from tkinter import *
import tkinter as tk
import tkinter.messagebox #消息框
from zhiqian import Find as F, Delete as DE, Sexfind as SF, Update as UP, sorsub as sb, AddStudent as AS, database as q
# from PIL import Image,ImageDraw,ImageFont
from PIL import Image, ImageTk

class Mian:
    def __init__(self):
        #新建窗口为root
        root = tk.Tk()
        root.title('zqf is trying')

        #在root窗口中创建一个label存放华电校徽
        image = Image.open(r"/zhiqian/hd.gif")
        # 获取图像的原始大小
        w, h = image.size
        #期望大小
        w_box,h_box=200,200
        # 缩放图像让它保持比例，同时限制在一个矩形框范围内
        image_resized = Mian.resize(w, h, w_box,h_box, image)
        logo = ImageTk.PhotoImage(image_resized)
        #建立一个label，属于root窗口,，在第0行第1列
        Label(root,image=logo,width=w_box,height=h_box,bg='LightBlue').grid(row=0,column=1)


        def add():
            AS.AddStudent()
        def edit():
            UP.Update()
        def dele():
            DE.Delete()
        def find():
            F.Find()
        def sfind():
            SF.Sexfind()
        def ss():
            sb.Sorsub()

        def queryall():
            text.delete('1.0','end') #从第一行开始，全部删除
            number=0
            list=['学号:','姓名:','年龄:','性别:','班级:','电话:','地址:']
            result=q.QueryAll()
            for items in result:
                for index,item in enumerate(items):
                    message=list[index]+str(item)+' '
                    text.insert(INSERT,message)
                    number+=1
                    if number==7:
                        text.insert(INSERT,'\n')
                        number=0
            tk.messagebox.showinfo('提示', '显示成功!')

        def queryall2():
            text.delete('1.0','end') #从第一行开始，全部删除
            number=0
            list=['序号:','班级:','人数:']
            result=q.QueryAll2()
            # print(result)
            for items in result:
                for index,item in enumerate(items):
                    message=list[index]+str(item)+' '
                    text.insert(INSERT,message)
                    number+=1
                    if number==3:
                        text.insert(INSERT,'\n')
                        number=0
            tk.messagebox.showinfo('提示', '显示成功!')

        def queryall3():
            text.delete('1.0','end') #从第一行开始，全部删除
            number=0
            list=['学号:','姓名:','C语言:','java:','python:']
            result=q.QueryAll3()
            # print(result)
            for items in result:
                for index,item in enumerate(items):
                    message=list[index]+str(item)+' '
                    text.insert(INSERT,message)
                    number+=1
                    if number==5:
                        text.insert(INSERT,'\n')
                        number=0
            tk.messagebox.showinfo('提示', '显示成功!')

        Button(root, text='ID/姓名\n查询', width=10, height=2,bg='LightBlue',command=find).grid(row=1,column=6,sticky=W)
        Button(root, text='添加学生', width=10,height=2,bg='LightBlue',command=add).grid(row=1,column=2,sticky=W)
        Button(root, text='编辑学生', width=10,height=2,bg='LightBlue',command=edit).grid(row=1,column=3,sticky=W)
        Button(root, text='成绩排序', width=10, height=2,bg='LightBlue',command=ss).grid(row=1, column=4, sticky=W)
        Button(root, text='删除学生', width=10,height=2,bg='LightBlue',command=dele).grid(row=1,column=7,sticky=N)
        Button(root, text='性别查询', width=10, height=2,bg='LightBlue',command=sfind).grid(row=2, column=6, sticky=W)
        Button(root, text='显示全部\n基本信息', width=10,height=2,bg='LightBlue',command=queryall).grid(row=2, column=2,sticky=W)
        Button(root, text='显示全部\n班级信息', width=10,height=2,bg='LightBlue',command=queryall2).grid(row=2, column=3,sticky=W)
        Button(root, text='显示全部\n学生成绩', width=10, height=2,bg='LightBlue',command=queryall3).grid(row=2, column=4, sticky=W)

        text=tk.Text()
        text.grid(row=3, column=0)
        mainloop()

    def resize(w, h, w_box, h_box, pil_image):
        '''
        对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
        别动这个
        '''
        f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        # print(f1, f2, factor) # test
        # use best down-sizing filter
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)

if __name__=='__main__':
    Mian()