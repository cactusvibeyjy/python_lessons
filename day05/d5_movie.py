import requests
from bs4 import BeautifulSoup

req = requests.get('https://movie.daum.net/ranking/reservation')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# name = soup.select(
#     '#mainContent > div > div.box_ranking > ol > li > div > div > strong > a')
# # print(name)
# grade = soup.select(
#     '#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont > span.txt_append > span:nth-child(1)')
# # print(grade)
# rate = soup.select(
#     '#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont > span.txt_append > span:nth-child(2)')
# # print(rate)

# for i in range(len(title)):
#     print(title[i].get_text())
#     print('평점:', grade[i].get_text())
#     print('예매율:', rate[i].get_text())
#     print()

ols = soup.find('ol', class_="list_movieranking")
rankcont = ols.find_all('div', class_='thumb_cont')
# print(rankcont)
for i in rankcont:
    movietitle = i.find('a', class_='link_txt').get_text()
    moviegrade = i.find('span', class_='txt_grade').get_text()
    # moviereser = i.find('span', class_='txt_num').get_text()
    moviereser = i.find('span', {'class': 'txt_num'}).get_text()
    print('제목 :', movietitle)
    print('평점 :', moviegrade)
    print('예매율 :', moviereser)
    print()
