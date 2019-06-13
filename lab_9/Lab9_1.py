#Employee record keeping system
from sqlite3 import *
from Tkinter import *
from tkMessageBox import *

con=Connection('data')
cur=con.cursor()
#cur.execute("drop table emp")
cur.execute("create table if not exists emp(code varchar2(5) PRIMARY KEY,fname varchar2(10),lname varchar2(10))")

root=Tk()
root.geometry("450x350")
root.title("Employee Record System")
Label(root,text="Employee",font='calibri 20 bold').grid(row=0,column=0)
Label(root,text=" Record Keeping",font='calibri 20 bold').grid(row=0,column=1)
Label(root,text=" System :",font='calibri 20 bold').grid(row=0,column=2)




Label(root,text="Enter Empl Code :",font='calibri 10').grid(row=1,column=0)
Label(root,text="Enter First Name :",font='calibri 10').grid(row=2,column=0)
Label(root,text="Enter Last Name :",font='calibri 10').grid(row=3,column=0)
Label(root,text="Enter ID to fetch :",font='calibri 10').grid(row=4,column=0)


code=Entry(root)
fname=Entry(root)
lname=Entry(root)
fetchId=Entry(root)

code.grid(row=1,column=1)
fname.grid(row=2,column=1)
lname.grid(row=3,column=1)
fetchId.grid(row=4,column=1)


def insert():
    try:
        cur.execute("insert into emp values(?,?,?)",(code.get(),fname.get(),lname.get()))
        showinfo('Success','The record has been inserted successfully')
    except:
        showerror('Error!','An entry with same ID already exists!')
        
    con.commit()

def show():
    showId=str(fetchId.get())
    if showId=="":
        Label(root,text="         Invalid Entry           ").grid(row=6,column=0)
    else:
        comm='select code,fname,lname from emp where code='+showId    
        cur.execute(comm)
        x=cur.fetchall()
        if x==[]:
            print 'Error'
        else:
            fsname=x[0][1]
            lsname=x[0][2]
            code=str(x[0][0])
            showinfo('ID :'+code,'Name :'+fsname+" "+lsname)
            
        

def show_all():
    cur.execute("select code,fname,lname from emp")
    x=cur.fetchall()
    new=Tk()
    new.geometry("200x400")
    new.title("All Records")
    for i in range (0,len(x)):
        fsname=x[i][1]
        lsname=x[i][2]
        Label(new,text=fsname+" "+lsname).pack()
    new.mainloop()
    
    

Button(root,text='Insert',command=insert).grid(row=5,column=0)
Button(root,text='Show',command=show).grid(row=5,column=1)
Button(root,text='Show All',command=show_all).grid(row=5,column=2)
Label(root,text="                                                  ").grid(row=6,column=0)


root.mainloop()
