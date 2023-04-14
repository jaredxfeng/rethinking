from functools import partial
import autograd.numpy as anp
from autograd import grad
from scipy.optimize import minimize
from scipy.stats import multivariate_normal as mvnorm


class pyquap:
    def __init__(self):
        self.model = None
    
    def define_objective(self, objective_func):
        self.objective_ = objective_func
    
    def update_objective(self, data):
        self.objective = partial(self.objective_, data=data)

    def set_init_params(self, init_params: anp.ndarray):
        self.init_params = init_params
    
    def fit(self, data, method="BFGS"):
        self.update_objective(data)
        opt = minimize(fun=self.objective,
                       x0=self.init_params,
                       jac=grad(self.objective),
                       method=method
                      )
        print(opt.message)
        if opt.success:
            self.model = mvnorm(mean=opt.x, cov=opt.hess_inv)
        self.opt = opt
        
    def sample(self, n_points=4000):
        assert self.model is not None, \
            "You think you've fitted a model with success?"
        return self.model.rvs(n_points)