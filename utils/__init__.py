from . import plots
from . import warnings


def init():
    plots.init()
    warnings.init()
    
    
class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__