from Tkinter import*
root=Tk()
root.title('My GuI')
#----------------------------------------------
def fun():
    root=Tk()
    root.title("new window")
    Label(root,text="NEW WINDOW MATERIAL WINDOW").pack()



Label(root,text='hello word').pack()
Button(root,text='ok', command=fun).pack()
root.mainloop()
           
