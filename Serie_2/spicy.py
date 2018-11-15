import numpy as np
from scipy.sparse import dok_matrix


"""
Funktion, die eine Blockmatrix erstellt
"""
def block(n, k):
    A = dok_matrix((n-1, n-1))
    for i in range(n-1):
        for j in range(n-1):
            if i==j:
                A[i, j] = 2*k
            elif i==(j+1) or i==(j-1):
                A[i, j] = -1
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
k=2



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

#print(mat2.todense())
#print(mat3.todense())
