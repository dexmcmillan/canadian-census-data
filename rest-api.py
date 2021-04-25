import pandas as pd
import numpy as np
import requests as requests

# This code generates a list of DGUIDs used by the following API call to get data.
# The list will be iterated through and separate calls will be made for each.
code = requests.get('https://www12.statcan.gc.ca/rest/census-recensement/CR2016Geo.json?lang=E&geos=FSA&cpt=35')
df_code = pd.json_normalize(data=code.json(), record_path="DATA", errors="ignore")

codes = []
for i in df_code[0]:
    codes.append(i)

# Define a place to collect all our separate HTTP calls.
df_all = []

# Make a separate API call for each item in codes list and push the results to df_all list.
for code in codes:
    x = requests.get('https://www12.statcan.gc.ca/rest/census-recensement/CPR2016.json?lang=E&dguid='+ code + '&topic=14&notes=0&stat=1')
    json = x.json()
    df = pd.json_normalize(data=json, record_path="DATA", errors="ignore")
    df.rename(columns={0: "region_code", 1: 'region'}, inplace=True)
    df_all.append(df)

# Take all of the dataframes in our df_all list and concatenate them into one big dataframe.
df_final = pd.concat(df_all)

# Print and save to CSV.
print(df_final)
filtered.to_csv(r'./data-minorities-rate.csv', index=True, header=True)