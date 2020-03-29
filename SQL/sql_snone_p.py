import mysql.connector
import sys 

prof_param = sys.argv[1]

# mySQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mysql"
)

# None for prof and subject
# sql_select_Query = "select * from handouts where subject like ('%s%') "
cursor = mydb.cursor()
cursor.execute("SELECT * FROM handouts WHERE professor LIKE %s", ("%" + prof_param + "%",))
records = cursor.fetchall()
if(len(records) == 0):
	print("Norman: I couldn't find any courses with your preferences. Sorry.")
else:
	print("Norman: You could try the following courses: ")
	for row in records:
		print(row[0] + " offered by " + "Prof. " + row[1] + ".")