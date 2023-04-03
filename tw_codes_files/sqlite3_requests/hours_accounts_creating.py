import sqlite3
from matplotlib import pyplot as plt

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

hours = []
creatings = []
hour_creats = 0
for i in range(10):
    query = 'SELECT count() FROM accounts WHERE created_at LIKE "%0' + str(i) + ':%:%"'
    cur.execute(query)
    hour_creats = cur.fetchone()[0] // 1000
    hours.append(i)
    creatings.append(hour_creats)
for i in range(10, 24):
    query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + str(i) + ':%:%"'
    cur.execute(query)
    hour_creats = cur.fetchone()[0] // 1000
    hours.append(i)
    creatings.append(hour_creats)

cur.close()

print(hours)
print(creatings)

plt.plot(hours, creatings, color='green', marker='o', linestyle='solid')
plt.title('Кол-во созданых аккаунтов в час')
plt.xlabel('Часы')
plt.ylabel('Создано аккаунтов тыс.')
plt.show()
# plt.savefig('accounts_creating_hours.png')