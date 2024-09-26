# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters for the binomial distribution
n_trials = 10  # Number of coin flips (trials)
p_success = 0.5  # Probability of success (e.g., flipping heads)

# Generate a binomial distribution for the given parameters
x = np.arange(0, n_trials+1)  # Possible outcomes (0 to n_trials successes)
probabilities = binom.pmf(x, n_trials, p_success)

# Plotting the binomial distribution
plt.figure(figsize=(10, 6))
plt.bar(x, probabilities, color='blue', edgecolor='black')

# Add titles and labels
plt.title(f'Binomial Distribution: n = {n_trials}, p = {p_success}')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.xticks(x)
plt.grid(True)

# Show plot
plt.show()

# Simulating coin flips (e.g., flipping a coin 10 times for 1000 experiments)
n_experiments = 1000
simulation_results = np.random.binomial(n_trials, p_success, n_experiments)

# Plotting the simulation results
plt.figure(figsize=(10, 6))
plt.hist(simulation_results, bins=np.arange(0, n_trials+2)-0.5, rwidth=0.8, color='green', edgecolor='black')

# Add titles and labels
plt.title(f'Simulation of {n_experiments} experiments: Flipping a coin {n_trials} times')
plt.xlabel('Number of Successes (Heads)')
plt.ylabel('Frequency')
plt.xticks(np.arange(0, n_trials+1))
plt.grid(True)

# Show plot
plt.show()

def my_function():
    """
    Explanation:
    
    Binomial Distribution (Theoretical)
    We simulate the binomial distribution using the formula for the probability mass function (PMF) in scipy.stats.binom.pmf.
    
    The parameters:
    n_trials = 10 (10 coin flips).
    p_success = 0.5 (50% probability of success, i.e., getting heads).

    The script calculates the probability of getting between 0 and 10 successes (heads) and plots the probabilities.
    Simulating Coin Flips

    We simulate flipping a coin 10 times across 1000 different experiments using np.random.binomial().
    The script then plots a histogram of the number of successes (heads) observed in each experiment.
    """
    pass