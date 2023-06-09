# twitter_database_analysis
## 1. Создание базы данных

### 1.1. Что такое база данных

Для создания базы сначала разберёмся - что это такое? База данных – совокупность данных, хранящихся и упорядоченных в соответствии с определённой структурой. Структура, в свою очередь, определяет то, каким образом данные будут располагаться и как к ним будет предоставляться доступ. Проще говоря — обычная таблица с возможностью настройки условий на столбцы.

### 1.2. Создание и настройка пустой базы

Для создания пустой базы я использовал команду CREATE TABLE. Таблица должна будет содержать информацию об аккаунтах пользователей. Столбцы будут содержать соответствующую информацию: идентификатор, имя, местоположение, описание, количество подписчиков, количество друзей, списки, дата создания, количество подписок, количество статусов, почта, телефон, ссылка на сайт аккаунта.

```ruby
CREATE TABLE "accounts" (
	"twitter_id"	TEXT,
	"name"	        TEXT,
	"location"	TEXT,
	"description"	TEXT,
	"followers"	INTEGER,
	"friends"	INTEGER,
	"listed"	INTEGER,
	"created_at"	TEXT,
	"favourites"	INTEGER,
	"statuses"	INTEGER,
	"email"	        TEXT,
	"phone"	        TEXT,
	"url"	        TEXT
);
```

## 2. Заполнение созданный базы

### 2.1. Что такое СУБД и SQL

Файл, найденный в интернете, имеет расширение json, т.е текстовый формат обмена данными, основанный на JavaScript. Файл был плохо структурирован, что мешало анализировать данные. Для выхода из этой ситуации создадим базу данных в удобном для анализа расширении db (data base) и наполним её данными из найденного файла, параллельно структурируя. Всё это происходит с помощью системы управления базой данных (СУБД), она позволяет создавать, удалять, изменять и делать любые манипуляции с данными базы. Для отправления запросов в СУБД будет использоваться отдельный язык - SQL, язык запросов, предоставляющий возможность манипулировать информацией в базе данных.

Первые строки json файла. (Рис. 1)

