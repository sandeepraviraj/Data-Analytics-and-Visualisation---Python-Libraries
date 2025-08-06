# Handling Data Across Rows and Columns
import pandas as pd
import numpy as np

df = pd.read_csv('mckinsey.csv')
print(df.head())
# Adding New row
new_row = {"country":"India", "year":"2025", "population": 1234567890, "continent":"Asia", "life_exp": 70.5, "gdp_cap": 5000}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print(df[df['country'] == 'India'])

new_row_val = list(new_row.values())
df.loc[len(df)] = new_row_val
print(df.tail())

# df.iloc[len(df)] = new_row_val # This will Error out because it is Not possible to add new row using iloc because the index position at which the row is being added needs to be present. I.e iloc will be useful for replacing a record 
# Dropping a row
df.drop([1, 2, 4], axis=0, inplace=True)
print(df.head())
print(df.iloc[4])
#df.reset_index(drop=False, inplace=True) # This will create a new index along with old index
df.reset_index(drop=True, inplace=True) # This will reset the existing index
print(df.head())

# Adding Multiple Records/Rows
new_rows = [
    {"country":"India", "year":"2025", "population": 1234567890, "continent":"Asia", "life_exp": 70.5, "gdp_cap": 5000},
    {"country":"Sri-Lanka", "year":"2025", "population": 1234567890, "continent":"Asia", "life_exp": 70.5, "gdp_cap": 5000},
    {"country":"Korea", "year":"2025", "population": 1234567890, "continent":"Asia", "life_exp": 70.5, "gdp_cap": 5000}]
new_rows = pd.DataFrame(new_rows)
df = pd.concat([df, new_rows], ignore_index=True)
print(df.tail())



# Handling Duplicate Records
print(df.loc[df.duplicated()])
#df.drop_duplicates(keep = 'first', inplace=True) # Drops all duplicates except first
df.drop_duplicates(keep = 'last', inplace=True) # Drops all duplicates except last
#df.drop_duplicates(keep = False, inplace=True) # Drops all duplicates
#df.reset_index(drop=True, inplace=True)
print(df.tail())
print(df.drop_duplicates(subset=['country'], keep='first'))

data = {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
        'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
        'C': ['small', 'large', 'large', 'small', 'small', 'large', 'large', 'small'],
        'D': [1, 2, 2, 3, 3, 4, 5, 6]}

df1 = pd.DataFrame(data)
print(df1)
print(df1[df1.duplicated(subset=['A', 'B'])])
print(sum(df1.duplicated(subset=['A', 'B'])))

# Built-in Functions
print(df['life_exp'].max())
print(df['life_exp'].min())
print(df['life_exp'].sum())
print(df['life_exp'].count())
print(df['life_exp'].sum()/df['life_exp'].count())
print(df['life_exp'].mean())
print(df['life_exp'].median())
print(df['life_exp'].mode())
print(df.sort_values(by=['year', 'life_exp'], ascending=True))

# How to sort by multiple columns where 1st column needs to be sorted in ascending and 2nd column in descending
print(df.sort_values(by=['year', 'life_exp'], ascending=[True, False]))

# Concatenate Dataframes


# Merging Dataframes
