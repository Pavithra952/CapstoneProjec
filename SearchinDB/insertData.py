import mysql.connector
from SearchinDB.DBconnection import databaseConnection
from Capstonexception.MysqlException import MysqlError
import re
class InsertFileDB(databaseConnection):
    def __init__(self):
        self.conn=self.Connect("localhost","root","pavithra1969","myhcl",3306)
    def insert(self,files):
        self.files=files
        self.insertcur=self.connect.cursor()
        for f in self.files:
            sql="insert into fileinfo(filename) values(%s);"
            self.insertcur.execute(sql,(f,))
            self.connect.commit()
        print("files added succesfully")

