import sqlite3
from matplotlib import pyplot as plt

#подключение
conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

#запрос
query = "SELECT created_at FROM accounts"

#отправляем запрос
cur.execute(query)

#получаем запрос
data = cur.fetchall()

#обрабатываем
years_ones = []
years_all = []
creatings = []
creates_year = 0
for i in range(len(data)):
    year = int(data[i][0][-4:])
    if not(year in years_ones):
        years_ones.append(year)
        years_ones.sort()
    years_all.append(year)
for i in range(len(years_ones)):
    creates_year = years_all.count(years_ones[i])
    creatings.append(creates_year)
del years_ones[-2:]
del creatings[-2:]
print(years_ones)
print(creatings)

#создаем линейную диаграмму(plt.plot(x, y, color, marker, linestyle), годы по OX, ВВП по OY
plt.plot(years_ones, creatings, color = 'green', marker = 'o', linestyle = 'solid')

#добавим диаграмме название plt.title('')
plt.title('Кол-во созданых аккаунтов в год')

#назовём оси
plt.xlabel('Годы')
plt.ylabel('Создано аккаунтов млн.')

#сохраним график
plt.savefig('accounts_creating_years.png')

#отключаемся от базы
cur.close()