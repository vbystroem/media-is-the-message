import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Beräknar korrelation mellan år och längd

# load data into a pandas DataFrame and select columns of interest
data = pd.read_csv('spotify_filtered-d.csv', usecols=['year', 'length'], delimiter=";")

# calculate correlation between variables
corr = data['year'].corr(data['length'], method='spearman')

# perform simple linear regression
slope, intercept = np.polyfit(data['year'], data['length'], 1)

# create scatter plot of data
plt.scatter(data['year'], data['length'], label='data')

# add regression line to plot
plt.plot(data['year'], slope * data['year'] + intercept, color='red', label='regression')

# add legend and labels to plot
plt.legend()
plt.xlabel('Release Year')
plt.ylabel('Duration')
plt.title(f'Correlation: {corr:.2f}')

# display plot
plt.show()