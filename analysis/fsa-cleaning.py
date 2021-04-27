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
export = pivot[["857"]]


# Join ICES vaccination rate data to census data.
export = export.join(ices_data[["% Vaccinated with at least 1 dose\n(All ages)"]], on="GEO_NAME")

# Rename columns to make more sense, and convert low income to true percentage.
export.rename(columns={"857": "Low income", "% Vaccinated with at least 1 dose\n(All ages)": "% vaccinated"}, inplace=True)
export["Low income"] = export["Low income"].str.replace("...", "0", regex=False).astype(float) / 100

# Reorder first two columns so vaccine rate is first.
export = export[["% vaccinated", "Low income"]]

# Calculate % columns for each FSA.
export["% visible minority"] = pivot["1324"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["% manufacturing"] = pivot["1904"].astype(float) / pivot["1897"].astype(float)
export["% wholesale trade"] = pivot["1905"].astype(float) / pivot["1897"].astype(float)
export["% transportation and warehousing"] = pivot["1907"].astype(float) / pivot["1897"].astype(float)
export["% retail trade"] = pivot["1906"].astype(float) / pivot["1897"].astype(float)
export["% information and cultural industries"] = pivot["1908"].astype(float) / pivot["1897"].astype(float)
export["% construction"] = pivot["1903"].astype(float) / pivot["1897"].astype(float)
export["% education services"] = pivot["1914"].astype(float) / pivot["1897"].astype(float)
export["% health care and social services"] = pivot["1915"].astype(float) / pivot["1897"].astype(float)
export["% accommodation and food services"] = pivot["1917"].astype(float) / pivot["1897"].astype(float)
export["% english nor french"] = pivot["104"].astype(float) / pivot["100"].astype(float)
export["median individual income"] = pivot["663"].astype(float)
export["average individual income"] = pivot["674"].astype(float)
export["income - % in bottom decile"] = pivot["836"].astype(float) / pivot["834"].astype(float)
export["income - % in top decile"] = pivot["846"].astype(float) / pivot["834"].astype(float)
export["average age"] = pivot["39"].astype(float)
export["median age"] = pivot["40"].astype(float)
export["population"] = pivot["1"].astype(float)
export["% commuting by car or truck as driver"] = pivot["1931"].astype(float) / pivot["1930"].astype(float)
export["% commuting by car or truck as passenger"] = pivot["1932"].astype(float) / pivot["1930"].astype(float)
export["% commuting by vehicle"] = pivot["1932"].astype(float) / pivot["1930"].astype(float)
export["% commuting by public transit"] = pivot["1933"].astype(float) / pivot["1930"].astype(float)
export["% commuting by walking"] = pivot["1934"].astype(float) / pivot["1930"].astype(float)
export["% commuting by bicycle"] = pivot["1935"].astype(float) / pivot["1930"].astype(float)
export["% commuting by other method"] = pivot["1936"].astype(float) / pivot["1930"].astype(float)
export["% leaving for work between 5am and 6am"] = pivot["1944"].astype(float) / pivot["1943"].astype(float)
export["% leaving for work between 6am and 7am"] = pivot["1945"].astype(float) / pivot["1943"].astype(float)
export["% leaving for work between 7am and 8am"] = pivot["1946"].astype(float) / pivot["1943"].astype(float)
export["% leaving for work between 8am and 9am"] = pivot["1947"].astype(float) / pivot["1943"].astype(float)
export["% leaving for work between 9am and 12pm"] = pivot["1948"].astype(float) / pivot["1943"].astype(float)
export["% leaving for work between 12pm and 5am"] = pivot["1949"].astype(float) / pivot["1943"].astype(float)
export["% first generation immigrants"] = pivot["1279"].astype(float) / pivot["1278"].astype(float)
export["% second generation immigrants"] = pivot["1280"].astype(float) / pivot["1278"].astype(float)
export["% third generation or more immigrants"] = pivot["1281"].astype(float) / pivot["1278"].astype(float)

# Drop FSAs with no vaccination value (ie. not in Toronto).
export.dropna(subset=["% vaccinated"], inplace=True)
# Save and print results.
export.to_csv("../data/data-fsa-clean.csv")
print(export)