from bs4 import BeautifulSoup
import requests
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib.request
import pandas as pd

# header ={'User-Agent': 'Mozilla/5.0'}
# req = requests.get('https://www.melon.com/chart/week/index.htm', headers = header)
# soup = BeautifulSoup(req.text, 'html.parser')

# tbody = soup.select_one('#frm > div > table > tbody')
# chart = tbody.select('tr')
# datas = []
# for i in chart:
#     rank = i.select_one('div > span').get_text()
#     title = i.select_one('div span > a').get_text()
#     singer = i.select_one('div.ellipsis.rank02 > a').get_text()
#     album = i.select_one('td:nth-child(7) > div > div > div > a').get_text()
#     datas.append([rank, title,singer,album])
# print(datas)
# melon_weekchart = pd.DataFrame(datas, columns=('순위', '곡명', '가수','앨범'))
# melon_weekchart.to_csv('melon_weekchart.csv', encoding='UTF-8', mode='w', index=False)

path = "C:\\utility\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path, options=options)

#순위, 곡명, 가수, 앨범 크롤링
driver.get('https://www.melon.com/chart/week/index.htm')
week_chart = driver.find_elements(By.ID, "tb_list")
print(week_chart)
#  title = video.find_element(By.ID, 'video-title').text
#     video_type = video.find_element(
#         By.CLASS_NAME, 'style-scope ytd-thumbnail-overlay-time-status-renderer').text
#     video_num = video.find_element(
#         By.CSS_SELECTOR, 'span.ytd-grid-video-renderer').text
#     datas.append([title, video_type, video_num])

datas = []
for chart in week_chart:
    rank = chart.find_element(By.CLASS_NAME, 'rank').text
    # title = chart.find('div', class_='ellipsis.rank01')
    # singer = chart.find('div', class_='ellipsis.rank02')
    # album = chart.find('td:nth-child(7) > div > div > div > a')
    # like = chart.find('span', class_='cnt')
    # datas.chart([rank, title, singer, album, like])
print(datas)

# melon_weekchart = pd.DataFrame(datas, columns=('순위', '곡명', '가수','앨범','좋아요'))
# print(melon_weekchart)
# melon_weekchart.to_csv('melon_weekchart.csv', encoding='UTF-8', mode='w', index=False)

