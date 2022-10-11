import pandas as pd
df = pd.read_csv('day03/survey.csv')
print(df[:5]) #print(df.head()) => head 는 다섯개만 출력해줌

print(df.mean())
#수입의 평균만 구하기

print(df['income'].mean()) #print('수입의 평균 : ', df.income.mean())
#반올림해서 출력 round
print('수입을 반올림한 평균 : ', round(df.income.mean(),1))
print('수입의 합계: ', df.income.sum())
print('수입의 중간 값: ', df.income.median())
print(df.describe())
print(df.income.describe())
print('====='*20)
print(df.sex.value_counts())
