import pandas as pd
import json

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

filepath = "/Volumes/GoogleDrive/My Drive/gitmac/demetrio/python/json-nested-list-file-to-tabular/cars-nested-list.json"

with open(filepath, 'r') as f:
    data = json.load(f)  # Dict

df = pd.json_normalize(data, "values")
df = df.apply(lambda f: f.explode()).reset_index(drop=True)

NESTED_LIST_FIELDS = ['details.availablecolors']

nested = list()
for col in NESTED_LIST_FIELDS:
    d = pd.json_normalize(df[col], sep='.')
    d.columns = [f'{col}.{d}' for d in d.columns]
    nested.append(d.copy())

df = pd.concat([df] + nested, axis=1).drop(columns=NESTED_LIST_FIELDS)

print(df)
