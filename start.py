import mysql.connector

mydb = mysql.connector.connect(
  host="i450.mysql.database.azure.com",
  user="i450",
  password="Team7Project"
)

print(mydb)
