import mysql.connector
import os
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_PASS = os.getenv("MYSQL_PASS")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_DB = os.getenv("MYSQL_DB")
if not MYSQL_DB or not MYSQL_DB:
    print("please set MYSQL_USER and MYSQL_DB")
    exit(1)

cnx = mysql.connector.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASS, database=MYSQL_DB)

def mysql_get_cur():
    # Get two buffered cursors
    curA = cnx.cursor(buffered=True)
    return curA

def mysql_commit():
    cnx.commit()

def mysql_close():
    cnx.close()