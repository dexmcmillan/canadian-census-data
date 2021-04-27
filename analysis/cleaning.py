import pandas as pd
import numpy as np

# Read in data.
data = pd.read_csv("../data/neighbourhood-profiles.csv")

data = data.transpose()
data = data.rename(columns=data.loc["Characteristic"])
data = data.drop(["Category", "Topic", "Data Source", "City of Toronto", "Characteristic", "TOR_Code"], axis=0)
data.reset_index(inplace=True)
data = data.rename(columns=lambda x: x.strip())
data = data.rename(columns={"index": "name"})

export = data[["Neighbourhood Number", "name"]]

export["% visible minority"] = data["Total visible minority population"].replace(',', "").astype(float) / (data["Total visible minority population"].replace(',', "").astype(float) + data["Not a visible minority"].replace(',', "").astype(float))
export["Prevalence of low income based on the Low-income cut-offs, after tax (LICO-AT) (%)"] = data["Prevalence of low income based on the Low-income cut-offs, after tax (LICO-AT) (%)"]/100
export["Average total income in 2015 among recipients ($)"] = data["Average total income in 2015 among recipients ($)"].replace(",", "")
export.set_index("Neighbourhood Number", inplace=True)
print(export)
export.to_csv("./data-other.csv")