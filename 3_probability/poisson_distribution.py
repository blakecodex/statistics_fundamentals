# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameters for the Poisson distribution
lambda_param = 5  # Average number of events (e.g., 5 cars passing through a tollbooth in an hour)

# Generate Poisson distribution for possible outcomes (0 to 15 events)
x = np.arange(0, 16)
probabilities = poisson.pmf(x, lambda_param)

# Plotting the Poisson distribution
plt.figure(figsize=(10, 6))
plt.bar(x, probabilities, color='purple', edgecolor='black')

# Add titles and labels
plt.title(f'Poisson Distribution: λ = {lambda_param}')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.xticks(x)
plt.grid(True)

# Show plot
plt.show()

# Simulating the Poisson process (e.g., number of cars passing in 1 hour for 1000 trials)
n_trials = 1000
simulation_results = np.random.poisson(lambda_param, n_trials)

# Plotting the simulation results
plt.figure(figsize=(10, 6))
plt.hist(simulation_results, bins=np.arange(0, 16)-0.5, rwidth=0.8, color='orange', edgecolor='black')

# Add titles and labels
plt.title(f'Simulation of {n_trials} trials: Number of events per interval (λ = {lambda_param})')
plt.xlabel('Number of Events')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, 16))
plt.grid(True)

# Show plot
plt.show()

"""
Explanation:
Poisson Distribution (Theoretical)

We simulate the Poisson distribution using the formula for the probability mass function (PMF) in scipy.stats.poisson.pmf.
The parameter:
lambda_param = 5 (the average number of events, such as 5 cars passing through a tollbooth in an hour).
The script calculates the probability of getting 0 to 15 events in the interval and plots the probabilities.
Simulating the Poisson Process

We simulate the Poisson process using np.random.poisson(), which simulates how many events (e.g., cars passing) occur over 1000 intervals (hours).
A histogram shows the frequency of different event counts in each trial.
Use Cases of Poisson Distribution
Number of customer arrivals at a store per hour.
Number of emails received in a given time frame.
Number of defects per unit in a manufacturing process.
"""