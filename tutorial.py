# https://www.sqlitetutorial.net/
# ----------------------------------------------------------------------------------------------------------------------------------------

import sqlite3                          # SQLite

conn = sqlite3.connect('customer.db')   # Create .db file in same directory

c = conn.cursor()                       # Create a cursor

# Create a table w/ 'dog string', which is """ ... """  allowing to write in multiple lines
#
# 5 datatypes in SQLite: null, int, real, text, blob
# null - exist or not, if not -> null
# real - decimal
# blob - image, mp3, etc. it's just a blob
#
c.execute("""CREATE TABLE IF NOT EXISTS customers (
    first_name text,
    last_name text,
    email text
)""")

# Insert into database values
#
# c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@code.com')")

# Insert into database multiple values
#
# many_customers = [
#     ('Wes', 'Brown', 'wes@br.com'),
#     ('User1', 'UserLast', 'user@com.com'),
#     ('Dan', 'Pas', 'dan@pas')
# ]
#
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Query the Database
#
c.execute("SELECT * FROM customers")
# print(c.fetchone())                   # fetch/get first thing from db
# print(c.fetchmany(3))                 # fetch/get first 3 values
# print(c.fetchall())                   # fetch/get all values as python list [('first_name', 'last_name', 'email'), (...), ...]
#
# print(c.fetchone()[0])                # get first_name from 1st tuple 'John'
#
# format data
items = c.fetchall()
print('Query the Database')
for item in items:
    print(item[0] + ' ' + item[1] + '\t' + item[2])
#
# OUTPUT:
# John Elder    john@code.com
# ...

# Primary Key / unique row id   (SQLite automatically creates it, it is rowid)
#
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
print('\nPrimary Key / unique row id')
for item in items:
    print(item)
#
# OUTPUT:
# (1, 'John', 'Elder', 'john@code.com')
# ...

# WHERE clause
#
# LIKE 'Use%' means those that start with Use... and whatever, can be written as '%abc' or whatever
#
c.execute(
    "SELECT rowid, * FROM customers WHERE first_name = 'Wes' OR first_name LIKE 'Use%'")
items = c.fetchall()
print('\nWHERE clause')
for item in items:
    print(item)
#
# OUTPUT:
# (3, 'Wes', 'Brown', 'wes@br.com')
# (4, 'User1', 'UserLast', 'user@com.com')

# Update Records
c.execute("""
    UPDATE customers SET first_name = 'DanUpdated'
    WHERE rowid = 5
""")
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
print('\nUpdate Records')
for item in items:
    print(item)

# Delete Records
c.execute("INSERT INTO customers VALUES ('Name6', 'LastN6', 'john@code.com')")
c.execute("DELETE from customers WHERE rowid = 6")

# Order by
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
items = c.fetchall()
print('\nOrder By (descending)')
for item in items:
    print(item)

c.execute("SELECT rowid, * FROM customers ORDER BY last_name")
items = c.fetchall()
print('\nOrder By (last_name)')
for item in items:
    print(item)

# LIMIT
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")
items = c.fetchall()
print('\nLIMIT (2 results)')
for item in items:
    print(item)

# Delete (Drop) Table & Backup
#
# c.execute("DROP TABLE customers")
# conn.commit()

conn.commit()                           # push into database

conn.close()                            # close the connection w/ database

conn = sqlite3.connect('emaildb.sqlite')
c = conn.cursor() 

c.execute("SELECT * FROM Counts")
items = c.fetchall()
print('\nQuery the Database')
for item in items:
    print(item[0] + ' ' + str(item[1]))

# Functions
c.execute("SELECT MAX(count) FROM Counts")
items = c.fetchall()
print('\nMax')
print(item[0] + ' ' + str(item[1]))

c.execute("SELECT COUNT(count) FROM Counts WHERE count > 3")
item = c.fetchone()
print('\nNumber of count > 3 ')
print(item)

c.execute("SELECT AVG(count) FROM Counts")
item = c.fetchone()
print('\nAverage of count')
print(item)

c.execute("SELECT SUM(count) FROM Counts")
item = c.fetchone()
print('\nSum of count')
print(item)

conn.commit()                          
conn.close() 