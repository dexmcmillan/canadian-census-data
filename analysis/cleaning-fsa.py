import pandas as pd
import numpy as np

# Read in data from Ontario census file (a subset of data-all.csv processed with ontario.py)
data = pd.read_csv("../data/data-ontario-fsa.csv")

# Read in ICES vaccination rate FSA data and set index to be the same as census data (FSA).
ices_data = pd.read_csv("../data/data-ices-vaccination.csv")
ices_data.set_index("FSA", inplace=True)

# The census data has white space on either side of the names so it needs to be trimmed.
data = data.rename(columns=lambda x: x.strip())

# Get rid of some str values from our main values column.
data["Dim: Sex (3): Member ID: [1]: Total - Sex"] = data["Dim: Sex (3): Member ID: [1]: Total - Sex"].str.replace(repl="0", pat="x", regex=True)

# Reshape table to have FSAs as index and convert new column labels to strings.
pivot = pd.pivot(data, index="GEO_NAME", columns=["Member ID: Profile of Forward Sortation Areas (2247)"], values="Dim: Sex (3): Member ID: [1]: Total - Sex")
pivot.columns = pivot.columns.astype(str)

# Create a new dataframe and load up low income stat (see readme in statscan download)
export = pivot[["862"]]
export.rename(columns={"862": "Low income"}, inplace=True)

# Join ICES vaccination rate data to census data.
export = export.join(ices_data[["% Vaccinated with at least 1 dose\n(All ages)"]], on="GEO_NAME")

# Reorder first two columns so vaccine rate is first.
export = export[["% Vaccinated with at least 1 dose\n(All ages)", "Low income"]]

# Calculate visible minority % for each FSA.
export["% visible minority"] = pivot["1324"].replace(',', "").astype(float) / (pivot["1324"].replace(',', "").astype(float) + pivot["1337"].replace(',', "").astype(float))

# Drop FSAs with no vaccination value (ie. not in Toronto).
export.dropna(subset=["% Vaccinated with at least 1 dose\n(All ages)"], inplace=True)

# Save and print results.
export.to_csv("../data/data-fsa-clean.csv")
print(export)