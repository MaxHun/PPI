"""
Dieses Programm dient zur Veranschulichung der Fehler bei der Approcimation der ersen und zeweiten Ableitungen
der Sinus Funtion durch die Methode der Vorwaertsdifferenz
"""
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import plotten

def fktn(x):
    """
    Das ist die zweite Ableitung der Testfunktion 
    
    Input:
        x (float):
            Wert, auf dem man die Funktion evaliuiren will
    
    Return: -
    """
    return -np.sin(x)

def main():
    """
    In dieser Funktion wird ein Plot des relativen Fehlers in Abhängigkeit von der Schrittweite mittles der Plottn Klasse gezeichnet.
    
    Input:-
    
    Return:-
    """
    fig = plt.figure()
    ax = plt.subplot(111)
    bereich = np.linspace(0, np.pi, 1000)
    h_array = np.logspace(-3,0,100)
    
    objct = plotten.Plotten(ax, 0, np.pi)
    err_array1 = np.vectorize(objct.err_abl)(np.sin, h_array, np.cos)
    err_array2 = np.vectorize(objct.err_abl2)(np.sin, h_array, fktn)
       
    ax.loglog(h_array, err_array1, label = r'$Fehler in erster Ableitung$')
    ax.loglog(h_array, err_array2, label = r'$Fehler in zweiter Ableitung$')
    ax.loglog(h_array, h_array, label = r'$y = h$')
    ax.loglog(h_array, (h_array)**2, label = r'$y = h^2$')
    ax.loglog(h_array, (h_array)**3, label = r'$y = h^3$')
    
    fig.suptitle('Relativer Fehler in Abhängigkeit von der Schrittweite')
    plt.xlabel('Schrittweite h')
    plt.ylabel('Relativer Fehler')
    ax.legend()
    plt.show()
    
main()
