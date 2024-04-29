import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mean = 1.5
std_dev = 2
num_samples = 1000

# Generating normal samples
normal_variables = np.random.normal(mean, std_dev, num_samples)

# For part B
greater_than_zero = np.sum(normal_variables > 0)
probability_empirical = greater_than_zero / num_samples
print(f"Number of variables greater than 0: {greater_than_zero}")
print(f"Empirical Probability that a variable is > 0: {probability_empirical:.4f}")

probability_theoretical = 1 - norm.cdf(0, loc=mean, scale=std_dev)
print(f"Theoretical Probability that a variable is > 0: {probability_theoretical:.4f}")

# Plotting the empirical histogram
plt.figure(figsize=(10, 6))
count, bins, ignored = plt.hist(normal_variables, bins=30, color='skyblue', alpha=0.8, edgecolor='black', density=True)

# Calculating and plotting the theoretical PDF
x = np.linspace(norm.ppf(0.001, loc=mean, scale=std_dev), norm.ppf(0.999, loc=mean, scale=std_dev), 100)
pdf = norm.pdf(x, loc=mean, scale=std_dev)
plt.plot(x, pdf, 'r-', lw=2, label='Theoretical PDF')

# Adding titles and labels
plt.title('Histogram and Theoretical PDF of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
