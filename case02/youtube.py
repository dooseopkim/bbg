import pandas as pd
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_colwidth', 200)

df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv",index_col=0)
# print(df.head())


# 인기동영상 제작횟수가 많은 채널 상위 10개명을 출력하라 (날짜기준, 중복포함)
answer = list(df.loc[df.channelId.isin(df.channelId.value_counts().head(10).index)].channelTitle.unique())
print(df.channelId)
print(df.channelId.value_counts())
print(df.channelId.value_counts().head(10))
print(df.channelId.value_counts().head(10).index)
print(df.channelId.isin(df.channelId.value_counts().head(10).index))
print(df.loc[df.channelId.isin(df.channelId.value_counts().head(10).index)])
print(df.loc[df.channelId.isin(df.channelId.value_counts().head(10).index)].channelTitle)
print(df.loc[df.channelId.isin(df.channelId.value_counts().head(10).index)].channelTitle.unique())
print(list(df.loc[df.channelId.isin(df.channelId.value_counts().head(10).index)].channelTitle.unique()))

# 논란으로 인기동영상이 된 케이스를 확인하고 싶다. dislikes수가 like 수보다 높은 동영상을 제작한 채널을 모두 출력하라
print([df.likes < df.dislikes])
print(df.loc[df.likes < df.dislikes])
print(df.loc[df.likes < df.dislikes].channelTitle.unique())
print(df.loc[df.likes < df.dislikes].channelId.value_counts())

# 채널명을 바꾼 케이스가 있는지 확인하고 싶다. channelId의 경우 고유값이므로 이를 통해 채널명을 한번이라도 바꾼 채널의 갯수를 구하여라
print(df[['channelTitle', 'channelId']])
print(df[['channelTitle', 'channelId']].drop_duplicates())
print(df[['channelTitle', 'channelId']].drop_duplicates().channelId)
print(df[['channelTitle', 'channelId']].drop_duplicates().channelId.value_counts())
change = df[['channelTitle', 'channelId']].drop_duplicates().channelId.value_counts()
print(len(change[change > 1]))

# 일요일에 인기있었던 영상들중 가장많은 영상 종류(categoryId)는 무엇인가?
print(df[['trending_date2']])
# print(pd.to_datetime(df[['trending_date2']]))
df['trending_date2'] = pd.to_datetime(df['trending_date2'])
print(df[['trending_date2']])
print(df.loc[df['trending_date2'].dt.day_name() == 'Sunday'].categoryId)
print(df.loc[df['trending_date2'].dt.day_name() == 'Sunday'].categoryId.value_counts())
print(df.loc[df['trending_date2'].dt.day_name() == 'Sunday'].categoryId.value_counts().index[0])

# 각 요일별 인기 영상들의 categoryId는 각각 몇개 씩인지 하나의 데이터 프레임으로 표현하라
print(df['trending_date2'].dt.day_name())
print(df.groupby([df['trending_date2'].dt.day_name(), 'categoryId']))
print(df.groupby([df['trending_date2'].dt.day_name(), 'categoryId'], as_index=False))
print(df.groupby([df['trending_date2'].dt.day_name(), 'categoryId'], as_index=False).size())
group = df.groupby([df['trending_date2'].dt.day_name(), 'categoryId'], as_index=False).size()
answer = group.pivot(index='categoryId', columns='trending_date2')
print(answer)

# 댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다. viewcount대비 댓글수가 가장 높은 영상을 확인하라 (view_count값이 0인 경우는 제외한다)
target2= df.loc[df.view_count!=0]
t = target2.copy()
t['ratio'] = (target2['comment_count']/target2['view_count']).dropna()
result = t.sort_values(by='ratio', ascending=False).iloc[0].title
print(t['ratio'])
print(t.sort_values(by='ratio', ascending=False))
print(t.sort_values(by='ratio', ascending=False).iloc[0:5])
print(t.sort_values(by='ratio', ascending=False).iloc[0].title)
print(result)
