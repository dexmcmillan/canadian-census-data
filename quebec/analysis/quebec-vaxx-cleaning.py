import pandas as pd
import numpy as np

# Read in ICES vaccination rate FSA data and set index to be the same as census data (FSA).
data = pd.read_csv("../data/data-quebec-vaxx.csv")


transposed = data.transpose()
transposed = transposed.rename(columns=transposed.loc["date"])
transposed.drop(["date"], inplace=True)
transposed = transposed[["2021-04-28"]]
transposed["tosplit"] = transposed.index
labels = transposed["tosplit"].str.split("_", expand=True)
labels.columns = labels.columns.astype(str)

labels.rename(columns={"0": "region"}, inplace=True)
labels = labels[labels["2"] == "Total"]
labels = labels[labels["3"] == "cumu"]
labels["region"] = labels["region"].str.replace("RSS0?", "")
labels = labels[labels["region"] != "99"]
export = labels.join(transposed)
export.set_index("region", inplace=True)
export.rename(columns={"2021-04-28": "vaccines_given"}, inplace=True)
export = export[["vaccines_given"]]



# export.to_csv("../data/data-quebec-vaxx-clean.csv")
print(export)

