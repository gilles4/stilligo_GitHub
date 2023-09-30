import pandas as pd

# Reading the Excel air pollution
df = pd.read_csv('../stilligo_GitHub/Russian tourist_attractions.csv')
df_rus=df.copy()
print(f'There are {df_rus.shape[0]} rows and {df_rus.shape[1]} columns') # fstring

#get information about the df_rus dataset
#df_rus.info()

#get the size of dataframe
#print ("Rows     : " , df_rus.shape[0])  #get number of rows/observations
#print ("Columns  : " , df_rus.shape[1]) #get number of columns
#print ("#"*40,"\n","Features :\n\n", df_rus.columns.tolist()) #get name of columns/features
#print ("#"*40,"\nMissing values :\n\n", df_rus.isnull().sum().sort_values(ascending=False))
#print( "#"*40,"\nPercent of missing :\n\n", round(df_rus.isna().sum() / df_rus.isna().count() * 100, 2).sort_values(ascending=False)) # looking at columns with most Missing Values

##########  Cleaning dataset  ###########

# Chargement du dataset
data = pd.read_csv('../stilligo_GitHub/Russian tourist_attractions.csv')

# Suppression des lignes avec des valeurs manquantes
data = data.dropna()

# Suppression des doublons
data = data.drop_duplicates()

# Nettoyage des colonnes spécifiques
#data['colonne'] = data['colonne'].apply(lambda x: x.strip())  # Supprime les espaces inutiles

# Conversion des colonnes au bon format
#data['colonne_date'] = pd.to_datetime(data['colonne_date'], format='%Y-%m-%d')

# Enregistrement du dataset nettoyé
data.to_csv('../stilligo_GitHub/Cleaned Rus_tourist_attractions_dataset.csv', index=False)

# Chargement du dataset nettoyé
df = pd.read_csv('../stilligo_GitHub/Cleaned Rus_tourist_attractions_dataset.csv')
#print(df.head(5))
print(df.info())
