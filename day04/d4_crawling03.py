from bs4 import BeautifulSoup
import re
import requests

r=requests.get("http://api.aoikujira.com/time/get.php")
txt=r.text #텍스트 형식으로 데이터 추출
print(txt)

bin = r.content
print(bin) #바이너리 형식으로 데이터 추출

html = """
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com/fuga">fuga*</li>
        <li><a href="https://example.com/foo">foo*</li>
        <li><a href="shttps://example.com/foobbb">foobbb*</li>
        <li><a href="http://example.com/aaa">aaa*</li>
"""
#https 로 시작하는 밸류 추출
soup = BeautifulSoup(html, 'html.parser')
lis = soup.find_all(href = re.compile(r'https://')) # https 문자열에 들어가 있는 모든 객체 추출

lis1 = soup.find_all(href = re.compile(r'^https://'))
print(lis1)
for i in lis1:
    # print(i)
    print(i.attrs['href'])
