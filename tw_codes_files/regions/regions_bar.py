import sqlite3
import matplotlib.pyplot as plt

def sorting(regions_accounts):
    sorted_values = sorted(regions_accounts.values())
    sorted_dict = {}
    for i in sorted_values:
        for k in regions_accounts.keys():
            if regions_accounts[k] == i:
                sorted_dict[k] = regions_accounts[k]
                break
    return sorted_dict

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_5mln\twitter_5mln.db')    # G:\project\dbase\tw_db_5mln\twitter_5mln.db
cur = conn.cursor()

regions_accounts = {'DE': 0, 'RU': 0, 'USA': 0, 'UA': 0, 'Japan': 0, 'China': 0}

for r in regions_accounts:
    query = 'SELECT count() FROM accounts WHERE location LIKE "%' + r + '%"'
    cur.execute(query)
    data = cur.fetchone()[0]
    regions_accounts[r] = data // 1000

sorted_regions_accounts = sorting(regions_accounts)

index = ['Япония (Japan)', 'Китай (China)', 'Россия (RU)', 'Украина (UA)', 'Америка (USA)', 'Германия (DE)'] #  sorted_regions_accounts.keys()
values = sorted_regions_accounts.values()

plt.bar(index, values)
plt.ylabel('создано аккаунтов тысяч')
plt.show()

print(sorted_regions_accounts)
