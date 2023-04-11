import sys
import argparse
import sqlite3
from matplotlib import pyplot as plt

def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--function', choices=['year', 'day', 'hour', 'years', 'days', 'hours'],
                        required=True, type=str, nargs=1, help='Варианты функций.')
    parser.add_argument('-Y', '--year', choices=['200'+str(i) for i in range(6, 10)]+['20'+str(i) for i in range(10, 21)],
                        type=str, help='По какому году нужен график?')
    parser.add_argument('-D', '--day', choices=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                        type=str, help='По какому дню недели нужен график?')
    parser.add_argument('-H', '--hour', choices=[str(i) for i in range(24)],
                        type=str, help='По какому часу нужен график?')
    parser.add_argument('-YS', '--years', choices=['200'+str(i) for i in range(6, 10)]+['20'+str(i) for i in range(10, 21)],
                        nargs='+', help='По каким годам нужен график?')
    parser.add_argument('-DS', '--days', choices=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                        nargs='+', help='По каким общим дням недели нужен график?')
    parser.add_argument('-HS', '--hours', choices=[str(i) for i in range(24)],
                        nargs='+', help='За какой промежуток общего дня нужен график?')
    return parser


def tw_year(year):
    conn = sqlite3.connect(token)
    cur = conn.cursor()

    query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + year + '%"'
    cur.execute(query)

    year_created = cur.fetchone()[0]
    cur.close()

    return year_created


def tw_day(day):
    conn = sqlite3.connect(token)
    cur = conn.cursor()

    query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + day + '%"'
    cur.execute(query)

    day_created = cur.fetchone()[0]
    cur.close()

    return day_created

def tw_hour(hour):
    conn = sqlite3.connect(token)
    cur = conn.cursor()

    if int(hour) < 10:
        query = 'SELECT count() FROM accounts WHERE created_at LIKE "%0' + hour + ':%:%"'
        cur.execute(query)
    else:
        query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + hour + ':%:%"'
        cur.execute(query)

    hour_created = cur.fetchone()[0]
    cur.close()

    return hour_created

def tw_years(years):
    year_creating = []
    for i in range(len(years)):
        year = years[i]
        creats = tw_year(year) / 5500000 * 100
        year_creating.append(creats)
    plot(x=years, y=year_creating, name='year')

def tw_days(days):
    day_creating = []
    for i in range(len(days)):
        day = days[i]
        creats = tw_day(day) / 5500000 * 100
        day_creating.append(creats)
    plot(x=days, y=day_creating, name='day')

def tw_hours(hours):
    hour_creating = []
    for i in range(len(hours)):
        hour = hours[i]
        creats = tw_hour(hour) / 5500000 * 100
        hour_creating.append(creats)
        # print(hour)
        # print(creats)
    plot(x=hours, y=hour_creating, name='hour')

def plot(x, y, name):
    if name == 'year':
        plt.plot(x, y, color='green', marker='o', linestyle='solid')
        plt.title('')
        plt.xlabel('год')
        plt.ylabel('создано аккаунтов в процентах')
        plt.show()
    if name == 'day':
        plt.plot(x, y, color='green', marker='o', linestyle='solid')
        plt.title('')
        plt.xlabel('день недели')
        plt.ylabel('создано аккаунтов в процентах')
        plt.show()
    if name == 'hour':
        plt.plot(x, y, color='green', marker='o', linestyle='solid')
        plt.title('')
        plt.xlabel('время суток')
        plt.ylabel('создано аккаунтов в процентах')
        plt.show()
    #plt.savefig('accounts_creating_days.png')

if __name__ == '__main__':
    token = r'G:\project\dbase\tw_db_5mln\twitter_5mln.db'
    parser = create_parser()
    func = parser.parse_args(sys.argv[1:])

    if func.function[0] == 'year':
        year = func.year
        acc_create = tw_year(year)
        print(acc_create)

    if func.function[0] == 'day':
        day = func.day
        acc_create = tw_day(day)
        print(acc_create)

    if func.function[0] == 'hour':
        hour = func.hour
        acc_create = tw_hour(hour)
        print(acc_create)

    if func.function[0] == 'years':
        years = func.years
        tw_years(years)

    if func.function[0] == 'days':
        days = func.days
        tw_days(days)

    if func.function[0] == 'hours':
        hours = func.hours
        tw_hours(hours)

    # print(func)
    # print(func.function[0])

