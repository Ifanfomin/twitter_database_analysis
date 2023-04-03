import sqlite3

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_2mln\twitter_2mln.db')
cur = conn.cursor()

query = "SELECT count() FROM accounts WHERE location LIKE '%'"
cur.execute(query)
len_all = cur.fetchone()[0]

query = 'SELECT location FROM accounts'
cur.execute(query)

data = cur.fetchone()[0]
regions = []
for i in range(len_all):
    finds = data.find(',')
    if data.find(',') != -1 and len(data[finds + 2:]) == 2 or len(data[finds + 2:]) == 3:
        if not(data[finds + 2:] in regions):
            regions.append(data[data.find(',') + 2:])
    data = cur.fetchone()[0]

print(regions)

cur.close()