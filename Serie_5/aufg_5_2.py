"""
Dieses Modul loest die Aufgabe 5.2, indem es die Differentialgleichung loest und
das Verhalten der Loesungen grafisch aufstellt.
Autoren Arsen Hnatiuk und Max Huneshagen
"""
import matplotlib
matplotlib.use ("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from sparse_erw import Sparse

matplotlib.rcParams.update({'font.size': 25})
plt.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}', r"\usepackage{nicefrac}"]

def modo(m_nb, numb):
    """
    Funktion, die die modofizierte Modolo Methode aus dem Bericht zu Serie 2 implementiert
    Input:
        m_nb (int):
            Zahl, fuer die wir den Wert der modifizierten Modolo Methode berechnen wollen
        numb (int):
            Feinheit der Diskretisierung
    Return:
        (int):
            Ausgabe der modifizierten Modolo Methode
    """
    if m_nb%(numb-1) == 0:
        return numb-1
    return m_nb%(numb-1)

def gitter(numb, dims):
    """
    Funktion, die fuer eine gegebene Dimension und Schritweite eine Menge von Punkten erzeugt, auf
    der die Differentialgleichung zu loesen ist.
    Input:
        numb (int):
            Feinheit der Diskretisierung
        dims (int):
            Dimension der Diskretisierung
    Return:
        arra (ndarray):
            Array mit den Punkten auf dem Diskretisierungsgitter
    """
    #Dimension 1
    if dims == 1:
        arra = np.zeros(numb-1)
        for i in range(numb-1):
            arra[i] = (i+1)/numb
        return arra
    #Dimension 2
    if dims == 2:
        arra = np.zeros(((numb-1)**2, 2))
        for i in range((numb-1)**2):
            arra[i] = [modo(i+1, numb)/numb, (i//(numb-1)+1)/numb]
        return arra
    #Dimension 3
    arra = np.zeros(((numb-1)**3, 3))
    for i in range((numb-1)**3):
        arra[i] = [modo(i+1, numb)/numb, modo((i//(numb-1)+1), numb)/numb,
                   (i//((numb-1)**2)+1)/numb]
    return arra

def fntn1(wert):
    """
    Beispielfunktion der Dimension 1
    Input:
        wert (float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return np.pi**2*np.sin(np.pi*wert)

def fntn2(wert):
    """
    Beispielfunktion der Dimension 2
    Input:
        wert (array von float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return 2*np.pi**2*(np.sin(np.pi*wert[0])*np.sin(np.pi*wert[1]))

def fntn3(wert):
    """
    Beispielfunktion der Dimension 3
    Input:
        wert (array von float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return 3*np.pi**2*(np.sin(np.pi*wert[0])*np.sin(np.pi*wert[1])*np.sin(np.pi*wert[2]))

def ulsg1(wert):
    """
    Exakte Loesung der Dimension 1
    Input:
        wert (float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return np.sin(np.pi*wert)

def ulsg2(wert):
    """
    Exakte Loesung der Dimension 2
    Input:
        wert (array von float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return np.sin(np.pi*wert[0])*np.sin(np.pi*wert[1])

def ulsg3(wert):
    """
    Exakte Loesung der Dimension 3
    Input:
        wert (array von float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return np.sin(np.pi*wert[0])*np.sin(np.pi*wert[1])*np.sin(np.pi*wert[2])

def loesg(dims, numb, fkt, ulsg):
    """
    Diese Methode dient zur Loesung der Differentialgleichung und zum Vergleichen der exakten
    und approxmierten Loesungen.
    Input:
        dims (int):
            Dimension der Diskretisierung
        numb (int):
            Feinheit der DiskretisierungS
        fkt (Funktion):
            Die gegebene Funktion f aus der Aufgabestellung
        ulsg (Funktion):
            Die exakte Loesung der Differentialgleichung

    Return:
        (float):
            Der absolute Fehler in der approximierten Loesung der Differentialgleichung
    """

#Grafik des Fehlers bezueglich des Iterationsschritts

    #CG Methode Loesung, Dimension 1
    los0 = 0.001*np.ones((numb-1)**dims)

    #Erstellung des Vektors b
    arra = gitter(numb, dims)
    arrb = np.zeros((numb-1)**dims)
    for i in range((numb-1)**dims):
        arrb[i] = fkt(arra[i])/(numb**2)

    #Erstellung und Loesen der Bandmatrix durch die CG-Methode
    eps = 10**-14
    mata = Sparse(dims, numb)
    los = mata.cg_meth(los0, arrb, eps)
    laeng = len(los)

    #Erstellung des Vektors der exakten Loesung
    arrex = np.zeros((numb-1)**dims)
    for i in range((numb-1)**dims):
        arrex[i] = ulsg(arra[i])

    #Erstellung des Vektors des Fehlers in der berechneten Loesung mit C-G-Verfahren
    maxfeh = np.zeros(laeng)
    for k in range(laeng):
        arrf = np.zeros((numb-1)**dims)
        for i in range((numb-1)**dims):
            arrf[i] = np.abs(arrex[i]-los[k][i])
        maxfeh[k] = np.amax(arrf)
        if k == laeng-1:
            print(np.amax(arrf))
    plt.semilogy(range(laeng), maxfeh)
    plt.title("Konvergenzverhalten der Loesung mit der CG-Methode in Dimension "+
              str(dims)+" mit Feinheit der Diskretisierung " + str(numb)+
              " und mit Schranke "+ str(eps))
    plt.xlabel("Iterationsschritt")
    plt.ylabel("Absoluter Fehler")
    
    #plt.savefig("./Bericht/Bilder/IterDim"+str(dims), dpi=300)
    plt.show()

    #Erstellung und Loesen der Bandmatrix durch die L-U-Zerlegung
    mata = Sparse(dims, numb)
    lsg_lu = mata.lgs_lsg(arrb)

    #Erstellung des Vektors des Fehlers in der berechneten Loesung mit L-U-Zerlegung
    arrf = np.zeros((numb-1)**dims)
    for i in range((numb-1)**dims):
        arrf[i] = np.abs(arrex[i]-lsg_lu[i])
    print(np.amax(arrf))

    #Grafik des Fehlers bezueglich Epsilon
    fehl = np.zeros(5)
    ind = 0
    for k in [-2, 0, 2, 4, 6]:
        eps = numb**(-k)
        los0 = 0.001*np.ones((numb-1)**dims)
        mata = Sparse(dims, numb)
        los = mata.cg_meth(los0, arrb, eps)
        laeng = len(los)
        lsg = los[laeng-1]
        arrf = np.zeros((numb-1)**dims)
        for i in range((numb-1)**dims):
            arrf[i] = np.abs(arrex[i]-lsg[i])
        fehl[ind] = np.amax(arrf)
        ind = ind+1
    plt.loglog([numb**2, 1, numb**-2, numb**-4, numb**-6], fehl)
    plt.title("Konvergenzverhalten der numerischen Loesung mit der CG-Methode in Dimension "+
              str(dims)+" und Feinheit der Diskretisierung " + str(numb))
    plt.xlabel("Schranke (abhaengig von der Feinheit der Diskretisierung)")
    plt.ylabel("Absoluter Fehler")

    plt.show()
    
    #Grafik des Fehlers bezüglch der Fehlerschranke
    
    eps = np.logspace(-15, 1, 30)
    los0 = 0.001*np.ones((numb-1)**dims)
    graf = np.zeros(30)
    abbr = 0
    for i in eps:
        mata = Sparse(dims, numb)
        los = mata.cg_meth(los0, arrb, i)
        laeng = len(los)
        arrf = np.zeros((numb-1)**dims)
        for k in range((numb-1)**dims):
            arrf[k] = np.abs(arrex[k]-los[laeng-1][k])
        graf[abbr] = np.amax(arrf)
        abbr = abbr+1
    plt.loglog(eps, graf)
    plt.title("Konvergenzverhalten der numerischen Loesung mit der CG-Methode in Dimension "+
              str(dims)+" und Feinheit der Diskretisierung " + str(numb))
    plt.xlabel("Schranke")
    plt.ylabel("Absoluter Fehler")
    plt.show()

    #Grafik des Fehlers bezüglich der Feinheit der Disretisierung

    if dims == 1:
        arrn = np.arange(4, 1004, 40)
        arrfa = np.zeros(len(arrn))
        refe = 0
        for k in arrn:
            #Erstellung des Vektors b
            arra = gitter(k, dims)
            arrb = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrb[i] = fkt(arra[i])/(k**2)

            #Erstellung und Loesen der Bandmatrix mit C-G-Verfahren
            los0 = 0.001*np.ones((k-1)**dims)
            eps = 10**-14
            mata = Sparse(dims, k)
            los = mata.cg_meth(los0, arrb, eps)
            laeng = len(los)
            lsg = los[laeng-1]

            #Erstellung des Vektors der exakten Loesung
            arrex = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrex[i] = ulsg(arra[i])

            #Erstellung des Vektors des Fehlers in der berechneten Loesung
            arrf = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrf[i] = np.abs(arrex[i]-lsg[i])

            arrfa[refe] = np.amax(arrf)
            refe = refe + 1
        plt.semilogy(arrn, arrfa, 'b', label="Mit C-G-Verfahren")
        
    if dims == 2:
        arrn = np.arange(5, 95, 10)
        arrfa = np.zeros(len(arrn))
        refe = 0
        for k in arrn:
            #Erstellung des Vektors b
            arra = gitter(k, dims)
            arrb = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrb[i] = fkt(arra[i])/(k**2)

            #Erstellung und Lösen der Bandmatrix mit C-G-Verfahren
            los0 = 0.001*np.ones((k-1)**dims)
            eps = 10**-14
            mata = Sparse(dims, k)
            los = mata.cg_meth(los0, arrb, eps)
            laeng = len(los)
            lsg = los[laeng-1]

            #Erstellung des Vektors der exakten Lösung
            arrex = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrex[i] = ulsg(arra[i])

            #Erstellung des Vektors des Fehlers in der berechneten Lösung
            arrf = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrf[i] = np.abs(arrex[i]-lsg[i])

            arrfa[refe] = np.amax(arrf)
            refe = refe + 1
        plt.semilogy(arrn, arrfa, 'b', label="Mit C-G-Verfahren")
        
    if dims == 3:
        arrn = np.arange(3, 23, 4)
        arrfa = np.zeros(len(arrn))
        refe = 0
        for k in arrn:
            #Erstellung des Vektors b
            arra = gitter(k, dims)
            arrb = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrb[i] = fkt(arra[i])/(k**2)

            #Erstellung und Lösen der Bandmatrix mit C-G-Verfahren
            los0 = 0.001*np.ones((k-1)**dims)
            eps = 10**-14
            mata = Sparse(dims, k)
            los = mata.cg_meth(los0, arrb, eps)
            laeng = len(los)
            lsg = los[laeng-1]

            #Erstellung des Vektors der exakten Lösung
            arrex = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrex[i] = ulsg(arra[i])

            #Erstellung des Vektors des Fehlers in der berechneten Lösung
            arrf = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrf[i] = np.abs(arrex[i]-lsg[i])

            arrfa[refe] = np.amax(arrf)
            refe = refe + 1
        plt.semilogy(arrn, arrfa, 'b', label="Mit C-G-Verfahren")

    #Plotten von dem Konvergenzverfahren, Dimension 1
    if dims == 1:
        arrn = np.arange(4, 1004, 20)
        arrfa = np.zeros(len(arrn))
        refe = 0
        for k in arrn:
            #Erstellung des Vektors b
            arra = gitter(k, dims)
            arrb = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrb[i] = fkt(arra[i])/(k**2)

            #Erstellung und Loesen der Bandmatrix
            mata = Sparse(dims, k)
            lsg = mata.lgs_lsg(arrb)

            #Erstellung des Vektors der exakten Loesung
            arrex = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrex[i] = ulsg(arra[i])

            #Erstellung des Vektors des Fehlers in der berechneten Loesung
            arrf = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrf[i] = np.abs(arrex[i]-lsg[i])

            arrfa[refe] = np.amax(arrf)
            refe = refe + 1
        plt.semilogy(arrn, arrfa, 'r', label="Mit L-U-Zerlegung")
        plt.title("Konvergenzverhalten in Dimension 1")
        plt.xlabel("Feinheit der Diskretisierung")
        plt.ylabel("Absoluter Fehler")

    #Plotten von dem Konvergenzverfahren, Dimension 2
    if dims == 2:
        arrn = np.arange(5, 95, 5)
        arrfa = np.zeros(len(arrn))
        refe = 0
        for k in arrn:
            #Erstellung des Vektors b
            arra = gitter(k, dims)
            arrb = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrb[i] = fkt(arra[i])/(k**2)

            #Erstellung und Loesen der Bandmatrix
            mata = Sparse(dims, k)
            lsg = mata.lgs_lsg(arrb)

            #Erstellung des Vektors der exakten Loesung
            arrex = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrex[i] = ulsg(arra[i])

            #Erstellung des Vektors des Fehlers in der berechneten Loesung
            arrf = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrf[i] = np.abs(arrex[i]-lsg[i])

            arrfa[refe] = np.amax(arrf)
            refe = refe + 1
        plt.plot(arrn, arrfa, 'r', label="Mit L-U-Zerlegung")
        plt.title("Konvergenzverhalten in Dimension 2")
        plt.xlabel("Feinheit der Diskretisierung")
        plt.ylabel("Absoluter Fehler")

    #Plotten von dem Konvergenzverfahren, Dimension 3
    if dims == 3:
        arrn = np.arange(3, 23, 2)
        arrfa = np.zeros(len(arrn))
        refe = 0
        for k in arrn:
            #Erstellung des Vektors b
            arra = gitter(k, dims)
            arrb = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrb[i] = fkt(arra[i])/(k**2)

            #Erstellung und Loesen der Bandmatrix
            mata = Sparse(dims, k)
            lsg = mata.lgs_lsg(arrb)

            #Erstellung des Vektors der exakten Loesung
            arrex = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrex[i] = ulsg(arra[i])

            #Erstellung des Vektors des Fehlers in der berechneten Loesung
            arrf = np.zeros((k-1)**dims)
            for i in range((k-1)**dims):
                arrf[i] = np.abs(arrex[i]-lsg[i])

            arrfa[refe] = np.amax(arrf)
            refe = refe + 1
        plt.plot(arrn, arrfa, 'r', label="Mit L-U-Zerlegung")
        plt.title("Konvergenzverhalten in Dimension 3")
        plt.xlabel("Feinheit der Diskretisierung")
        plt.ylabel("Absoluter Fehler")

    plt.legend()

    plt.show()

    return np.amax(arrf)

def main():
    """
    In dieser Funktion werden alle Loesungen der Aufgabe dem Nutzer ausgegeben
    """
    dims = 1
    numb = 100
    fntn = [fntn1, fntn2, fntn3]
    ulsg = [ulsg1, ulsg2, ulsg3]
    maxfl = loesg(dims, numb, fntn[dims-1], ulsg[dims-1])
    print("Der maximale Fehler ist "+str(maxfl))
if __name__ == "__main__":
    main()
