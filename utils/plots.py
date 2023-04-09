import matplotlib.pyplot as plt
import seaborn as sns
import arviz as az
from daft import PGM


def init():
    az.style.use("arviz-doc")
    az.rcParams["stats.hdi_prob"] = 0.89
    plt.rcParams["figure.dpi"] = 125
    plt.rcParams["axes.titleweight"] = "light"
    plt.rcParams["font.size"] = 10
    plt.rcParams["figure.titlesize"] = 10
    plt.rcParams["figure.labelsize"] = 10
    plt.rcParams["legend.fontsize"] = 10
    plt.rcParams["legend.title_fontsize"] = 10
    sns.set_context({"font.size": 10,
                     "xtick.labelsize": 10, 
                     "ytick.labelsize": 10, 
                     "axes.labelsize": 10, 
                     "axes.titlesize": 10,
                     "legend.fontsize": 10,
                     "legend.title_fontsize": 10,})
    

def init_dag():
    return PGM(dpi=125, observed_style="inner", alternate_style="shaded")