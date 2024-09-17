# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Auto MPG dataset (available at UCI Machine Learning Repository)
mpg_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
mpg_columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name']
mpg_df = pd.read_csv(mpg_url, delim_whitespace=True, names=mpg_columns, na_values='?')

# Drop rows with missing values
mpg_df.dropna(inplace=True)

# Convert horsepower to numeric
mpg_df['horsepower'] = pd.to_numeric(mpg_df['horsepower'])

# Create the first scatterplot: Horsepower vs MPG
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(data=mpg_df, x='horsepower', y='mpg', color='blue')
plt.title('Scatterplot of Horsepower vs MPG')

# Create the second scatterplot: Weight vs MPG
plt.subplot(1, 2, 2)
sns.scatterplot(data=mpg_df, x='weight', y='mpg', color='green')
plt.title('Scatterplot of Weight vs MPG')

# Show the plots
plt.tight_layout()
plt.show()

def myfunction(): 
    """
    Explanation:
    Scatterplots: Scatterplots are used to show relationships between two numerical variables. In this case, we're visualizing the relationship between horsepower and MPG, and between weight and MPG.
    First Scatterplot: Shows how horsepower affects miles per gallon (MPG). We expect to see a negative correlation, where higher horsepower might be associated with lower MPG.
    
    Second Scatterplot: Shows how weight affects MPG. Similarly, we expect a negative correlation between the weight of the car and its fuel efficiency (MPG).
    The Auto MPG dataset is a classic dataset that contains data for various cars from the 1970s and 1980s. More details about the dataset can be found
    https://archive.ics.uci.edu/dataset/9/auto+mpg
    """