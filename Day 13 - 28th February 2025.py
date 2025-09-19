# Multivariate Data Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

games = pd.read_csv('vgsales.csv')
print(games.head())

top3_publishers = games['Publisher'].value_counts().index[:3]
top3_genres = games['Genre'].value_counts().index[:3]
top3_platforms = games['Platform'].value_counts().index[:3]

top3_games = games[(games['Publisher'].isin(top3_publishers)) & (games['Genre'].isin(top3_genres)) & (games['Platform'].isin(top3_platforms))]
print(top3_games.head())

# Categorical - Categorical - Numerical
# Visualize Global Sales for each publisher seperated by Genre
'''plt.figure(figsize = (10,8))
sns.boxplot(x = 'Publisher', y = 'Global_Sales', hue = 'Genre', data = top3_games)
plt.xticks(rotation = 75, fontsize = 8)
plt.title(" Global Sales for each publisher seperated by Genre")
plt.show()

# Categorical - Numerical - Numerical
# Visualize NA_Sales and EU_Sales for different Publishers
plt.figure(figsize = (10,8))
sns.scatterplot(x = 'NA_Sales', y = 'EU_Sales', hue = 'Publisher', data = top3_games)
plt.show()

plt.figure(figsize = (10,8))
sns.kdeplot(x = 'NA_Sales', y = 'EU_Sales', hue = 'Publisher', data = top3_games)
plt.show()

# Categorical - Categorical - Categorical --> Not Part of Curriculum

# Numerical - Numerical - Numerical
# Visualize NA Salesa and JP Sales according to their ranks
plt.figure(figsize = (10,8))
sns.scatterplot(x = 'NA_Sales', y = 'JP_Sales', data = games, size = 'Rank', sizes = (10, 200))
plt.show()

# Joint Plots
plt.figure(figsize = (10, 8))
sns.jointplot(x = 'NA_Sales', y = 'JP_Sales', hue = 'Genre', data = top3_games)
plt.title("Joint Plot with hue attribute")
plt.show()

plt.figure(figsize = (10, 8))
sns.jointplot(x = 'NA_Sales', y = 'JP_Sales', kind = 'reg', data = top3_games)
plt.title("Joint Plot with kind attribute as reg")
plt.show()

plt.figure(figsize = (10, 8))
sns.jointplot(x = 'NA_Sales', y = 'JP_Sales', kind = 'scatter', data = top3_games)
plt.title("Joint Plot with kind attribute as scatter")
plt.show()

plt.figure(figsize = (10, 8))
sns.jointplot(x = 'NA_Sales', y = 'JP_Sales', kind = 'kde', data = top3_games)
plt.title("Joint Plot with kind attribute as kde")
plt.show()

plt.figure(figsize = (10, 8))
sns.jointplot(x = 'NA_Sales', y = 'JP_Sales', kind = 'hist', data = top3_games)
plt.title("Joint Plot with kind attribute as hist")
plt.show()

plt.figure(figsize = (10, 8))
sns.jointplot(x = 'NA_Sales', y = 'JP_Sales', kind = 'resid', data = top3_games)
plt.title("Joint Plot with kind attribute as resid")
plt.show()

plt.figure(figsize = (10, 8))
sns.jointplot(x = 'NA_Sales', y = 'JP_Sales', kind = 'hex', data = top3_games)
plt.title("Joint Plot with kind attribute as hex")
plt.show()

# Pair Plots
plt.figure(figsize = (10, 8))
sns.pairplot(top3_games)
plt.show()

plt.figure(figsize = (10, 8))
sns.pairplot(top3_games, hue = 'Genre')
plt.show()

plt.figure(figsize = (10, 8))
sns.pairplot(top3_games, x_vars = 'Year', y_vars = ['NA_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'], hue = 'Genre')
plt.show()'''

# Correlation Heatmaps
numeric_top3_games = top3_games.select_dtypes(include = ['float64', 'int64'])
corr = numeric_top3_games.corr()
print(corr)

sns.scatterplot(x = 'Global_Sales', y = 'Rank', data = top3_games)
plt.show()

sns.heatmap(data = corr, cmap = "coolwarm", annot = True)
plt.show()

# Spanning Across The Grid Layout
fig = plt.figure(figsize = (8, 4))
plt.subplot(2, 3, (1,2))
sns.scatterplot(x = top3_games["EU_Sales"], y = top3_games["NA_Sales"], data = top3_games, color = "grey")

plt.subplot(2, 3, 3)
sns.scatterplot(x = top3_games["EU_Sales"], y = top3_games["JP_Sales"], data = top3_games, color = "orange")

plt.subplot(2, 3, 4)
sns.scatterplot(x = top3_games["EU_Sales"], y = top3_games["Global_Sales"], data = top3_games, color = "blue")

plt.subplot(2, 3, 6)
sns.scatterplot(x = top3_games["EU_Sales"], y = top3_games["Other_Sales"], data = top3_games, color = "green")

#plt.subplot(1, 3, 2)
#sns.countplot(x = "Publisher", data = top3_games, order = sorted(top3_publishers))
plt.xlabel("Publisher")
plt.ylabel("Number of Games")
plt.xticks(rotation=90, fontsize=8)
fig.suptitle("Games Sales Dashboard", fontsize = 16)

plt.show()