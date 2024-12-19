#Gör ett linjediagram som visar hur lång musik blivit över tid

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Spotify_Dataset_1973-2021_Tracks_cleaned.csv', delimiter=';')
mean_duration_df = df.groupby('year')['length'].mean().reset_index()

y = 'length'
x = 'year'

plt.plot(mean_duration_df[x], mean_duration_df[y])

plt.title('Line diagram')
plt.ylabel('Length')
plt.xlabel('Year')

plt.show()