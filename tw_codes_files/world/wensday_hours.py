import sqlite3
from matplotlib import pyplot as plt

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

hours = []
creatings = []
hour_creats = 0
for i in range(10):
    query = 'SELECT count() FROM accounts WHERE created_at LIKE "%0' + str(i) + ':%:%" AND created_at LIKE "Wed%"'
    cur.execute(query)
    hour_creats = cur.fetchone()[0]
    hours.append(i)
    creatings.append(hour_creats)
    print(i, hour_creats)
for i in range(10, 24):
    query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + str(i) + ':%:%" AND created_at LIKE "Wed%"'
    cur.execute(query)
    hour_creats = cur.fetchone()[0]
    hours.append(i)
    creatings.append(hour_creats)
    print(i, hour_creats)

cur.close()

summ_creatings = sum(creatings)
for i in range(len(creatings)):
    creatings[i] = creatings[i] / summ_creatings * 100

print(hours)
print(creatings)

plt.plot(hours, creatings, color='green', marker='o', linestyle='solid')
plt.title('Регистрации за все среды')
plt.xlabel('время суток')
plt.ylabel('создано аккаунтов в процентах')
plt.show()
# plt.savefig('accounts_creating_hours.png')