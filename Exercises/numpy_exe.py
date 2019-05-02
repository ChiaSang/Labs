# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:16:07 2018

@author: ChiaS
"""

import numpy as np
from scipy import linalg
aArray = np.ones((3, 4))
print(aArray)
arr = np.array([[3, 5], [5, 3]])
detrminant = linalg.det(arr)
print(detrminant)