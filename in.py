import pandas as pd

df = pd.read_json("sample1.json", orient = 'index')

print('displaying the info of data set')
print(df.info())