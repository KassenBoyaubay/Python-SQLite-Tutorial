import sqlite3

conn = sqlite3.connect('../emaildb.sqlite')
c = conn.cursor()

c.execute('''
    DROP TABLE IF EXISTS Counts
''')

c.execute('''
    CREATE TABLE Counts (email TEXT, count INTEGER)
''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    c.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = c.fetchone()
    if row is None:
        c.execute('''
            INSERT INTO Counts (email, count) VALUES (?, 1)
        ''', (email,))
    else:
        c.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in c.execute(sqlstr):
    print(str(row[0]), row[1])

c.close()
