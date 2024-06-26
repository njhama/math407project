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
![two results](/img/two_results.png)
---


### 3. Binomial Distribution Simulation
Generate 5000 Binomial distributed \(n = 70, p = 0.7\) random numbers by doing: Use Bernoulli random variables. Plot the histogram and use your data to calculate the probability that the Binomial random variable is less than 50. Compare with the theoretical answer.

##### Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
```

##### Parameters
```python
n = 70           # Num of trials
p = 0.7          # prob success
num_samples = 5000
```

##### Libraries
```python
bernoulli_trials = np.random.binomial(1, p, (num_samples, n))
binomial_samples = np.sum(bernoulli_trials, axis=1)
```

##### Calculations
```python
# emp
prob_empirical = np.mean(binomial_samples < 50)
print(f"Empirical Probability (X < 50): {prob_empirical:.4f}")

# thoery
prob_theoretical = binom.cdf(49, n, p)  # with cdf
print(f"Theoretical Probability (X < 50): {prob_theoretical:.4f}")
```

##### Plot
```python
plt.figure(figsize=(10, 6))
plt.hist(binomial_samples, bins=range(n+2), alpha=0.75, color='purple', edgecolor='black')
plt.title('Histogram of Binomial Distribution ($n=70, p=0.7$)')
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
```
##### Graph Results
![3 reulst](/img/three_result.png)

---
### 4. Normal Distribution Analysis
- **a)** Simulate 1000 random normal variables with mean 1.5 and standard deviation 2. Create a histogram. Use a build in software package or investigate how to build your own (not that difficult).
- **b)** Find out how many of your 1000 variables are bigger than 0, and estimate the probability that a single normal variable with mean 1.5 and standard deviation 2 is above 0. Also, compute and write the theoretical value for this probability.

##### Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
```

##### Parameters
```python
mean = 1.5
std_dev = 2
num_samples = 1000
```

##### Calculations + Part B
```python
normal_variables = np.random.normal(mean, std_dev, num_samples)

# For part B
greater_than_zero = np.sum(normal_variables > 0)
probability_empirical = greater_than_zero / num_samples
print(f"Number of variables greater than 0: {greater_than_zero}")
print(f"Empirical Probability that a variable is > 0: {probability_empirical:.4f}")

probability_theoretical = 1 - norm.cdf(0, loc=mean, scale=std_dev)
print(f"Theoretical Probability that a variable is > 0: {probability_theoretical:.4f}")
```

##### Plot
```python
plt.figure(figsize=(10, 6))
plt.hist(normal_variables, bins=30, color='skyblue', alpha=0.8, edgecolor='black')
plt.title('Histogram of 1000 Random Normal Variables')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

```
##### Graph Results
![4 reulst](/img/four_result.png)


---
### 5. Simulation of Sample Means
Simulate 100 sample means, each made by taking the average of 20 normal variables with mean 1.5 and standard deviation 2. Make a histogram of these sample means in the range −4 to 10 with class intervals of length 0.5. As in the previous question, estimate the probability that a sample mean is bigger than 0. Also, compute and write the theoretical value for this probability.

##### Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
```

##### Parameters
```python
mean = 1.5
std_dev = 2
num_samples = 20
num_simulations = 100
```

##### Calculations
```python
sample_means = np.array([np.mean(np.random.normal(mean, std_dev, num_samples)) for _ in range(num_simulations)])
# Calc empirical prob  sample mean > 0
empirical_prob = np.mean(sample_means > 0)
print(f"Empirical Probability (Sample Mean > 0): {empirical_prob:.4f}")

# Calculate the theoretical prob sample mean > 0
theoretical_mean = mean
theoretical_std_dev = std_dev / np.sqrt(num_samples)
theoretical_prob = norm.sf(0, loc=theoretical_mean, scale=theoretical_std_dev)
print(f"Theoretical Probability (Sample Mean > 0): {theoretical_prob:.4f}")
```

##### Plot
```python
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=np.arange(-4, 10.5, 0.5), color='skyblue', edgecolor='black')
plt.title('Histogram of Sample Means')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
```

##### Graph Results
![5 reulst](/img/five_results.png)

---
### 6. Expected Value of Sum of Uniform Random Variables
- **a)** Let \(U_1, U_2, \dots, U_n\) be uniform random variables on \([0, 1]\). Define \(N = \min\{n : \sum_{i=1}^n U_i > 1\}\). Organize in a table the estimates of \(E[N]\) obtained by generating 10, 10^2, \dots, 10^6 values of \(N\).
- **b)** Are your estimates in part a) converging to a particular value? If so, in what sense?
- **c)** Calculate theoretically the \(E[N]\) and compare your result with the one obtained in part a).

##### Libraries
```python
import numpy as np
```

##### Calculations
```python
def simulate_E_N(max_trials):
    results = []
    for trials in [10, 100, 1000, 10000, 100000, 1000000]:  
        N_values = []
        for _ in range(trials):
            sum_U = 0
            n = 0
            while sum_U <= 1:
                sum_U += np.random.uniform(0, 1)
                n += 1
            N_values.append(n)
        results.append((trials, np.mean(N_values)))
    return results

# Sim
simulation_results = simulate_E_N(1000000)
```

##### Display
```python
print("Trials\tEstimated E[N]")
for trials, estimate in simulation_results:
    print(f"{trials}\t{estimate:.4f}")
```

##### Results
| Trials  | Estimated E[N] |
|---------|----------------|
| 10      | 2.8000         |
| 100     | 2.7800         |
| 1000    | 2.6830         |
| 10000   | 2.7244         |
| 100000  | 2.7214         |
| 1000000 | 2.7186         |

---
### 7. Log-Normal Variable Simulation and Analysis
- **a)** Let's consider the Normal random variables \(X_1\) with mean \(\mu_1 = 10\) and variance \(\sigma_1^2 = 0.202\)
    - Generate 10000 log-normal random variables \(Y_1 = e^{X_1}\)
- **b)** Estimate \(E[Y_1]\) and compare with the theoretical result.

##### Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
```

