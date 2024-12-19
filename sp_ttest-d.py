#Vår data är inte normalfördelad, så detta funkar inte att använda o(TヘTo)

import pandas as pd
from scipy.stats import ttest_ind

data = pd.read_csv('spotify_filtered-d.csv', usecols=['year', 'length'], delimiter=";")

year = data['year']
duration = data['length']

tstat, pvalue = ttest_ind(year, duration)

print(f"T-statistic: {tstat:.3f}")
print(f"P-value: {pvalue:.3f}")