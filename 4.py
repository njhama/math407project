import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mean = 1.5
std_dev = 2
num_samples = 1000

# Calculate normal variables
normal_variables = np.random.normal(mean, std_dev, num_samples)

# Calculate the number of variables greater than 0
greater_than_zero = np.sum(normal_variables > 0)
# Calculate the empirical probability of a variable being greater than 0
probability_empirical = greater_than_zero / num_samples
print(f"Number of variables greater than 0: {greater_than_zero}")
print(f"Empirical Probability that a variable is > 0: {probability_empirical:.4f}")

# Calculate the theoretical probability using the CDF of the normal distribution
probability_theoretical = 1 - norm.cdf(0, loc=mean, scale=std_dev)
print(f"Theoretical Probability that a variable is > 0: {probability_theoretical:.4f}")

# Plotting
plt.figure(figsize=(10, 6))
# Plot a histogram of the normal variables
plt.hist(normal_variables, bins=30, color='skyblue', alpha=0.8, edgecolor='black')
# Add title and labels
plt.title('Histogram of 1000 Random Normal Variables')
plt.xlabel('Value')
plt.ylabel('Frequency')
# Add grid
plt.grid(True)

# Add text annotations for empirical values
plt.text(x=-4, y=80, s=f'Empirical Probability > 0: {probability_empirical:.4f}', color='red')
plt.text(x=-4, y=75, s=f'Number > 0: {greater_than_zero}', color='red')

# Show the plot
plt.show()
