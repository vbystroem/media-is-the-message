import pandas as pd

# Load the dataset from a CSV file
dataset = pd.read_csv('Spotify_Dataset_1973-2021_Tracks_cleaned.csv', delimiter=';')

loud = 'loudness'

# Calculate the quartiles
first_quartile = dataset[loud].quantile(0.05)
third_quartile = dataset[loud].quantile(0.95)

# Filter the dataset based on quartile values
filtered_dataset = dataset[
    (dataset[loud] >= first_quartile) & (dataset[loud] <= third_quartile)
]

# Drop empty rows from the filtered dataset
filtered_dataset = filtered_dataset.dropna(how='all')

# Save the filtered dataset to a new CSV file
filtered_dataset.to_csv('spotify_filtered-l.csv', index=False, sep=';')