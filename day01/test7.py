# f= open('c:/test/새파일.txt', 'w')
# print(f)
# f.close()

# f= open('c:/test/새파일.txt', 'w')
# for i in range(1,6):
#     data = '%d번째 줄입니다. \n' %i
#     f.write(data)
# f.close()

# f=open('c:/test/새파일.txt', 'a')
# for i in range(6,11):
#     data = '%d번째 줄입니다. \n' %i
#     f.write(data)
# f.close()

f=open('c:/test/새파일.txt', 'r')
line = f.readline()
print(line)


while True:
    line = f.readline()
    if not line :
        break
    print(line)

f.close()
print('-----------------------------')

f=open('c:/test/새파일.txt', 'r')
lines = f.readlines()
print(lines)
f.close()
print('-----------------------------')
f=open('c:/test/새파일.txt', 'r')
data = f.read()
print(data)
f.close()

#close를 포함한 구문
with open('c:/test/새파일.txt', 'w') as f:
    f.write('aa bb cc')
#with를 써서 이미 클로징 된 상태로 read 하면 오류 뜸
#data = f.read()
