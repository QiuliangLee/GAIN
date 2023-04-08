import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('./data/1min.csv')
profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("your_report.html")
