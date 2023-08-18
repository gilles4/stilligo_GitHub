Test_python
import pandas as pd
import numpy as np

# Reading the Excel air pollution
df = pd.read_csv('../stilligo_GitHub/Russian tourist_attractions.csv')
df_rus=df.copy()
print(f'There are {df_rus.shape[0]} rows and {df_rus.shape[1]} columns') # fstring

#get the size of dataframe
print ("Rows     : " , df_rus.shape[0])  #get number of rows/observations
print ("Columns  : " , df_rus.shape[1]) #get number of columns
print ("#"*40,"\n","Features :\n\n", df_rus.columns.tolist()) #get name of columns/features
print ("#"*40,"\nMissing values :\n\n", df_rus.isnull().sum().sort_values(ascending=False))
print( "#"*40,"\nPercent of missing :\n\n", round(df_rus.isna().sum() / df_rus.isna().count() * 100, 2).sort_values(ascending=False)) # looking at columns with most Missing Values
