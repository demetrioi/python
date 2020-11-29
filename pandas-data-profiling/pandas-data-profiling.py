# Dataset: https://www.kaggle.com/sakshigoyal7/credit-card-customers
# This Pandas library can be used to replace SSIS Data Profiling
# https://docs.microsoft.com/en-us/sql/integration-services/control-flow/data-profiling-task?view=sql-server-ver15

import pandas as pd
import pandas_profiling as pf

path = '/Volumes/GoogleDrive/My Drive/gitmac/demetrio/python/pandas-data-profiling/BankChurners.csv'

df = pd.read_csv(path)

profile = pf.ProfileReport(
    df, title='Profiling - Like SSIS)', explorative=True)

# Large Datasets: Use this command on
# profile = pf.ProfileReport(
#    df, title='Profiling - Like SSIS)', minimal=True)

profile.to_file(
    "/Volumes/GoogleDrive/My Drive/gitmac/demetrio/python/pandas-data-profiling/BankChurners.html")
