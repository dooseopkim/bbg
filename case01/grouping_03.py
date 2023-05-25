import pandas as pd
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print("44. 데이터를 로드하고 상위 5개 컬럼을 출력하라")
df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv")
print(type(df))
print(df.head())

print("\n\n45. 데이터의 각 host_name의 빈도수를 구하고 host_name으로 정렬하여 상위 5개를 출력하라 ▼")
result = df.groupby('host_name').size()
print("\ndf.groupby('host_name').size() : \n{}".format(result))
result = df['host_name'].value_counts().sort_index()
print("\ndf.groupby('host_name').size() : \n{}".format(result))

print("\n\n46. 데이터의 각 host_name의 빈도수를 구하고 빈도수 기준 내림차순 정렬한 데이터 프레임을 만들어라. 빈도수 컬럼은 counts로 명명하라 ▼")
result = df.groupby('host_name').size().\
    to_frame().rename(columns={0:'counts'}).\
    sort_values('counts', ascending=False)
print("\n{}".format(result))

print("\n\n47. neighbourhood_group의 값에 따른 neighbourhood컬럼 값의 갯수를 구하여라 ▼")
result = df.groupby(['neighbourhood_group','neighbourhood'], as_index=False).size()
print("\n{}".format(result))

print("\n\n48. neighbourhood_group의 값에 따른 neighbourhood컬럼 값 중 neighbourhood_group그룹의 최댓값들을 출력하라 ▼")
result = df.groupby(['neighbourhood_group','neighbourhood'], as_index=False).size().\
    groupby(['neighbourhood_group'], as_index=False).max()
print("\n{}".format(result))

print("\n\n49. neighbourhood_group 값에 따른 price값의 평균, 분산, 최대, 최소 값을 구하여라 ▼")
result = df[['neighbourhood_group','price']].groupby('neighbourhood_group').agg(['mean','var','max','min'])
print("\n{}".format(result))

print("\n\n50. neighbourhood_group 값에 따른 reviews_per_month 평균, 분산, 최대, 최소 값을 구하여라 ▼")
result = df[['neighbourhood_group','reviews_per_month']].groupby('neighbourhood_group').agg(['mean','var','max','min'])
print("\n{}".format(result))

print("\n\n51. neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 구하라 ▼")
result = df.groupby(['neighbourhood', 'neighbourhood_group'])['price'].mean()
print("\n{}".format(result))

print("\n\n52. neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하라 ▼")
result = df.groupby(['neighbourhood','neighbourhood_group']).price.mean().unstack()
print("\n{}".format(result))
################################################################
print("\n\n53. neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하고 nan 값은 -999값으로 채워라 ▼")
result = df.groupby(['neighbourhood','neighbourhood_group']).price.mean().unstack().fillna(-999)
print("\n{}".format(result))

print("\n\n54. 데이터중 neighbourhood_group 값이 Queens값을 가지는 데이터들 중 neighbourhood 그룹별로 price값의 평균, 분산, 최대, 최소값을 구하라 ▼")
result = df[df.neighbourhood_group=='Queens'].groupby(['neighbourhood']).price.agg(['mean','var','max','min'])
print("\n{}".format(result))

print("\n\n55. 데이터중 neighbourhood_group 값에 따른 room_type 컬럼의 숫자를 구하고 neighbourhood_group 값을 기준으로 각 값의 비율을 구하여라 ▼")
result = df[['neighbourhood_group','room_type']].groupby(['neighbourhood_group','room_type']).size().unstack()
print("\n{}".format((result.values /result.sum(axis=1).values.reshape(-1,1))))
