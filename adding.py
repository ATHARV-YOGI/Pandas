import pandas as pd

data = {
    "name" : ["aman", "naman","taman","chaman","sanam"],
    "age":[23,43,23,45,67],
    "salary":[23434,23443,43534,3454,35445],
    "perfomance score":[23,43,45,45,65]
}

df = pd.DataFrame(data)
print(df)

# adding new column name Bonus
df["Bonus"] = df['salary']*0.1 
print(df)

# adding new column name Bonus using insert() , mostly used method in companies
df.insert(0, "Employee ID", [10,20,30,40,50])
print(df)