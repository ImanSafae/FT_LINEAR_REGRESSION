import numpy as np
import pandas as pd
import os, sys

def load(path: str):
    ret = None

    try:
        if (isinstance(path, str) is False):
            raise ValueError("Path must be a string")
        if (path.endswith(".csv") is False):
            raise ValueError("Path must be a csv file")
        if (os.path.exists(path) is False):
            raise ValueError("File not found")
        ret = pd.read_csv(path)
    except Exception as e:
        print(e)
    return ret