from selenium import webdriver
import time
import pandas as pd

path = "C:\\utility\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.instagram.com/p/CjsDH4vJGd9/")
time.sleep(3)


comment_more_btn = 'div._ab8w._ab94._ab99._ab9h._ab9m._ab9p._abcj._abcm'

while True:
    try:
        more_btn = driver.find_element_by_css_selector(comment_more_btn)
        more_btn.click()
    except:
        break

id_f = []

rp_f = []



ids = driver.find_elements_by_css_selector('div._a9zr > h3 > div > span > a')

replies = driver.find_elements_by_css_selector('div._a9zr > div._a9zs > span')



for id, reply in zip(ids, replies):

    id_a = id.text.strip()

    id_f.append(id_a)

    rp_a = reply.text.strip()

    rp_f.append(rp_a)

    data = {"아이디": id_f, "코멘트": rp_f}


df = pd.DataFrame(data)

df.to_excel('result.xlsx')