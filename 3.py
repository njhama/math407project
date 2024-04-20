import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 70           
p = 0.7          
num_samples = 5000


bernoulli_trials = np.random.binomial(1, p, (num_samples, n))
binomial_samples = np.sum(bernoulli_trials, axis=1)
prob_empirical = np.mean(binomial_samples < 50)
print(f"Empirical Probability (X < 50): {prob_empirical:.4f}")

prob_theoretical = binom.cdf(49, n, p)  
print(f"Theoretical Probability (X < 50): {prob_theoretical:.4f}")

# Plot
plt.figure(figsize=(10, 6))
plt.hist(binomial_samples, bins=range(n+2), alpha=0.75, color='purple', edgecolor='black')
plt.title('Histogram of Binomial Distribution ($n=70, p=0.7$)')
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


