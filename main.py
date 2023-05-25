import pandas as pd

# Create a DataFrame
data = {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
        'B': ['one', 'one', 'two', 'two', 'two', 'one', 'two', 'one'],
        'C': [1, 2, 3, 4, 5, 6, 7, 8],
        'D': [10, 20, 30, 40, 50, 60, 70, 80]}

df = pd.DataFrame(data)

# Group by column 'A' and 'B' without setting the groups as the index
grouped = df.groupby(['A', 'B'], as_index=False)
#grouped = df.groupby(['A', 'B']).groupby(['A']).size().unstack()
grouped1 = df.groupby(['A', 'B'])

# Perform an aggregation operation on the groups, for example, calculating the sum
result = grouped.sum()
result1 = grouped1.sum()

print(result)
print(result1)