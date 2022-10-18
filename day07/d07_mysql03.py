import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pymysql
import requests
from bs4 import BeautifulSoup

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"
conn = pymysql.connect(host = dbURL, port = dbPort, user = dbUser, 
                passwd =dbPass, db = 'bigdb', charset = 'utf8', use_unicode=True)
font_path = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)


select_data = "select * from forecast where city = '부산'"
cur = conn.cursor()
cur.execute(select_data)
result = cur.fetchall()

high =[]
low =[]
xdata=[]
whState =[]

#num, city, tmef, tmn, tmx

for row in result:
    high.append(float(row[5])) #최고기온
    low.append(float(row[4])) #최저기온
    whState.append(row[3]) #날씨상태
    xdata.append(row[2].split('-')[2]) #가로축 

plt.figure(figsize=(10,6))
plt.plot(xdata, low, label = '최저기온')
plt.plot(xdata, high, label = '최고기온')
plt.title(result[0][2].split('-')[1]+"월") #타이틀
plt.legend()
plt.show()


select_data1 = "select wf, count(*) from forecast where city = '부산' group by wf"
cur.execute(select_data1)
result2 = cur.fetchall()
whData = []
whDataCount =[]
for row in result2:
    whData.append(row[0])
    whDataCount.append(row[1])

plt.bar(whData, whDataCount)
plt.legend()
plt.show()
#bar 그래프  (wf기준으로 만들어보기)


#pie 그래프
plt.pie(whDataCount, labels =whData, autopct='%.1f%%')
plt.show()