import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


def hollys_store(result):
    for page in range(1, 6):
        url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' % page
        # print(url)
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')

        tag_tbody = soup.select_one('tbody')
        # print(tag_tbody)

        for store in tag_tbody.select('tr'):
            tds = store.select('td')
            store_sido = tds[0].string
            store_name = tds[1].string
            store_address = tds[3].string
            store_phone = tds[-1].string

            result.append([store_sido, store_name, store_address, store_phone])

    return


result = []
print('-- Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>')
hollys_store(result)
hollys_df = pd.DataFrame(result, columns=(
    'store', 'sido-gu', 'address', 'phone'))
# print(hollys_df)
hollys_df.to_csv('hollys.csv', encoding='cp949', mode='w', index=True)
