#Vår data är inte normalfördelad, så detta funkar inte att använda o(TヘTo)

import pandas as pd
from scipy.stats import ttest_ind

data = pd.read_csv('Spotify_Dataset_1973-2021_Tracks_cleaned.csv', usecols=['year', 'loudness'], delimiter=";")

year = data['year']
loudness = data['loudness']

tstat, pvalue = ttest_ind(year, loudness)

print(f"T-statistic: {tstat:.3f}")
print(f"P-value: {pvalue:.3f}")