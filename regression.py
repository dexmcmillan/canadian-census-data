import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
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

    # (this handles any blank or N/A values in the data.)
    imputer = SimpleImputer()
    Y = imputer.fit_transform(Y)

    # ...then do a linear regression...
    linear_regressor = LinearRegression()
    reg = linear_regressor.fit(X.astype(float), Y.astype(float))
    score = reg.score(X, Y)

    # ..and finally put into a new dataframe that will be concatenated together at the end.
    row = pd.DataFrame([[measure, score]])
    parts.append(row)

# Put everything in our parts list together into a dataframe for export.
results = pd.concat(parts)
results.reset_index(drop=True, inplace=True)

# Save and print it.
results.to_csv("./results.csv")
print(results)
