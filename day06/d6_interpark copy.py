from xml.dom.minidom import Document
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
path = "C:\\utility\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-longging'])
driver = wd.Chrome(path, options=options)
driver.implicitly_wait(2)
driver.get('https://search-travel.interpark.com/search/%EC%A0%9C%EC%A3%BC%EB%8F%84')
# all_videos = driver.find_elements(By.ID, "dismissible")
# body_tag = driver.find_element(By.TAG_NAME, 'body')
#print(body_tag)
# driver.find_element(By.ID, 'search_btn').click() # click 마우스 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[2]').click() # click 마우스 클릭
time.sleep(1)
result = []
# /html/body/div[3]/div/div[1]/div[2]/div[3]/div[2]/div[3]/button[3]
for k in range(10):
    for i in range(1,11):
        driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[2]/div[3]/div[2]/div[3]/ul/li[{i}]').click() # click 마우스 클릭
        time.sleep(1)
        list = driver.find_elements(By.XPATH, f'/html/body/div[3]/div/div[1]/div[2]/div[3]/div[2]/div[2]/ul/li') # click 마우스 클릭
        for j in range(1,len(list)+1):
                title=driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[2]/div[3]/div[2]/div[2]/ul/li[{j}]/div/div[2]/div[2]/div[1]/a/h5').text # click 마우스 클릭
                price = driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[2]/div[3]/div[2]/div[2]/ul/li[{j}]/div/div[2]/div[2]/div[2]/div/p[1]/strong').text # click 마우스 클릭
                print([title,price])
                result.append([title,price])
    time.sleep(1)
    driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[1]/div[2]/div[3]/div[2]/div[3]/button[3]').click()
    time.sleep(1)


