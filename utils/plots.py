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


def scatter(x, y, alpha=.7, c="C0", **args):
    plt.plot(x, y, c=c, alpha=alpha, 
            marker="o", fillstyle="none", linestyle="", **args)


def shade(x, y_PI, c="C0", **args):
    plt.fill_between(x, y_PI[0], y_PI[1], color=c, **args)
    
    
def dens(x, bw_adjust=.5, linewidth=0, fill=True, **args):
    sns.kdeplot(x, bw_adjust=bw_adjust, linewidth=linewidth, fill=fill, **args)