from bs4 import BeautifulSoup
import requests
import re

res = requests.get('https://news.daum.net/economic/')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text())

links = soup.select('a[href]')
print(links)
for t in links:
    if re.search('https://v.\w+', t['href']): # .임의의 문자 1개 
        print(t.get_text().strip())           #\w 숫자와 문자
                                              # + 1회 이상
print('======================='*7)
links2 = soup.find_all(href = re.compile(r'https://v.\w+')) # https 들어가 있는 모든 객체 추출
for i in links2:
    # print(i)
    print(i.get_text().strip())