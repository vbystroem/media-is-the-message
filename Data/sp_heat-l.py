import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Spotify_Dataset_1973-2021_Tracks_cleaned.csv', delimiter=';')
sampled_df = df.groupby('year', group_keys=False).apply(lambda x: x.sample(frac=0.1))

y = 'loudness'
x = 'year'

plt.hist2d(sampled_df[x], sampled_df[y], bins=(200, 200), cmap=plt.cm.jet)
plt.colorbar()

plt.title('Heatmap')
plt.ylabel('duration')
plt.xlabel('year')

plt.show()