import pandas as pd
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_colwidth', 20)

print("\n\n1. 데이터를 로드하라. 데이터는 '\\t'을 기준으로 구분되어있다. ▼")
data_url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(data_url, sep='\t')
print("type(df) : {}".format(type(df)))

print("\n\n2. 데이터의 상위 5개 행을 출력하라 ▼")
상위5개 = df.head(5)
print("상위5개 ∨\n{}".format(상위5개))
하위5개 = df.tail(5)
print("하위5개 ∨\n{}".format(하위5개))

print("\n\n3. 데이터의 행과 열의 갯수를 파악하라 ▼")
print(df.shape)
print('행:',df.shape[0])
print('열:',df.shape[1])

print("\n\n4. 전체 컬럼 출력 ▼")
print(df.columns)

print("\n\n5. 6번째 컬럼명을 출력하라 ▼")
print(df.columns[5])

print("\n\n6. 6번째 컬럼의 데이터 타입을 확인하라 ▼")
print(df.iloc[:,5].dtype)
print(df.iloc[3:10,2:4])

print("\n\n7. 데이터셋의 인덱스 구성은 어떤가 ▼")
print(df.index)

print("\n\n8. 6번째 컬럼의 3번째 값은 무엇인가? ▼")
print(df.iloc[2,5])

print("\n\n9. 데이터를 로드하라. 컬럼이 한글이기에 적절한 처리해줘야함 ▼")
df1 = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv", encoding="euc-kr")
print(df1)

print("\n\n10. 데이터 마지막 3개행을 출력하라 ▼")
print(df1.tail(3))

print("\n\n11. 수치형 변수를 가진 컬럼을 출력하라 ▼")
print(df1.select_dtypes(exclude=object).columns)

print("\n\n12. 범주형 변수를 가진 컬럼을 출력하라 ▼")
print(df1.select_dtypes(include=object).columns)

print("\n\n13. 각 컬럼의 결측치 숫자를 파악하라 ▼")
print(df1.isnull().sum())

print("\n\n14. 각 컬럼의 데이터수, 데이터타입을 한번에 확인하라 ▼")
print(df1.info())

print("\n\n 15. 각 수치형 변수의 분포(사분위, 평균, 표준편차, 최대 , 최소)를 확인하라 ▼")
ans = df1.describe()
print(ans)

print("\n\n 16. 거주인구 컬럼의 값들을 출력하라 ▼")
print(df1['거주인구'])

print("\n\n 17. 평균 속도 컬럼의 4분위 범위(IQR) 값을 구하여라 ▼")
print(df1['평균 속도'].quantile(.75) - df1['평균 속도'].quantile(.25))

print("\n\n18. 읍면동명 컬럼의 유일값 갯수를 출력하라. ▼")
print(df1['읍면동명'].nunique())

print("\n\n19. 읍면동명 컬럼의 유일값을 모두 출력하라. ▼")
print(df1['읍면동명'].unique())