import pandas as pd
import matplotlib.pyplot as plt

# load data into a pandas DataFrame and select columns of interest
data = pd.read_csv('spotify_filtered-d.csv', delimiter=';')

# create histogram of the 'Value (For Charting)' variable for the filtered DataFrame
plt.hist(data['length'], bins=1000)

# add labels to the plot
plt.xlabel('Length')
plt.ylabel('Frequency')
plt.title('Histogram of Track Length from 1973 to 2021')

# display plot
plt.show()