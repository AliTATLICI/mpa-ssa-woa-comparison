import numpy as np
from numpy.random import rand

class SalpSwarmAlgorithm:
    def __init__(self, objective_func, lb, ub, dim, n_particles, max_iter):
        self.objective_func = objective_func
        self.lb = lb
        self.ub = ub
        self.dim = dim
        self.n_particles = n_particles
        self.max_iter = max_iter
        
        # Initialize best solution
        self.best_solution = None
        self.best_fitness = float('inf')
        self.convergence_curve = np.zeros(self.max_iter)
    
    def optimize(self):
        # Initialize population
        salp_positions = self.lb + (self.ub - self.lb) * rand(self.n_particles, self.dim)
        fitness = np.zeros(self.n_particles)
        
        # Evaluate initial population
        for i in range(self.n_particles):
            fitness[i] = self.objective_func(salp_positions[i])
            if fitness[i] < self.best_fitness:
                self.best_fitness = fitness[i]
                self.best_solution = salp_positions[i].copy()
        
        # Main loop
        for t in range(self.max_iter):
            # Update c1 parameter
            c1 = 2 * np.exp(-((4 * t / self.max_iter) ** 2))
            
            for i in range(self.n_particles):
                # Update leader position (first salp)
                if i == 0:
                    for j in range(self.dim):
                        c2 = rand()
                        c3 = rand()
                        if c3 >= 0.5:
                            salp_positions[i, j] = self.best_solution[j] + c1 * ((self.ub - self.lb) * c2 + self.lb)
                        else:
                            salp_positions[i, j] = self.best_solution[j] - c1 * ((self.ub - self.lb) * c2 + self.lb)
                
                # Update followers position
                else:
                    salp_positions[i] = (salp_positions[i] + salp_positions[i-1]) / 2
                
                # Boundary check
                salp_positions[i] = np.clip(salp_positions[i], self.lb, self.ub)
                
                # Update fitness
                new_fitness = self.objective_func(salp_positions[i])
                if new_fitness < fitness[i]:
                    fitness[i] = new_fitness
                    if new_fitness < self.best_fitness:
                        self.best_fitness = new_fitness
                        self.best_solution = salp_positions[i].copy()
            
            # Record convergence
            self.convergence_curve[t] = self.best_fitness
        
        return self.best_solution, self.best_fitness, self.convergence_curve