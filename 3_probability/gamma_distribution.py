def overview_function ():
    """
    Gamma Distribution Overview:
    The Gamma Distribution is a two-parameter family of continuous probability distributions. It’s often used to model the time until an event happens for a process that has multiple stages (e.g., the time for multiple radioactive particles to decay).

    It can be thought of as a generalization of the Exponential Distribution.
    Parameters:
    -Shape parameter (k): This controls the shape of the distribution.
    -Scale parameter (θ): This is similar to the inverse of the rate parameter in an Exponential Distribution, determining the spread of the distribution.
    """
    pass

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Parameters for the Gamma Distribution
shape_param = 2.0  # Shape parameter (k)
scale_param = 2.0  # Scale parameter (theta)
n_samples = 1000  # Number of samples

# Generate Gamma distribution data
gamma_data = np.random.gamma(shape=shape_param, scale=scale_param, size=n_samples)

# Plot the Gamma Distribution
plt.figure(figsize=(10, 6))

# Plot a histogram of the data with KDE
sns.histplot(gamma_data, bins=30, kde=True, color='lightcoral')
plt.title(f"Gamma Distribution (k={shape_param}, θ={scale_param}) - {n_samples} Samples")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Check basic statistics of the generated data
mean_gamma = np.mean(gamma_data)
std_gamma = np.std(gamma_data)

print(f"Mean of the generated data: {mean_gamma}")
print(f"Standard deviation of the generated data: {std_gamma}")

"""
Key Parameters:
 - Shape Parameter (k): Controls the shape of the distribution. Higher values of k make the distribution more symmetric and bell-shaped.
 - Scale Parameter (θ): Similar to the scale in the Exponential Distribution, it controls how spread out the distribution is.

Insights:
  - Flexible Distribution: By adjusting the shape and scale parameters, the Gamma Distribution can take on many forms. When k=1, the Gamma Distribution becomes an Exponential Distribution.
  - Applications: This distribution is used in reliability analysis, queuing models, and Bayesian statistics, among other fields.
This Gamma Distribution example provides a great way to model sums of waiting times, such as the time for multiple independent events to occur.
"""