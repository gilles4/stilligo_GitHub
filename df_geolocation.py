import pandas as pd

# Exemple de données
#data = {'coordinates': ['(10, 20)', '(30, 40)', '(50, 60)']}
#df = pd.DataFrame(data)

# Chargement du dataset nettoyé
df = pd.read_csv('../stilligo_GitHub/Cleaned Rus_tourist_attractions_dataset.csv')


# Diviser la colonne "coordinates" en deux colonnes "latitude" et "longitude"
df[['longitude', 'latitude']] = df['geolocation'].str.strip('()').str.split(', ', expand=True)

# Remove non-numeric characters and convert to numeric type
df['longitude'] = df['longitude'].str.replace(r'[^0-9. ]', '', regex=True).astype(str)
df['latitude']  = df['latitude'].str.replace(r'[^0-9. ]', '', regex=True).astype(str)

#garder juste la colonne desiré
columns_to_drop = ['geolocation']  # List of columns to drop
df = df.drop(columns=columns_to_drop)

# change latitude and longitude type from str to float step
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')

# empty rows droped
df = df.dropna()

# Enregistrement du dataset nettoyé
df.to_csv('../stilligo_GitHub/two_columns_geolocation_dataset3.csv', index=False)
df_geo3 = df
# Afficher le DataFrame résultant
#print(df_geo.head(3))
print(df_geo3.info())
#print(df_geo.dtypes)
#print(df_geo['latitude'].head(2))
