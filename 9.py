import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Params
num_samples = 10000

# Part a): Normal Approximation Binomial Distribution
def normal_approximation_to_binomial():
    n = 1000  # number of trials
    p = 0.5  # probability of success
    mu = n * p
    sigma = np.sqrt(n * p * (1 - p))
    binomial_data = binom.rvs(n, p, size=10000)
    #normal_data = norm.rvs(loc=mu, scale=sigma, size=10000)
    bins = np.linspace(min(binomial_data), max(binomial_data), 30)
    
    # Set up the figure and axes for plotting
    plt.figure(figsize=(12, 6))

    plt.hist(binomial_data, bins=bins, alpha=0.5, color='blue', label='Binomial Distribution', density=True)

    # Calculate the normal density function 
    x = np.linspace(min(binomial_data), max(binomial_data), 1000)
    pdf = norm.pdf(x, mu, sigma)

    plt.plot(x, pdf, 'r-', lw=2, label='Normal Approximation')
    plt.title('Normal Approximation to Binomial Distribution')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()

# Part (b): Sum of Two Normal Random Vars
def sum_of_two_normals():
    normal1 = norm.rvs(loc=0, scale=2, size=num_samples)
    normal2 = norm.rvs(loc=0, scale=3, size=num_samples)
    sum_normal = normal1 + normal2

    plt.figure(figsize=(12, 6))
    plt.hist(sum_normal, bins=30, alpha=0.5, color='green')
    plt.title('Sum of Two Normal Random Variables')
    plt.show()

# Part (c): Density of the Sum of Two Uniform [0,1] Random Vars
def density_of_sum_of_uniforms():
    uniform1 = np.random.uniform(low=0.0, high=1.0, size=num_samples)
    uniform2 = np.random.uniform(low=0.0, high=1.0, size=num_samples)
    sum_uniform = uniform1 + uniform2

    plt.figure(figsize=(12, 6))
    plt.hist(sum_uniform, bins=30, alpha=0.5, color='purple')
    plt.title('Density of Sum of Two Uniform [0,1] Random Variables')
    plt.show()

# Part (d): Distr of the Sum of Dice Rolls Approaching Normal Distr
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

normal_approximation_to_binomial()
sum_of_two_normals()
density_of_sum_of_uniforms()
dice_rolls_convergence()
