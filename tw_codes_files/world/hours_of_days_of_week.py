import sqlite3
from matplotlib import pyplot as plt

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

rus_week_days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
colors = ['g', 'r', 'c', 'm', 'y', 'orange', 'violet']
hour_creats = 0
for w_d in week_days:
    hours = []
    creatings = []
    for i in range(10):
        query = 'SELECT count() FROM accounts WHERE created_at LIKE "%0' + str(i) + ':%:%" AND created_at LIKE "' + w_d + '%"'
        cur.execute(query)
        hour_creats = cur.fetchone()[0]
        hours.append(i)
        creatings.append(hour_creats)
        print(i, hour_creats)
    for i in range(10, 24):
        query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + str(i) + ':%:%" AND created_at LIKE "' + w_d + '%"'
        cur.execute(query)
        hour_creats = cur.fetchone()[0]
        hours.append(i)
        creatings.append(hour_creats)
        print(i, hour_creats)

    summ_creatings = sum(creatings)
    for i in range(len(creatings)):
        creatings[i] = creatings[i] / summ_creatings * 100

    print('day of week = ' + w_d)
    print(creatings)
    print(hours)

    plt.plot(hours, creatings, color=colors[week_days.index(w_d)], marker='o', linestyle='solid',
             label=rus_week_days[week_days.index(w_d)] + '(' + w_d + ')')

cur.close()


plt.title('')
plt.xlabel('время суток')
plt.ylabel('создано аккаунтов в процентах')
plt.legend()
plt.show()
# plt.savefig('accounts_creating_hours.png')

# [[4.347487896462217, 4.521497815153039, 4.519239575400744, 4.249505382765365, 3.7028859049456706, 3.291133523443665, 2.9488847432067757, 2.781900459300874, 2.7481523207804477, 2.7958262711067006, 2.894059700331585, 3.249857919082251, 3.6626139626963887, 4.13257874670203, 4.647708325753594, 4.906778608447573, 5.165723433377536, 5.201227980594194, 5.232843337126339, 5.315394545849167, 5.2327178793623235, 5.106883742053818, 4.79047926120432, 4.554618664853384],
#                  [4.476726839648578, 4.659686896657157, 4.610741382753919, 4.199451119828974, 3.744763323166146,
#                   3.246801281213553, 2.9530049093460042, 2.806784809876884, 2.7278802030807316, 2.8118396362497626,
#                   2.9288403735146824, 3.2406368588076035, 3.721585094919776, 4.221519752042273, 4.626768881009387,
#                   4.946702403878161, 5.044470143236519, 5.181936762889191, 5.155799611887965, 5.20511499113556,
#                   5.226690469556383, 5.020182318957078, 4.733290100184193, 4.508781836159516],
#                  [4.527177029272094, 4.7429319140803035, 4.581452676046674, 4.229824896716997, 3.7267643873345393,
#                   3.2480850375641386, 2.9724186600408724, 2.7903563324855063, 2.7228486995898087, 2.7746739785641825,
#                   2.9272093741270564, 3.2701383477659993, 3.7594767974672996, 4.261312122949655, 4.693066929346095,
#                   4.963955089658958, 5.035628347815007, 5.153491039004955, 5.141851791953973, 5.216833046640301,
#                   5.125311809302576, 5.047390113256, 4.676159391524668, 4.411642187492343],
#                  [4.4535080335979975, 4.605987796623716, 4.595123145204193, 4.222103446467241, 3.723952934829575,
#                   3.2583963774504787, 2.9750412731872893, 2.8375472362574645, 2.7902173180046006, 2.8140695987072313,
#                   2.926587425477233, 3.237291479865428, 3.7331941325887095, 4.241335128290304, 4.7254989622384675,
#                   4.972139037566717, 5.115002959680904, 5.142351909805909, 5.107759858734555, 5.188183255449184,
#                   5.20716517517065, 5.045693976487396, 4.655940216943361, 4.425909321371393],
#                  [4.547618739568643, 4.6177433336352225, 4.542443492774062, 4.261039448318692, 3.7273421226274728,
#                   3.276707507989287, 3.0311420475863944, 2.8830006080914985, 2.808088910739931, 2.8205095030469267,
#                   2.9766725750734238, 3.330530074652935, 3.812474932398339, 4.317190876039901, 4.7480301716888125,
#                   5.068766091783002, 5.115343312934235, 5.138243780000259, 5.095547993944962, 5.0977474738326585,
#                   5.043019238979959, 4.858780453092857, 4.582810417771797, 4.29920689342873],
#                  [4.275465699262218, 4.314324922892974, 4.313102080191307, 4.183209010991997, 3.846519653799644,
#                   3.4840147284609846, 3.19501623663365, 3.0399869563445154, 2.966752265655783, 2.9213712142828028,
#                   3.050313183603038, 3.318523349502031, 3.7188005271810756, 4.216497506759603, 4.7012867022649765,
#                   4.948844413646924, 5.149934102365521, 5.236212448538703, 5.197489096319243, 5.161211429503118,
#                   5.028872674900474, 4.867593309691707, 4.562426119920108, 4.3022323672875995],
#                  [4.053322263335556, 4.075409037748426, 4.16615108684227, 4.068091130563438, 3.821145026284592,
#                   3.4422104869601546, 3.1448373495338493, 2.97413053283678, 2.934746886895757, 2.944592798381013,
#                   3.0266864117107803, 3.2236046414158954, 3.592826322112986, 4.032299911785955, 4.563047761984404,
#                   4.943046724172112, 5.215272871453642, 5.287786679013972, 5.436805879871897, 5.436140615582352,
#                   5.306813237694939, 5.074902106359794, 4.734819001544744, 4.5013112359146925]
#                  ]