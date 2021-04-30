import pandas as pd
import numpy as np
import scipy.stats
import seaborn as sns; sns.set_theme(color_codes=True)
import matplotlib.pyplot as plt
import math

# Read in data.
data = pd.read_csv("../data/data-quebec-clean.csv")

# A list that will store rows for the final export.
rows = []
plots = []

# Get only numerical columns.
census_columns = data.iloc[:, 3:]

# For each measure...
for col in census_columns:
    col_number = data.columns.get_loc(col)
    # ...prepare the data...
    measure_name = data.columns[col_number]
    
    X = data["vaccination #"].values.reshape(-1, 1)  # values converts it into a numpy array
    Y = data.iloc[:, col_number].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
    
    result = scipy.stats.linregress(X[:,0], Y[:,0])
    r_value = '{:.2f}'.format(result.rvalue)
    p_value = '{:.6f}'.format(result.pvalue)
    r_squared = result.rvalue*result.rvalue
    std_error = '{:.6f}'.format(result.stderr)
    coords = {"title": measure_name, "X": X, "Y": Y}

    # ..and finally put into a new dataframe that will be concatenated together at the end.
    row = pd.DataFrame([[measure_name, r_value, p_value, r_squared, std_error]], columns=["measure", "r-value", "p-value", "r squared", "standard error"])
    plots.append(coords)
    rows.append(row)

# Put everything in our parts list together into a dataframe for export.
results = pd.concat(rows)
results.reset_index(drop=True, inplace=True)

# Save and print it.
results.to_csv("../fsa-results-apr26.csv")
fig, axs = plt.subplots(ncols=2, sharey=True)
sns.regplot(data=plots[11], x="X", y="Y", label="Test", truncate=True, scatter_kws={"s": 5}, line_kws={"color": 'red'}, ax=axs[1])
sns.regplot(data=plots[10], x="X", y="Y", label="Test", truncate=True, scatter_kws={"s": 5}, line_kws={"color": 'red'}, ax=axs[0])
fig.text(0.04, 0.5, 'common Y', va='center', rotation='vertical')
axs[0].set_title(plots[10].get("title"))
axs[1].set_title(plots[11].get("title"))

# plt.ylim(0, .08)
# plt.ylabel("% Vaccinated")
# plt.show()
print(results)