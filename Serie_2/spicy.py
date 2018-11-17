import numpy as np
from scipy.sparse import dok_matrix
import scipy.sparse as sp
from timeit import default_timer as timer
"""
Funktion, die eine Blockmatrix erstellt
"""
#def block(n, k):
#    A = dok_matrix((n-1, n-1))
#    for i in range(n-1):
#        for j in range(n-1):
#            if i==j:
#                A[i, j] = 2*k
#            elif i==(j+1) or i==(j-1):
#                A[i, j] = -1
#    return A 
def A_matr(d, n):
    k=d
    l=d
    if d == 1:
        A = dok_matrix((n-1, n-1))
        A.setdiag(2*k)
        A.setdiag(-1,1)
        A.setdiag(-1,-1)
        return A
    elif d>1:
        A = sp.dok_matrix(((n-1)**l,(n-1)**l))
        for min_ind in (n-1)**(l-1)*np.arange(n-1):
            max_ind = min_ind + (n-1)**(l-1)
            A[min_ind:max_ind, min_ind:max_ind] = A_matr(d-1,n)
        for min_spalt in (n-1)**(l-1)*np.arange(n-2):
            min_zeil = min_spalt + (n-1)**(l-1)
            max_zeil = min_zeil + (n-1)**(l-1)
            max_spalt = min_spalt + (n-1)**(l-1)
            A[min_spalt:max_spalt, min_zeil:max_zeil] = sp.eye((n-1)**(l-1))
            A[min_zeil:max_zeil, min_spalt:max_spalt] = sp.eye((n-1)**(l-1))
        return A
start_A_matr = timer()
T = A_matr(3,20)
end_A_matr = timer()
print("Die Slicing-Methode dauerte {} s.".format(-start_A_matr+end_A_matr))
#print(T.todense())
### AB HIER KOMMEN ARSENS SACHEN ###

def block(n, k):
    A = dok_matrix((n-1, n-1))
    A.setdiag(2*k)
    A.setdiag(-1,1)
    A.setdiag(-1,-1)
    return A

"""
Fukntion, die die Matrix der groesserer Ordnung ausfuellt
"""
#Für die Matrix der Dimension 2
def ausfuellen(l, block, mat2, n):
    for i in range(n-1):
        for j in range(n-1):
            if i==j or i==(j+1) or i==(j-1):
                mat2[l*(n-1)+i, l*(n-1)+j]=block[i, j]

#Für die Matrix der Dimension 3    
def ausfuellen2(l, mat2, mat3, n):
    for i in range((n-1)**2):
        if i>0:
            mat3[l*((n-1)**2)+i, l*((n-1)**2)+i-1]=mat2[i, i-1]
        if i<((n-1)**2-1):
            mat3[l*((n-1)**2)+i, l*((n-1)**2)+i+1]=mat2[i, i+1]
        if i>(n-2):
            mat3[l*((n-1)**2)+i, l*((n-1)**2)+i-n+1]=-1
        if i<((n-1)**2-(n-1)):
            mat3[l*((n-1)**2)+i, l*((n-1)**2)+i+n-1]=-1

n=50
k=3

s = timer()

array1 = np.zeros((n-1)**3)
array2 = np.zeros((n-1)**3)
for i in range((n-1)**3):
    array1[i] = -1
    array2[i] = k*2

mat1 = block(n, k)
#Matrix der Dimension 2
mat2 = dok_matrix(((n-1)**2, (n-1)**2))
mat2.setdiag(array1, n-1)
mat2.setdiag(array1, -(n-1))
for i in range(n-1):
    ausfuellen(i, mat1,mat2, n)

#Metrix der Dimension 3
mat3 = dok_matrix(((n-1)**3, (n-1)**3))
mat3.setdiag(array1, (n-1)**2)
mat3.setdiag(array1, -(n-1)**2)
mat3.setdiag(array2)
for i in range(n-1):
    ausfuellen2(i, mat2,mat3, n)
e = timer()
print("Die for-Schleifen-Methode dauerte {} s.".format(e-s))
#print(mat1.todense())
#print(mat2.todense())
#print(mat3.todense())
