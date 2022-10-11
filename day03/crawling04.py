from bs4 import BeautifulSoup
import urllib.request as req


url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
print(res)
soup = BeautifulSoup(res, 'html.parser')
# print(soup)
# div = soup.select_one('ul#exchangeList > li >a.head> div')
div = soup.select_one('#exchangeList > li.on >a.head.usd> div')
print(div)

