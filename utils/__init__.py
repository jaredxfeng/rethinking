from . import plots
from . import warnings
from contextlib import contextmanager
import inspect


def init():
    plots.init()
    warnings.init()

    
def thisglobals():
    return globals()


def prevglobals():
    """Behaves like the builtin globals(), but written in Python!"""
    return inspect.currentframe().f_back.f_globals


def prevglobals2():
    return inspect.currentframe().f_back.f_back.f_globals


@contextmanager
def attach(dict_):
    script_globals = inspect.currentframe().f_back.f_back.f_globals
    update_script_globals = inspect.currentframe().f_back.f_back.f_globals.update
    for k, v in dict_.items():
        update_script_globals({f"{k}": v})
    yield
    for k in dict_.keys():
        exec(f"del {k}", script_globals)
        
    
@contextmanager
def attach_test():
    inspect.currentframe().f_back.f_back.f_globals.update({"hi": 76})
    yield