"""
DIESES FILE _NICHT_ MIT ABGEBEN!

kleiner Test zum Plotten des Fehlers in Abh. von h
"""
from matplotlib import pyplot as plt
import numpy as np
import plotten

def quadrat(x):
    return x**5
def abl_quadrat(x):
    return 5*x**4

plt.figure()
ax = plt.subplot(111)
IM = plotten.Plotten(ax,0,10)
h_array = np.logspace(-3,0,100)

# Hier wird die sehr nützliche np.vectorize-Funktion benutzt:

err_array = np.vectorize(IM.err_abl)(np.sin, h_array, np.cos)

ax.loglog(h_array, err_array,".")
ax.plot(h_array, h_array)
plt.show()

