import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters
num_samples = 10000

# Part (a): Normal Approximation Binomial Distribution
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

# Part (b): Sum of Two Normal Random Variables
def sum_of_two_normals():
    normal1 = norm.rvs(loc=0, scale=2, size=num_samples)
    normal2 = norm.rvs(loc=0, scale=3, size=num_samples)
    sum_normal = normal1 + normal2

    plt.figure(figsize=(12, 6))
    plt.hist(sum_normal, bins=30, alpha=0.5, color='green')
    plt.title('Sum of Two Normal Random Variables')
    plt.show()

# Part (c): Density of the Sum of Two Uniform [0,1] Random Variables
def density_of_sum_of_uniforms():
    uniform1 = np.random.uniform(low=0.0, high=1.0, size=num_samples)
    uniform2 = np.random.uniform(low=0.0, high=1.0, size=num_samples)
    sum_uniform = uniform1 + uniform2

    plt.figure(figsize=(12, 6))
    plt.hist(sum_uniform, bins=30, alpha=0.5, color='purple')
    plt.title('Density of Sum of Two Uniform [0,1] Random Variables')
    plt.show()

# Part (d): Distribution of the Sum of Dice Rolls Approaching Normal Distribution
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

# Execute the functions
normal_approximation_to_binomial()
sum_of_two_normals()
density_of_sum_of_uniforms()
dice_rolls_convergence()
