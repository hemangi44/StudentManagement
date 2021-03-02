import pymysql
class Connection:   #User defined class
    def __init__(self):			#constructor
        #to establish connection between python and mysql
        self.servername="localhost"
        self.username="hemangi"
        self.password="bipin1993"
        self.dbname="school_management"         #database
        try:
            self.con=pymysql.connect(self.servername,self.username,self.password,self.dbname)
        except Exception as e:
            print("Connection Error",e)
        else:
            print("Connection Successful")

    