import pandas as pd

data = {
    "Name" : ['Ram', 'Shyam', 'Shubh','Ishan'],
    "Age" : [10,20,30,40],
    "salary" : [23434,3243,3455,234232],
    "perfomance score" : [34,56,54,43]
}

df = pd.DataFrame(data)
print("sample dataframe")
print(df)
print('descriptive statistics')
print(df.describe)
