import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Discrete Random Variable Example (e.g., number of defective products in a batch)
# We'll simulate 1000 batches, each batch can have 0, 1, 2, 3 defective products with different probabilities
probabilities = [0.6, 0.25, 0.1, 0.05]  # Probabilities of 0, 1, 2, or 3 defective products
batch_size = 1000
defective_products = np.random.choice([0, 1, 2, 3], size=batch_size, p=probabilities)

# Continuous Random Variable Example (e.g., stock prices, modeled by a normal distribution)
# We'll simulate stock prices based on a normal distribution with a mean of 100 and std of 15
mean_stock_price = 100
std_stock_price = 15
stock_prices = np.random.normal(loc=mean_stock_price, scale=std_stock_price, size=batch_size)

# Plot Discrete Random Variable
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(defective_products, discrete=True, color='skyblue', edgecolor='black', bins=4)
plt.title("Discrete Random Variable (Defective Products)")
plt.xlabel("Number of Defective Products")
plt.ylabel("Frequency")

# Plot Continuous Random Variable
plt.subplot(1, 2, 2)
sns.histplot(stock_prices, kde=True, color='salmon', edgecolor='black')
plt.title("Continuous Random Variable (Stock Prices)")
plt.xlabel("Stock Price")
plt.ylabel("Frequency")

# Show the plots
plt.tight_layout()
plt.show()

# Print basic statistics for each
print("Discrete Random Variable (Defective Products) - Mean:", np.mean(defective_products))
print("Continuous Random Variable (Stock Prices) - Mean:", np.mean(stock_prices))
