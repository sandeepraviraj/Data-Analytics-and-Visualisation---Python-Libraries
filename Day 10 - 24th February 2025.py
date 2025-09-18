import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

games = pd.read_csv("final_vg.csv")
print(games.head())

# Univariate Analysis
# Line Plot
x_val = [2, 6, 10]
y_val = [3, 7, 11]
plt.plot(x_val, y_val)
plt.show()

# Categorical
cat_counts = games["Genre"].value_counts()
print(cat_counts)

cat_names = cat_counts.index
cat_counts = cat_counts.values

# Method 1: Using Matplotlib
# Bar Plot
plt.figure(figsize=(9, 5)) # Default Size is (6.4, 4.8)
plt.bar(cat_names, cat_counts, width=0.2, color = "orange")
plt.title("Genre Distribution", fontsize = 15)
plt.xlabel("Genre", fontsize = 12)
plt.ylabel("Count", fontsize = 12)
plt.xticks(rotation=90, fontsize=8)
plt.show()

# Note: Bar Plot in matplotlib is same as countplot in seaborn

# Method 2: Using Seaborn
# Bar Plot
sns.countplot(x = "Genre", data = games, order = cat_names, color = "black")
plt.xticks(rotation=90, fontsize=8)
plt.show()

# Pie Chart For Sales Distribution
sales_data = games[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
print(sales_data.head())
region_sales = sales_data.T.sum(axis = 1)
print(region_sales)

plt.pie(region_sales, labels = region_sales.index, startangle = 0, explode = [0.2, 0.2, 0, 0, 0.5], autopct='%0.2f%%')
plt.show()

# Numerical

# Method 1: Using Matplotlib
# Histogram
plt.hist(games["Year"])
plt.show() # Default Bins = 10
count, bins, patches = plt.hist(games["Year"], bins = 4)
print(count, bins)
for counts, patch in zip(count, patches):
    if counts == count.max():
        patch.set_facecolor("green")
    elif counts == count.min():
        patch.set_facecolor("red")
    else:
        patch.set_facecolor("black")
plt.show()

# Method 2: Using Seaborn
# Histogram
sns.histplot(games["Year"], bins = 4)
plt.show()

# KDE Plot
sns.kdeplot(games["Year"])
plt.show()
print(games.info())

# Box Plot
plt.figure(figsize=(15, 20))
sns.boxplot(data = sales_data)
plt.yticks(fontsize = 11)
plt.ylabel("Region Sales (in million dollars)", fontsize = 15)
plt.title("Region Sales in Video Games", fontsize = 20)
plt.show()

games["Year"] = games["Year"].astype("Int64")
plt.figure(figsize=(40, 50))
sns.boxplot(x = "Year", y = "Global_Sales", data = games)
plt.yticks(fontsize = 11)
plt.xticks(rotation = 90, fontsize = 11)
plt.ylabel("Global Sales (in million dollars)", fontsize = 15)
plt.title("Global Sales in Video Games", fontsize = 20)
plt.show()