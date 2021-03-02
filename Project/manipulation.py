from connect import Connection 			#connect file connect.py and class Connection
class Data_manipulation:
    def add_student(self,rno,name,address,physics,chemistry,maths,english,comp):
        #create object of class connection
        con=Connection()
        con=con.con
        #create the object of cursor cur cursor() inbuilt method of connect class)
        cursor=con.cursor()
        
        val=(rno,name,address,physics,chemistry,maths,english,comp)
        #Insert query run
        query="INSERT INTO student (rno,name,address,physics,chemistry,maths,english,comp) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(query,val)
            
        except Exception as e:
            print("Insertion Issue",e)
        
        else:
        #save in database  use commit()
            con.commit()
            print("Record Insert Successfully")
        #close connection
            cursor.close()
            con.close()

    def view_students(self):
        query="SELECT * FROM student"
        #create object of class connection
        con=Connection()
        con=con.con
        #create the object of cursor cur cursor() inbuilt method of connect class)
        cursor=con.cursor()
        try:
            cursor.execute(query)            
            data=cursor.fetchall()  #fetchall() to display all records
        except Exception as e:
            print("Selection Issue",e)
        
        else:
        #close connection
            cursor.close()
            con.close()
        return data
    
    def update_student(self,rno,name,address,physics,chemistry,maths,english,comp):
        query="UPDATE student SET name='%s',address='%s',physics='%s',chemistry='%s',maths='%s',english='%s',comp='%s' where rno='%s'"
        args=(name,address,physics,chemistry,maths,english,comp,rno)
        #create object of class connection
        con=Connection()
        con=con.con
        #create the object of cursor cur cursor() inbuilt method of connect class)
        cursor=con.cursor()
        try:
            cursor.execute(query%args)     #run update query         
            
        except Exception as e:
            print("Updation Issue",e)
        
        else:
            con.commit()
        #close connection
            cursor.close()
            con.close()
    def delete_student(self,rno):
        query="DELETE FROM student where rno='%s'"  #fire DELETE query
        args=(rno)
        #create object of class connection
        con=Connection()
        con=con.con
        #create the object of cursor cur cursor() inbuilt method of connect class)
        cursor=con.cursor()
        try:
            cursor.execute(query%args)            
            
        except Exception as e:
            print("Updation Issue",e)
        
        else:
            con.commit()
        #close connection
            cursor.close()
            con.close()
        