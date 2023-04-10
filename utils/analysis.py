import pandas as pd
import xarray as xr
import arviz as az
from typing import List, Optional


class Prefs:
    hdi_lower = 0.055
    hdi_upper = 0.945
    hdi_width = hdi_upper - hdi_lower
    hdi_lower_perc = str(hdi_lower*100) + "%"
    hdi_upper_perc = str(hdi_upper*100) + "%"
    
    round_to = 2


def precis(data, pars: Optional[List[str]]=None, round_to=Prefs.round_to):
    if isinstance(data, pd.DataFrame):
        if isinstance(pars, list) or isinstance(pars, str):
            data = data[pars]
        des = data.describe(percentiles=[Prefs.hdi_lower, Prefs.hdi_upper])
        des = des[des.index.isin(["mean", "std", Prefs.hdi_lower_perc, Prefs.hdi_upper_perc])].T.round(round_to)
        return des.rename({"std": "sd"}, axis=1)
    else:
        if isinstance(pars, str):
            pars = [pars]
        des = az.summary(data, kind="stats", var_names=pars, round_to=round_to)
        return des.rename({f"hdi_{Prefs.hdi_lower_perc}": Prefs.hdi_lower_perc, 
                           f"hdi_{Prefs.hdi_upper_perc}": Prefs.hdi_upper_perc}, 
                          axis=1)