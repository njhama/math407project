import numpy as np

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

# Display
print("Trials\tEstimated E[N]")
for trials, estimate in simulation_results:
    print(f"{trials}\t{estimate:.4f}")
