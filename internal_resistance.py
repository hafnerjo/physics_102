# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:49:22 2020

@author: John
"""

import numpy as np
import matplotlib.pyplot as plt

#voltage_drops = np.array([2.6, 4.99, 4.62, 4.83, 5.09, 5.28, 5.31, 5.60])
#resistances = np.array([10, 30, 50, 100, 150, 200, 300, 500])
# Remove an outlier
voltage_drops = np.array([2.6, 4.62, 4.83, 5.09, 5.28, 5.31, 5.60])
resistances = np.array([10, 50, 100, 150, 200, 300, 500])



current = voltage_drops / resistances

plt.plot(current, voltage_drops, 'ro')

m, b = np.polyfit(current, voltage_drops, 1)

print('m=', m)
print('b=', b)

x = np.linspace(0, 0.3)
y = m*x + b

plt.plot(x, y, 'g--')

# Removed an outlier to plot as a separate color.
# When you get something like this is worth throwing it out to check
# what kind of impact it has.
outlier_v = np.array([4.99])
outlier_r = np.array([30])
outlier_current = outlier_v / outlier_r
plt.plot(outlier_current, outlier_v, 'bo')

plt.show()

print(voltage_drops)
print(current)