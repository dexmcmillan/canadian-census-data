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


data["% visible minority"] = data["Total visible minority population"].replace(',', "").astype(float) / (data["Total visible minority population"].replace(',', "").astype(float) + data["Not a visible minority"].replace(',', "").astype(float))
data.sort_values("% visible minority", inplace=True)
export = data[["Neighbourhood Number", "name", "% visible minority", "Prevalence of low income based on the Low-income cut-offs, after tax (LICO-AT) (%)"]]
export["Prevalence of low income based on the Low-income cut-offs, after tax (LICO-AT) (%)"] = export["Prevalence of low income based on the Low-income cut-offs, after tax (LICO-AT) (%)"]/100
export.set_index("Neighbourhood Number", inplace=True)
print(export)
export.to_csv("./data-other.csv")