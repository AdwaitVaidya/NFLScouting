import pandas as pd


data = pd.read_csv("data/pffScoutingData.csv")
grouped = data.groupby(data.pff_role)
df_new = grouped.get_group("Pass")
print(df_new)