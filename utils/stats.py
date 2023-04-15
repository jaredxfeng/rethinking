# assign r::stats function names to scipy.stats functions

from scipy.stats import binom, uniform, norm, lognorm
import autograd.numpy as np
from autograd.numpy import pi, sqrt, exp

# rvs
def rbinom(size=1, n=10, p=0.5): 
    return binom.rvs(n, p, size)

def rlnorm(size=1, mu=0, sigma=1):
    return lognorm.rvs(scale=exp(mu), s=sigma, size=size)

def rnorm(size=1, mu=0, sigma=1): 
    return norm.rvs(mu, sigma, size)

def runif(size=1, l=0, u=1): 
    return uniform.rvs(loc=l, scale=u - l, size=size)


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