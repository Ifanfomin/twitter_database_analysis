import json
import sqlite3

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_5mln\twitter_5mln.db')
cur = conn.cursor()

with open(r'D:\projects\base\twitter.json') as tw_file:
    try:
        # for i in range(4757775): # 2281511, 4152431, 4757774
        #     tw_file.readline()
        # tw_str = tw_file.readline()
        while tw_str:
            tw = json.loads(tw_str)
            tw_str = tw_file.readline()
            if not('email' in tw):
                tw['email'] = ""
            if not ('phone' in tw):
                tw['phone'] = ""
            if tw['url'] == None:
                tw['url'] = ""
            query = (f"INSERT INTO accounts(twitter_id, name, location, description, followers, friends, listed,"
                     f" created_at, favourites, statuses, email, phone, url) "
                     f"VALUES(" + str(tw['id']) + "," + "'" + tw['name'] + "'" + "," + "'" + tw['location']
                     + "'" + "," + "'" + tw['description'] + "'" + "," + str(tw['followers_count']) + "," +
                     str(tw['friends_count']) + "," + str(tw['listed_count']) + "," + "'" + str(tw['created_at'])
                     + "'" + "," + str(tw['favourites_count']) + "," + str(tw['statuses_count']) + "," + "'" +
                     tw['email'] + "'" + "," + "'" + tw['phone'] + "'" + "," + "'" + tw['url'] + "'" + ");")
            cur.execute(query)
            conn.commit()
            # print(id, name, location, description, followers, friends, listed, created_at, favourites,statuses,email)
    except:
        print("Warning:" + query)

