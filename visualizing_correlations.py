import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Wine Quality dataset (from UCI)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_data = pd.read_csv(url, delimiter=';')

# Calculate the correlation matrix
correlation_matrix = wine_data.corr()


# Pair plot to visualize relationships between variables
sns.pairplot(wine_data[['fixed acidity', 'volatile acidity', 'citric acid', 'alcohol', 'quality']])
plt.suptitle('Pair Plot of Selected Features', y=1.02)
plt.show()

# Plotting the heatmap of the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Correlation Matrix')
plt.show()
