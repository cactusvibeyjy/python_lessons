from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)
print(res)
soup = BeautifulSoup(res, 'html.parser')

# title = soup.channel.title.string
# print(title)
title = soup.find('title').string
print(title)
print('======================================')
wf = soup.find('wf').string
print(wf)
print('======================================')
