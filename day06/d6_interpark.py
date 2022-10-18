import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


path = "C:\\utility\\chromedriver.exe"
driver = webdriver.Chrome(path)


driver.get("https://tour.interpark.com/?mbn=tour&mln=tour_tour")
time.sleep(1)

input_text = driver.find_element(By.ID, "SearchGNBText")
input_text.send_keys("제주도")
search_btn = driver.execute_script('searchBarModule.ClickForSearch()')
time.sleep(2)

morebtn= driver.find_element(By.CSS_SELECTOR, 'div.searchAllBox.domesticHotel.col1 > div > button')
morebtn.click()
time.sleep(1)
#boxList

#app > div > div:nth-child(1) > div.resultAtc > div.contentsZone > div.panelZone > div.pageNumBox > ul > li:nth-child(1)
pageNum_list = driver.find_elements(By.CSS_SELECTOR, 'div.pageNumBox > ul > li')
datas = []
for l in range(len(pageNum_list)):
    # product_list = driver.find_elements(By.CLASS_NAME, 'boxItem')
    product_list = driver.find_elements(By.CSS_SELECTOR, '#boxList > li')
    for i in product_list:
        try:
            hotel = i.find_element(By.TAG_NAME, 'h5').text
            price = i.find_element(By.TAG_NAME,'strong').text
        #boxList > li:nth-child(1) > div > div.productInfo > div:nth-child(3) > div:nth-child(2) > p:nth-child(1)
            rating = i.find_element(By.CSS_SELECTOR,'div.productInfo > div:nth-child(3) > div:nth-child(2) > p.info').text.split('평점')[1]
            datas.append([hotel, price, rating])
        except:
            
            continue
    pageNum_list[l].click()
    time.sleep(1)
print(datas)


#hotel.csv


hotel = pd.DataFrame(datas, columns=('호텔명', '가격', '평점'))
print(hotel)
# hotel.to_csv('hotel.csv', encoding='UTF-8', mode='w', index=False)
