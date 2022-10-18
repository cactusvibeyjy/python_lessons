from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

path = "C:\\utility\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path, options=options)

# driver.get('https://google.com')
# r = driver.execute_script('return 100*50')
# print(r)

driver.get('https://www.youtube.com/c/paikscuisine/videos')
all_videos = driver.find_elements(By.ID, "dismissible")
# print(all_videos)

time.sleep(2)
datas = []

# 제목, 재생시간, 조회수
for video in all_videos:
    title = video.find_element(By.ID, 'video-title').text
    video_type = video.find_element(
        By.CLASS_NAME, 'style-scope ytd-thumbnail-overlay-time-status-renderer').text
    video_num = video.find_element(
        By.CSS_SELECTOR, 'span.ytd-grid-video-renderer').text
    datas.append([title, video_type, video_num])

print(datas)
