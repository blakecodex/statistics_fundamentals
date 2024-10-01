import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Step 1: Simulate a population
# Let's simulate a population of 10,000 people with a mean of 60 and a standard deviation of 15
population_mean = 60
population_std = 15
population_size = 10000

# Generate the population data
population = np.random.normal(loc=population_mean, scale=population_std, size=population_size)

# Step 2: Take a random sample
sample_size = 100
sample = np.random.choice(population, size=sample_size)

# Step 3: Calculate sample mean and standard error
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)
standard_error = sample_std / np.sqrt(sample_size)

# Step 4: Compute the 95% Confidence Interval
confidence_level = 0.95
z_score = stats.norm.ppf((1 + confidence_level) / 2)
margin_of_error = z_score * standard_error
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

print(f"Sample Mean: {sample_mean:.2f}")
print(f"Standard Error: {standard_error:.2f}")
print(f"Z-Score (95% Confidence): {z_score:.2f}")
print(f"Margin of Error: {margin_of_error:.2f}")
print(f"95% Confidence Interval: {confidence_interval}")

# Step 5: Visualize the confidence interval
plt.figure(figsize=(10, 6))

# Plot the population distribution
plt.hist(population, bins=50, alpha=0.5, label='Population Distribution', color='lightblue')

# Plot the sample mean with the confidence interval
plt.axvline(sample_mean, color='green', linestyle='--', label=f'Sample Mean = {sample_mean:.2f}')
plt.axvline(confidence_interval[0], color='red', linestyle='--', label=f'Lower CI = {confidence_interval[0]:.2f}')
plt.axvline(confidence_interval[1], color='red', linestyle='--', label=f'Upper CI = {confidence_interval[1]:.2f}')

# Add titles and labels
plt.title("Confidence Interval for Sample Mean")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()

plt.grid(True)
plt.show()

""""
Steps Explained:
-Population Simulation: We create a population of 10,000 individuals with a mean of 60 and a standard deviation of 15.
-Random Sampling: We randomly sample 100 individuals from this population.

Confidence Interval Calculation:
-Sample mean: The mean of the randomly sampled data.
-Standard error: The standard deviation of the sample divided by the square root of the sample size.
-Z-score: For a 95% confidence level, the z-score is approximately 1.96.
-Confidence Interval: We compute the margin of error and derive the confidence interval.

Visualization:
-The histogram shows the population distribution.
-The sample mean and the confidence interval are displayed on the graph as vertical lines, helping visualize the range in which the true population mean likely falls.

Key Output:
-Sample Mean: The calculated mean from the sample.
-95% Confidence Interval: The interval where the true population mean is likely to fall with 95% confidence.
"""