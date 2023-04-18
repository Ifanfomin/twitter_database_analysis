import sqlite3
from matplotlib import pyplot as plt

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

colors = ['g', 'r', 'c', 'm', 'y', 'orange', 'violet']

regions = ['Japan', 'China', 'UK', 'RU', 'UA', 'FR', 'DE'] # , 'RU', 'USA', 'UA', 'Japan', 'China'

norm_regions = ['Япония (Japan)', 'Китай (China)', 'Соед. Кор. (UK)', 'Россия (RU)', 'Украина (UA)', 'Франция (FR)', 'Германия (DE)']

years = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
years_creats =[]

for reg in regions:
    for year in years:
        query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + str(i) + '%" AND location LIKE "%' + reg + '%"'
        cur.execute(query)
        year_creats = cur.fetchone()[0]
        years_creats.append(year_creats)

    summ_registrations = sum(years_creats)

    for i in range(len(years_creats)):
        years_creats[i] = (years_creats[i] / summ_registrations) * 100
    plt.plot(years, years_creats, color=colors[regions.index(reg)], marker='o', linestyle='solid',
             label=norm_regions[regions.index(reg)])
    
plt.locator_params(axis='x', nbins=len(years) + 5)
plt.title('')
plt.xlabel('год')
plt.ylabel('создано аккаунтов в процентах')
plt.legend()
plt.show()
