from bs4 import BeautifulSoup
import urllib.request as req
html = """
    <html><body>
        <div id = "meigen">
            <h1>위키북스 도서</h1>
            <ul class = "items">
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인의 정석</li>
            </ul>
        </div>
        <div>
            <h1>위키북스222도서</h1>
        </div>
        <h1>위키북스22 도서</h1>
    </body></html>
"""
#위키북스 도서만 추출해서 출력

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.find('h1').string
print(h1)

h1_1 =soup.select_one('h1').string
print(h1_1)

h1_2 =soup.select_one('div>h1').string
print(h1_2)

h1_3 =soup.select_one('div#meigen > h1').string #div 즉 아이디 값이 "meigen"값 안에 있는 div 만 출력할때 # 사용
print(h1_3)
print('========================================')
li =soup.select('div#meigen > ul.items > li')
for i in li:
    print(i.string)

print('========================================')
li2 =soup.select('ul.items>li')
for i in li2:
    print(i.string)
print('========================================')
list =soup.select('li')
print(list)
print('========================================')
for i in list:
    print(i.string)

