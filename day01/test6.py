import codecs
import re

f = codecs.open('friends101.txt', 'r', encoding='utf-8')
script101 = f.read()
print(script101[:100])
lines = re.findall(r'Monica:.+',script101)
print(lines)
print(type(lines))

#script101에서 All:
all = re.findall(r'All:.+', script101)
print(all)
#All: 마지막 출력
print(all[-1])
#리스트의 길이 (All: 대사 개수)
print(len(all)) 
print('------------------------------------')
char = re.compile(r'[A-Z][a-z]+:')
print(re.findall(char, script101))
names = re.findall(char, script101)
print(len(names))
print('------------------------------------')
print(re.findall(char, script101))
print(set(names))
print(len(set(names)))
print('------------------------------------')
setType= set(re.findall(char, script101))
print(type(setType))
#등장인물 이름이 일곱자 이상인 사람들만 출력
for i in setType:
    if len(i) > 7:
        print("== : ", i)
character = list(setType) #list로 타입 변경
print(type(character))
#character에서 : 제거해서 출력

character_list=[]
for i in character:
    character_list += [i[:-1]]
print('character_list : ', character_list)

character_list2 = []
for i in character:
    # character_list2 = re.sub(':', '', i)
    # print(character_list2, end= ' ')
    character_list2.append(re.sub(':', '', i))
print('\n###',character_list2)

ch = 'Scene:'
ch = re.sub(':', '', ch)
print('ch>>', ch)
##################################
a= '제 이메일 주소는 greate@naver.com'
#내용 추가 += 
a += ' 오늘은 tpday@naver 내일은 apple@gmail.com life@abc.co.kr라는 메일을 사용합니다.'
print(a)
#이메일 주소만 추출
#패턴 : 영문자 @영문자.
a1 = re.findall(r'[a-z]+@[a-z.]+',a)
print(a1)

#a로 시작하는 단어 출력 
#패턴 : a + 영문자
words = ['apple', 'cat', 'brave', 'drama', 'asise', 'blow','coat','above']
w1=[]
for i in words:
    w1 += re.findall(r'a.+', i)
    #w1 += re.findall(r'a[a-z]+', i)
print(w1)
print('--------여기를 봐---------------')
for i in words:
    m = re.search(r'a[a-z].+', i)#서치는 중간에 단어가 있는 밸류도 출력
    if m:
        print(m.group())
print('---------------------------------------')
for i in words:
    #m = re.match(r'a[a-z]+', i)#매치는 시작하는 첫단어가 있는 밸류 출력
    m=re.match(r'a\D+', i) #영문자 \D(숫자가 아닌) /  \d(숫자)
    if m:
        print(m.group())

exam1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2022년 입니다.'
print(re.findall(r'\d.+년', exam1)) #뒤에 따르는 문장까지 출력
print(re.findall(r'\d+년', exam1))
print(re.findall(r'\d+.년', exam1))
print(re.findall(r'\d.+?년', exam1))