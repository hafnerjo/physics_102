# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:29:11 2020

@author: John
"""

import numpy as np
import matplotlib.pyplot as plt

r = 11.0
v = 15

resistors = np.linspace(0, 500, 200)

power = v**2 / (r + resistors)

plt.plot(resistors, power, 'b-')
plt.show()