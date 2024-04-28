'''
a) Use the random number generator 𝒙𝒏 ≡ (𝒂𝒙𝒏−𝟏 + 𝒄) 𝒎𝒐𝒅(𝒎) with 𝒂 = 𝟕
𝟓, 𝒄 = 𝟎 𝒂𝒏𝒅 𝒎 = 𝟐^𝟑𝟏 − 𝟏 togenerate 10000 uniformly distributed random numbers on [𝟎, 𝟏] and plot the histogram.

b) Generate 10000 uniformly distributed random numbers on [𝟎, 𝟏] using built-in function of MATLAB or other
statistical software package.

c) Compare the histograms obtained in parts a) and b).
'''

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# params
a = 7**5
c = 0
m = 2**31 - 1
n_samples = 10000
x0 = 1

# funcy
def lcg_random_numbers(x0, n_samples, a, c, m):
    random_numbers = np.zeros(n_samples)
    random_numbers[0] = x0
    for i in range(1, n_samples):
        random_numbers[i] = (a * random_numbers[i-1] + c) % m
    # normalize 
    return random_numbers / m  

lcg_numbers = lcg_random_numbers(x0, n_samples, a, c, m)
numpy_numbers = np.random.uniform(low=0.0, high=1.0, size=n_samples)

# Plot
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(lcg_numbers, bins=50, color='blue', alpha=0.7)
plt.title('Histogram of LCG Random Numbers')
plt.xlabel('Number range')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(numpy_numbers, bins=50, color='green', alpha=0.7)
plt.title('Histogram of Numpy Random Numbers')
plt.xlabel('Number range')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
