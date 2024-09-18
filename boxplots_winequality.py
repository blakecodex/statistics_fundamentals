# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Wine Quality dataset (available at UCI Machine Learning Repository)
wine_df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", delimiter=';')

# Create the first boxplot: Fixed Acidity
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(data=wine_df, y='fixed acidity', color='lightblue')
plt.title('Boxplot of Fixed Acidity')

# Create the second boxplot: Alcohol
plt.subplot(1, 2, 2)
sns.boxplot(data=wine_df, y='alcohol', color='lightgreen')
plt.title('Boxplot of Alcohol')

# Show the plots
plt.tight_layout()
plt.show()

def my_function():
    """
    Explanation: using sns.boxplot(): We use Seaborn's boxplot() function to create the boxplots. Each plot shows the distribution of a feature, including the median (central line), quartiles (box), and potential outliers (points outside the whiskers).
    First Boxplot: Shows the distribution of fixed acidity in the wine dataset.
    Second Boxplot: Shows the distribution of alcohol content.
    """
    pass
