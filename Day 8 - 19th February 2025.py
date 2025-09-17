# Multi-Indexing
import numpy as np
import pandas as pd

movies = pd.read_csv('movies.csv', index_col = 0)
directors = pd.read_csv('directors.csv', index_col = 0)

result = pd.merge(movies, directors, how = 'left', left_on = 'director_id', right_on = 'id')
result.drop(['director_id', 'id_y'], axis = 1, inplace = True)
result.rename(columns = {'id_x': 'id'}, inplace = True)
print(result.head())
print(result.info())

# To identify the most productive director
productive_director = result.groupby(['director_name'])[['year','title']].agg({'year': ['min', 'max'], 'title': 'count'})
print(productive_director)

print(productive_director['year'])
print(productive_director['year']['min'])

# Converting multi level columns into single level columns
# Method 1
res_col = []
for col in productive_director.columns:
    res_col.append('_'.join(col))

productive_director.columns = res_col
print(productive_director.head())
productive_director.reset_index(inplace = True)
print(productive_director.head())

# Method 2
# productive_director.columns = ['_'.join(col) for col in productive_director.columns]

productive_director['yrs_active'] = productive_director['year_max'] - productive_director['year_min'] + 1
print(productive_director.head())

productive_director["movies_per_year"] = productive_director['title_count'] / productive_director['yrs_active']

print(productive_director.sort_values("movies_per_year", ascending = False).head())

# Resturcturing The Data
Pfizer = pd.read_csv('Pfizer_1.csv')
print(Pfizer)
print(Pfizer.columns)
# melt()
# Converting wide data format(more number of columns) to long format(more number of rows) ---> Useful for EDA
Pfizer_long = pd.melt(Pfizer, id_vars = ['Date', 'Drug_Name', 'Parameter'], var_name = 'Time', value_name = 'Result')
print(Pfizer_long) 

# pivot()
# Converting long data format(more number of rows) to wide format(more number of columns) ---> Useful for Reporting
Pfizer_wide = Pfizer_long.pivot(index = ['Date', 'Drug_Name', 'Parameter'], columns = 'Time', values = 'Result')
print(Pfizer_wide)
print(Pfizer_wide.columns)
Pfizer_wide = Pfizer_wide.reset_index()
print(Pfizer_wide)
Pfizer_wide.columns.name = None
print(Pfizer_wide)
Pfizer_wide = Pfizer_wide[['Date', 'Drug_Name', 'Parameter', '1:30:00', '2:30:00', '3:30:00',   
       '4:30:00', '5:30:00', '6:30:00', '7:30:00', '8:30:00', '9:30:00',    
       '10:30:00', '11:30:00', '12:30:00']]
print(Pfizer_wide)

Pfizer_tidy = Pfizer_long.pivot(index = ['Date', 'Drug_Name', 'Time'], columns = 'Parameter', values = 'Result').reset_index()
Pfizer_tidy.columns.name = None
print(Pfizer_tidy)

# Binning
# cut()
temp_points = [5, 20, 35, 50, 65] # exclude initial and include last
temp_labels = ['low', 'medium', 'high', 'extreme']
Pfizer_tidy['temp_level'] = pd.cut(Pfizer_tidy['Temperature'], bins = temp_points, labels = temp_labels)
print(Pfizer_tidy)

# pivot_table()
pivot_table = Pfizer_tidy.pivot_table(index = ['Drug_Name'], columns = ['Date'], values = ['Temperature', 'Pressure'], aggfunc = 'min', margins = True)
print(pivot_table)