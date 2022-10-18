from bs4 import BeautifulSoup

fp = open('day04/fruits-vegetables.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

print(soup.select_one('ul#ve-list > li:nth-child(4)').string) #li:nth-of-type(4)

print(soup.select('#ve-list > li[data-lo="us"]')[1].string)
print(soup.select('#ve-list > li.black')[1].string)
print('====='*30)
cond = {'data-lo': 'us', 'class': 'black'}
print(soup.find("li", cond).string)
print('====='*30)
print(soup.find(id="ve-list").find("li", cond).string)
