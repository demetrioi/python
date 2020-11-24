# Data from https://www.kaggle.com/unanimad/us-election-2020
import pandas as pd

# File with 31407 rows.
file = '/Volumes/GoogleDrive/My Drive/gitmac/demetrio/python/tabulator/uselection/president_county_candidate.csv'

# Default
df = pd.read_csv(file)
print(df.shape[0])

# Using Chunk. Read 500 per batch
# Returns a iterator
chunk = pd.read_csv(file, chunksize=500)
print(type(chunk))  # <class 'pandas.io.parsers.TextFileReader'>

df1 = pd.concat(c for c in chunk)
print(df1.shape[0])

# You can also use a for loop
for d in chunk:
    print(d.shape[0])
