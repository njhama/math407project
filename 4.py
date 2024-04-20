import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mean = 1.5
std_dev = 2
num_samples = 1000

# Calc
normal_variables = np.random.normal(mean, std_dev, num_samples)

# For part B
greater_than_zero = np.sum(normal_variables > 0)
probability_empirical = greater_than_zero / num_samples
print(f"Number of variables greater than 0: {greater_than_zero}")
print(f"Empirical Probability that a variable is > 0: {probability_empirical:.4f}")

probability_theoretical = 1 - norm.cdf(0, loc=mean, scale=std_dev)
print(f"Theoretical Probability that a variable is > 0: {probability_theoretical:.4f}")

# Plot
plt.figure(figsize=(10, 6))
plt.hist(normal_variables, bins=30, color='skyblue', alpha=0.8, edgecolor='black')
plt.title('Histogram of 1000 Random Normal Variables')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

