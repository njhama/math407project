import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters 
mean = 1.5
std_dev = 2
num_samples = 20
num_simulations = 100

# Calc
sample_means = np.array([np.mean(np.random.normal(mean, std_dev, num_samples)) for _ in range(num_simulations)])
# Calc empirical prob  sample mean > 0
empirical_prob = np.mean(sample_means > 0)
print(f"Empirical Probability (Sample Mean > 0): {empirical_prob:.4f}")

# Calculate the theoretical prob sample mean > 0
theoretical_mean = mean
theoretical_std_dev = std_dev / np.sqrt(num_samples)
theoretical_prob = norm.sf(0, loc=theoretical_mean, scale=theoretical_std_dev)
print(f"Theoretical Probability (Sample Mean > 0): {theoretical_prob:.4f}")

# Plotting the histogram of the sample means
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=np.arange(-4, 10.5, 0.5), color='yellow', edgecolor='black')
plt.title('Histogram of Sample Means')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

