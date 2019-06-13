a,b=input('enter two number')
from Tkinter import*
root=Tk()
def fun1():
    print a+b
Button(root,text='sum',command=fun1).pack()
def fun2():
    print a-b
Button(root,text='dif',command=fun2).pack()
def fun3():
    print a*b
Button(root,text='mul',command=fun3).pack()
def fun4():
    print a/b
Button(root,text='div',command=fun4).pack()
root.mainloop()
