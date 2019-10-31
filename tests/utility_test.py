"""
Test for utility class functionality
"""

from core.utility import Utility
import pandas as pd
import numpy as np


d1 = [4,3,2,1]
d2 = [1,2,3,4]
d3 = [2,np.nan,6,8]
df = pd.DataFrame()
df['c1'] = d1
df['c2'] = d2

def test_utility():
    mod = Utility(df)
    dfc = mod.add_col('c3', d3)
    assert dfc.shape[1] == 3
    return

