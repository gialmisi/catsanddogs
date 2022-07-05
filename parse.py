import numpy as np
import pandas as pd 

def read_excel(fname: str = "Feline_dataset.xlsx", sheet_name: str = "Dataset"):
    path = "./data/"

    with pd.ExcelFile(path+fname) as exfile:
        df = pd.read_excel(exfile, sheet_name)

    return df