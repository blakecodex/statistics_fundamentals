import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate a large dataset
np.random.seed(0)
large_data = np.random.normal(loc=50, scale=10, size=1000)  # Normally distributed large dataset

# Generate a small dataset
small_data = np.random.normal(loc=50, scale=10, size=30)  # Normally distributed small dataset

# Add an outlier to both datasets
small_data_with_outlier = np.append(small_data, [200])  # Adding an extreme outlier to small dataset
large_data_with_outlier = np.append(large_data, [200])  # Adding the same outlier to large dataset

# Calculate variance and standard deviation
small_data_std = np.std(small_data)
small_data_outlier_std = np.std(small_data_with_outlier)

large_data_std = np.std(large_data)
large_data_outlier_std = np.std(large_data_with_outlier)

# Print standard deviations
print(f"Small Dataset Standard Deviation (without outlier): {small_data_std:.2f}")
print(f"Small Dataset Standard Deviation (with outlier): {small_data_outlier_std:.2f}")
print(f"Large Dataset Standard Deviation (without outlier): {large_data_std:.2f}")
print(f"Large Dataset Standard Deviation (with outlier): {large_data_outlier_std:.2f}")

# Visualize both small and large datasets with outliers
plt.figure(figsize=(12, 6))

# Small dataset histogram
plt.subplot(2, 2, 1)
sns.histplot(small_data_with_outlier, kde=True, color='red', bins=10)
plt.title('Small Dataset with Outlier')

# Large dataset histogram
plt.subplot(2, 2, 2)
sns.histplot(large_data_with_outlier, kde=True, color='blue', bins=30)
plt.title('Large Dataset with Outlier')

# Small dataset boxplot
plt.subplot(2, 2, 3)
sns.boxplot(data=small_data_with_outlier, color='orange')
plt.title('Small Dataset with Outlier: Boxplot')

# Large dataset boxplot
plt.subplot(2, 2, 4)
sns.boxplot(data=large_data_with_outlier, color='green')
plt.title('Large Dataset with Outlier: Boxplot')

plt.tight_layout()
plt.show()

"""
Explanation:
Data Generation:

A small dataset with 30 data points and a large dataset with 1000 data points are generated using normal distribution.
We then introduce an outlier (value = 200) to both datasets to observe its effect.
Descriptive Statistics:

We calculate the standard deviation for both datasets with and without the outlier.
The small dataset’s standard deviation increases much more drastically after adding the outlier compared to the large dataset, illustrating how outliers have a disproportionate effect on smaller datasets.
Visualization:

Histograms and box plots are used to show the spread of data and outliers. You’ll notice that the small dataset is significantly influenced by the outlier, showing a large spread in the histogram and an outlier in the box plot. The large dataset, on the other hand, remains more stable.
Why This Matters:
In small samples, outliers can significantly distort descriptive statistics like variance and standard deviation, leading to overfitting or incorrect conclusions. 
This happens because, in smaller datasets, each individual data point has a larger impact on the overall statistics.
In larger datasets, the effect of outliers is often mitigated because the data points are more numerous and tend to "average out" the impact of extreme values.
By visualizing this effect, we can clearly demonstrate why small datasets are more prone to overfitting or misinterpretation due to the presence of outliers or anomalies.

"""