import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'gargi123'
	)

cursorobject = database.cursor()
cursorobject.execute("CREATE DATABASE data_base")

print("all fine")