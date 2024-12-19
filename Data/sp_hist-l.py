import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('spotify_filtered-l.csv', delimiter=';')

plt.hist(data['loudness'], bins=500)

plt.xlabel('Loudness')
plt.ylabel('Frequency')
plt.title('Histogram of Track Loudness from 1973 to 2021')

plt.show()