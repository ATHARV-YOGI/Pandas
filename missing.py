import pandas as pd

data = {
    "name" : ["aman",None, "naman","taman","raman","chaman"],
    "age" : [23,None,32,23,23,32],
    "salary" : [243324,None,23434,234342,23434,2343]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())