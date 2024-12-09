# Optional: Configure Matplotlib for inline plotting (Jupyter only)
# %matplotlib inline

# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (update the file path with your dataset's location)
file_path = r"D:\Personal\Kifiya 10 Academy\Datasource\benin-malanville.csv"
data = pd.read_csv(file_path)

# Preview the dataset
print(data.head())

# Summary Statistics
print("\nSummary Statistics:")
print(data.describe())

# Check for Missing Values
print("\nMissing Values:")
print(data.isnull().sum())

# Time Series Analysis
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data.set_index('Timestamp', inplace=True)

# Plotting GHI, DNI, and DHI over time
plt.figure(figsize=(10, 6))
data[['GHI', 'DNI', 'DHI']].plot(title="Solar Irradiance Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Irradiance (W/m²)")
plt.legend()
plt.show()

# Correlation Matrix
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Outlier Detection Using Z-Score
from scipy.stats import zscore
z_scores = np.abs(zscore(data.select_dtypes(include=[np.number])))
outliers = (z_scores > 3).sum(axis=0)
print("\nOutliers Detected:")
print(outliers)

# Impact of Cleaning on Sensor Readings
plt.figure(figsize=(10, 6))
data.groupby('Cleaning')[['ModA', 'ModB']].mean().plot(kind='bar', title="Impact of Cleaning on Sensor Readings")
plt.ylabel("Irradiance (W/m²)")
plt.show()

# Distribution of Variables
numeric_cols = ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS', 'BP']
data[numeric_cols].hist(figsize=(12, 10), bins=20)
plt.suptitle("Distribution of Variables")
plt.show()

# Wind Analysis - Wind Rose
from windrose import WindroseAxes
wind_df = data.dropna(subset=['WD', 'WS'])
ax = WindroseAxes.from_ax()
ax.bar(wind_df['WD'], wind_df['WS'], normed=True, opening=0.8, edgecolor='white')
ax.set_title("Wind Rose - Wind Speed and Direction")
plt.show()

