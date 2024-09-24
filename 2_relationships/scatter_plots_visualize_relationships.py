# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

# Load the Breast Cancer dataset from scikit-learn
breast_cancer = load_breast_cancer()

# Create a DataFrame for the features
data1 = pd.DataFrame(breast_cancer['data'], columns=breast_cancer['feature_names'])

# Add the target column to the DataFrame
data1['target'] = breast_cancer['target']

# Create a scatter plot of 'mean radius' vs 'mean texture'
plt.figure(figsize=(10, 6))

# Set a very light blue background color
plt.gca().set_facecolor('#E0F7FA')  # Light blue background

# Plot the points, coloring by the 'target' (malignant or benign)
scatter = plt.scatter(data1['mean radius'], data1['mean texture'], c=data1['target'], cmap='coolwarm', alpha=0.7)

# Add light gridlines
plt.grid(True, color='lightgray', linestyle='--', linewidth=0.5)

# Add labels and title
plt.xlabel('Mean Radius')
plt.ylabel('Mean Texture')
plt.title('Mean Radius vs Mean Texture (Colored by Tumor Type)')

# Add a legend
plt.legend(*scatter.legend_elements(), title="Target (0 = Malignant, 1 = Benign)")

# Show the plot
plt.show()
