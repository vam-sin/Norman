import mysql.connector
import sys 

subject_param = sys.argv[1]
prof_param = sys.argv[2]

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
cursor.execute("SELECT * FROM handouts WHERE subject LIKE %s and professor like %s", ("%" + subject_param + "%", "%" + prof_param + "%", ))
records = cursor.fetchall()
print("Norman: You could try the following courses: ")
for row in records:
	print(row[0] + " offered by " + "Prof. " + row[1] + ".")