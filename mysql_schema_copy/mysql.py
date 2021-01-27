import mysql.connector
import os
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_DB = os.getenv("MYSQL_DB")
if not MYSQL_DB or not MYSQL_DB:
    print("please set MYSQL_USER and MYSQL_DB")
    exit(1)

cnx = mysql.connector.connect(user=MYSQL_USER, database=MYSQL_DB)

def mysql_get_cur():
    # Get two buffered cursors
    curA = cnx.cursor(buffered=True)
    return curA

def mysql_commit():
    cnx.commit()

def mysql_close():
    cnx.close()