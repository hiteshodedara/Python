from tkinter import *
from tkinter import messagebox
import sqlite3 as sq


class db:
    def __init__(self):
        self.con = sq.connect("studentdb.db")
        self.cur = self.con.cursor()
        self.cur.execute(
            "create table if not exists student(sid INTEGER PRIMARY KEY AUTOINCREMENT,sname TEXT,srno INTEGER,"
            "semail TEXT,scity TEXT)")


class insert(db):
    def insertdata(self, sname, srno, semail, scity):
        query = f"insert into student(sname,srno,semail,scity) values('{sname}','{srno}','{semail}','{scity}')"
        self.cur.execute(query)
        self.con.commit()


class update(db):
    def updatedata(self, *args):
        query = f"update  student set sname='{args[0]}',srno='{args[1]}',semail='{args[2]}',scity='{args[3]}' where sid={args[4]}"
        self.cur.execute(query)
        self.con.commit()


class delete(db):
    def deletedata(self, tbid):
        query = f'''delete from student where sid={tbid}'''
        self.cur.execute(query)
        self.con.commit()


class show(db):
    def showdata(self):
        query = "select * from student"
        self.cur.execute(query)
        ok = self.cur.fetchall()
        return ok


class stu(insert, delete, update, show):
    pass


# tkinter code (GUI)
app = Tk()
app.title("Student Database")
app.geometry("800x600")


def instudent():
    instud = Toplevel(app)
    instud.geometry("600x400")
    instud.config(bg="light blue")

    in_lb_title = Label(instud, text="-- Insert Student Information --", font=("Helvatica", 20), bg="light blue")
    in_lb_title.grid(row=0, column=2)

    in_lb_name = Label(instud, text="Student Name:", font=("Helvatica", 10), bg="light blue")
    in_lb_name.grid(row=1, column=1, pady=10, padx=10)

    in_en_name = Entry(instud)
    in_en_name.grid(row=1, column=2)

    in_lb_rno = Label(instud, text="Student Roll No:", font=("Helvatica", 10), bg="light blue")
    in_lb_rno.grid(row=2, column=1, pady=10, padx=10)

    in_en_rno = Entry(instud)
    in_en_rno.grid(row=2, column=2)

    in_lb_email = Label(instud, text="Student Email:", font=("Helvatica", 10), bg="light blue")
    in_lb_email.grid(row=3, column=1, pady=10, padx=10)

    in_en_email = Entry(instud)
    in_en_email.grid(row=3, column=2)

    in_lb_city = Label(instud, text="Student City:", font=("Helvatica", 10), bg="light blue")
    in_lb_city.grid(row=4, column=1, pady=10, padx=10)

    in_en_city = Entry(instud)
    in_en_city.grid(row=4, column=2, pady=10)

    def insr():
        s1 = stu()
        name = in_en_name.get()
        rno = in_en_rno.get()
        email = in_en_email.get()
        city = in_en_city.get()
        s1.insertdata(name, rno, email, city)
        messagebox.showinfo("Info", "Data Inserted...")

    in_btn_sub = Button(instud, text="Insert Student Data", font=("Helvatica", 10), command=insr)
    in_btn_sub.grid(row=5, column=2, pady=10)


def upstudent():
    upstud = Toplevel(app)
    upstud.geometry("600x400")
    upstud.config(bg="light blue")

    in_lb_title = Label(upstud, text="-- Update Student Information --", font=("Helvatica", 20), bg="light blue")
    in_lb_title.grid(row=0, column=2)

    in_lb_name = Label(upstud, text="Student Name:", font=("Helvatica", 10), bg="light blue")
    in_lb_name.grid(row=1, column=1, pady=10, padx=10)

    in_en_name = Entry(upstud)
    in_en_name.grid(row=1, column=2)

    in_lb_rno = Label(upstud, text="Student Roll No:", font=("Helvatica", 10), bg="light blue")
    in_lb_rno.grid(row=2, column=1, pady=10, padx=10)

    in_en_rno = Entry(upstud)
    in_en_rno.grid(row=2, column=2)

    in_lb_email = Label(upstud, text="Student Email:", font=("Helvatica", 10), bg="light blue")
    in_lb_email.grid(row=3, column=1, pady=10, padx=10)

    in_en_email = Entry(upstud)
    in_en_email.grid(row=3, column=2)

    in_lb_city = Label(upstud, text="Student City:", font=("Helvatica", 10), bg="light blue")
    in_lb_city.grid(row=4, column=1, pady=10, padx=10)

    in_en_city = Entry(upstud)
    in_en_city.grid(row=4, column=2, pady=10)

    in_lb_id = Label(upstud, text="Student ID:", font=("Helvatica", 10), bg="light blue")
    in_lb_id.grid(row=5, column=1, pady=10, padx=10)

    in_en_id = Entry(upstud)
    in_en_id.grid(row=5, column=2, pady=10)

    def upda():
        id = in_en_id.get()
        name = in_en_name.get()
        rno = in_en_rno.get()
        email = in_en_email.get()
        city = in_en_city.get()
        s1 = stu()
        s1.updatedata(name, rno, email, city, id)
        messagebox.showinfo("Info", "Data Updated...")

    in_btn_sub = Button(upstud, text="Update Student Data", font=("Helvatica", 10), command=upda)
    in_btn_sub.grid(row=6, column=2, pady=10)

    lb = Label(upstud, text="[all detail needed]")
    lb.grid(row=7, column=2, pady=10)


