from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd
import re

path = "C:\\utility\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-longging'])
driver = wd.Chrome(path, options=options)
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/week/index.htm')

all_music = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')

trs = all_music.find_elements(By.TAG_NAME, 'tr')
datas = []
# for i in trs:
#     rank = i.find_element(By.CLASS_NAME, "rank").text.strip()
#     title = i.find_element(By.CLASS_NAME, "rank01").text.strip()
#     #title = i.find_element(By.CLASS_NAME, "wrap_song_info").find_element(By.TAG_NAME, 'a').text.strip()
#     singer = i.find_element(By.CLASS_NAME, "rank02").text.strip()
#     album = i.find_element(By.CLASS_NAME, "rank03").text.strip()
#     like = i.find_element(By.CLASS_NAME, "cnt").text
#     like = re.sub(',', '', like)
#     datas.append([rank, title, singer, album, like])


#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
for chart in trs:
    num = chart.find_element(By.CLASS_NAME,'rank').text
    name = chart.find_element(By.CLASS_NAME,'wrap_song_info').find_element(By.TAG_NAME,'a').text
    singer = chart.find_element(By.CSS_SELECTOR,'div.rank02').find_element(By.TAG_NAME,'a').text
    album = chart.find_element(By.CSS_SELECTOR,'div.rank03').find_element(By.TAG_NAME,'a').text
    likes = chart.find_element(By.CLASS_NAME, 'like').find_element(By.CLASS_NAME, 'cnt').text
    likes = re.sub(',', '', likes)
    datas.append([num, name, singer, album, likes])

print(datas)

# melon_df = pd.DataFrame(datas, columns=('순위','곡명','가수','앨범','좋아요'))
# melon_df.to_csv('day06/melon.csv',enco