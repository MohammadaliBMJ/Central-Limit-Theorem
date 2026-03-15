# Central-Limit-Theorem
## Overview
This repository is an implementation of the Central Limit Theorem. The CLT states that when we take many samples of a distribution and take the mean of these samples, the distribution of the means will follow a normal distribution. Sampling is done with replacement.

## Included Distributions
- Uniform Distribution
    - Parameters :
        - a : Minimum value of the distribution
        - b : Maximum value of the distribution
    - mean : $\frac{a + b}{2}$
    - standard deviation : $\frac{b - a}{\sqrt{12}}$
- Exponential Distribution
    - Parameters :
        - $\lambda$ : Rate parameter
    - mean : $\frac{1}{\lambda}$
    - standard deviation : $\frac{1}{\lambda}$
- Bernoulli Distribution
    - Parameters :
        - $p$ : Probability of success
    - mean : $p$
    - standard deviation : $\sqrt{p \times (1 - p)}$
- Poisson Distribution
    - Parameters :
        - $\lambda$ : Average rate of events
    - mean : $\lambda$
    - standard deviation : $\sqrt{\lambda}$

## Standardization
Shift the sample mean so the mean is $0$ and the std is $1$.

$$
Z = \frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}}
$$

- $\bar{X}$ : sample mean
- $\mu$ : true mean
- $\sigma$ : true std
- $n$ : sample size

## Visualization
This project demonstrates the Central Limit Theorem for the above distributions using a $4\times 2$ grid with eight histograms with sample sizes $10, 20, 30, 50, 100, 200, 500, 1000$. Each figure opened in a separate window corresponds to one distribution.

## How to Run
Simply run the command `python clt.py`

