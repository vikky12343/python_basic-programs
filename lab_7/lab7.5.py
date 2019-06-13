from Tkinter import *
root=Tk()
root.title('utk')
Label(root,text='Enter your name').pack()
name=Entry(root)
name.pack()
def fun():
    Label(root,text=''+name.get()).pack()
Button(root,text='GO',command=fun).pack()
root.mainloop()

