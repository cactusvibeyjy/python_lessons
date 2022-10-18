from bs4 import BeautifulSoup
import requests

#평점 크롤링
req=requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20221011')
html = req.text
soup = BeautifulSoup(html, 'html.parser')


ratingRank = soup.select('div.tit5 a')
for i in ratingRank:
    print('-', i.get_text())
rating = soup.select('#old_content > table > tbody > tr> td.point')
for i in rating:
    print('-', i.get_text())

print(len(ratingRank))
print(len(rating))
for i in range(len(ratingRank)):
    print((i+1), '위 : ', ratingRank[i].get_text().strip(), '//',
          rating[i].get_text().strip(),'점')    

