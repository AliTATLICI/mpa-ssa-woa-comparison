import numpy as np
from scipy import stats
import pandas as pd
from datetime import datetime
import json

from algoritmalar.mpa import MarinePredatorsAlgorithm
from algoritmalar.ssa import SalpSwarmAlgorithm
from algoritmalar.woa import WhaleOptimizationAlgorithm
from problem.benchmark import test_functions

# Experimental parameters
n_runs = 30
dimension = 30
population_size = 30
max_iterations = 500
selected_function = 'sphere'  # you can change to 'rosenbrock' or 'rastrigin'

# Initialize results storage
results = {
    'MPA': [],
    'SSA': [],
    'WOA': []
}

# Run experiments
func = test_functions[selected_function]['func']
lb = test_functions[selected_function]['lb']
ub = test_functions[selected_function]['ub']

for run in range(n_runs):
    print(f"Run {run + 1}/{n_runs}")
    
    # Marine Predators Algorithm
    mpa = MarinePredatorsAlgorithm(func, lb, ub, dimension, population_size, max_iterations)
    _, best_fitness, _ = mpa.optimize()
    results['MPA'].append(best_fitness)
    
    # Salp Swarm Algorithm
    ssa = SalpSwarmAlgorithm(func, lb, ub, dimension, population_size, max_iterations)
    _, best_fitness, _ = ssa.optimize()
    results['SSA'].append(best_fitness)
    
    # Whale Optimization Algorithm
    woa = WhaleOptimizationAlgorithm(func, lb, ub, dimension, population_size, max_iterations)
    _, best_fitness, _ = woa.optimize()
    results['WOA'].append(best_fitness)

# Calculate statistics
stats_df = pd.DataFrame()
for alg in results.keys():
    stats_df[alg] = [
        np.min(results[alg]),  # Best
        np.max(results[alg]),  # Worst
        np.median(results[alg]),  # Median
        np.mean(results[alg]),  # Average
        np.std(results[alg])  # Std
    ]
stats_df.index = ['Best', 'Worst', 'Median', 'Average', 'Std']

# Wilcoxon signed-rank test
wilcoxon_results = pd.DataFrame(columns=['Algorithm 1', 'Algorithm 2', 'p-value', 'Significant'])
algorithms = list(results.keys())
for i in range(len(algorithms)):
    for j in range(i + 1, len(algorithms)):
        stat, p_value = stats.wilcoxon(results[algorithms[i]], results[algorithms[j]])
        wilcoxon_results = pd.concat([wilcoxon_results, pd.DataFrame([{
            'Algorithm 1': algorithms[i],
            'Algorithm 2': algorithms[j],
            'p-value': p_value,
            'Significant': p_value < 0.05
        }])], ignore_index=True)

# Friedman test
friedman_stat, friedman_p_value = stats.friedmanchisquare(*[results[alg] for alg in algorithms])

# Save results
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
results_folder = f"C:/Users/Yusra/Desktop/development/claude/sezgisel/sonuclar/{selected_function}_{timestamp}"

# Save raw results
np.save(f"{results_folder}_raw.npy", results)

# Save statistical analysis
with open(f"{results_folder}_stats.txt", "w") as f:
    f.write(f"Function: {selected_function}\n")
    f.write(f"Dimension: {dimension}\n")
    f.write(f"Population Size: {population_size}\n")
    f.write(f"Max Iterations: {max_iterations}\n")
    f.write(f"Number of Runs: {n_runs}\n\n")
    
    f.write("Statistical Results:\n")
    f.write(stats_df.to_string())
    f.write("\n\nWilcoxon Signed-Rank Test Results:\n")
    f.write(wilcoxon_results.to_string())
    f.write("\n\nFriedman Test Results:\n")
    f.write(f"Statistic: {friedman_stat}\n")
    f.write(f"p-value: {friedman_p_value}\n")

print("Experiments completed and results saved.")