from selenium import webdriver
from selenium.webdriver.common.by import By
import time


path = "C:\\utility\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://instagram.com/accounts/login")
time.sleep(3)


#login intagram
#f'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input'
username_input = driver.find_element(By.XPATH,f'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
#f'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input'
password_input = driver.find_element(By.XPATH, f'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input') 
username_input.send_keys("epinephrine_yjy") 
time.sleep(2)
password_input.send_keys("Yodle0521!") 
time.sleep(2)
#f'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button'
login_button = driver.find_element(By.XPATH,f'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button') 
login_button.click() 
time.sleep(10)

#백업코드 버튼 클릭해서 백업코드로 로그인하는 방법
#react-root > section > main > div > div > div:nth-child(1) > div.FsQoP > form > div:nth-child(4) > button
backUp_login = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(4) > button')
backUp_login.click()
time.sleep(5)
#백업코드 인풋
backUp_code = driver.find_element(By.XPATH,f'/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input')
backUp_code.send_keys("새로운코드 받기") #백업코드는 한번씩만 사용 할 수 있음 
time.sleep(2)
#백업코드 서밋
#react-root > section > main > div > div > div:nth-child(1) > div.FsQoP > form > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm.MGdpg.CovQj.jKUp7.iHqQ7 > button
backUp_submit = driver.find_element(By.CSS_SELECTOR,'div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm.MGdpg.CovQj.jKUp7.iHqQ7 > button')
backUp_submit.click()
time.sleep(5)
