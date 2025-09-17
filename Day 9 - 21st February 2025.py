import numpy as np
import pandas as pd

Pfizer = pd.read_csv('Pfizer_1.csv')
print(Pfizer)

Pfizer_long = pd.melt(Pfizer, id_vars = ['Date', 'Drug_Name', 'Parameter'], var_name = 'Time', value_name = 'Result')
print(Pfizer_long)

Pfizer_wide = Pfizer_long.pivot(index = ['Date', 'Drug_Name', 'Time'], columns = 'Parameter', values = 'Result').reset_index()
Pfizer_wide.columns.name = None
print(Pfizer_wide)

# Null/Missing Values
# Both None and NaN are considered as missing values in pandas
# None vs NaN
# Case 1: None in Non-Numeric columns is treated as string objects and hence shows 'None'
# Case 2: None in Numeric columns is treated as NaN and hence shows 'NaN'
# Case 3: NaN in Non-Numeric columns is treated as NaN and hence shows 'NaN'
# Case 4: NaN in Numeric columns is treated as NaN and hence shows 'NaN'

# isna() and isnull() both are the same. It returns the same boolean DataFrame for a given dataset
print(Pfizer.isna().sum())
print(Pfizer.isna().sum(axis = 1))

# Removing Null Values
# dropna()
Pfizer_dropped = Pfizer.dropna() # Drops all the rows which has at least one null value
print(Pfizer_dropped)
Pfizer_dropped_ = Pfizer.dropna(how = 'all') # Drops all the rows which has all null values
print(Pfizer_dropped_)
Pfizer_dropped_col = Pfizer.dropna(axis = 1) # Drops all the columns which has at least one null value
print(Pfizer_dropped_col)
Pfizer_dropped_col_ = Pfizer.dropna(axis = 1, how = 'all') # Drops all the columns which has all null values
print(Pfizer_dropped_col_)
# Pfizer.dropna(thresh = 14, inplace = True) # Retains all the rows which has at least 14 non-null values
# print(Pfizer)

# Data Imputation --> Replacing missing values with meaningful values
# Constant Value Imputation --> Leads to ambiguity as the value can't be decided easily
# fillna()
Pfizer_filled = Pfizer.fillna(0) 
print(Pfizer_filled)

Pfizer_col = Pfizer["11:30:00"].fillna(0)
print(Pfizer_col)

print(Pfizer_wide)
print(Pfizer_wide.info())

def replace_missing(x):
    x['Temperature'] = x['Temperature'].mean()
    return x

Pfizer_wide_replaced = Pfizer_wide.groupby(['Drug_Name'], group_keys = False).apply(replace_missing)
print(Pfizer_wide_replaced)

avg_temp = Pfizer_wide['Temperature'].mean()
Pfizer_wide['Temperature'].fillna(avg_temp, inplace = True)
print(Pfizer_wide)
print(Pfizer_wide.isna().sum())

avg_psr = Pfizer_wide['Pressure'].mean()
Pfizer_wide['Pressure'].fillna(avg_psr, inplace = True)
print(Pfizer_wide)
print(Pfizer_wide.isna().sum()) 

# String Methods
drug_hydrochloride = Pfizer_wide[Pfizer_wide["Drug_Name"].str.contains("hydrochloride")]
print(drug_hydrochloride)
drug_hydrochloride["Year"] = drug_hydrochloride["Date"].str.split("-").str[2]
print(drug_hydrochloride)

# Datetime Values
Pfizer_wide["Timestamp"] = Pfizer_wide["Date"] + " " + Pfizer_wide["Time"]
Pfizer_wide["Timestamp"] = pd.to_datetime(Pfizer_wide["Timestamp"], format = "%d-%m-%Y %H:%M:%S")
Pfizer_wide.drop(columns = ["Date", "Time"], inplace = True)
print(Pfizer_wide)
print(Pfizer_wide.info())

Pfizer_wide["Year"] = Pfizer_wide["Timestamp"].dt.year
print(Pfizer_wide)

Pfizer_wide["Timestamp"] = Pfizer_wide["Timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
print(Pfizer_wide)

# Write to a file
Pfizer_wide.to_csv("Pfizer_Cleaned.csv", sep = ",", index = False)