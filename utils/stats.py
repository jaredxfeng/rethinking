# assign r::stats function names to scipy.stats functions

from scipy.stats import binom, uniform, norm, lognorm
import autograd.numpy as np
from autograd.numpy import pi, sqrt, exp
import numpyro.distributions as dist
from jax import random

seed = random.PRNGKey(0)


# pdfs and pmfs
def dbinom(k, n, p, log=False): 
    return binom.pmf(k, n, p) if not log else binom.logpmf(k, n, p)

def dnorm(x, loc=0, scale=1, log=False): 
    return norm.pdf(x, loc, scale) if not log else norm.logpdf(x, loc, scale)

def dunif(x, lower=0, upper=1, log=False): 
    return uniform.pdf(x, lower, upper - lower) if not log else uniform.logpdf(x, lower, upper - lower)


# autograd compatible pdfs and pmfs
def dlnorm_(x, mu=0, sigma=1, log=True):
    res = (1/x/sigma/sqrt(2*pi)) 
    res *= exp(-(np.log(x) - mu)**2/2/sigma**2)
    return res if not log else np.log(res)

def dnorm_(x, mu=0, sigma=1, log=True):
    res = (1/sqrt(2*pi)/sigma) 
    res *= exp(-(x - mu)**2/2/sigma**2)
    return res if not log else np.log(res)
    
def dunif_(x, lower=0, upper=1, log=True):
    res = 1/(upper - lower)
    return res if not log else np.log(res)


# cdfs
# def pnorm


# quantiles
# def qnorm