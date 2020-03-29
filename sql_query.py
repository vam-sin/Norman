import mysql.connector

# mySQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mysql"
)

sql_select_Query = "select * from handouts"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
print("Total number of rows in Laptop is: ", cursor.rowcount)

for row in records:
    print(row)