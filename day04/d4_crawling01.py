from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
print(res)
soup = BeautifulSoup(res, 'html.parser')

# lst = soup.select('#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li')
lst = soup.select('#mw-content-text > div.mw-parser-output > ul>li a') #공백을 주면 후손관계 (더 하위로 들어간다) / > 자식관계 (바로 아래 개체만)
for i in lst:
    print('-',i.string)
