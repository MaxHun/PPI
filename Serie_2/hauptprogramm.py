"""
Dieses Program dient zur Veranschaulichung der Funktionalitaet der Sparse-Klasse.
Es wird zu der durch den Benutzer eingegebenen Feinheit der Diskretisierung
und Raumdimension eine Koeffizientenmatrix mittles der Sparse Klasse erstellt.
Anschließend werden die absolute und relative Anzahl der Null- und nicht-Null-Eintraege
ausgegeben.
"""
import sparse

def main():
    
    abbr = 1
    while abbr == 1:
        try:
            dis = int(input('Geben Sie eine die Feinheit der Diskretisierung ein' +
                            ' (eine natürliche Zahl)\n'))
            if dis < 1:
                print('Nicht gültiger Wert eingegeben. Versuchen Sie erneut.\n')
                abbr = 1
            else:
                abbr = 0
        except ValueError:
            print('Nicht gültiger Wert eingegeben. Versuchen Sie erneut.\n')
            abbr = 1
    abbr = 1
    while abbr == 1:
        try:
            dim = int(input('Geben Sie die Raumdimension ein (1, 2 oder 3)\n'))
            if dim not in [1, 2, 3]:
                print('Nicht gültiger Wert eingegeben. Versuchen Sie erneut.\n')
                abbr = 1
            else:
                abbr = 0
        except ValueError:
            print('Nicht gültiger Wert eingegeben. Versuchen Sie erneut.\n')
            abbr = 1
    

    sparse_obj = sparse.Sparse(dim, dis)
    print("Es wurden die Dimension {} und die Diskretisierung {} gewaehlt.".format(dim, dis))
    print('Die Anzahl der nicht-Null-Einträge in der Koeffizientenmatrix ist {}'.format(sparse_obj.anz_nn_abs()))
    print('Die Anzahl der Null-Einträge in der Koeffizientenmatrix ist {}. '.format(sparse_obj.anz_n_abs()))
    print('Die relative Anzahl der nicht-Null-Einträge in der Koeffizientenmatrix ist {}.'.format(sparse_obj.anz_nn_rel()))
    print('Die relative Anzahl der Null-Einträge in der Koeffizientenmatrix ist {}.'.format(sparse_obj.anz_n_rel()))

if __name__ == "__main__":
    main()
