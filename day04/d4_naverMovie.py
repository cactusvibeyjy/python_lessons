from bs4 import BeautifulSoup
import requests

req=requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver')
html = req.text
soup = BeautifulSoup(html, 'html.parser')


rank2 = soup.find_all('div', class_ = "tit3")
print(rank2)
for i in rank2:
    print(i.get_text().strip())
print('-----------------------------------------')
for i in range(len(rank2)):
    print((i+1), '위 :', rank2[i].get_text().strip())
print('-----------------------------------------')


rank = soup.select('div.tit3 a') #div.tit3 #old_content > table > tbody > tr> td.title a
for i in rank:
    print('-', i.string)