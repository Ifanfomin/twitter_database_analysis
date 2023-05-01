import sqlite3
from matplotlib import pyplot as plt

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

colors = ['g', 'r', 'c', 'm', 'y', 'orange', 'violet']

regions = ['Japan', 'China', 'UK', 'RU', 'UA', 'FR', 'DE'] # , 'RU', 'USA', 'UA', 'Japan', 'China'

norm_regions = ['Япония (Japan)', 'Китай (China)', 'Соед. Кор. (UK)', 'Россия (RU)', 'Украина (UA)', 'Франция (FR)', 'Германия (DE)']

years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

print(years)

for reg in regions:
    years_creats = []
    print(reg)
    for year in years:
        query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + year + '%" AND location LIKE "%' + reg + '%"'
        cur.execute(query)
        year_creats = cur.fetchone()[0]
        years_creats.append(year_creats)

    summ_registrations = sum(years_creats)

    for i in range(len(years_creats)):
        years_creats[i] = (years_creats[i] / summ_registrations) * 100

    print(years_creats)

    plt.plot(years, years_creats, color=colors[regions.index(reg)], marker='o', linestyle='solid',
             label=norm_regions[regions.index(reg)])
    
plt.locator_params(axis='x', nbins=len(years) + 5)
plt.title('')
plt.xlabel('год')
plt.ylabel('создано аккаунтов в процентах')
plt.legend()
plt.show()

# [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
# Japan
# [0.0, 1.2761780104712042, 1.5052356020942408, 9.653141361256544, 13.1217277486911, 15.608638743455497, 12.205497382198953, 9.325916230366492, 5.6609947643979055, 7.951570680628272, 12.30366492146597, 7.75523560209424, 1.2761780104712042, 1.0143979057591623, 1.3416230366492148]
# China
# [0.0, 0.17917293771948686, 0.20784060775460472, 1.3688812441768794, 4.593994123127643, 12.491937217802624, 15.530710241525119, 11.968752239661722, 9.79717623450154, 8.012613774815453, 20.44004873503906, 15.007525263384219, 0.22934136028094315, 0.06450225757901526, 0.10750376263169212]
# UK
# [0.03126367785906334, 0.5502407303195148, 1.869567935971988, 16.350903520290128, 14.093665978865754, 23.541549427874696, 17.332583005064716, 9.566685424873382, 5.883824173075721, 3.8266741699493525, 3.3264553242043395, 2.263490276996186, 0.5064715813168261, 0.43143875445507407, 0.4251860188832614]
# RU
# [0.010126240464456896, 0.2227772902180517, 0.8978599878485115, 8.509417403631945, 15.017214608789578, 22.5376358603929, 16.228988051036254, 10.22075204212516, 7.169378248835483, 6.315398636332952, 6.791331938162425, 4.428542496455816, 0.745966380881658, 0.4219266860190373, 0.4826841288057787]
# UA
# [0.006007268795242243, 0.13516354789295046, 0.5466614603670441, 7.09758808157871, 16.159553059201635, 24.20929324482624, 16.6100982188448, 9.948037124921155, 6.202505031087616, 4.998047637641546, 7.6472531763433755, 5.448592797284714, 0.43252335325744146, 0.2943561709668699, 0.2643198269906587]
# FR
# [0.03269527999048864, 0.6004042325526097, 2.3362263702294612, 12.138865771014148, 10.569492331470693, 19.186184758054928, 16.668648198787302, 9.921531328022827, 6.5420282962786835, 5.9683747473546545, 7.2642967542503865, 5.255023183925812, 1.483176792295803, 0.9808583997146594, 1.0521935560575437]
# DE
# [0.00970716712506067, 0.25670064175160434, 1.1907458340074422, 11.423178557946395, 13.349511945208434, 21.84975462438656, 16.1764547268511, 9.695302809685595, 6.978374588793615, 5.683007064660519, 6.079922342662999, 4.457746858652861, 1.1551528878822197, 0.8197163350051231, 0.8747236153804671]
