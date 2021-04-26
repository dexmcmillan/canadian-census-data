import pandas as pd
import numpy as np
import scipy.stats
from sklearn.impute import SimpleImputer

import matplotlib.pyplot as plt  # To visualize

# Read in data.
data = pd.read_csv("./data-combined.csv")

# A list that will store rows for the final export.
parts = []

# For each measure...
for col in range(20):
    
    # ...prepare the data...
    measure = data.columns[3+col]
    X = data.iloc[:, 2].values.reshape(-1, 1)  # values converts it into a numpy array
    Y = data.iloc[:, 3+col].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
    print(data.columns[2])
    # (this handles any blank or N/A values in the data.)
    imputer = SimpleImputer()
    Y = imputer.fit_transform(Y)

    result = scipy.stats.linregress(X[:,0], Y[:,0])
    r_value = result.rvalue
    p_value = result.pvalue

    # ..and finally put into a new dataframe that will be concatenated together at the end.
    row = pd.DataFrame([[measure, '{:f}'.format(r_value), '{:f}'.format(p_value)]], columns=["measure", "r-value", "p-value"])
    parts.append(row)

# Put everything in our parts list together into a dataframe for export.
results = pd.concat(parts)
results.reset_index(drop=True, inplace=True)

# Save and print it.
results.to_csv("./results.csv")
print(results)
