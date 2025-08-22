import pandas as pd

df_customers = pd.DataFrame({
    'customerid':[1,2,3],
    'name':['ramesh','suresh','monkesh']
})

df_orders = pd.DataFrame({
    'customerid':[1,2,4],
    'orderamount':[242,343,454]
})


# df_merged = pd.merge(df_customers, df_orders, on="customerid", how="inner")
# print('inner join')
# print(df_merged)

# df_merged = pd.merge(df_customers, df_orders, on="customerid", how="outer")
# print('outer join')
# print(df_merged)


# df_merged = pd.merge(df_customers, df_orders, on="customerid", how="left")
# print('left join')
# print(df_merged)


df_merged = pd.merge(df_customers, df_orders, on="customerid", how="right")
print('right join')
print(df_merged)


