# Bivariate Data Visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

games = pd.read_csv('vgsales.csv')
print(games.head())
print(games.info())

# Continuous - Continuous
# Line Plots
# Plot Sales for a longest running game over series
longest_running_game = games.groupby("Name").agg(min_year = ("Year", "min"), max_year = ("Year", "max")).reset_index()
print(longest_running_game)
longest_running_game['yrs_active'] = longest_running_game['max_year'] - longest_running_game['min_year'] + 1
print(longest_running_game["yrs_active"].max())
longest_running_game = longest_running_game.sort_values("yrs_active", ascending = False)
longest_running_game = longest_running_game[0:5]
print(longest_running_game)

ih_max_sale = games[games['Name'] == longest_running_game['Name'].values[0]]["NA_Sales"].max()
ih_max_sale_yr = games[games['Name'] == longest_running_game['Name'].values[0]][games[games['Name'] == longest_running_game['Name'].values[0]]['NA_Sales'] == games[games['Name'] == longest_running_game['Name'].values[0]]['NA_Sales'].max()]["Year"]
bb_max_sale = games[games['Name'] == longest_running_game['Name'].values[1]]["NA_Sales"].max()
bb_max_sale_yr = games[games['Name'] == longest_running_game['Name'].values[1]][games[games['Name'] == longest_running_game['Name'].values[1]]['NA_Sales'] == games[games['Name'] == longest_running_game['Name'].values[1]]['NA_Sales'].max()]["Year"]

sns.lineplot(x = "Year", y = "NA_Sales", data = games[games['Name'] == longest_running_game['Name'].values[0]], color = "black", label = longest_running_game['Name'].values[0])
sns.lineplot(x = "Year", y = "NA_Sales", data = games[games['Name'] == longest_running_game['Name'].values[1]], color = "blue", label = longest_running_game['Name'].values[1])
plt.title("North American Sales of " + longest_running_game['Name'].values[0] + " and " + longest_running_game['Name'].values[1] + " over the years")
plt.xlabel("Year")
plt.text(ih_max_sale_yr, ih_max_sale, "Maximum Sales For " + longest_running_game['Name'].values[0], horizontalalignment = 'right', color = "orange")
plt.text(bb_max_sale_yr, bb_max_sale, "Maximum Sales For " + longest_running_game['Name'].values[1], horizontalalignment = 'left', color = "orange")
plt.ylabel("NA Sales (in millions)")

plt.show()

plt.plot(games[games['Name'] == longest_running_game['Name'].values[0]].sort_values('Year')['Year'], games[games['Name'] == longest_running_game['Name'].values[0]].sort_values('Year')['NA_Sales'], color = "red", label = longest_running_game['Name'].values[0])
plt.plot(games[games['Name'] == longest_running_game['Name'].values[1]].sort_values('Year')['Year'], games[games['Name'] == longest_running_game['Name'].values[1]].sort_values('Year')['NA_Sales'], color = "grey", label = longest_running_game['Name'].values[1])
plt.title("North American Sales of " + longest_running_game['Name'].values[0] + " and " + longest_running_game['Name'].values[1] + " over the years")
plt.xlabel("Year")
plt.ylabel("NA Sales (in millions)")
plt.legend(loc = (1, 1))
plt.show()

plt.plot(games[games['Name'] == longest_running_game['Name'].values[0]].sort_values('Year')['Year'], games[games['Name'] == longest_running_game['Name'].values[0]].sort_values('Year')['NA_Sales'], color = "orange", label = longest_running_game['Name'].values[0])
plt.plot(games[games['Name'] == longest_running_game['Name'].values[1]].sort_values('Year')['Year'], games[games['Name'] == longest_running_game['Name'].values[1]].sort_values('Year')['NA_Sales'], color = "green", label = longest_running_game['Name'].values[1])
plt.title("North American Sales of " + longest_running_game['Name'].values[0] + " and " + longest_running_game['Name'].values[1] + " between 1995 and 2010")
plt.xlabel("Year")
plt.ylabel("NA Sales (in millions)")
plt.xlim(1995, 2010)
plt.legend(loc = 'center')
plt.show()

plt.figure(figsize = (10, 6))
for i in range(len(longest_running_game)):
    lgr = games[games['Name'] == longest_running_game['Name'].values[i]]
    #print(lgr)
    lgr_max_na_sale = lgr["NA_Sales"].max()
    lgr_max_na_sale_yr = lgr[lgr['NA_Sales'] == lgr['NA_Sales'].max()]["Year"]
    sns.lineplot(x = "Year", y = "NA_Sales", data = lgr, label = longest_running_game['Name'].values[i])
    plt.text(lgr_max_na_sale_yr, lgr_max_na_sale, "Maximum Sales For " + longest_running_game['Name'].values[i], horizontalalignment = 'right')
plt.title("North American Sales For Top 5 Longest Running Games over the years")
plt.xlabel("Year")
plt.ylabel("NA Sales (in millions)")
plt.legend(loc = (0.85, 1))
plt.show()

# Note: plt.plot() is a low level function, whereas sns.lineplot() is a high level function because plt.plot() does the plotting based on the raw data provided, whereas sns.lineplot() does the plotting by internally sorting the data based on x axis and then plotting it.

# Scatter Plots
sns.lineplot(x = "Rank", y = "Global_Sales", data = games, color = "grey")
plt.show()

sns.scatterplot(x = "Rank", y = "Global_Sales", data = games, color = "orange")
plt.show()

# Count Plots
top5_publisher = games["Publisher"].value_counts().head().index
top5_genre = games["Genre"].value_counts().head().index
top5_platform = games["Platform"].value_counts().head().index

top5_games_data = games[games['Publisher'].isin(top5_publisher) & games['Genre'].isin(top5_genre) & games['Platform'].isin(top5_platform)]
print(top5_games_data.head())



# Categorical - Categorical
# Dodged Count Plots
sns.countplot(x = "Publisher", hue = "Genre", data = top5_games_data, order = sorted(top5_publisher))
plt.show()
# Stacked Count Plots
stacked_plot = pd.crosstab(top5_games_data['Publisher'], top5_games_data['Genre'])
stacked_plot.plot(kind = 'bar', stacked = True)
plt.title("Stacked Bar Plot for Top 5 Publishers and their Genre Distribution")
plt.xlabel("Publisher")
plt.ylabel("Number Of Genres")
plt.show()

# Categorical - Continuous
# Box Plots
sns.boxplot(hue = "Publisher", y = "Global_Sales", data = top5_games_data)
plt.legend(loc = (1, 1))
plt.show()

# Bar Plots
sns.barplot(x = "Publisher", y = "Global_Sales", data = top5_games_data, order = sorted(top5_publisher), estimator = np.min)
plt.show()

sns.barplot(x = "Publisher", y = "Global_Sales", data = top5_games_data, order = sorted(top5_publisher), estimator = np.mean)
plt.show()

sns.barplot(x = "Publisher", y = "Global_Sales", data = top5_games_data, order = sorted(top5_publisher), estimator = np.max)
plt.show()

# Subplots
