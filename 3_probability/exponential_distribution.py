# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Parameters for the Exponential Distribution
lambda_rate = 0.3  # Rate parameter (1/mean time between events)
n_samples = 1000  # Number of samples to generate

# Generate exponential distribution data
exp_data = np.random.exponential(1/lambda_rate, n_samples)

# Plot the Exponential Distribution
plt.figure(figsize=(10, 6))
sns.histplot(exp_data, bins=50, kde=True, color='purple')
plt.title(f"Exponential Distribution (λ = {lambda_rate})")
plt.xlabel("Time between events")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Check total number of experiments to ensure correctness
print(f"Total number of experiments: {n_samples}")
print(f"Sum of frequencies: {len(exp_data)}")

# Interpretation:
"""
The Exponential Distribution models the time between independent events happening at a constant rate.
For example, it could represent the time between arrivals of buses at a station or the time between phone calls at a call center.

Explanation:
-Exponential Distribution: It models the waiting time between successive events in a Poisson process, like waiting for a bus or phone calls arriving at a call center.
-Lambda (λ): The rate parameter controls how quickly events happen. A smaller λ means longer waiting times, while a larger λ means shorter waiting times.

Practical Example:
-If you're working in a setting like network traffic management, where events like packet arrivals follow a Poisson process, 
the Exponential Distribution is used to model the time between incoming packets.
"""
