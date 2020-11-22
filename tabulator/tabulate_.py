# Data from https://www.kaggle.com/unanimad/us-election-2020
from tabulate import tabulate
import pandas as pd

df = pd.read_csv(
    '/Volumes/GoogleDrive/My Drive/gitmac/demetrio/python/tabulator/uselection/house_state.csv', nrows=2)

print(tabulate(df, headers='keys', tablefmt='pgsql'))
print(tabulate(df, headers='keys', tablefmt='grid', numalign='left'))
print(tabulate(df, headers='keys', tablefmt='grid', numalign='right'))
print(tabulate(df, headers='keys', tablefmt='simple'))
