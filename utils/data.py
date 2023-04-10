import pandas as pd

DATA_DIR = "../data"

def data(name="milk"):
    file_path = DATA_DIR + "/" + name + ".csv"
    return pd.read_csv(file_path, delimiter=";")