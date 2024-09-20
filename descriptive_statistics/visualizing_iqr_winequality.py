import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Wine Quality dataset (from UCI)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_data = pd.read_csv(url, delimiter=';')

# Calculate the IQR for two features (e.g., alcohol and fixed acidity)
Q1 = wine_data.quantile(0.25)
Q3 = wine_data.quantile(0.75)
IQR = Q3 - Q1

# Detecting outliers: data points below Q1 - 1.5*IQR or above Q3 + 1.5*IQR
outliers = ((wine_data < (Q1 - 1.5 * IQR)) | (wine_data > (Q3 + 1.5 * IQR)))

# Create boxplots to visualize IQR and outliers
plt.figure(figsize=(12, 6))

# Boxplot for Alcohol
plt.subplot(1, 2, 1)
sns.boxplot(data=wine_data['alcohol'], color='lightblue')
plt.title('Alcohol: Boxplot and IQR')

# Boxplot for Fixed Acidity
plt.subplot(1, 2, 2)
sns.boxplot(data=wine_data['fixed acidity'], color='lightgreen')
plt.title('Fixed Acidity: Boxplot and IQR')

plt.tight_layout()
plt.show()

"""
Explanation:
Dataset: The Wine Quality dataset is loaded from UCI, containing various properties of wine (like alcohol content and acidity).
IQR Calculation: The IQR is calculated using the 25th and 75th percentiles, and outliers are defined as any values outside 1.5 times the IQR.

Visualization: Box plots are used to visualize the spread of the data and identify potential outliers.
Why IQR Matters:The IQR helps visualize the middle 50% of the data, making it a powerful tool for detecting anomalies that lie far from this range.
The box plot is a visual tool that displays both the IQR and any potential outliers, making it easy to spot anomalies in the dataset.

The Wine Quality dataset is available here: https://archive.ics.uci.edu/dataset/186/wine+quality
"""