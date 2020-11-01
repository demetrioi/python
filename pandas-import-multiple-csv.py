import pandas as pd
from glob import glob

files = sorted(glob(
    '/Volumes/GoogleDrive/My Drive/data/wine/*.csv'))

df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)

print(df)