def destudent():
    upstud = Toplevel(app)
    upstud.geometry("600x400")
    upstud.config(bg="light blue")

    in_lb_title = Label(upstud, text="-- Delete Student Information --", font=("Helvatica", 20), bg="light blue")
    in_lb_title.grid(row=0, column=2)

    in_lb_id = Label(upstud, text="Student ID:", font=("Helvatica", 10), bg="light blue")
    in_lb_id.grid(row=1, column=1, pady=10, padx=10)

    in_en_id = Entry(upstud)
    in_en_id.grid(row=1, column=2)

    def delt():
        id = in_en_id.get()

        s1 = stu()
        s1.deletedata(id)
        messagebox.showinfo("Info", "Data Deleted...")

    in_btn_sub = Button(upstud, text="Delete Student Data", font=("Helvatica", 10), command=delt)
    in_btn_sub.grid(row=2, column=2, pady=10)


def sostudent():
    sostud = Toplevel(app)
    sostud.geometry("600x400")
    sostud.config(bg="light blue")

    stud = stu()
    hi = stud.showdata()
    lb_id = Label(sostud, text="ID", bg="light blue")
    lb_id.grid(row=1, column=0, padx=10, pady=10)
    lb_id = Label(sostud, text="Name", bg="light blue")
    lb_id.grid(row=1, column=1, padx=10, pady=10)
    lb_id = Label(sostud, text="Roll No", bg="light blue")
    lb_id.grid(row=1, column=2, padx=10, pady=10)
    lb_id = Label(sostud, text="Email", bg="light blue")
    lb_id.grid(row=1, column=3, padx=10, pady=10)
    lb_id = Label(sostud, text="City", bg="light blue")
    lb_id.grid(row=1, column=4, padx=10, pady=10)

    num = 2
    for i in hi:
        lb_id = Label(sostud, text=i[0], bg="light blue")
        lb_id.grid(row=num, column=0, padx=10, pady=5)
        lb_id = Label(sostud, text=i[1], bg="light blue")
        lb_id.grid(row=num, column=1, padx=10, pady=5)
        lb_id = Label(sostud, text=i[2], bg="light blue")
        lb_id.grid(row=num, column=2, padx=10, pady=5)
        lb_id = Label(sostud, text=i[3], bg="light blue")
        lb_id.grid(row=num, column=3, padx=10, pady=5)
        lb_id = Label(sostud, text=i[4], bg="light blue")
        lb_id.grid(row=num, column=4, padx=10, pady=5)

        num = num + 1


menubar = Menu(app)
filemenu = Menu(app, tearoff=0)
filemenu.add_command(label="Insert Student", command=instudent)
filemenu.add_command(label="Updete Student", command=upstudent)
filemenu.add_command(label="Delete Student", command=destudent)
filemenu.add_command(label="Show Student", command=sostudent)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=app.quit)
menubar.add_cascade(label="CRUD OP", menu=filemenu)
exit = Menu(app, tearoff=0)
exit.add_command(label="hello", command=app.destroy)
menubar.add_cascade(label="more", menu=exit)

l1 = Label(app, text="This Is Student DataBase", font=("Helvatica", 30))
l1.pack(pady=200)

l2 = Label(app, text="For CRUD Operations Top Side Menu Avalable", font=("Helvatica", 10))
l2.pack(pady=20)

app.config(menu=menubar)
app.mainloop()
