import pandas as pd
df = pd.read_json("sample1.json", orient='index')

print('display 2 rows of the first')
print(df.head(2))

print('display 2 rows of last')
print(df.tail(2))