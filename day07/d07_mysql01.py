from asyncio import wait_for
from distutils.util import execute
import pymysql
import requests
from bs4 import BeautifulSoup

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"
conn = pymysql.connect(host = dbURL, port = dbPort, user = dbUser, 
                passwd =dbPass, db = 'bigdb', charset = 'utf8', use_unicode=True)

insert_weather = "insert into forecast(city,tmef,wf,tmn,tmx) values (%s, %s, %s, %s, %s)"
select_data = "select tmef from forecast order by tmef desc limit 1"
cur = conn.cursor()
cur.execute(select_data)
last_date = cur.fetchone() #db에 있는 최신날짜라 한다면 db 에 insert 하겠다
# print(last_date)


req = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
html = req.text
soup = BeautifulSoup(html, 'lxml')

weather ={}
for i in soup.find_all('location'):
   weather[i.find('city').text] = []
   for j in i.find_all('data'):
        tmp =[]
        if(last_date is None) or (str(last_date[0]) < j.find('tmef').text ):
            tmp.append(j.find('tmef').text)
            tmp.append(j.find('wf').text)
            tmp.append(j.find('tmn').text)
            tmp.append(j.find('tmx').text)
  
            weather[i.find('city').string].append(tmp)
            print(tmp)
# for i in weather:
#     for j in weather[i]:
#         cur = conn.cursor()
#         cur.execute(insert_weather, (i, j[0], j[1], j[2], j[3]))
#         conn.commit()