![image](https://user-images.githubusercontent.com/129762316/230782387-d9265d60-bc1f-4548-9723-e0e75b6d0021.png)

### 2.2. Обход ограничений ресурсов компьютера

Подключившись к пустой базе открываем найденный файл в оперативной памяти и начинаем перенос в ранее открытое хранилище, но продлевается данный процесс не долго, файл, выгруженный в память, весит так много, что занимает все ресурсы системы и тормозит весь компьютер вплоть до системной остановки процесса или отключения компьютера. Для избежания данной проблемы выгружаем только одну строку исходного файла, достаём из неё нужные данные, сохраняем в нашу базу и освобождаем память для нового цикла, пока не будут перенесены все строки найденного в интернете файла.
```ruby
with open(r'D:\projects\base\twitter.json') as tw_file:
    tw_str = 1
	while tw_str:
            tw = json.loads(tw_str)
            tw_str = tw_file.readline()
```
### 2.3. Решение проблемных мест исходного файла

В процессе заполнения новой базы оказалось, что в исходном файле иногда столбцы с email отсутствовали, а вместо них был столбец с номером телефона. Выходом стала обычная проверка на наличие или отсутствие того или иного столбца перед отправлением запроса. Также находились строки, заполненные иероглифами в несколько десятков символов. Данных строк было четыре из пяти миллионов, так что самым простым решением был их пропуск.

Арабские символы были представлены на кодировке Unicode, включающей в себя знаки почти всех письменных языков мира. (Рис. 2)

![image](https://user-images.githubusercontent.com/129762316/230782712-40969742-66bb-4c2d-ac5f-32970e4dbe98.png)

## 3.  Поиск информации внутри созданной базы

### 3.1. Количество регистраций за год, день или час

Итак, у меня есть систематизированная база данных, как теперь на достать из неё информацию? Изначально я хотел отправлять запросы в нашу базу построчно, но ещё немного изучив виды запросов SQL нашёл функцию, позволяющую делать запрос на поиск по всей базе, при том, что он не станет сильно использовать ресурсы компьютера. Поиск производился только по одному столбцу, который содержит в себе полную дату регистрации пользователя, и считает только те строки, которые содержали нужный год, день недели или час дня. Теперь я мог одним запросом найти количество пользователей в нужную мне дату.
```ruby
query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + year + '%"'
```
### 3.2. Количество регистраций за нужный промежуток

Чтобы получить ещё больше информации логичнее всего было рассматривать нужный нам промежуток и строить график по частоте регистраций. Простым способом будет сделать цикл, перебирающий выбранные года, дни недели или время суток, и отправляющий по одному запросу. Теперь мы просто сохраняем ответы и строим по ним график с помощью библиотеки matplotlib, она требует на вход данные точек и названия осей.
```ruby
def tw_years(years):
    year_creating = []
    for i in range(len(years)):
        year = years[i]
        creats = tw_year(year) / 5500000 * 100
        year_creating.append(creats)
    plot(x=years, y=year_creating, name='year')
```
```ruby
def plot(x, y, name):
    if name == 'year':
        plt.plot(x, y, color='green', marker='o', linestyle='solid')
        plt.title('')
        plt.xlabel('год')
        plt.ylabel('создано аккаунтов в процентах')
        plt.show()
```
### 3.3. Количество регистраций в нужных регионах
Первым делом нужно узнать количество аккаунтов в выбранных странах. Удобнее всего это реализовать через гистограмму, где столбцы - страны, а их высота - количество регистраций. Для этого производим поиск по столбцу местоположения регистрации для каждого региона, сортируем по количесту регистраций и с помощью библиотеки matplotlib строим столбчатый график.
```ruby
for r in regions_accounts:
    query = 'SELECT count() FROM accounts WHERE location LIKE "%' + r + '%"'
    cur.execute(query)
    data = cur.fetchone()[0]
    regions_accounts[r] = data // 1000
```
```ruby
index = sorted_regions_accounts.keys()
values = sorted_regions_accounts.values()
plt.bar(index, values)
plt.ylabel('создано аккаунтов тысяч')
plt.show()
```
### 3.4. Количество регистраций за нужные время суток и года по выбранным регионам
Запросы на количество регистраций за нужные время суток и года у нас есть, остаётся только добавить условие на выборку регионов. Добавляем в запрос новое условие на проверку региона с помощью логической операции `AND` и сохраняем полученную информацию. Далее строим на одной координатной плоскости графики регистраций по странам и выводим на экран.
```ruby
query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + year + '%" ' \
                                         'AND location LIKE "%' + reg + '%"'
```
```ruby
plt.plot(years, years_creats, color=colors[regions.index(reg)], marker='o', linestyle='solid',
         label=norm_regions[regions.index(reg)])
plt.locator_params(axis='x', nbins=len(years) + 5)
plt.title('')
plt.xlabel('год')
plt.ylabel('создано аккаунтов в процентах')
plt.legend()
plt.show()
```
## 4. Простая реализация удобного способа отправления запросов
### 4.1. Что такое argparse

Наша программа успешно выполняет свою работу, но для её использования нам требуется изменять файл либо использовать отдельно файлы для нужной функции. Также требуется запуск файла из специальной среды. Для облегчения данного процесса нужно реализовать простой и удобный способ отправки запросов с возможностью выбора функции. В этом мне помогла библиотека argparse, представляющая из себя набор функций для принятия запросов из командной строки консоли.

Пример запроса из командной строки. (Рис. 3)

![image](https://user-images.githubusercontent.com/129762316/230784653-97fb04f6-c5cd-40c6-980b-dde34b4da9e9.png)

### 4.2. Создание шаблона запроса

Идея заключается в том, чтобы одной строкой в консоли можно было получить нужный нам график. Для её реализации с помощью библиотеки argparse принимаем введенный в консоль текст и прогоняем через условия, выбирая нужную функцию, которая будет доставать данные из базы и выводить график.

```ruby
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', choices=['year', 'day', 'hour', 'years', 'days', 'hours'],
                        required=True, type=str, nargs=1, help='Варианты функций.')
    parser.add_argument('-YS', '--years', choices=['200'+str(i) for i in range(6, 10)]+['20'+str(i) for i in range(10, 21)],
                        nargs='+', help='По каким годам нужен график?')
			
def tw_years(years):
    year_creating = []
    for i in range(len(years)):
        year = years[i]
        creats = tw_year(year) / 5500000 * 100
        year_creating.append(creats)
    plot(x=years, y=year_creating, name='year')
			
if __name__ == '__main__':
    token = r'G:\project\dbase\tw_db_5mln\twitter_5mln.db'
    parser = create_parser()
    func = parser.parse_args(sys.argv[1:])
    
    if func.function[0] == 'years':
        years = func.years
        tw_years(years)
```

## 5. Анализ активности пользователей социальной сети твиттер на основе данных регистраций их аккаунтов

### 5.1. Анализ активности пользователей со всего мира

#### 5.1.1. Анализ активности пользователей по годам
График зависимости регистраций от периода лет (Рис. 4)

![график по годам в процентах](https://user-images.githubusercontent.com/129762316/230916034-b40ebd91-5d09-42ce-aac6-844bcac4fef4.png)

Первые три года социальная сеть не имела особой популярности, полным ходом шла разработка и распространение на различных внутререгионных мероприятиях. В 2008 году сеть начали использовать журналисты и политики и уже за 2009 год было зарегистрировано 7% от всех пользователей: 330 миллионов. Дальше, как видно из графика, твиттер набрал огромные обороты и стал популярен во всём мире, и, получив за 2011-2012 года пользователей, основная волна регистраций была пройдена, количество ежегодных регистраций начало сильно падать.

#### 5.1.2 Анализ активности пользователей в течение дней недели
График зависимости регистраций от дней недели (Рис. 5)

![график по дням недели в процентах](https://user-images.githubusercontent.com/129762316/230920526-e4e6f68c-b1ba-403b-aaf6-1da53f9cd9b2.png)

Данный график показался мне самым необычным из всех. Оказалось, что люди чаще всего пользуются социальными сетями в будние дни, конкретнее в среду. Скорее всего это происходит из-за того, что после работы людям хочется максимально отвлечся от всех дел и окунуться в новости и прессу. Ну а реже всего, как видим из графика, заходят по субботам и своскресеньям. Объясняется это тем, что на данные дни обычно больше всего планов: убраться по дому, сходить в кино, магазин и т.д.

#### 5.1.3. Анализ внутрисуточной активности пользователей
График зависимости регистраций от времени суток (Рис. 6)

![график по времени суток с 8 утра в процентахpng](https://user-images.githubusercontent.com/129762316/230923788-cf0c7895-8fdf-43f9-9e66-c8e196701acf.png)

Видно два всплеска. Превый происходит с 11 утра и до 15 часов дня, после чего держится вплоть до 19 часов вечера и идёт на спад, часть людей идёт спать. И второй всплеск виден уже в 1 и 2 час ночи и обусловлен обычным, бессмысленным просмотром прессы после обыденных вечерних дел. Дальше и оставшаяся часть засыпает, начиная новый цикл.

#### 5.1.4. Анализ внутрисуточной активности пользователей за разные дни недели
Графики зависимости регистраций по разным дням недели от времени суток (Рис. 7)
![внутрисуточная активность по дням недели](https://user-images.githubusercontent.com/129762316/232316606-d5b3ae2c-8d4f-4d83-912a-376875a355d7.png)

По графику видим, что понедельник и вторник не сильно выделяются, находятся где-то между остальных графиков. Среда выделяется наибольшей активностью в ночное время и наименьшей утром, но тоже не сильно. Четверг и пятница имеют наименьшую активность в вечернее время, скорее всего люди хотят хорошо выспаться на выходных. Начало субботы и воскресенья необычные практически полным отсутствием второго, ночного, всплеска. Объясняется это тем, что перед выходным днём все ложаться спать пораньше. Но также выходные особенны наибольшей утренней активностью, обусловленные не рабочим днём.

### 5.2. Анализ активности пользователей в некоторых регионах Евразии

#### 5.2.1. Анализ количества активности пользователей в некоторых регионах Евразии
Гистограмма зависимости количества регистраций от некоторых регионов Евразии (Рис. 8)
![диаграмма регистраций по регионам](https://user-images.githubusercontent.com/129762316/232312990-d2b31a2f-d089-4e9e-af8a-a69bf8e56136.png)

Взяты были такие регионы Евразии, как: Япония, Китай, Соединённое Королевство, Россия, Украина, Франция и Германия. Выбор делался на основе расстояния между странами и их важности в различных мировых сферах. Как видим, среди выбраных стран, твиттер наиболее распространён в Германии и наименее в таких восточных странах, как: Китай, Япония. Но остальные страны находятся примерно на одном уровне. Данная информация не в совершенстве точная, т.к. в твиттере со временем менялся способ указания региона и пользователи могли указывать что угодно.

#### 5.2.2. Анализ по годовой активности пользователей регионов
График зависимости регистраций в регионов от периода лет (Рис. 9)

![регионы по годам](https://user-images.githubusercontent.com/129762316/236236186-6087b9b3-80d0-438e-a72b-40cf48f3c236.png)

Первее других твиттер стал популярен в Соединённом Королевстве, обогнав по количеству регистраций в 2009 году. С 2010 практически все идут вровень, пик в 2011 и спад к 2018. В Японии и Китае сильно меньше других подъём в 2010-2012 годах, но ярко выделяется 2016 год с неожиданно большим наплывом людей, особенно в Китае, вероятно из-за китайской автогонки чемпионата мира «Формулы-1».

#### 5.2.3. Анализ внутрисуточной активности пользователей регионов
График зависимости регистраций в регионах от времени суток (Рис. 10)

![регионы за время суток](https://user-images.githubusercontent.com/129762316/232316507-84d595ed-35c2-4318-8e32-dc40a63722db.png)

Графики очень разные, но это было ожидаемо, ведь взяты страны с совершенно различными часовыми поясами. Япония и Китай имеют рост к трем часам ночи и спад в три часа дня, это логично, ведь в данных странах часовые пояса UTC+8 и +9. Соединённое Королевство, в свою очередь, имеет рост в шесть утра и спад только к десяти вечера. Здесь UTC+1. График регистраций России идёт рядом с графиком Франции. Он плавно начинает рост в пять утра и меняет направление только к десяти вечера. Украина и Гремания имеют похожие графики, только с разницей в один два часа. Они больше других сходны с графиком внутрисуточной активности: подъём с восьми утра и спад с восьми вечера. 



 










