import pandas as pd

# read data from csv file into a dataframe
# df = pd.read_csv("industry.csv", encoding="latin1")
# df = pd.read_excel("file_example_XLSX_10.xlsx")
df = pd.read_json("sample1.json", orient='index')

print(df)