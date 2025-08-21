import pandas as pd

data = {
    "name" : ["aman","naman","taman","chaman"],
    "age":[23,34,34,34],
    "salary":[23434,23434,32443,234324],
    "perfomance score":[3,23,32,32]
} 

df = pd.DataFrame(data)
print(df)

high_salary =  df[df['salary']>25000]
print('employees with salary > 25000')
print(high_salary)


filtered = df[(df['salary']>25000) & (df['age']>23)]
print(filtered)


filtered_or = df[(df['salary']>25000) | (df['perfomance score']>3)]
print(filtered_or)