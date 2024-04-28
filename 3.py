import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 70
p = 0.7
num_samples = 5000

# Generating binomial samples
bernoulli_trials = np.random.binomial(1, p, (num_samples, n))
binomial_samples = np.sum(bernoulli_trials, axis=1)

# Calculating empirical and theoretical probabilities
prob_empirical = np.mean(binomial_samples < 50)
print(f"Empirical Probability (X < 50): {prob_empirical:.4f}")
prob_theoretical = binom.cdf(49, n, p)
print(f"Theoretical Probability (X < 50): {prob_theoretical:.4f}")

# Counting occurrences of each number of successes
count = {}
for val in binomial_samples:
    if val not in count:
        count[val] = 1
    else:
        count[val] += 1
print(count)


# Plotting the empirical histogram
fig, ax = plt.subplots(figsize=(10, 10))
ax.hist(binomial_samples, bins=range(n+2), alpha=0.75, color='pink', edgecolor='black', density=True, label='Empirical Data')

# Calculating and plotting the theoretical PMF
x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)
ax.plot(x, pmf, 'bo-', label='Theoretical PMF', markersize=5)

# Adding titles and labels
ax.set_title(f"Histogram and Theoretical PMF of Binomial Distribution ($n=70, p=0.7$)")
plt.suptitle(f"Empirical Prob (X < 50): {prob_empirical:.4f} & Theoretical Prob (X < 50): {prob_theoretical:.4f}", fontsize=10, fontweight='bold')
ax.set_xlabel('Number of Successes')
ax.set_ylabel('Probability')
ax.grid(True)
ax.legend()

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 1]) 
plt.show()
