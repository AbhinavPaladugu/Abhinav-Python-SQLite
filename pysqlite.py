import sqlite3

connection = sqlite3.connect('emp.db')
cursor = connection.cursor()

#cursor.execute("CREATE TABLE empinfo (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER)")

#cursor.execute("INSERT INTO empinfo (id, name, salary) VALUES (37195,'Abhinav', 20000)")
#cursor.execute("INSERT INTO empinfo (id, name, salary) VALUES (37196,'Krishna', 30000)")
#cursor.execute("INSERT INTO empinfo (id, name, salary) VALUES (37197,'Jahanav', 30000)")
#connection.commit()
cursor.execute("INSERT INTO empinfo (id,name, salary) VALUES (?, ?, ?)", (37198,'Venkata', 40000))
connection.commit()
cursor.execute("SELECT * FROM empinfo")
rows = cursor.fetchall()
for row in rows:
    print(row)
# try:
#     cursor.execute("SELECT * FROM Abhinav")
# except sqlite3.OperationalError as e:
#     print(f"An error occurred: {e}")
