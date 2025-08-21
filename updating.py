import pandas as pd

data = {
    "name" : ["aman","naman","taman","raman","chaman"],
    "age" : [23,32,23,23,32],
    "salary" : [243324,23434,234342,23434,2343]
}

df = pd.DataFrame(data)
print(df)

# updating dataframe
df.loc[0,"salary"] = 68768678877
print(df)

