import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = "Omonlumhen-7419"
DATABASE = "alx_book_store"

dbconnect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Omonlumhen-7419"
    
)

cursor=dbconnect.cursor()
try:
   if  cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store"):
    print(f"Database alx_book_store created successfully!")
except TypeError:
    print(f"Database alx_book_store was not created!")



cursor.close()
dbconnect.close()