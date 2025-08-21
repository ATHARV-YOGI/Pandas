import pandas as pd

data = {
    "name" : ["ishan","kishan","nishan","ankit","naman","aman"],
    "age" : [34,34,23,5,4,3],
    "salary" : [34234,234324,43253,345,34543,2323],
    "perfomance score": [34,65,35,34,32,23]
}

df = pd.DataFrame(data)
print(df)
print(f'shape:{df.shape}')
print(f'column name: {df.columns}')
