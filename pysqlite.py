import sqlite3

connection = sqlite3.connect('emp.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE employeeinfo (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER)")
cursor.execute("INSERT INTO employeeinfo (id, name, salary) VALUES (37295,'Abhinav', 20000)")
cursor.execute("SELECT * FROM employeeinfo")
rows = cursor.fetchall()
for row in rows:
    print(row)
