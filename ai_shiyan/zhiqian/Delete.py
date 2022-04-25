from tkinter import *
from zhiqian import database as delete


class Delete:
    def __init__(self):
        root = Tk()
        root.title('删除学生')
        Label(root, text='学号:').grid(row=0)
        id = Entry(root, textvariable=StringVar())
        id.grid(row=0, column=1, padx=10, pady=10)
        def deles():
            sid = int(id.get())
            delete.Delete(sid)
            id.delete(0,END)
        Button(root, text='删除', width=10, command=deles).grid(row=7, column=0, sticky=W, padx=10, pady=5)
        Button(root, text='取消', width=10,command=root.quit).grid(row=7, column=1, sticky=E, padx=10, pady=5)
        mainloop()
if __name__ == '__main__':
    Delete()