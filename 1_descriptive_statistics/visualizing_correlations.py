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



"""
Explanation:
Correlation Matrix:

The correlation matrix is calculated using wine_data.corr(), which computes the correlation between numerical variables.
The heatmap is then used to visually display the correlation matrix, where high correlations (close to 1 or -1) are marked by warm colors (red), 
and weak correlations (close to 0) are marked by cool colors (blue).

Pair Plot: The pair plot is used to visualize pairwise relationships between selected variables (like fixed acidity, volatile acidity, citric acid, alcohol, and quality).
This plot helps identify trends, clusters, and outliers by showing scatterplots for each pair of variables and the distribution of individual variables along the diagonal.

Why These Visualizations Matter:
Heatmaps: They provide an at-a-glance understanding of the strength and direction of relationships between variables. For example, you can quickly 
spot which variables are highly correlated, which is critical for feature selection and multicollinearity analysis.
Pair Plots: They give a deeper look into the actual distribution and pairwise relationships of the variables. These plots can reveal non-linear relationships 
and outliers that might not be apparent in a heatmap.

You can find the Wine Quality dataset here: https://archive.ics.uci.edu/dataset/186/wine+quality
"""