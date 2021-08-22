"""
Mediante lambda cree una fución que permita obtener el IMC a partir 
de un data frame que contenga el peso y la estatura de personas.
"""
import numpy as np
import pandas as pd
import requests as req
from io import StringIO

url = 'https://raw.githubusercontent.com/rmcelreath/rethinking/master/data/Howell1.csv'
data = req.get(url)

"""
Converting the text obtained from the raw data into a StringIO object
So in that way the read_csv method can read the data through the I/O stream
"""
with StringIO(data.text) as csv:
    df = pd.read_csv(csv, sep=';')
    print('Data frame\n', df, "\n -----------------------")
    imc = lambda x: (x['weight']/x['height']**2)*10000 # * 10000 to move the decimal dat
    print("IMCs:\n", df.apply(imc, axis=1))
