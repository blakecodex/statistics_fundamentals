# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Number of trials (coin flips)
n_trials = 1000

# Simulate flipping a fair coin (0 = Tails, 1 = Heads)
coin_flips = np.random.choice([0, 1], size=n_trials)

# Calculate the cumulative mean of heads
cumulative_mean = np.cumsum(coin_flips) / np.arange(1, n_trials + 1)

# Plot the cumulative mean to visualize the Law of Large Numbers
plt.figure(figsize=(10, 6))
plt.plot(cumulative_mean, label="Cumulative Mean of Heads")
plt.axhline(y=0.5, color='r', linestyle='--', label="Expected Value (0.5)")
plt.xlabel("Number of Trials")
plt.ylabel("Proportion of Heads")
plt.title("Law of Large Numbers: Coin Flip Example")
plt.legend()
plt.grid(True)
plt.show()