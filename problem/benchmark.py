import numpy as np

def sphere(x):
    """Sphere function
    Global minimum: f(0,...,0) = 0
    Bounds: [-5.12, 5.12]
    """
    return np.sum(x**2)

def rosenbrock(x):
    """Rosenbrock function
    Global minimum: f(1,...,1) = 0
    Bounds: [-2.048, 2.048]
    """
    return np.sum(100.0 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

def rastrigin(x):
    """Rastrigin function
    Global minimum: f(0,...,0) = 0
    Bounds: [-5.12, 5.12]
    """
    return 10 * len(x) + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

# Dictionary of available test functions
test_functions = {
    'sphere': {
        'func': sphere,
        'lb': -5.12,
        'ub': 5.12,
        'optimum': 0.0
    },
    'rosenbrock': {
        'func': rosenbrock,
        'lb': -2.048,
        'ub': 2.048,
        'optimum': 0.0
    },
    'rastrigin': {
        'func': rastrigin,
        'lb': -5.12,
        'ub': 5.12,
        'optimum': 0.0
    }
}