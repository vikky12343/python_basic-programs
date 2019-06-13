#Employee record keeping system
from sqlite3 import *
from Tkinter import *

con=Connection('data')
cur=con.cursor()
#cur.execute("drop table record")
cur.execute("create table if not exists record(er number(5),fname varchar2(10),lname varchar2(10),dob date(11),father varchar2(20),course varchar2(10) ,dept varchar2(6),addr varchar2(30),mobile number(10),email varchar2(20),cgpa number(3,1),cert varchar2(5))")
#check course in ('B.Tech','M.Tech')
#check cert in ('RHCE','MCSE','CCNA','OCP')
#check dept in ('CSE','ECE','MEC','Civil')

root=Tk()
root.geometry("450x350")
root.title("Student Record System")
Label(root,text="Student",font='calibri 20 bold').grid(row=0,column=0)
Label(root,text=" Record Keeping",font='calibri 20 bold').grid(row=0,column=1)
Label(root,text=" System :",font='calibri 20 bold').grid(row=0,column=2)


Label(root,text="Student Er.No. :",font='calibri 10').grid(row=1,column=0)
Label(root,text="First Name :",font='calibri 10').grid(row=2,column=0)
Label(root,text="Last Name :",font='calibri 10').grid(row=3,column=0)
Label(root,text="DOB :",font='calibri 10').grid(row=4,column=0)
Label(root,text="Father's Name :",font='calibri 10').grid(row=5,column=0)
Label(root,text="Course :",font='calibri 10').grid(row=6,column=0)
Label(root,text="Department :",font='calibri 10').grid(row=7,column=0)
Label(root,text="Address :",font='calibri 10').grid(row=8,column=0)
Label(root,text="Mobile no. :",font='calibri 10').grid(row=9,column=0)
Label(root,text="Email :",font='calibri 10').grid(row=10,column=0)
Label(root,text="CGPA :",font='calibri 10').grid(row=11,column=0)
Label(root,text="Certification :",font='calibri 10').grid(row=12,column=0)

eno=Entry(root)
fname=Entry(root)
lname=Entry(root)
dob=Entry(root)
father=Entry(root)
course=Entry(root)
dept=Entry(root)
addr=Entry(root)
mobile=Entry(root)
email=Entry(root)
cgpa=Entry(root)
certi=Entry(root)

eno.grid(row=1,column=1)
fname.grid(row=2,column=1)
lname.grid(row=3,column=1)
dob.grid(row=4,column=1)
father.grid(row=5,column=1)
course.grid(row=6,column=1)
dept.grid(row=7,column=1)
addr.grid(row=8,column=1)
mobile.grid(row=9,column=1)
email.grid(row=10,column=1)
cgpa.grid(row=11,column=1)
certi.grid(row=12,column=1)

def insert():
    cur.execute("insert into record values(?,?,?,?,?,?,?,?,?,?,?,?)",(eno.get(),fname.get(),lname.get(),dob.get(),father.get(),course.get(),dept.get(),addr.get(),mobile.get(),email.get(),cgpa.get(),certi.get()))
    con.commit()

def show_all():
    cur.execute("select * from record")
    x=cur.fetchall()
    new=Tk()
    new.geometry("400x400")
    new.title("All Records")
    for i in range (0,len(x)):
        enum=str(x[i][0])
        fsname=x[i][1]
        lsname=x[i][2]
        dob=str(x[i][3])
        father=x[i][4]
        course=x[i][5]
        dept=x[i][6]
        addr=x[i][7]
        mobile=str(x[i][8])
        email=x[i][9]
        cgpa=str(x[i][10])
        certi=x[i][11]
        
        
        Label(new,text=enum+" "+fsname+" "+lsname+" "+dob+" "+father+" "+course+" "+dept+" "+addr+" "+mobile+" "+email+" "+cgpa+" "+certi).pack()
    new.mainloop()
    
    

Button(root,text='Insert',command=insert).grid(row=13,column=0)
Button(root,text='Show All',command=show_all).grid(row=13,column=1)


root.mainloop()
