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
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
print(f"DATABASE {DATABASE} IS READY")


cursor.close()
dbconnect.close()