"""
Dieses Program dient zur Veranschaulichung der Funktionnalitaet der Sparse Klasse.
Es wird zu der durch den Benutzer eingegebenen Feinheit der Diskretisierung
und Raumdimension eine Koeffizientenmatrix mittles der Sparse Klasse erstellt.
Anschließend werden die absolute und relative Anzahl der Null- und nicht-Null-Eintraege
ausgedruckt.
"""

abbr = 1
while abbr == 1:
    try:
        dis = int(input('Geben Sie eine die Feinheit der Diskretisierung ein' +
                        ' (eine natürliche Zahl)\n'))
        abbr = 0
    except ValueError:
        print('Nicht gültiger Wert eingegeben. Versuchen Sie erneut.\n')
        abbr = 1
    if dis < 1:
        print('Nicht gültiger Wert eingegeben. Versuchen Sie erneut.\n')
        abbr = 1
abbr = 1
while abbr == 1:
    try:
        dim = int(input('Geben Sie die Raumdimension ein (1, 2 oder 3)\n'))
        abbr = 0
    except ValueError:
        print('Nicht gültiger Wert eingegeben. Versuchen Sie erneut.\n')
        abbr = 1
    if dim not in [1, 2, 3]:
        print('Nicht gültiger Wert eingegeben. Versuchen Sie erneut.\n')
        abbr = 1
sparse = Sparse(dim, dis)

print('Die Anzahl der nicht-Null-Einträge in der Koeffizientenmatrix ist ' + sparse.anz_nn)
print('Die Anzahl der Null-Einträge in der Koeffizientenmatrix ist ' + sparse.anz_n)
print('Die relative Anzahl der nicht-Null-Einträge in der Koeffizientenmatrix ist ' + sparse.rel_nn)
print('Die relative Anzahl der Null-Einträge in der Koeffizientenmatrix ist ' + sparse.rel_n)
