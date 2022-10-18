from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

path = "C:\\utillity\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(service=Service(
    ChromeDriverManager(). install()), options=options)

driver.get('https://naver.com')
driver.find_element(By.ID, 'query').send_keys('파이썬')
driver.find_element(By.ID, 'search_btn').click()
