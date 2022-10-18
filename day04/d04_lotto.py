from bs4 import BeautifulSoup
import requests


res = requests.get('https://m.dhlottery.co.kr/gameResult.do?method=byWin')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup.get_text())

winNum = soup.select('#container > div > div.bx_lotto_winnum > span') #container > div > div.bx_lotto_winnum > span.ball
for i in winNum:
    print(i.string, end=' ')

# ballNum = soup.find_all('span', class_="ball")
# for i in ballNum:
#     print(i.get_text(), end = '\t')


# print(winNum.get_text())

# for i in range(len(winNum)):
#     print(winNum[i].get_text())