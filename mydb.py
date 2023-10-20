import mysql.connector

database = mysql.connector.connect(
	
	)

cursorobject = database.cursor()
cursorobject.execute("CREATE DATABASE data_base")

print("all fine")
