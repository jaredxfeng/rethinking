import pandas as pd

DATA_DIR = "../data"

def data(name="milk", delim=";"):
    file_path = DATA_DIR + "/" + name + ".csv"
    return pd.read_csv(file_path, delimiter=delim)

def scale(x): 
    if x.ndim == 1:
        return (x - x.mean())/x.std()
    else:
        return (x - x.mean(0))/x.std(0)