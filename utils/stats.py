# this module provides functional translations from R to scipy.stats 

import numpy as np
from scipy.stats import binom, uniform, norm

# rvs
def rbinom(size, n, p): return binom.rvs(n, p, size)
def rnorm(size, loc=0, scale=1): return norm.rvs(loc, scale, size)
def runif(size, lower=0, upper=1): return uniform.rvs(lower, upper, size)

# pdfs and pmfs
def dbinom(k, n, p): return binom.pmf(k, n, p)
def dnorm(x, loc=0, scale=1): return norm.pdf(x, loc, scale)
def dunif(x, lower=0, upper=1): return uniform.pdf(x, lower, upper)