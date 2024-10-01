import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Step 1: Generate a non-normal population distribution (Exponential)
population = np.random.exponential(scale=5, size=10000)

# Population mean and standard deviation
pop_mean = np.mean(population)
pop_std = np.std(population)

print(f"Population mean: {pop_mean:.2f}, Population std deviation: {pop_std:.2f}")

# Step 2: Define sample size and take multiple samples to calculate sample means
sample_size = 50
num_samples = 1000
sample_means = []

for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size, replace=True)
    sample_means.append(np.mean(sample))

# Step 3: Calculate the mean and standard deviation of the sample means
sample_mean = np.mean(sample_means)
sample_std = np.std(sample_means)

print(f"Sample means distribution mean: {sample_mean:.2f}, Sample means std deviation: {sample_std:.2f}")

# Step 4: Use CLT to approximate the probability of the sample mean being above a threshold (e.g., 8)
threshold = 8
z_score = (threshold - sample_mean) / (sample_std / np.sqrt(sample_size))  # Calculate Z-score
probability_above_threshold = 1 - stats.norm.cdf(z_score)  # Use normal CDF to calculate the probability

print(f"Z-score: {z_score:.2f}")
print(f"Probability that the sample mean is above {threshold}: {probability_above_threshold:.4f}")

# Step 5: Visualize the distribution of the sample means
plt.figure(figsize=(12, 6))
plt.hist(sample_means, bins=30, edgecolor='black', alpha=0.7, color='lightgreen')
plt.axvline(threshold, color='red', linestyle='dashed', linewidth=2, label=f'Threshold = {threshold}')
plt.title('Distribution of Sample Means (Using CLT)')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

""""
Explanation:
-Population: We generate a population using an exponential distribution to ensure it's not normally distributed.
-Sample Means: We draw random samples of size 50 and calculate their means.
-Normal Approximation (CLT): Using the sample means' distribution, we calculate the Z-score to find the probability that the sample mean is greater than 8.
-Probability Calculation: Using the Z-score and the standard normal distribution, we compute the probability of the sample mean exceeding the threshold.

Output:
-Z-Score tells us how many standard deviations the threshold is away from the sample mean.
-The Probability value represents the likelihood that a random sample of size 50 will have a mean spending greater than $8, based on the CLT.

Visualization:
-The histogram of sample means will demonstrate how the distribution of means becomes approximately normal, even though the original population was skewed.
"""