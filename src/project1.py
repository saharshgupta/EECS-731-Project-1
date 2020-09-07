# Importing required libraries
import pandas as pd

# Reading the csv data files
df1 = pd.read_csv("../Data/Fifa18.csv") # data frame 1 reading in Fifa 2018 dataset
df2 = pd.read_csv("../Data/Fifa19.csv") # data frame 2 reading in Fifa 2019 dataset

# Cleaning dataset by dropping redundant columns
df1.drop("Unnamed: 0",axis=1,inplace=True) # Dropping unnamed column in data frame 1 with inplace = true
df2.drop("Unnamed: 0",axis=1,inplace=True) # Dropping unnamed column in data frame 2 with inplace = true

# Adding a feature so that the data points are distinguishable when merged
df1["Year"] = [2018 for i in range(len(df1))] # Adding year 2018 to the 2018 Fifa dataset
df2["Year"] = [2019 for i in range(len(df2))] # Adding year 2019 to the 2019 Fifa dataset

# Printing out the shapes of the data frames
print("DataFrame 1 Shape: ",df1.shape) # Shape of data frame 1
print("DataFrame 2 Shape: ",df2.shape) # Shape of data frame 1

df = df1.merge(df2,how="outer") # Merging the two data frames together using outer.
# Removing the letter K from the end of numbers, converting string to numbers so that we can run analysis
df["Wage"] = df["Wage"].replace('[\€*K+,]', '', regex=True).astype(float)
df.sort_values(["Wage","Overall"],inplace=True,ascending=False) # Sorting the merged dataset with Wage and Overall as key features 
print("Merged Dataframe Shape: ",df.shape) # Shape of the merged data frame

# df.dropna(axis=1,inplace=True) # Multiple features added from the two have many NaN fields which can be dropped
# df.drop(["Photo","Flag","Club Logo","Special"],axis=1, inplace=True) # Can drop features which wont be used

print(df.head(10)) # Printing out the top 10 of the merged dataset