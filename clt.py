import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


def sample_generator(distribution: str, size: int, parameters: dict, num_samples: int = 10000) -> Tuple:
    """
    Generating samples from several distributions.

    Args:
        distribution(str): Name of the distribution('uniform', 'exponential', 'bernoulli', 'poisson')
        size(int): Number of the samples.
        parameters(dict): Parameters of the distribution
        num_samples(int): number of samples to produce

    Returns:
        (samples, samples_mean, standard_mean)(tuple): A tuple of samples, mean of the samples,
        and the standardized mean of the samples.
    """
    distribution = distribution.lower()

    if distribution == "uniform":
        a = parameters.get("a")
        b = parameters.get("b")
        samples = np.random.uniform(low = a, high = b, size = (num_samples, size))
        samples_mean = samples.mean(axis = 1)
        true_mean = (a + b) / 2
        true_std = (b - a) / np.sqrt(12)
    
    elif distribution == "exponential":
        lamb = parameters.get("lambda_exp")
        samples = np.random.exponential(scale = 1 / lamb, size = (num_samples, size))
        samples_mean = samples.mean(axis = 1)
        true_mean = 1 / lamb
        true_std = 1 / lamb
    
    elif distribution == "bernoulli":
        p = parameters.get("p")
        samples = np.random.binomial(n = 1, p = p, size = (num_samples, size))
        samples_mean = samples.mean(axis = 1)
        true_mean = p
        true_std = np.sqrt(p * (1 - p))

    elif distribution == "poisson":
        lamb = parameters.get("lambda_poi")
        samples = np.random.poisson(lam = lamb, size = (num_samples, size))
        samples_mean = samples.mean(axis = 1)
        true_mean = lamb
        true_std = np.sqrt(lamb)
        
    # Standardized mean   
    standard_mean = (samples_mean - true_mean) / (true_std / np.sqrt(size))  
        
    return samples, samples_mean, standard_mean


# Name of the distributions
distributions = ["uniform", "exponential", "bernoulli", "poisson"]

# Parameters of the distributions
parameters = {
    "a": 0,
    "b": 1,
    "lambda_exp": 1,
    "p": 0.5,
    "lambda_poi": 1
}

# Sample sizes
sample_size = [10, 20, 30, 50, 100, 200, 500, 1000]


if __name__ == "__main__":
    for dist in distributions:
        fig, axs = plt.subplots(nrows = 4, ncols = 2)
        fig.suptitle(dist)
        axs = axs.flatten()

        for i, size in enumerate(sample_size):
            _, _, standard_mean = sample_generator(
                distribution = dist, size = size, parameters = parameters
                )
            axs[i].hist(standard_mean, bins = 100)
            axs[i].set_title(f"sample size={size}")
        
        plt.tight_layout()
        plt.show()