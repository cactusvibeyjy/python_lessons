import re
text = "<title>지금은 문자열 연습입니다.</title>"
# 1. 0~7 사이 추출
print(text[0:7])
# 2. 문 있으면 위치 값 출력
print(text.find('문'))
print(text.index('문'))
# 3. 파 있으면 위치 값 없으면 -1 출력
print(text.find('파'))
# 4. 파 없으면 오류를 발생
#print(text.index('파'))

text1 = "        <title>지금은 문자열 연습입니다.</title>"
text2 = ";"
# 공백제거 하고 1,2 연결
print(text1.strip()+text2)
# text1 왼쪽 공백제거하고 text2 연결
print(text1.lstrip()+text2)
# text1 오른쪽 공백 제거하고  text2 연결
print(text1.rstrip()+text2)
# text1 <title> 을 <div>로 바꾸기
print(text1.replace("<title>", "<div>"))
print(text1.replace("<title>", ""))

text3 = ('111<head>안녕하세요</head>22')
body = re.search('<head.*/head>', text3)
print(body)
body = body.group()
print(body)

#[0-9], [a-z]
#ab*c : *의 의미는 0번 이상??? abc | abbc | abbbbc 를 의미 할 수 있음
# +의 의미는 한 번이상
# ?의 의미는 0번이거나 한번일때 사용

text4=('<head>안녕하세요...<title>지금은 문자열 연습</title></head>')
#search 사용 : <title>지금은 문자열 연습</title>
body1 = re.search('<title.*/title>', text4)
body1 = body1.group()
print(body1)
body1=re.sub('<.+?>',' ', text4)
print(body1)

