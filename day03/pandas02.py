from encodings import utf_8
import pandas as pd
#name => 'Mark','Jane','aaa', 'rr'
#age => 33,44,55,11
#score => 91.2,88.5,55.6,88.9

data ={
    'name' :['Mark','Jane','aaa', 'rr'],
    'age' :[33,44,55,11],
    'score' : [91.2,88.5,55.6,88.9]
}
print(data)
print('========================================================================')
df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.sum())
print(df.mean())
print(df.age)
print(df['age'])

data_dic = {
    'year' : [2018, 2019, 2020,2021,2022],
    'sales' : [350, 400,1050,2000,1000]
}
df2 = pd.DataFrame(data_dic)
print(df2)

df3 = pd.DataFrame([
    [89.2,92.5,90.8], [92.8,89.9,95.2]
], index =['중간고사', '기말고사'], columns = ['1반', '2반', '3반'])
print(df3)

df4 = pd.DataFrame([
    [89.2,92.5,90.8], [92.8,89.9,95.2]
], columns = ['1반', '2반', '3반'])

df4.index = ['중간고사1', '기말고사2']
print(df4)

df5 = pd.DataFrame([
    [89.2,92.5,90.8], [92.8,89.9,95.2]
])
df5.index = ['중간5고사', '기말5고사']
df5.columns = ['A', 'B', 'C']
print(df5)

print('========================================================================')

print(df3.sum())
print(df3.mean())
#1반의 합계
print(df3['1반'].sum())

print(df3['1반'].mean())
print(df3.loc['중간고사'].sum())
#df5를 df5.csv로 내보내기
# df5.to_csv('df5.csv', header='False')
df5_read = pd.read_csv('df5.csv', encoding='utf-8')
print(df5_read)


