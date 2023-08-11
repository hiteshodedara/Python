import sqlite3 as sq

class db:
    def __init__(self) :
        self.con=sq.connect("studentdb.db")
        self.cur=self.con.cursor()
        self.cur.execute("create table if not exists student(sid INTEGER PRIMARY KEY AUTOINCREMENT,sname TEXT,srno INTEGER,semail TEXT,scity TEXT)")
        


class insert(db):
    def insertdata(self,sname,srno,semail,scity):
        query=f"insert into student(sname,srno,semail,scity) values('{sname}','{srno}','{semail}','{scity}')"
        self.cur.execute(query)
        self.con.commit()
        
        print("data inserts..")


class update(db):
    def updatedata(self,sid,sname,srno,semail,scity):
        query=f'''update  student set sname='{sname}',srno='{srno}',semail='{semail}',scity='{scity}' where id={sid}'''
        self.cur.execute(query)
        self.con.commit()
        
        print("data updated")

class delete(db):
    def deletedata(self,tbid):
        query=f'''delete from student where id={tbid}'''
        self.cur.execute(query)
        self.con.commit()
        
        print("data deleted")

class show(db):
    def showdata(self):
        query="select * from student"
        hi=self.cur.execute(query)
        ok=hi.fetchall()
        print(f"id      name        city\n")
        for i in ok:
            print(f"{i[0]}      {i[1]}       {i[2]}")

class stu(insert,delete,update,show):
    pass


