import matplotlib as mpl
from selenium import webdriver as wd
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


path = "C:\\utility\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = wd.Chrome(path, options=options)


driver.get('https://www.youtube.com/c/paikscuisine/videos')

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
all_videos = soup.find_all(id='dismissible')

datas = []
for video in all_videos:
    title = video.find(id='video-title').text
    video_time = video.find(
        'span', class_='style-scope ytd-thumbnail-overlay-time-status-renderer').text.strip()
    video_num = video.find(
        'span', {'class': 'style-scope ytd-grid-video-renderer'}).text
    datas.append([title, video_time, video_num])
print(datas)
# DataFrame 형태로 변환하여 제목, 재생시간, 조회수

youtube_df = pd.DataFrame(datas, columns=('제목', '재생시간', '조회수'))
print(youtube_df)
youtube_df.to_csv('youtube.csv', encoding='UTF-16', mode='w', index=True)



dict_youtube = {'100만이상': 0, '50만이상': 0, '10만이상': 0}


for item in datas:
    item = float(str(item).split('조회수')[1].split('만회')[0].strip())
    if item >=100:
        dict_youtube['100만이상'] +=1
    elif item >= 50:
        dict_youtube['50만이상'] +=1
    elif item >=10:
        dict_youtube['10만이상'] +=1
print(dict_youtube)      

#그래프그리기
#한글

font_name = mpl.font_manager.FontProperties(fname = 'c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family = font_name)
figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(dict_youtube.values(), labels=dict_youtube.keys(), autopct='%.1f%%')
plt.show()