from functools import partial
import autograd.numpy as anp
from autograd import grad, jacobian
from scipy.optimize import minimize
from scipy.stats import multivariate_normal as mvnorm
from typing import Union
import pandas as pd
from utils.analysis import precis
from utils.stats import *


class pyquap:
    def __init__(self):
        self.model = None
    
    def define_objective(self, objective_func):
        self.objective_ = objective_func
    
    def update_objective(self, data):
        self.objective = partial(self.objective_, data=data)

    def initialize(self, pars0: dict):
        self.var_names = pars0.keys()
        vs = list(pars0.values())
        self.x0 = [eval(v)[0] if isinstance(v, str) else v for v in vs]
        self.x0 = anp.array(self.x0).flatten()
    
    def fit(self, data, method="BFGS", tol=None):
        self.update_objective(data)
        gradient, hessian = grad(self.objective), None
        if method in ["Newton-CG", "dogleg", "trust-ncg", "trust-krylov", "trust-exact", "trust-constr"]:
            hessian = jacobian(gradient)
        opt = minimize(fun=self.objective,
                       x0=self.x0,
                       jac=gradient,
                       method=method,
                       hess=hessian,
                       tol=tol
                      )
        print(opt.message)
        self.opt = opt
        try:
            hess_inv = opt.hess_inv
        except:
            hess_inv = anp.linalg.inv(hessian(opt.x))
        self.model = mvnorm(mean=opt.x, cov=hess_inv)
        
    def sample(self, n_points=4000):
        samples = self.model.rvs(n_points)
        return pd.DataFrame(samples, columns=self.var_names)
        
    def precis(self):
        return precis(self.sample())