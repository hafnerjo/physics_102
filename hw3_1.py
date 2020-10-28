# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:29:11 2020

@author: John
"""

import numpy as np
import matplotlib.pyplot as plt

r = 11.0
v = 15

R = np.linspace(0, 200, 200)
current = v / (r + R)
power = current**2 * R

# Plot the calculated value for R='r' that appears to be the max
plt.axvline(x=r, linestyle='--', color='g')

plt.plot(R, power, 'b-')
plt.show()