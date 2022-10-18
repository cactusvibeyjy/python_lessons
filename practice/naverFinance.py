from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests


req=requests.get('https://finance.naver.com/')
html = req.content
soup = BeautifulSoup(html, 'html.parser')

tbody = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular > table > tbody')
trs = tbody.select('tr')
datas = []
for i in trs:
    name = i.select_one("th>a").get_text()
    curr_price = i.select_one('td').get_text()
    ch_direction = i.select_one('td> img')['alt']
    ch_updown = i.select_one('td > span').get_text().strip()
    datas.append([name, curr_price,ch_direction,ch_updown])
print(datas)

# stock = soup.select('#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr > th a')
# for i in stock:
#     print(i.get_text())
# price = soup.select('#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr> td:nth-child(2)')

# for i in price:
#     print(i.get_text())

# upDown = soup.select('#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr> td> span')
# for i in upDown:
#     print(i.get_text())

# for i in range(len(stock)):
#     print('[',stock[i].get_text().strip(),
#           price[i].get_text().strip(),upDown[i].get_text().strip(),']')    

write_wb = Workbook()
write_ws = write_wb.create_sheet('결과')
for data in datas:
    write_ws.append(data)
write_wb.save(r'stockRanking.xlsx')