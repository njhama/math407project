# Math 407 Project

### 1. Random Number Generation and Histogram Comparison
- **a)** Use the random number generator \(x_n \equiv (ax_{n-1} + c) \mod m\) with \(a = 75\), \(c = 0\) and \(m = 2^{31} - 1\) to generate 10000 uniformly distributed random numbers on \([0, 1]\) and plot the histogram.
- **b)** Generate 10000 uniformly distributed random numbers on \([0, 1]\) using built-in function of MATLAB or other statistical software package.
- **c)** Compare the histograms obtained in parts a) and b).

##### Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
```

##### Parameters used
```python
a = 75
c = 0
m = 2**31 - 1
n_samples = 10000
x0 = 1
```

##### Function
```python
def lcg_random_numbers(x0, n_samples, a, c, m):
    random_numbers = np.zeros(n_samples)
    random_numbers[0] = x0
    for i in range(1, n_samples):
        random_numbers[i] = (a * random_numbers[i-1] + c) % m
    # normalize 
    return random_numbers / m  

lcg_numbers = lcg_random_numbers(x0, n_samples, a, c, m)
numpy_numbers = np.random.uniform(low=0.0, high=1.0, size=n_samples)
```

##### Plot 
```python
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
```

##### Graph Results
![one result](img/one_results.png)

---
### 2. Daily Price Fluctuation Simulation
- **a)** Use the numbers generated in problem 1 b) to generate 10000 random numbers that represent the daily price fluctuation of a financial asset that can have an increase of 100 with probability 0.45, a decrease of 200 with probability 0.25, or stays the same with probability 0.3. In other words, generate a discrete random variable that takes the values 100, 200 and 0 with probabilities 0.45, 0.25 and 0.3 respectively.
- **b)** Plot the histogram obtained using the data generated in part a).
##### Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
```

##### Parameters
```python
numbers_to_gen = 10000
uniform_numbers = np.random.rand(numbers_to_gen)
```


##### Calculations
```python
def map_to_fluctuations(uniform_numbers):
    fluctuations = np.zeros_like(uniform_numbers)
    fluctuations[uniform_numbers <= 0.45] = 100                                 # [0,45%] => +100
    fluctuations[(uniform_numbers > 0.45) & (uniform_numbers <= 0.70)] = -200   # (45%, 70%) => -200
    fluctuations[uniform_numbers > 0.70] = 0                                    # (70%,100%] => 0
    return fluctuations

price_fluctuations = map_to_fluctuations(uniform_numbers)
weights = np.ones_like(price_fluctuations) / len(price_fluctuations) * 100
```

##### Plot
```python
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
```

---
### 3. Binomial Distribution Simulation
Generate 5000 Binomial distributed \(n = 70, p = 0.7\) random numbers by doing: Use Bernoulli random variables. Plot the histogram and use your data to calculate the probability that the Binomial random variable is less than 50. Compare with the theoretical answer.

### 4. Normal Distribution Analysis
- **a)** Simulate 1000 random normal variables with mean 1.5 and standard deviation 2. Create a histogram. Use a build in software package or investigate how to build your own (not that difficult).
- **b)** Find out how many of your 1000 variables are bigger than 0, and estimate the probability that a single normal variable with mean 1.5 and standard deviation 2 is above 0. Also, compute and write the theoretical value for this probability.

### 5. Simulation of Sample Means
Simulate 100 sample means, each made by taking the average of 20 normal variables with mean 1.5 and standard deviation 2. Make a histogram of these sample means in the range −4 to 10 with class intervals of length 0.5. As in the previous question, estimate the probability that a sample mean is bigger than 0. Also, compute and write the theoretical value for this probability.

### 6. Expected Value of Sum of Uniform Random Variables
- **a)** Let \(U_1, U_2, \dots, U_n\) be uniform random variables on \([0, 1]\). Define \(N = \min\{n : \sum_{i=1}^n U_i > 1\}\). Organize in a table the estimates of \(E[N]\) obtained by generating 10, 10^2, \dots, 10^6 values of \(N\).
- **b)** Are your estimates in part a) converging to a particular value? If so, in what sense?
- **c)** Calculate theoretically the \(E[N]\) and compare your result with the one obtained in part a).

### 7. Log-Normal Variable Simulation and Analysis
- **a)** Let's consider the Normal random variables \(X_1\) with mean \(\mu_1 = 10\) and variance \(\sigma_1^2 = 0.202\)
    - Generate 10000 log-normal random variables \(Y_1 = e^{X_1}\)
- **b)** Estimate \(E[Y_1]\) and compare with the theoretical result.

### 8. Integral Estimation
- **a)** Consider the integral \(I = \int_0^1 \int_0^1 e^{x+y} dx dy\).
    - Estimate the integral \(I\). Compare with the theoretical result. You can see this integral as an expectation.

### 9. Verification of Theoretical Statistical Properties
- **a)** The normal approximation of the binomial distribution.
- **b)** The sum of two normal random variables is a normal random variable.
- **c)** The density of the sum of two uniform \([0,1]\) random variables has a triangular distribution.
- **d)** Let \(X_i\) be the sum of the results of \(i\) rolls of the same die. (take
