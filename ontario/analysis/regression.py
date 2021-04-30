import pandas as pd
import numpy as np
import scipy.stats

# Read in data.
data1 = pd.read_csv("../data/data-combined.csv")
data2 = pd.read_csv("../data/data-other.csv")

data = data1.join(data2, on="TOR_Code", how="left")
data = data.drop("name", axis=1)
data = data.fillna(0)
data = data.drop(["TOR_Code", "Neighbourhood Number"], axis=1)

# A list that will store rows for the final export.
rows = []

# Get only numerical columns.
slice = data.iloc[:, 2:]

# For each measure...
for col in slice:
    num = data.columns.get_loc(col)
    # ...prepare the data...
    measure_name = data.columns[num]
    X = data["% population ACTUALLY vaccinated (55+ yo)"].values.reshape(-1, 1)  # values converts it into a numpy array
    Y = data.iloc[:, num].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

    result = scipy.stats.linregress(X[:,0], Y[:,0])
    r_value = '{:.2f}'.format(result.rvalue)
    p_value = '{:.6f}'.format(result.pvalue)
    r_squared = result.rvalue*result.rvalue
    std_error = '{:.6f}'.format(result.stderr)

    # ..and finally put into a new dataframe that will be concatenated together at the end.
    row = pd.DataFrame([[measure_name, r_value, p_value, r_squared, std_error]], columns=["measure", "r", "p-value", "r squared", "standard error"])
    rows.append(row)

# Put everything in our parts list together into a dataframe for export.
results = pd.concat(rows)
results.reset_index(drop=True, inplace=True)

# Save and print it.
results.to_csv("../data/neighbourhood-results-apr26.csv")
print(results)