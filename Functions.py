import mysql.connector
import pandas as pd
from itertools import chain
connection = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="",
                                     database="base_onix")


def Default(root, path):
    try:
        obj = root.find(path).text
    except:
        obj = None
    finally:
        return obj

def Xml_to_Mysql(list,table,connection,tuple):
    try:
        cursor=connection.cursor()
        columns=','.join(tuple)
        dt=pd.DataFrame(list)
        dt.to_csv('C:/Users/user/Desktop/creation_csv/{}.csv'.format(table),header=False,index=False,sep='¤',line_terminator='α')
        query='''LOAD DATA INFILE "C:/Users/user/Desktop/creation_csv/{}.csv" INTO table {}
         FIELDS TERMINATED BY "¤" LINES TERMINATED BY "α" ({})'''.format(table,table,columns)
        cursor.execute(query)
        connection.commit()
    except:
        print('query error',query)
    finally:
        print('Query executed')
