#조건문
a = 2 
if (a==1):
    print(1)
else:
    print("1 아님")

if (a==1):
    print(1)
elif(a ==2 ):
    print(2)
else:
    print(3)

x=3
y=2
print(x==y)
print(x!=y)
money = 1300
if money >=1200 and money <3500:
    print('버스를 탈 수 있다')
    
print(1 in [1,2,3])
print(x in [1,2,3])
print(x not in [1,2,3])
print('i' not in 'python')

if money <10:
    pass
else:
    print('save it')

# 반복문
for i in [1,2,3]:
    print(i)

for i in (1,2,3):
    print(i)
for i in {1,2,3}:
    print(i)

for i in 'Hello':
    print(i)
    #print(i, end='     ')

# test_list라는 객체를 생성 one two three
test_list = ['one', 'two', 'three']
# test_list의 값을 반복문을 이용해서 하나씩 출력
for i in test_list:
    print(i)
# one! two! three!
for i in test_list:
    x = i+'!'
    print(x)
    #print(i, end='!') #print(i+'!')

number = 0
for score in[90,25,67,45,93]:
    number +=1
    if score >=60:
        print("%d 학생은 합격입니다." % number)
    else:
        print("%d 학생은 불합격입니다." % number)

num = 5
while (num>0):
    print(num)
    num-=1

#while 문 이용하여 num = 10
#10 9 8 7 --end-- 출력
num = 10
while (num > 0):
    if (num == 6):
        print('---end---')
        break
    print(num, end=' ' )
    num -=1

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i, end=' ')
print()
for i in range(10):
    print(i, end=' ')
print()
print('==========================================')
#100까지 수의 범위 안에서 7의 배수와 합계 출력
total=0
for i in range(101):
    if (i !=0 | i % 7 == 0):
        total += i
        print(i, end=' ')
        
print("\ntotal: ",total)
    
#한행에 3개씩 출력
for i in range(3):
    for j in range(3):
        print('*', end = ' ')
    print()
print('=====================================')
i = 0
while i <5:
    i+=1
    print('*'*i)


