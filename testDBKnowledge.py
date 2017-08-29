# NOTE: Use these templates when executing a certain type of query

# UPDATE https://www.tutorialspoint.com/sqlite/sqlite_update_query.htm


import sqlite3

# Create a db
conn = sqlite3.connect("testDB.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS new_table (col1 text, col2 text, col3 text)""")
c.execute("""INSERT INTO new_table ("col1", "col2", "col3") VALUES (1, 2, 3)""")
c.execute("""UPDATE new_table
SET col1 = "Blah blee blah", col2 = "Boosh....", col3 = "Bop!"
WHERE col1 == 1;""")

# Select all the elements and print them
c.execute("""SELECT * FROM new_table""")
print(c.fetchall())
for row in c:
    print(row)

conn.commit()
conn.close()

# Copyright (c) 2017 Aaron Bell. All Rights Reserved.
