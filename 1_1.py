import numpy as np
import matplotlib  
matplotlib.use("TkAgg") 
from matplotlib import pyplot as plt


class Plotten(object):
    def __init__(self, plotbereich, oben, unten, h, fkt):
        self.plotbereich = plotbereich
        self.oben = oben
        self.unten = unten
        self.h = h
        self.fkt = fkt
        self.anz = int((oben - unten)/h) # Anzahl der Teilintervalle
        #print(anz)
        self.intervall = np.linspace(unten, oben, self.anz)
        #print(intervall) 
    def zeichnen(self):
        print("Hallo")
        self.plotbereich.plot(self.intervall, self.fkt(self.intervall))
        

plt.figure()
AX=plt.subplot(111)

plot = Plotten(AX, 2*np.pi, 0, 0.01, np.sin)
plot.zeichnen()

plt.show()









#f=plt.figure()

#plotten(f, 2*np.pi, 0, 0.01, sinus)
#plt.plot(1,2)
#plt.show()

#x=np.linspace(1,2,100)
#plt.figure()
#plt.plot(x, np.sin(x))
#plt.show()
