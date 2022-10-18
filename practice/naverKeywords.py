from selenium import webdriver
import time
from openpyxl import Workbook
import pandas as pd





wb = Workbook()
ws = wb.create_sheet()
path = "C:\\utility\\chromedriver.exe"
driver = webdriver.Chrome(path)

final = {}

# 연관검색어 추출할 쿼리 리스트
keyword_list = ['신라면', '진라면', '열라면', '안성탕면', '무파마']

for i in range(len(keyword_list)):
    URL = "https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query={}".format(keyword_list[i])
    driver.get(URL)
    driver.implicitly_wait(10)

    searches = driver.find_elements_by_css_selector(".lst_related_srch li")

    temp = []

    for keyword in searches:
        result = keyword.text
        temp.append(result)

    final[keyword_list[i]] = pd.Series(temp)

df = pd.DataFrame(final)

df.to_excel('result.xlsx')

driver.quit()