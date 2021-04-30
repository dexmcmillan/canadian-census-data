import pandas as pd
import numpy as np

# Read in data.
data = pd.read_csv("../data/neighbourhood-profiles-2.csv")

# Bring in covid infection data.
infection_rates = pd.read_csv("../data/covid-cases.csv")
infection_rates.set_index("Neighbourhood Number", inplace=True)

data = data.transpose()
data = data.rename(columns=data.loc["MEMBER_ID"])
data = data.drop(["Category", "Topic", "Data Source", "City of Toronto", "TOR_Code"], axis=0)
data.set_index("Neighbourhood Number", inplace=True)

data.columns = data.columns.astype(str)
data = data.rename(columns={"index": "name"})
print(data)
# data.dropna(axis=1, inplace=True)

export = data[["Characteristic"]]

print(export)

export = export.join(infection_rates)

export["minority - % visible minority"] = data["1324"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % not visible minority"] = data["1337"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % south asian"] = data["1325"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % chinese"] = data["1326"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % black"] = data["1327"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % filipino"] = data["1328"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % latin american"] = data["1329"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % arab"] = data["1330"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % southeast asian"] = data["1331"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % west asian"] = data["1332"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % korean"] = data["1333"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["minority - % japanese"] = data["1334"].replace(',', "").astype(float) / data["1323"].replace(',', "").astype(float)
export["industry - % manufacturing"] = data["1904"].astype(float) / data["1897"].astype(float)
export["industry - % wholesale trade"] = data["1905"].astype(float) / data["1897"].astype(float)
export["industry - % transportation and warehousing"] = data["1907"].astype(float) / data["1897"].astype(float)
export["industry - % retail trade"] = data["1906"].astype(float) / data["1897"].astype(float)
export["industry - % information and cultural industries"] = data["1908"].astype(float) / data["1897"].astype(float)
export["industry - % construction"] = data["1903"].astype(float) / data["1897"].astype(float)
export["industry - % education services"] = data["1914"].astype(float) / data["1897"].astype(float)
export["industry - % health care and social services"] = data["1915"].astype(float) / data["1897"].astype(float)
export["industry - % accommodation and food services"] = data["1917"].astype(float) / data["1897"].astype(float)
export["industry - % mining, quarrying and oil and gas extraction"] = data["1901"].astype(float) / data["1897"].astype(float)
export["industry - % utilities"] = data["1902"].astype(float) / data["1897"].astype(float)
export["industry - % agriculture, forestry, fishing and hunting"] = data["1900"].astype(float) / data["1897"].astype(float)
export["industry - % information and cultural industries"] = data["1908"].astype(float) / data["1897"].astype(float)
export["industry - % finance and insurance"] = data["1909"].astype(float) / data["1897"].astype(float)
export["industry - % real estate and rental and leasing"] = data["1910"].astype(float) / data["1897"].astype(float)
export["industry - % professional, technical and scientific enterprises"] = data["1911"].astype(float) / data["1897"].astype(float)
export["industry - % management of companies and enterprises"] = data["1912"].astype(float) / data["1897"].astype(float)
export["industry - % administrative, support, waste management and remediation services"] = data["1913"].astype(float) / data["1897"].astype(float)
export["industry - % arts, entertainment and recreation"] = data["1916"].astype(float) / data["1897"].astype(float)
export["industry - % other services (except public administration)"] = data["1918"].astype(float) / data["1897"].astype(float)
export["industry - % public administration"] = data["1919"].astype(float) / data["1897"].astype(float)

print(export)
export.to_csv("./data-other.csv")