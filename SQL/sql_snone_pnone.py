import mysql.connector

# mySQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mysql"
)

# None for prof and subject
sql_select_Query = "select * from handouts order by rand()"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
print("Norman: Try " + records[0][0] + " offered by " + "Prof. " + records[0][1] + ".")