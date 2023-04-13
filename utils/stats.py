# assign r::stats function names to scipy.stats functions

from scipy.stats import binom, uniform, norm
import autograd.numpy as np
from autograd.numpy import pi, sqrt, exp

# rvs
def rbinom(size, n, p): 
    return binom.rvs(n, p, size)
def rnorm(size, loc=0, scale=1): 
    return norm.rvs(loc, scale, size)
def runif(size, lower=0, upper=1): 
    return uniform.rvs(loc=lower, scale=upper - lower, size=size)


# pdfs and pmfs
def dbinom(k, n, p, log=False): 
    return binom.pmf(k, n, p) if not log else binom.logpmf(k, n, p)
def dnorm(x, loc=0, scale=1, log=False): 
    return norm.pdf(x, loc, scale) if not log else norm.logpdf(x, loc, scale)
def dunif(x, lower=0, upper=1, log=False): 
    return uniform.pdf(x, lower, upper - lower) if not log else uniform.logpdf(x, lower, upper - lower)

# autograd compatible pdfs and pmfs
def dnorm_(x, loc=0, scale=1, log=False):
    res = (1/sqrt(2*pi)/scale) * exp(-(x - loc)**2/2/scale**2)
    return res if not log else np.log(res)
    
def dunif_(x, lower=0, upper=1, log=False):
    res = 1/(upper - lower)
    return res if not log else np.log(res)

# cdfs
# def pnorm


# quantiles
# def qnorm