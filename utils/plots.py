import matplotlib.pyplot as plt
import seaborn as sns
import arviz as az
from daft import PGM
from utils.analysis import Prefs


def init():
    #az.style.use("arviz-doc")
    plt.style.use("ggplot")
    az.rcParams["stats.hdi_prob"] = Prefs.hdi_width
    
    plt.rcParams["axes.titleweight"] = "light"
    plt.rcParams["figure.dpi"] = 150
    plt.rcParams["figure.figsize"] = (11, 3.5)
    plt.rcParams["figure.labelsize"] = 10
    plt.rcParams["figure.subplot.top"] = 1
    plt.rcParams["figure.subplot.bottom"] = 0.05
    plt.rcParams["figure.titlesize"] = 10
    plt.rcParams["font.size"] = 10
    plt.rcParams["legend.fontsize"] = 10
    plt.rcParams["legend.title_fontsize"] = 10
    plt.rcParams["lines.linewidth"] = 0.8
    plt.rcParams["lines.markersize"] = 7
    
    sns.set_context({"font.size": 10,
                     "xtick.labelsize": 10, 
                     "ytick.labelsize": 10, 
                     "axes.labelsize": 10, 
                     "axes.titlesize": 10,
                     "legend.fontsize": 10,
                     "legend.title_fontsize": 10,})
    

def init_dag():
    return PGM(dpi=125, observed_style="inner", alternate_style="shaded")


def scatter(x, y, ax, s=None, alpha=0.5):
    return ax.scatter(x, y, edgecolor="C0", color="w", alpha=alpha, s=s)


def shade(x, sample_ys, ax, color="C3", alpha=0.4):
    return az.plot_hdi(x, sample_ys, ax=ax, color=color, fill_kwargs={"alpha": alpha})