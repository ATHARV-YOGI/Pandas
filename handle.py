import pandas as pd

data = {
    "name" : ["aman",None, "naman","taman","raman","chaman"],
    "age" : [23,None,32,23,23,32],
    "salary" : [243324,None,23434,234342,23434,2343]
}

df = pd.DataFrame(data)
print(df)

# #remove NUll values
# df.dropna(inplace=True)
# print(df)



# #put 0 at the Null values
# df.fillna(0,inplace=True)
# print(df)


# fill age column with mean value
df['age'].fillna(df['age'].mean(),inplace=True)
print(df)