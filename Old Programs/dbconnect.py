#this work in python 3.7..
#open cmd as administrator and run this ("pip install mysql-connector-python")
#open xampp control panel and start mysql server 
#and than this code work

import mysql.connector

#for a create database in mysql database
    #db=mysql.connector.connect(host="localhost",user="root",password="")
    #cursor=db.cursor()
    #query="create database python"
    #cursor.execute(query)

#main connection
db1=mysql.connector.connect(host="localhost",user="root",password="",database="python")
cursor=db1.cursor()

#for a create table
    #cursor.execute("create table hitesh (id int(10),name varchar(100),password varchar(100))")

#for a insert values in table
    #query="insert into hitesh(id,name,password) values(%s,%s,%s)"
    #user=[(1,"odedara hitesh","hitesh123"),(2,"solanki raj","raj123"),(3,"lathiya jenil","jenil123"),]
    #cursor.executemany(query,user)


#for a fetch data from table
"""
query="select * from hitesh"
cursor.execute(query)
result=cursor.fetchall()
for data in result:
    print(data)
"""


#for update table
    #query="update hitesh set password='hiteshodii' where name='odedara hitesh'"
    #cursor.execute(query)


#for a delete data from table
    #query="delete from hitesh where id=1"
    #cursor.execute(query)


#for a drop table
    #query="drop table hitesh"
    #cursor.execute(query)


db.commit()
