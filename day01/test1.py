print('Hello')

a = 0
print(a)
print(type(a))
b ='Hello World'
print(b)
print(type(b))
c = " '안녕하세요' "
print(c)

d = "\'안녕하세요\'"
print(d)
print(b+c)
print(2*3)
print('2'*3)
print(c*3)

# b[1]='c' 오류발생 (문자열 못바꿈 = 에러)
print('-----------------------------------------')
print(b)
print(b[0])
print(b[-3]) #글자 오른쪽에서 

e = '반갑습니다'
print(e)
print(e[0:3])
print(e[0:5:3])

print(e.find('안')) #해당 문자 위치값을 알려준다 -1 = 값이 없다라는 뜻을 의미
print(e.index('반'))#해당 문자 위치값을 알려준다
#print(e.index('안'))#해당 문자 위치값이 없으면 오류를 발생시킴

bb=','
print(bb.join('ABCD'))
print(b.upper())
print(b.lower())

dd='       py       '
print(dd.lstrip()) #왼쪽 공백 제거
print(dd.rstrip()) #오른쪽 공백 제거
print(dd.strip()) #양쪽 공백 제거

aa='now is aa bb cc'
print(aa.split()) #공백으로 구분 => 대괄호의 값으로 변경 => list

#리스트(list)
l=list()
print(l,type(l))
lst=[1,2,3]
print(lst, type(lst))
l2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,25]
print(l2, type(l2))
print(l2[0])
print(len(l2))#리스트의 길이를 구하는 함수
print(l2[-1])
#l2의 마지막 값을 출력 할 때
print(l2[-1]) 
print(l2[len(l2)-1])#리스트의 마지막 원소 (l2의 길이)
#l2dml 첫번째 값을 99로 수정

l2[0] = 99
print(l2) #리스트는 자료 변경이 가능
l2[1]=[1,2,3] #리스트 안에 리스트 삽입 가능
print(l2)
print(len(l2))
l2[2] = '사과'
print(l2)
l2.append(999) #배열의 끝에 삽입
l2.remove(5)
print(l2)

a1 = [1,2,3]

b1 = ['life', 'is', 'too', 'short']
c1 =[1,2,'life','is']
d1=[1,2,[3,4], ['life', 'is']]
print(a1)
print(b1)
print(c1)
print(d1)
#d1 첫번째 값 / 세번째 출력
print(d1[0])
print(d1[3]) #life is 출력
print(d1[3][-1])
print(d1[0:3])
d1.insert(2,'aa') #위치를 지정하여 밸류 삽입
print(d1)
d1.append('dd')
print(d1)
print(len(d1))
d1.pop() #맨위의 밸류를 제거
print(d1) #dd 값을 제거 후 출력

a2 = [2,1,0,2,3,2,4,2]
print(a2.count(2))#2라는 숫자의 개수를 리스트에서 카운트
######################################
#튜플(tuple): 수정이 안됨 () = 튜플 (리스트는 [])
t = tuple()
print(t, type(t))
t1 = (1,2,3)
print(t1, type(t1))
print(t1[0], t1[0:2]) #튜플 형태로 출력
print(t1+t1)
#t[0]=5 => 오류발생
t4 =(1,2,(3,4),('life','is'))
print(t4)

#dict (딕셔너리) = 중괄호 {} 이루어짐
d=dict()
print(d,type(d))
d1 ={
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(d1,type(d1))
print(d1['a']) #[]안에 키값을 넣으면 밸류가 리턴
d1['c']=33
print(d1)
print("keys() :", d1.keys())
print("values :", d1.values) #괄호가 있으면 함수를 알려주고 없으면 객체를 알려줌
print("values() :", d1.values())
print("items :", d1.items)
print("items() :", d1.items())

print("type keys() : ", type(d1.keys()))
print("type values() : ", type(d1.values()))
print("type items() : ", type(d1.items()))
print('#####################')
print("type list", type(list(d1.keys())))

# 1. name은 Hong, phone은 01011112222, birth는 0814로 이루어진 dict 생성
dict = {
    'name' : 'Hong',
    'phone' : '01011112222',
    'birth' : '0814'
}
print(dict)
# 2. dict 키값이 1이고 value가 'a'를 추가
dict[1]='a'
print(dict)
# 3. dict 키값이 pet이고 value가 'dog'를 추가
dict['pet'] = 'dog'
print(dict)
# 4. key가 pet은 value  값 출력
print(dict['pet'])
#dict에서 key값만 출력
print(dict.keys())
print("keys() : ", dict.keys())
#리스트 형태로 key 값만 출력
lst=list(dict.keys())
print(lst)
print(list(dict.keys()))
del dict[1]
print('dict:', dict)
dict.clear() #키값, 밸류값 삭제
print(dict)


#set 중복을 허용하지 않고 키 값만 가진다.
s1 = {1,2,3,4,4,4,4}
print(s1, type(s1))
s2 = set([1,2,3,4,5])
print(s2, type(s2))
print(s1|s2)
print(s2-s1) #차집합 or print(s2.difference(s1))

#리스트, 튜플, 딕셔너리(중복을 허용하지 않고 키와 밸류값을 가진다), 셋(중복을 허용하지 않고 키값만 가진다.)




