import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
np.random.seed(0)
data = {
    'feature_1': np.random.normal(loc=50, scale=10, size=1000),  # Normally distributed
    'feature_2': np.random.exponential(scale=2, size=1000)       # Skewed (exponential distribution)
}
df = pd.DataFrame(data)

# Function to calculate descriptive statistics
def calculate_stats(column):
    stats = {
        'mean': np.mean(column),
        'median': np.median(column),
        'variance': np.var(column),
        'std_dev': np.std(column),
        'skewness': pd.Series(column).skew(),
        'kurtosis': pd.Series(column).kurtosis()
    }
    return stats

# Apply normalization (StandardScaler)
scaler = StandardScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Apply log transformation to the skewed feature
df_log_transformed = df.copy()
df_log_transformed['feature_2'] = np.log(df_log_transformed['feature_2'] + 1)  # Add 1 to avoid log(0)

# Descriptive statistics before transformation
stats_before = df.apply(calculate_stats)
print("Descriptive Statistics Before Transformation:")
print(stats_before)

# Descriptive statistics after normalization and log transformation
stats_after = df_log_transformed.apply(calculate_stats)
print("\nDescriptive Statistics After Normalization and Log Transformation:")
print(stats_after)

# Visualization (optional)
plt.figure(figsize=(12, 6))

# Original feature_2 distribution (skewed)
plt.subplot(1, 2, 1)
sns.histplot(df['feature_2'], kde=True, color='blue')
plt.title('Feature 2: Original Distribution')

# Log transformed feature_2 distribution (more normalized)
plt.subplot(1, 2, 2)
sns.histplot(df_log_transformed['feature_2'], kde=True, color='green')
plt.title('Feature 2: Log Transformed Distribution')

plt.tight_layout()
plt.show()

def my_function ():
    """
    Explanation:
    
    Descriptive Statistics Calculation: We compute the mean, median, variance, standard deviation, skewness, and kurtosis for each feature. 
    These help understand the central tendency and spread of the data.

    Normalization: We apply StandardScaler from sklearn to normalize the data, which is a common preprocessing step before feeding data into machine learning models. 
    It ensures all features are on a similar scale.
    
    Log Transformation: We apply a log transformation to the skewed feature (feature_2). Logarithmic transformations are useful for reducing skewness, 
    which makes it easier for machine learning models to handle skewed data.
    
    Visualization (Optional): We plot the distribution of the original skewed feature (feature_2) and the log-transformed version to see how 
    the transformation affects the distribution.

    Why This Matters for Feature Engineering:
    -Central Tendency and Spread: Understanding the mean, median, and spread helps identify which features need scaling or transformation before being used in machine learning models.
    -Skewness: A high skewness might signal the need for transformations like log or square root.
    -Normalization: Ensures that features with different units and ranges don’t affect the performance of machine learning algorithms that assume normally distributed data or equal feature importance.
    -This approach helps in feature engineering by making the data more suitable for machine learning models, reducing the chance of overfitting, and improving performance.

    """
    pass