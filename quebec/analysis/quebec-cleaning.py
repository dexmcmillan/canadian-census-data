import pandas as pd
import numpy as np

# Read in data from Ontario census file (a subset of data-all.csv processed with ontario.py)
data = pd.read_csv("../data/data-quebec-census.csv")
vaxx = pd.read_csv("../data/data-quebec-vaxx-clean.csv")
print(data)

# The census data has white space on either side of the names so it needs to be trimmed.
data = data.rename(columns=lambda x: x.strip())

# Get rid of some str values from our main values column.
# data["total"].astype(str)
# data["total"] = data["total"].str.replace(repl="0", pat="x", regex=True)

# Reshape table to have FSAs as index and convert new column labels to strings.
pivot = pd.pivot(data, index="GEO_NAME", columns=["Member ID: Profile of Economic Regions (2247)"], values="total")
pivot.columns = pivot.columns.astype(str)
pivot["neighbourhood_number"] = [8, 1, 3, 17, 12, 9, 5, 11, 14, 15, 13, 4, 6, 16, 10, 7, 2]
pivot["neighbourhood_name"] = pivot.index
pivot.set_index("neighbourhood_number", inplace=True)

# Create a new dataframe and load up low income stat (see readme in statscan download)
export = pivot[["neighbourhood_name"]].join(vaxx)
export.rename(columns={"2021-04-28": "vaccination #"}, inplace=True)
export["vaccination %"] = export["vaccination #"] / (pivot["1"]*2)
export["population"] = pivot["1"]

# Calculate % columns for each FSA.
export["minority - % visible minority"] = pivot["1324"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % not visible minority"] = pivot["1337"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % south asian"] = pivot["1325"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % chinese"] = pivot["1326"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % black"] = pivot["1327"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % filipino"] = pivot["1328"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % latin american"] = pivot["1329"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % arab"] = pivot["1330"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % southeast asian"] = pivot["1331"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % west asian"] = pivot["1332"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % korean"] = pivot["1333"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["minority - % japanese"] = pivot["1334"].replace(',', "").astype(float) / pivot["1323"].replace(',', "").astype(float)
export["industry - % manufacturing"] = pivot["1904"].astype(float) / pivot["1897"].astype(float)
export["industry - % wholesale trade"] = pivot["1905"].astype(float) / pivot["1897"].astype(float)
export["industry - % transportation and warehousing"] = pivot["1907"].astype(float) / pivot["1897"].astype(float)
export["industry - % retail trade"] = pivot["1906"].astype(float) / pivot["1897"].astype(float)
export["industry - % information and cultural industries"] = pivot["1908"].astype(float) / pivot["1897"].astype(float)
export["industry - % construction"] = pivot["1903"].astype(float) / pivot["1897"].astype(float)
export["industry - % education services"] = pivot["1914"].astype(float) / pivot["1897"].astype(float)
export["industry - % health care and social services"] = pivot["1915"].astype(float) / pivot["1897"].astype(float)
export["industry - % accommodation and food services"] = pivot["1917"].astype(float) / pivot["1897"].astype(float)
export["industry - % mining, quarrying and oil and gas extraction"] = pivot["1901"].astype(float) / pivot["1897"].astype(float)
export["industry - % utilities"] = pivot["1902"].astype(float) / pivot["1897"].astype(float)
export["industry - % agriculture, forestry, fishing and hunting"] = pivot["1900"].astype(float) / pivot["1897"].astype(float)
export["industry - % information and cultural industries"] = pivot["1908"].astype(float) / pivot["1897"].astype(float)
export["industry - % finance and insurance"] = pivot["1909"].astype(float) / pivot["1897"].astype(float)
export["industry - % real estate and rental and leasing"] = pivot["1910"].astype(float) / pivot["1897"].astype(float)
export["industry - % professional, technical and scientific enterprises"] = pivot["1911"].astype(float) / pivot["1897"].astype(float)
export["industry - % management of companies and enterprises"] = pivot["1912"].astype(float) / pivot["1897"].astype(float)
export["industry - % administrative, support, waste management and remediation services"] = pivot["1913"].astype(float) / pivot["1897"].astype(float)
export["industry - % arts, entertainment and recreation"] = pivot["1916"].astype(float) / pivot["1897"].astype(float)
export["industry - % other services (except public administration)"] = pivot["1918"].astype(float) / pivot["1897"].astype(float)
export["industry - % public administration"] = pivot["1919"].astype(float) / pivot["1897"].astype(float)

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

# Save and print results.
export.to_csv("../data/data-quebec-clean.csv")
print(export)