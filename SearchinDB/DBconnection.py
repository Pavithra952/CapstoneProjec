import mysql.connector
from Capstonexception.MysqlException import MysqlError
class databaseConnection():
    def Connect(self,host,username,password,database,port):
            self.hostname=host
            self.username=username
            self.password=password
            self.database=database
            self.portnum=port
            self.connect=mysql.connector.Connect(host=self.hostname,username=self.username,password=self.password,database=self.database,port=self.portnum)
            self.cur=self.connect.cursor()



