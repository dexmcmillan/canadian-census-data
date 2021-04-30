import pandas as pd
import numpy as np

# Read in data. This set is not included in github repo because it is too large.
# Download from https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/details/page_Download-Telecharger.cfm?Lang=E&Tab=1&Geo1=PR&Code1=01&Geo2=PR&Code2=01&SearchText=Canada&SearchType=Begins&SearchPR=01&B1=All&TABID=1&type=0.
data = pd.read_csv("../data/data-all.csv")

# Filter for Ontario FSAs.
ontario = (data[
    data["GEO_NAME"].str.contains("(H|M|L|K|N|P)[A-Z0-9]{2}")]
    )

# Save file.
ontario.to_csv("./data-ontario-fsa.csv")