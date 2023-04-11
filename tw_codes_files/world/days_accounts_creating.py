import sqlite3
from matplotlib import pyplot as plt

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_2mln\twitter_2mln.db')
cur = conn.cursor()

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
day_creating = []
for i in range(7):
    query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + days[i] + '%"'
    cur.execute(query)
    day_creating.append(cur.fetchone()[0] // 1000)

print(days)
print(day_creating)

plt.plot(days, day_creating, color = 'green', marker = 'o', linestyle = 'solid')
plt.title('Кол-во созданых аккаунтов в день')
plt.xlabel('Дни')
plt.ylabel('Создано аккаунтов тыс.')
plt.savefig('accounts_creating_days.png')

cur.close()