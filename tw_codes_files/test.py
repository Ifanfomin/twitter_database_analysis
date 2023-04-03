import sqlite3

conn = sqlite3.connect(r'G:\project\dbase\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

query = 'SELECT * FROM accounts'

cur.execute(query)

data = cur.fetchone()

reg_accounts = {}

while :
    data = cur.fetchone()
    if data == None:
        break

    if data[2].count('DE') > 0:
        reg_accounts[DE]


# [print(cur.fetchone()) for _ in range(1)]