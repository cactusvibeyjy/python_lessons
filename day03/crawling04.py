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

print("value : ", soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').string)
txt1 = soup.select_one('div.head_info')
print('>>>>>>>>>>>>',txt1)

print(txt1.select('span')[0].string)
print(txt1.select('span')[1].string)
print(txt1.select('span')[2].string)
print(txt1.select('span')[3].string)
txt2 = txt1.select('span')
print('>>>>>>>>>>>>',txt2) #리스트로 출력

for sp in txt2:
    print(sp.string)

#가격
price = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').string
print(price)

#상승/하락
updown =soup.select_one('#exchangeList > li.on > a.head.usd > div > span.blind').string
print(updown)