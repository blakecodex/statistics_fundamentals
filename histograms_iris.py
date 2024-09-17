# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Create the first histogram: Sepal Length
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(iris_df['sepal length (cm)'], kde=True, color='blue')
plt.title('Distribution of Sepal Length')

# Create the second histogram: Petal Length
plt.subplot(1, 2, 2)
sns.histplot(iris_df['petal length (cm)'], kde=True, color='green')
plt.title('Distribution of Petal Length')

# Show the plots
plt.tight_layout()
plt.show()

def my_function():
    """
    Explanation: using sns.histplot(): We use Seaborn's histplot() to create the histograms, adding KDE (Kernel Density Estimate) to smooth the curve.
    First Histogram: Shows the distribution of sepal length.
    Second Histogram: Shows the distribution of petal length.
    
    This gives you a clear visual representation of how different features in the Iris dataset are distributed.

    The Iris dataset is a classic dataset from the UCI repository and is available for use in Python. You can explore more about it 
    here: https://archive.ics.uci.edu/dataset/53/iris
    """
    pass