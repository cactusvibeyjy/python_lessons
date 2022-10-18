import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import pymysql
import requests
from bs4 import BeautifulSoup

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"
conn = pymysql.connect(host = dbURL, port = dbPort, user = dbUser, 
                passwd =dbPass, db = 'bigdb', charset = 'utf8', use_unicode=True, cursorclass=pymysql.cursors.DictCursor)
font_path = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)


select_data = "select * from forecast where city = '서울' order by tmef desc"
cur = conn.cursor()
cur.execute(select_data)
result = cur.fetchall()

df = pd.DataFrame(result)
print(df)

plt.plot(pd.to_numeric((df['tmn'])), label = '최저기온')
plt.plot(pd.to_numeric((df['tmx'])), label = '최고기온')

plt.legend()
plt.show()
