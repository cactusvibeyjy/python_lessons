def separate():
    a = int(input('수 입력: '))
    if a % 2 == 0:
        print('짝수')
    else:
        print('홀수')

def addResult(a,b):
    return a+b

#문제
nums = [1,1,1,2,2,3,2,3,2,3,3,3,1]
def max_count(num):
    counts={} #딕셔너리로 선언함
    for i in num:
        if i in counts:
            counts[i] +=1
        else:
            counts[i] = 1

# counts = max_count(nums)
# print(counts) #{1:4, 2:4, 3:5}
# print("counts 최대 값", max(counts.values()))
# ####################
# first = [] #list 형
# maxValue = max(counts.values())
# for name, count in counts.items():
#     print(name, ";", count)
#     if(count == maxValue):
#             first.append(count)
# print('first:', first)
       
#     return counts
# nums = [1,1,1,2,2,3,2,3,2,3,3,3,1]
# def max_count(nums):
#      max_count={} #딕셔너리로 선언함
#     for i in nums:
#             max_count[i] = nums.count(i)
#     return max_count






#separate()

print(addResult(3,5))
ret = addResult(10,20)
print(ret)
#print(sum(10)) #1부터 10까지의 합을 출력
def sum(num):
    total = 0
    for i in range(1,num+1):
        total += i
    return total
print("sum: ", sum(10))
dict = {1:4, 2:4, 3:5}
if 1 in dict: 
    print('yes')
else: 
    print('no')

