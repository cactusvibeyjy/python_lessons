from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
import time


def CoffeeBean_store(result):
    path = "C:\\utility\\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(path, options=options)

    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"

    for i in range(1, 100):
        wd.get(CoffeeBean_URL)
        time.sleep(1)
        try:
            wd.execute_script("storePop2(%d)" % i)
            time.sleep(1)
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            store_name = ""
            # 매장이름출력
            store_name_h2 = soupCB.select(
                'div.store_txt > h2')
            # print(store_name_h2)
            store_name = store_name_h2[0].string

            # storeListUL > li > div.store_txt > p.name > span
            print(store_name)

        except:
            continue


result = []
CoffeeBean_store(result)