"""
Introduction and sample example on pandas module,
Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
Pandas mainly contains two primary data structures,  1. series, 2.dataframes
"""
import pandas as pd


# series is 1D data sets, it can be created by using .Series method
a = [1, 7, 2]
myvar = pd.Series(a, name = "SL No")
print("---------series---------------")
print(myvar)


# Dataframe is 2D data set
my_dict = {
        "Name": ["virat","abd","elissa"],
        "Age": [30, 35, 28],
        "Jersy": [18, 17, 8],
    }
df = pd.DataFrame(my_dict, index = ["IND", "SA", "AUS"])

print("--------------Dataframe----------------")
print(df)
print("---------age min max-----------------")
print(df["Age"].max())
print(df["Age"].min())

print("----------describe------------")
print(df["Age"].describe())

print("---------age > 30---------------")
print(df[df["Age"] > 30])

print("---------find age > 30 and gat name---------------")
print(df.loc[df["Age"] > 30, "Name"])

print("----------csv data---------------")
df_csv = pd.read_csv('data.csv')
print(df_csv) 

print("--------csv head data------------")
print(df_csv.head(2)) # gets only 2 rows of data frame for csv file
df_csv.to_excel("data.xlsx", sheet_name="data", index=False) # convert the csv to excel


print("----------excel data-----")
df_xl = pd.read_excel("data.xlsx", sheet_name="data") # read excel file
print(df_xl) 

print("----------json data-----")
df_json = pd.read_json('data.json')
print(df_json) 


import matplotlib.pyplot as plt
df_plt = pd.read_csv('data.csv')
print("----------plot data-----")
df_plt.plot()
plt.show()

df_plt.plot(kind = 'scatter', x = 'Duration', y = 'Pulse')
plt.show()

df_plt.plot(kind = 'hist', x = 'Duration', y = 'Pulse')
plt.show()

