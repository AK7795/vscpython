import sqlite3

con = sqlite3.connect('st.db')

cursor = con.cursor()
sql_query = '''CREATE TABLE stud(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               marks INTEGER NOT NULL)'''

cursor.execute(sql_query)

print('table is created successfully')

i1 = '''INSERT INTO stud
      VALUES (1011,'TOM',91)'''

cursor.execute(i1)

print("a record is inserted")

con.commit()
con.close()
