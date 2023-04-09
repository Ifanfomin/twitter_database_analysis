import sqlite3
from matplotlib import pyplot as plt

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

colors = ['g', 'r', 'c', 'm', 'y', 'orange']

regions = ['Japan', 'China', 'RU', 'UA', 'USA', 'DE'] # , 'RU', 'USA', 'UA', 'Japan', 'China'

norm_regions = ['Япония (Japan)', 'Китай (China)', 'Россия (RU)', 'Украина (UA)', 'Америка (USA)', 'Германия (DE)']

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

    summ_registrations = sum(creatings)

    for i in range(len(creatings)):
        creatings[i] = (creatings[i] / summ_registrations) * 100

    print(hours)
    print(creatings)

    print(reg)

    plt.plot(hours, creatings, color=colors[regions.index(reg)], marker='o', linestyle='solid', label=norm_regions[regions.index(reg)])
plt.xlabel('час')
plt.ylabel('создано аккаунтов тысяч')
plt.legend()
plt.show()
# plt.savefig('accounts_creating_hours.png')