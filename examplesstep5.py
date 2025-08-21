import pandas as pd

data = {
    "name":["ishan" , "shubh","nitin"],
    "age":[34,34,34],
    "salary":[32434,23424,234423],
    "perfomance score":[23,32,32,]
}

df = pd.DataFrame(data)
print("sample dataframe")
print(df)

print("names (single column series)")
name=df['name']
print(name)

subset = df[['name' , 'age']]
print(subset)