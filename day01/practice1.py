import re

import pandas as pd


# 1.번 문제
str = '20201231Thursday'
year=(str[:4])
# year = re.findall('\d{4}', str)
print(year)
mmdd=(str[4:8])
print(mmdd)
day=(str[8:16])
print(day)

# 2.번 문제
a=['쓰','레','기','통']
a.reverse()
print(a)

# 3.번 문제
dic={
    'year' : 2020,
    'mm' : 12,
    'dd' : 31,
    'day' : 'Thursday',
    'weather': 'snow'
}
print(dic)

# 5.번 문제
i = 0
while i <5:
    i+=1
    print('*'*i)


# 6.번 문제 (가변 인자)
def avg(*args):
    x=0
    for i in args:
        x+=i

    return x/len(args)
print(avg(5,3,12,9))
print(avg(2.4,3.2,7.3))
print(avg(10,5))
        
# a1 = [5,3,12,9]
# avg1 = sum(a1) / len(a1)
# print(avg1)
# a2 = [2.4, 3.2, 7.3]
# avg2 = sum(a2) / len(a2)
# print(avg2)
# a3 = [10,5]
# avg3 = sum(a3) / len(a3)
# print(avg3)

# 7.번 문제
table = pd.DataFrame([
    [500,450,520,610],
    [690,700,820,900],
    [1100,1030,1200,1380],
    [1500,1650,1700,1850],
    [1990,2020,2300,2420],
    [1020,1600,2200,2550]
], index = ['2015','2016','2017','2018', '2019', '2020'], columns = ['1분기', '2분기', '3분기', '4분기'])
table.to_csv('c:/test/practice.csv', header='False')
print(table)