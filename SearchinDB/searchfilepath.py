from Capstonexception.MysqlException import MysqlError
from SearchinDB.DBconnection import databaseConnection
import mysql.connector
class SearchFile(databaseConnection):
    def Search(self,filename):
        print("Searching in Database....")
        self.filename=filename

        sql="""select * from fileinfo where filename like '%{0}'""".format(filename)
        self.cur.execute(sql)
        data=self.cur.fetchall()
        return data

