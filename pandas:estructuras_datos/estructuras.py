import numpy as np
import pandas as pd

# sin indicar los indices
s = pd.Series(np.random.randn(5))
print(s)
print(s.index)

# diccionario
d = {'b': 1 }
s = pd.Series(d)
print(s)
print(s.index)
