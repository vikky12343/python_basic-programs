from Tkinter import*
root=Tk()
root.title('My GUI')
Label(root,text='heelo word').pack()
def fun():
    Label(root,text='welcome').pack()
Button(root,text='ok',command=fun).pack()
root.mainloop()
