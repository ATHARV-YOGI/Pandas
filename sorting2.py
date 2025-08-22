import pandas as pd

data = {
    "name":["aman","naman","taman","chaman"],
    "age":[23,12,24,55],
    "salary":[23323,54566,23434,643534]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by=["age", "salary"], ascending=[True,False], inplace=True)
print('sorted age by descending')
print(df)