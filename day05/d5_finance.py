import requests
from bs4 import BeautifulSoup

codes = ['252670', '251340']
datas = []

for code in codes:
    url = 'https://finance.naver.com/item/main.naver?code='+code

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.select_one(
        '#middle > div.h_company > div.wrap_company > h2 > a').get_text()
    # print(title)

    append = soup.select_one(
        '#chart_area > div.rate_info > div > p.no_today span').get_text().strip()
    # print(append)

    datas.append([title, append])

print(datas)
