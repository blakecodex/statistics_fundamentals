def my_function ():
    """
    The idea here:
    -Start with a population that has a non-normal distribution (e.g., a skewed or uniform distribution).
    -Randomly draw many samples of a certain size from this population.
    -Calculate the mean of each sample.
    -Plot the distribution of these sample means to observe how it approaches a normal distribution as the sample size increases, even though the original population may not be normally distributed.
    """
    pass

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate a non-normal population distribution (right-skewed)
population = np.random.exponential(scale=2, size=10000)

# Visualize the population distribution
plt.figure(figsize=(12, 6))
sns.histplot(population, bins=30, kde=True, color='darkblue')
plt.title('Original Population Distribution (Exponential)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Step 2: Simulate the Central Limit Theorem
def sample_means(population, sample_size, num_samples):
    means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size, replace=True)
        means.append(np.mean(sample))
    return means

# Simulate for different sample sizes
sample_sizes = [5, 30, 100]
num_samples = 1000

plt.figure(figsize=(12, 6))

for i, sample_size in enumerate(sample_sizes, 1):
    means = sample_means(population, sample_size, num_samples)
    
    # Step 3: Visualize the distribution of the sample means
    plt.subplot(1, 3, i)
    sns.histplot(means, bins=30, kde=True, color='darkred')
    plt.title(f'Sample Size = {sample_size}')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')
    plt.grid(True)

plt.tight_layout()
plt.show()

"""
Explanation:
-Step 1: We generate a right-skewed population using an exponential distribution to ensure the population is not normally distributed.
-Step 2: We repeatedly draw samples of varying sizes (e.g., 5, 30, and 100) from this population and calculate the mean of each sample.
-Step 3: We plot the distribution of these sample means. As the sample size increases, the distribution of the sample means will tend to be normally distributed, regardless of the skewness of the original population.

Results:
-For small sample sizes (e.g., 5), the distribution of sample means might still resemble the original population's skewed shape.
-As the sample size increases (e.g., 30 or 100), the distribution of the sample means approaches a normal distribution, even though the original population is skewed. This is the essence of the Central Limit Theorem (CLT).
"""