##### Parameters
```python
mu = 10
sigma = np.sqrt(0.202)  
num_samples = 10000

X = np.random.normal(mu, sigma, num_samples)
Y = np.exp(X)
```

##### Calculations
```python
# Calc empirical exp value of Y
empirical_E_Y = np.mean(Y)
print(f"Empirical Expected Value of Y_1: {empirical_E_Y:.4f}")

# Theoretical exp value E[Y] n
theoretical_E_Y = np.exp(mu + (sigma**2 / 2))
print(f"Theoretical Expected Value of Y_1: {theoretical_E_Y:.4f}")
```

##### Plot
```python
plt.figure(figsize=(10, 6))
plt.hist(Y, bins=50, color='green', alpha=0.8, edgecolor='black')
plt.title('Histogram of Log-Normal Random Variables')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
```

##### Graph Results
![7 reulst](/img/seven_results.png)

---
### 8. Integral Estimation
- **a)** Consider the integral \(I = \int_0^1 \int_0^1 e^{x+y} dx dy\).
    - Estimate the integral \(I\). Compare with the theoretical result. You can see this integral as an expectation.

##### Libraries
```python
import numpy as np
```

##### Calculations
```python
def func(num_samples=100000):
    # create uniform distr
    x_samples = np.random.uniform(low=0.0, high=1.0, size=num_samples)
    y_samples = np.random.uniform(low=0.0, high=1.0, size=num_samples)
    
    # Calculate func values
    function_values = np.exp(x_samples + y_samples)
    
    # Estimate the integral as the average of the function values
    integral_estimate = np.mean(function_values)
    return integral_estimate

num_samples = 1000000
estimated_integral = func(num_samples)

# Theoretical value 
theoretical_integral = (np.exp(1) - 1) ** 2
```

##### Results
```python
print(f"Estimated Integral (n={num_samples}): {estimated_integral:.6f}")
print(f"Theoretical Integral: {theoretical_integral:.6f}")
```

##### Display
- Estimated Integral (n=1000000): 2.951288
- Theoretical Integral: 2.952492


### 9. Verification of Theoretical Statistical Properties
- **a)** The normal approximation of the binomial distribution.
- **b)** The sum of two normal random variables is a normal random variable.
- **c)** The density of the sum of two uniform \([0,1]\) random variables has a triangular distribution.
- **d)** Let \(X_i\) be the sum of the results of \(i\) rolls of the same die. (take 𝑖 = 2,5,10,20,40,80) and show that the
probability distribution of the 𝑋𝑖 approach the probability density of a normal random variable.

##### Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm
```

##### Parameters
```python
num_samples = 10000
```

##### Part (a): Normal Approximation Binomial Distribution
```python
def normal_approximation_to_binomial():
    n = 100  # num trials
    p = 0.5  # probab success
    binomial_data = binom.rvs(n, p, size=num_samples)
    normal_approx = norm.rvs(loc=n*p, scale=np.sqrt(n*p*(1-p)), size=num_samples)
    
    plt.figure(figsize=(12, 6))
    plt.hist(binomial_data, bins=30, alpha=0.5, label='Binomial', color='blue')
    plt.hist(normal_approx, bins=30, alpha=0.5, label='Normal Approx', color='red')
    plt.title('Normal Approximation 4 Binomial Distribution')
    plt.legend()
    plt.show()
```

##### Part (b): Sum of Two Normal Random Vars
```python
def sum_of_two_normals():
    normal1 = norm.rvs(loc=0, scale=2, size=num_samples)
    normal2 = norm.rvs(loc=0, scale=3, size=num_samples)
    sum_normal = normal1 + normal2

    plt.figure(figsize=(12, 6))
    plt.hist(sum_normal, bins=30, alpha=0.5, color='green')
    plt.title('Sum of Two Normal Random Variables')
    plt.show()
```

##### Part (c): Density of the Sum of Two Uniform [0,1] Random Vars
```python
def density_of_sum_of_uniforms():
    uniform1 = np.random.uniform(low=0.0, high=1.0, size=num_samples)
    uniform2 = np.random.uniform(low=0.0, high=1.0, size=num_samples)
    sum_uniform = uniform1 + uniform2

    plt.figure(figsize=(12, 6))
    plt.hist(sum_uniform, bins=30, alpha=0.5, color='purple')
    plt.title('Density of Sum of Two Uniform [0,1] Random Variables')
    plt.show()
```

##### Part (d): Distr of the Sum of Dice Rolls Approaching Normal Distr
```python
def dice_rolls_convergence():
    dice_counts = [2, 5, 10, 20, 40, 80]
    for count in dice_counts:
        dice_sum = np.sum(np.random.randint(1, 7, size=(num_samples, count)), axis=1)
        plt.figure(figsize=(12, 6))
        plt.hist(dice_sum, bins=range(count, 6*count + 2, 1), density=True, alpha=0.75, color='orange')
        plt.title(f'Distribution of Sum of {count} Dice Rolls')
        plt.xlabel('Sum')
        plt.ylabel('Probability')
        plt.grid(True)
        plt.show()
```

##### Results
![9results](/img/nine-one.png)
![9results](/img/nine-two.png)
![9results](/img/nine-three.png)
![9results](/img/nine-four.png)
![9results](/img/nine-five.png)
![9results](/img/nine-six.png)
![9results](/img/nine-seven.png)
![9results](/img/nine-eight.png)
![9results](/img/nine-nine.png)