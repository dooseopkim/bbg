import numpy as np
import pandas as pd

blood = ['A', 'A', 'A', 'B', 'B', 'AB', 'O']
print(np.unique(blood, return_counts=True))
print(pd.Series(blood).value_counts())
