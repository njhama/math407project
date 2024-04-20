import numpy as np
import matplotlib.pyplot as plt

# Parameters
mu = 10
sigma = np.sqrt(0.202)  
num_samples = 10000

X = np.random.normal(mu, sigma, num_samples)
Y = np.exp(X)

# Calc empirical exp value of Y
empirical_E_Y = np.mean(Y)
print(f"Empirical Expected Value of Y_1: {empirical_E_Y:.4f}")

# Theoretical exp value E[Y] n
theoretical_E_Y = np.exp(mu + (sigma**2 / 2))
print(f"Theoretical Expected Value of Y_1: {theoretical_E_Y:.4f}")

# Plot
plt.figure(figsize=(10, 6))
plt.hist(Y, bins=50, color='green', alpha=0.8, edgecolor='black')
plt.title('Histogram of Log-Normal Random Variables')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


