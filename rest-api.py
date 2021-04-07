import pandas as pd
import numpy as np
import requests as requests

# WIP for grabbing data through HTTP request.
x = requests.get('https://www12.statcan.gc.ca/rest/census-recensement/CPR2016.json?lang=E&dguid=2016A001111124&topic=14&notes=0&stat=0')
json = x.json()
df = pd.json_normalize(data=json, record_path="DATA", errors="ignore")
df.rename(columns={0: "region_code", 1: 'region'}, inplace=True)
