import numpy as np

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

print(f"Estimated Integral (n={num_samples}): {estimated_integral:.6f}")
print(f"Theoretical Integral: {theoretical_integral:.6f}")
