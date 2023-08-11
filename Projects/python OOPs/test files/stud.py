import sqlite3 as sq

# connect with database
con=sq.connect("stud1.db")

# make cursor using con string
cur=con.cursor()

# create table query
cur.execute("create table if not exists student(id INTEGER PRIMARY KEY AUTOINCREMENT,s_name TEXT,s_email TEXT,s_rno INTEGER, s_city TEXT)")


#insert data in table
#cur.execute('''insert into student(s_name,s_email,s_rno,s_city) values('hitesh','hit@gmail.com',27,'juna')''')






con.commit()
con.close()