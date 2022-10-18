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

# insert_weather = "insert into forecast(city,tmef,wf,tmn,tmx) values (%s, %s, %s, %s, %s)"
# select_data = "select tmef from forecast order by tmef desc limit 1"
#cur = conn.cursor()
#cur.execute(select_data)
#last_date = cur.fetchone() #db에 있는 최신날짜라 한다면 db 에 insert 하겠다
# print(last_date)


# req = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
# html = req.text
# soup = BeautifulSoup(html, 'lxml')

#부산의 날씨
select_data = "select * from forecast where city = '부산' order by tmef desc"
cur = conn.cursor()
cur.execute(select_data)
result = cur.fetchall()

datas = []
for row in result:
    datas.append([row[2], row[4], row[5]])
#print(datas)


#부산의 날짜, 최저기온, 최고기온
select_data2 = "select max(tmx), min(tmn) from forecast where city = '부산'"
cur = conn.cursor()
cur.execute(select_data2)
result2 = cur.fetchone()
# print(result2)
# print("최고 : " + result2[0])
# print("최저 : " + result2[1])


select_data3 = "select max(tmx), min(tmn) from forecast where city = '서울'"
cur = conn.cursor()
cur.execute(select_data3)
result3 = cur.fetchall()
print(result3)