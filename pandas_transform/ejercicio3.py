"""
Mediante agg cree un dataframe resumen que contenga 5 valores estadísticos de un dataframe de entra
"""

import numpy as np
import pandas as pd
import requests as req
import statistics as stat

from io import StringIO

url = 'https://raw.githubusercontent.com/rmcelreath/rethinking/master/data/Howell1.csv'
data = req.get(url)

with StringIO(data.text) as csv:
    df = pd.read_csv(csv, sep=';')
    print(df.agg([np.min, np.max, np.sum, np.mean, np.median, stat.mode]))