import matplotlib.pyplot as plt
import seaborn as sns
import arviz as az
from daft import PGM
from utils.analysis import Prefs


def init():
    az.style.use("arviz-doc")
    az.rcParams["stats.hdi_prob"] = Prefs.hdi_width
    plt.rcParams["figure.dpi"] = 150
    plt.rcParams["axes.titleweight"] = "light"
    plt.rcParams["font.size"] = 10
    plt.rcParams["figure.titlesize"] = 10
    plt.rcParams["figure.labelsize"] = 10
    plt.rcParams["legend.fontsize"] = 10
    plt.rcParams["legend.title_fontsize"] = 10
    plt.rcParams["lines.markersize"] = 7
    plt.rcParams["lines.linewidth"] = 0.8
    sns.set_context({"font.size": 10,
                     "xtick.labelsize": 10, 
                     "ytick.labelsize": 10, 
                     "axes.labelsize": 10, 
                     "axes.titlesize": 10,
                     "legend.fontsize": 10,
                     "legend.title_fontsize": 10,})
    

def init_dag():
    return PGM(dpi=125, observed_style="inner", alternate_style="shaded")


def scatter(x, y, ax, s=None):
    return ax.scatter(x, y, edgecolor="b", color="w", alpha=0.5, s=s)

def shade(x, sample_ys, ax):
    return az.plot_hdi(x, sample_ys, ax=ax, color="C6", fill_kwargs={"alpha": 0.2})