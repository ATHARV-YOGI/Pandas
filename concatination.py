import pandas as pd

df_region1 = pd.DataFrame({
    'customerid':[1,2],
    'name':['gopal','bhopal']
})

df_region2 = pd.DataFrame({
    'customerid':[3,4],
    'name':['shyam','baburao']
})

# vertically
# df_concat = pd.concat([df_region1,df_region2],ignore_index=True)
# print(df_concat)


df_concat = pd.concat([df_region1,df_region2],axis=1,ignore_index=True)
print(df_concat)