import logging
logging.basicConfig(filename='..//logger//capstone.log',level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
from SearchfilesinDrives.Searchfiles import SearchFilesdrives
from Capstonexception.MysqlException import MysqlError
from SearchinDB.DBconnection import databaseConnection
from SearchinDB.searchfilepath import SearchFile
from SearchinDB.insertData import InsertFileDB
import mysql.connector
import openpyxl as xl
import time
def userdata():
    dir=input("enter the drive like c:// d:// \n")
    filename=input("enter the file name with extension like demo.txt \n")
    logging.info(f"drive name{dir} file name {filename}")
    dbobj=SearchFile()
    logging.info(f"class used{SearchFile.__name__}")
    wb=xl.load_workbook("C://testdata//testfiles.xlsx")
    ws=wb.active

    try:
        dbobj.Connect("localhost",'root','pavithra1969','myhcl',3306)
        logging.info("myhcl database is connected")
        result=dbobj.Search(filename)
    except mysql.connector.Error as err:
        logging.exception(err, exc_info=True)
        raise MysqlError(f'{err.msg}',err.errno)
    finally:
        dbobj.connect.close()

    if len(result)==0:
        print("Not Found in Database")
        print("Now searching in Drives...")
        logging.info("Not Found in database")
        logging.info("Now Searching in Drives")
        start_time=time.time()
        obj=SearchFilesdrives()
        logging.info(f' Searching in drive {SearchFilesdrives.__name__} is used')
        files=obj.searchfiles(dir,filename)
        ws.cell(row=1,column=1).value=str(files)
        wb.save("C://testdata//testfiles.xlsx")
        wb.close()
        inserobj=InsertFileDB()
        inserobj.insert(files)
        logging.info(f'files found {files}')
        print(obj.searchfiles(dir,filename))
        print(files)
        obj.start()
        #obj.join()
        end_time=time.time()
        logging.info(f'time taken{end_time-start_time}')
        logging.info("Ending")
        print(end_time-start_time)
    else:
        print("Found in database")
        print(result)
userdata()