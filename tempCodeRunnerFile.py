
df_merged = pd.merge(df_customers, df_orders, on="customerid", how="right")
print('right join')
print(df_merged)