import sqlite3
from matplotlib import pyplot as plt

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

colors = ['g', 'r', 'c', 'm', 'y', 'orange']

regions = ['DE', 'RU', 'USA', 'UA', 'Japan', 'China']

for reg in regions:
    hours = []
    creatings = []
    hour_creats = 0
    for i in range(10):
        query = 'SELECT count() FROM accounts WHERE created_at LIKE "%0' + str(i) + ':%:%" AND location LIKE "%' + reg +'%"'
        cur.execute(query)
        hour_creats = cur.fetchone()[0]
        hours.append(i)
        creatings.append(hour_creats)
        print(i, hour_creats)
    for i in range(10, 24):
        query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + str(i) + ':%:%" AND location LIKE "%' + reg + '%"'
        cur.execute(query)
        hour_creats = cur.fetchone()[0]
        hours.append(i)
        creatings.append(hour_creats)
        print(i, hour_creats)

    print(hours)
    print(creatings)

    print(reg)

    plt.plot(hours, creatings, color=colors[regions.index(reg)], marker='o', linestyle='solid')
plt.xlabel('час')
plt.ylabel('создано аккаунтов тысяч')
plt.show()
# plt.savefig('accounts_creating_hours.png')