# Pandas
# Intoduction To Pandas
# Dataframes - The entire data is called dataframe.
# Series - An entire column in a dataframe/table is called a series.
# Basic Operations On Dataframes
# Basic Operations On Columns
# Basic Operations On Rows

import numpy as np
import pandas as pd

df = pd.read_csv('mckinsey.csv')
print(df)
print(df.info())
print(df.head())
print(df.tail())

print(df['country'].unique())
print(df['country'].nunique())
print(df['country'].value_counts().head())