'''
a) Use the numbers generated in problem 1 b) to generate 10000 random numbers that represent the daily price
fluctuation of a financial asset that can have an increase of 100 with probability 0.45, a decrease of 200 with
probability 0.25, or stays the same with probability 0.3. In other words, generate a discrete random variable that
takes the values 100, 200 and 0 with probabilities 0.45, 0.25 and 0.3 respectively.

b) Plot the histogram obtained using the data generated in part a)
'''

import numpy as np
import matplotlib.pyplot as plt

numbers_to_gen = 10000

uniform_numbers = np.random.rand(numbers_to_gen)

def map_to_fluctuations(uniform_numbers):
    fluctuations = np.zeros_like(uniform_numbers)
    fluctuations[uniform_numbers <= 0.45] = 100                                 # [0,45%] => +100
    fluctuations[(uniform_numbers > 0.45) & (uniform_numbers <= 0.70)] = -200   # (45%, 70%) => -200
    fluctuations[uniform_numbers > 0.70] = 0                                    # (70%,100%] => 0
    return fluctuations

price_fluctuations = map_to_fluctuations(uniform_numbers)
weights = np.ones_like(price_fluctuations) / len(price_fluctuations) * 100

# Plot 
plt.figure(figsize=(8, 5))
# [-250, -150] = -200
# [-150,-50] = 0
# [50, 150] = 100
plt.hist(price_fluctuations, bins=[-250, -150, -50, 50, 150], weights=weights, align='mid', color='blue', rwidth=0.8)
plt.title('Daily Price Fluctuations')
plt.xlabel('Price Fluctuation')
plt.ylabel('Percentage (%) = 1')
plt.xticks([-200, 0, 100])
plt.grid(True)
plt.show()