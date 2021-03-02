from connect import Connection 			#connect file connect.py and class Connection
con=None
try:
    c=Connection()                      #creation of object for class Connection
    con=c.con
    print("connected")
    cursor=con.cursor()
    #table creation query
    sql="create table student(rno int primary key, name varchar(40), address varchar(80),physics int,chemistry int,maths int,english int,comp int)"
    cursor.execute(sql)         #run the query
    print("table created")
except Exception as e:
    print("table creation issue ",e)
finally:
    if con is not None:
        con.close()             #close connection
        print("disconnected")
    