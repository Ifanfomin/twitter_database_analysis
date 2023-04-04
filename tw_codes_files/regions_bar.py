import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect(r'D:\project\dbase\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

regions_accounts = {'DE': 0, 'RU': 0, 'USA': 0, 'LV': 0, 'UA': 0, 'Tokyo': 0, 'Japan': 0, 'China': 0}

for r in regions_accounts:
    query = 'SELECT count() FROM accounts WHERE location LIKE "%' + r + '%"'
    cur.execute(query)
    data = cur.fetchone()[0]
    regions_accounts[r] = data

sorted_values = sorted(regions_accounts.values())
sorted_regions_accounts ={}
for i in sorted_values:
    for k in regions_accounts.keys():
        if regions_accounts[k] == i:
            sorted_regions_accounts[k] = regions_accounts[k]
            break
index = sorted_regions_accounts.keys()
values = sorted_regions_accounts.values()

plt.bar(index, values)
plt.show()

print(sorted_regions_accounts)