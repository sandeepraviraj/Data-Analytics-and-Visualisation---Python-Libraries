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
print(df.columns)
print(df.keys())

df.rename({"country":"Country", "gdp_cap": "GDP_CAP"}, axis = 1, inplace=True)
print(df.keys())
print(df.columns)

df.drop(columns ={"continent"}, axis = 1, inplace=True)
print(df.head())

df['year + 7'] = df['year'] + 7
print(df.head())
df.drop(columns ={"year + 7"}, axis = 1, inplace=True)
print(df.head())

 # Explicit Indexing
print(df.head())

#print(df.index[1704]) # Error
print(df.index[1703])
# Cannot access rows using explicit index, it can be accessed using implicit index only.
df.index = np.arange(1, df.shape[0] + 1, dtype = float)
print(df.head())

sample = df.head()
print(sample.index)
sample.index = ['a', 'b', 'c', 'd', 'e']
print(sample.index)
print(sample)

df.index = np.arange(1, df.shape[0] + 1, dtype = int)
print(df.head())

ser = df['Country']
print(ser.head(20))
#print(ser[0]) # 0 index is not available as we have explicity started the index from 1. Here we are using explicit index.
print(ser[5:15]) # Here we are using implicit index.

#loc - Uses explicit index and end index is inclusive
#iloc - Use implicit index

print(df.loc[1])
print(df.loc[5:10])

print(df.iloc[0])
print(df.iloc[5:10])

#print(df.loc[-1]) # Negative Indexing is not possible for loc as it is explicit indexing
print(df.iloc[-1])

demo = pd.Series(['a', 'b', 'c', 'd', 'e'], index = [1, 5, 3, 2, 4])
print(demo)
print(demo.loc[1])
print(demo.loc[1:4])

print(df.iloc[29:40, -3:])

temp = df.set_index("Country")
print(temp.head())
print(temp.loc['Albania'])
print(temp.head())
temp.reset_index(inplace=True)
print(temp.head())

#df.columns = [0, 1, 2, 3, 4, 5]
#print(df.columns)
#print(df.keys())

print(df.nunique())

data = {'name':["Sam","Roma","Mark"], "profession":['dev','mle','Data scientist'],"gender":['male','female','male'], "age":[21,20,25],"review":['No comments','hardworker','need improvement'],"rating":[10,5,7]}
df1 = pd.DataFrame(data)
print(df1[df1["rating"] > 6])
new_df = df1[df1["rating"] > 6].iloc[:, 1:4]
print(new_df)


df2 = pd.DataFrame({'emp_id':[1, 2], 'name': ['Ram', 'Shyam'], 'dept':['IT', 'Ops']})
print(df2)