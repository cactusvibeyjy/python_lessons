from bs4 import BeautifulSoup
import pandas as pd
import requests

req = requests.get(
    'https://www.weather.go.kr/weather/observation/currentweather.jsp')
soup = BeautifulSoup(req.text, 'html.parser')

table = soup.find('table', {'class': 'table-col'})

datas = []


for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) > 0:
        print('지역 :', tds[0].text)
        print('온도 :', tds[5].text)
        print('습도 :', tds[-4].text)
        datas.append([tds[0].text, tds[5].text, tds[-4].text])

print(datas)

with open('weather.csv', 'w') as file:
    file.write('point, temp, num \n')
    for item in datas:
        row = ','.join(item)
        file.write(row+'\n')

df = pd.read_csv('weather.csv', index_col='point', encoding='euc-kr')
print(df)
