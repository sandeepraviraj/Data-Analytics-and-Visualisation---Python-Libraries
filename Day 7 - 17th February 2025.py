# Merging Dataset
import pandas as pd
import numpy as np

movies = pd.read_csv('movies.csv', index_col = 0)
print(movies.head())
directors = pd.read_csv('directors.csv', index_col = 0)
print(directors.head())

print(movies.info())
print(directors.info())

print(movies['director_id'].nunique())
print(directors['id'].nunique())

validation = movies['director_id'].isin(directors['id'])
print(np.all(validation))
result = pd.merge(movies, directors, how = 'left', left_on = 'director_id', right_on = 'id')
result.drop(['director_id', 'id_y'], axis=1, inplace=True)
result.rename(columns={'id_x':'id'}, inplace=True)

print(result.head())
print(result.info())

# apply()
def encode(data):
    if data == 'Male':
        return 'M'
    else:
        return 'F'
result['gender'] = result['gender'].apply(encode)
print(result.head())

print(result[['budget', 'revenue']].apply(np.sum, axis=0))

def profit(movie):
    return movie['revenue'] - movie['budget']
result['profit'] = result.apply(profit, axis = 1)
print(result.head())

# groupby()
# Grpup Based Aggregation
print(result.groupby('director_name').ngroups)
print(result.groupby('director_name').groups)
print(result.groupby('director_name').get_group('Steven Spielberg').head())
print(result.groupby('director_name')['title'].count())
print(result.groupby('director_name').agg({'year': ['min', 'max', 'count']}))

# Grpup Based Filtering
budget_directors = result.groupby('director_name')['budget'].max()
budget_directors = budget_directors.reset_index()
high_budget_directors = budget_directors[budget_directors['budget'] >= 100000000]['director_name']
print(high_budget_directors)
print(result.loc[result['director_name'].isin(high_budget_directors)])

# Grpup Based apply()
def risky_director(directors):
    directors['risky'] = directors['budget'] - directors['revenue'].mean() >= 0
    return directors

risky_directors = result.groupby('director_name', group_keys = True).apply(risky_director)
print(risky_directors)
print(risky_directors.loc[risky_directors['risky']])
print(risky_directors[risky_directors['risky'] == True])

eg = pd.DataFrame({'Group': ['G1', 'G2', 'G2', 'G3', 'G3', 'G3'], 'Points' : [2, 4, 6, 8, 10, 12]})
print(eg)
print(eg.groupby('Group')['Points'].sum())
print(eg.groupby('Group')['Points'].apply(lambda x: x.sum()))