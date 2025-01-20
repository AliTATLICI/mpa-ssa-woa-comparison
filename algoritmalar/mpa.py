import numpy as np
from numpy.random import rand, randn
import math

class MarinePredatorsAlgorithm:
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
        prey = self.lb + (self.ub - self.lb) * rand(self.n_particles, self.dim)
        fitness = np.zeros(self.n_particles)
        
        # Evaluate initial population
        for i in range(self.n_particles):
            fitness[i] = self.objective_func(prey[i])
            if fitness[i] < self.best_fitness:
                self.best_fitness = fitness[i]
                self.best_solution = prey[i].copy()
        
        # Main loop
        for t in range(self.max_iter):
            # Adaptive step size
            step_size = (1 - t/self.max_iter) * 0.5
            
            # Phase 1: Brownian motion
            for i in range(self.n_particles):
                if rand() < 0.5:
                    R = randn()
                    new_position = self.best_solution + R * step_size * randn(self.dim)
                else:
                    R = rand()
                    random_prey = prey[np.random.randint(0, self.n_particles)]
                    new_position = random_prey + R * step_size * randn(self.dim)
                
                # Boundary check
                new_position = np.clip(new_position, self.lb, self.ub)
                
                # Update if better
                new_fitness = self.objective_func(new_position)
                if new_fitness < fitness[i]:
                    prey[i] = new_position
                    fitness[i] = new_fitness
                    if new_fitness < self.best_fitness:
                        self.best_fitness = new_fitness
                        self.best_solution = new_position.copy()
            
            # Phase 2: Levy flight
            beta = 1.5  # Levy component
            sigma = (math.gamma(1 + beta) * math.sin(math.pi * beta / 2) / 
                    (math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
            
            for i in range(self.n_particles):
                u = randn(self.dim) * sigma
                v = randn(self.dim)
                step = u / abs(v) ** (1 / beta)
                
                new_position = prey[i] + step * step_size
                new_position = np.clip(new_position, self.lb, self.ub)
                
                new_fitness = self.objective_func(new_position)
                if new_fitness < fitness[i]:
                    prey[i] = new_position
                    fitness[i] = new_fitness
                    if new_fitness < self.best_fitness:
                        self.best_fitness = new_fitness
                        self.best_solution = new_position.copy()
            
            # Record convergence
            self.convergence_curve[t] = self.best_fitness
            
        return self.best_solution, self.best_fitness, self.convergence_curve