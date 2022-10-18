from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = "C:\\utility\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://entertain.naver.com/ranking")
time.sleep(2)

sympathybtn = driver.find_element(By.ID,'sympathy_ranking_btn').find_element(By.TAG_NAME, 'a')
#sympathy_ranking_btn > a > span
sympathybtn.click()
time.sleep(2)


listBox = driver.find_element(By.ID, 'newsWrp')


#newsWrp > div.likeitnews > ul
list = listBox.find_elements(By.CSS_SELECTOR, 'div.likeitnews')
time.sleep(3)

datas = []
for i in list:
    #newsWrp > div.likeitnews > ul > li:nth-child(1) > div.rank_num
    #f'/html/body/div/div[3]/div/div/div[1]/div[2]/ul/li[1]/div[1]'
    rank = i.find_element(By.CSS_SELECTOR, 'div.rank_num').text
    
    #newsWrp > div.likeitnews > ul > li:nth-child(1) > div.tit_area
    title = i.find_element(By.CSS_SELECTOR,' div.tit_area').find_element(By.CSS_SELECTOR, 'a').text
    
    # #newsWrp > div.likeitnews > ul > li:nth-child(1) > div.tit_area > p
    summary= i.find_element(By.CSS_SELECTOR,'div.tit_area').find_element(By.TAG_NAME, 'p').text
    #newsWrp > div.likeitnews > ul > li:nth-child(1) > div.tit_area > a.likeitnews_item_likeit.like
    likes = i.find_element(By.CSS_SELECTOR,'a.likeitnews_item_likeit.like').text.split('공감수')[1]
    
    datas.append([rank, title, summary, likes])
print(datas)




#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div > div:nth-child(2) > a > strong