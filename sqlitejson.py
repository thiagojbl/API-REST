import json
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

# Insert values
c.execute('''insert into data values(?)''', (json.dumps({'test': 'test2'}),))
conn.commit()

# Select those values, get them to be json
c.execute('select * from data')
data = c.fetchall()

# print statement will print:
# [(u'{"test": "test2"}',)]

# To load the JSON for python use
for item in data:
    print(json.loads(item[0]))

# print statement will print:
# {u'test': u'test2'}
