import numpy as np
from numpy.random import rand, randn

class WhaleOptimizationAlgorithm:
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
        whales = self.lb + (self.ub - self.lb) * rand(self.n_particles, self.dim)
        fitness = np.zeros(self.n_particles)
        
        # Evaluate initial population
        for i in range(self.n_particles):
            fitness[i] = self.objective_func(whales[i])
            if fitness[i] < self.best_fitness:
                self.best_fitness = fitness[i]
                self.best_solution = whales[i].copy()
        
        # Main loop
        for t in range(self.max_iter):
            a = 2 - t * (2 / self.max_iter)  # a decreases linearly from 2 to 0
            
            for i in range(self.n_particles):
                # Update parameters
                r = rand()
                A = 2 * a * r - a
                C = 2 * r
                l = rand() * 2 - 1  # parameter for spiral
                p = rand()  # probability for hunting choice
                
                if p < 0.5:
                    # Shrinking encircling mechanism
                    if abs(A) < 1:
                        D = abs(C * self.best_solution - whales[i])
                        new_position = self.best_solution - A * D
                    # Search for prey
                    else:
                        random_whale = whales[np.random.randint(0, self.n_particles)]
                        D = abs(C * random_whale - whales[i])
                        new_position = random_whale - A * D
                else:
                    # Spiral bubble-net attacking
                    D = abs(self.best_solution - whales[i])
                    spiral = D * np.exp(2 * l) * np.cos(2 * np.pi * l)
                    new_position = self.best_solution + spiral
                
                # Boundary check
                new_position = np.clip(new_position, self.lb, self.ub)
                
                # Update position if better
                new_fitness = self.objective_func(new_position)
                if new_fitness < fitness[i]:
                    whales[i] = new_position
                    fitness[i] = new_fitness
                    if new_fitness < self.best_fitness:
                        self.best_fitness = new_fitness
                        self.best_solution = new_position.copy()
            
            # Record convergence
            self.convergence_curve[t] = self.best_fitness
        
        return self.best_solution, self.best_fitness, self.convergence_curve