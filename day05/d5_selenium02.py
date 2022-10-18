from selenium import webdriver as wd
from selenium.webdriver.common.by import By

path = "C:\\utility\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path, options=options)

driver.get('https://naver.com')
driver.find_element(By.ID, 'query').send_keys('파이썬')
driver.find_element(By.ID, 'search_btn').click()
