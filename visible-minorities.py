import pandas as pd
import numpy as np

# Read in the full dataset downloaded from StatsCan, split by FSAs.
# Data is not included in this repo as it's too large. Please download from
# https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/details/page_Download-Telecharger.cfm?Lang=E&Tab=1&Geo1=PR&Code1=01&Geo2=PR&Code2=01&SearchText=Canada&SearchType=Begins&SearchPR=01&B1=All&TABID=1&type=0.
df = pd.read_csv("./data.csv")

# Filter for only Ontario FSAs (starting with K, L, N, or P)
ontario = df[df["GEO_NAME"].str.contains("[K|L|N|P][0-9][A-Z]", regex=True)]

# Get only the total visible minority rows.
minorities = ontario[ontario["DIM: Profile of Forward Sortation Areas (2247)"].str.contains("Total - Visible minorit")]

# Strip out irrelevant columns.
filtered = minorities[["GEO_NAME", "DIM: Profile of Forward Sortation Areas (2247)", "Dim: Sex (3): Member ID: [1]: Total - Sex"]]

# Save to CSV.
filtered.to_csv(r'./data-output.csv', index=True, header=True)