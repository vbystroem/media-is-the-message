import pandas as pd
import matplotlib.pyplot as plt

# load data into a pandas DataFrame and select columns of interest
data = pd.read_csv('RIAA_Revenue_Chart_1973-2021.csv', usecols=['Format', 'Value (For Charting)'], delimiter=';')

# filter the DataFrame to only include rows with the value 'CD' in the 'Format' column
cd_data = data[data['Format'] == 'CD']

# create histogram of the 'Value (For Charting)' variable for the filtered DataFrame
plt.hist(cd_data['Value (For Charting)'], bins=1000)

# add labels to the plot
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.title('Histogram of Revenue for CD format')

# display plot
plt.show()