import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

# Params
mu = 10
sigma_1_squared = 0.20**2 
sigma = np.sqrt(sigma_1_squared)
num_samples = 10000

X = np.random.normal(mu, sigma, num_samples)
Y = np.exp(X)

# Empirical expected value of Y
empirical_E_Y = np.mean(Y)
print(f"Empirical Expected Value of Y_1: {empirical_E_Y:.4f}")

# Empirical variance of Y
empirical_var_Y = np.var(Y)
print(f"Empirical Variance of Y_1: {empirical_var_Y:.4f}")

# Theoretical expected value of Y
theoretical_E_Y = np.exp(mu + (sigma**2 / 2))
print(f"Theoretical Expected Value of Y_1: {theoretical_E_Y:.4f}")

plt.figure(figsize=(10, 6))
plt.hist(Y, bins=50, color='green', alpha=0.8, edgecolor='black', density=True, label='Empirical Histogram')

# Calculating and plotting the theoretical PDF
s = sigma 
scale = np.exp(mu) 
x = np.linspace(min(Y), max(Y), 1000)
pdf = lognorm.pdf(x, s=s, scale=scale)
plt.plot(x, pdf, 'r-', lw=2, label='Theoretical PDF')
plt.title('Empirical Histogram and Theoretical PDF of Log-Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()
plt.show()
