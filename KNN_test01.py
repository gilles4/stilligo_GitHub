import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load your dataset
data = pd.read_csv('../stilligo_GitHub/two_columns_geolocation_dataset.csv')

# Assuming you have latitude and longitude columns in your dataset
coordinates = data[['latitude', 'longitude']].values


# Create a NearestNeighbors model
k = 1  # You can change k to find more nearest neighbors if needed
knn_model = NearestNeighbors(n_neighbors=k)
knn_model.fit(coordinates)

# Define the query point for which you want to find the closest place
## query_point = [[query_latitude, query_longitude]] # original line
query_point = [[50, 34]]

# Find the nearest neighbors to the query point
distances, indices = knn_model.kneighbors(query_point)

# Get the index of the closest place
closest_place_index = indices[0][0]

# Get the details of the closest place
closest_place = data.iloc[closest_place_index]

print("Closest Place:")
print(closest_place)
