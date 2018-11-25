"""
Dieses Program dient zur Veranschaulichung der Funktionalitaet der Sparse-Klasse.
Es wird zu der durch den Benutzer eingegebenen Feinheit der Diskretisierung
und Raumdimension eine Koeffizientenmatrix mittles der Sparse Klasse erstellt.
Anschliessend werden die absolute und relative Anzahl der Null- und nicht-Null-Eintraege
ausgegeben. Wenn die Matrix nicht groesser als 20x20 ist, wird sie auf der Konsole ausgegeben.
"""
import sparse

def main():
    """
    Hauptprogramm, das die Funktionalitaet der sparse.Sparse-Klasse demonstriert.

    Input: -

    Return: -
    """

    # Abfrage der Parameter dis und dim:

    abbr = 1
    while abbr == 1:
        try:
            dis = int(input('Geben Sie eine die Feinheit der Diskretisierung ein' +
                            ' (eine natuerliche Zahl)\n'))
            if dis < 1:
                print('Nicht gueltiger Wert eingegeben. Versuchen Sie erneut.\n')
                abbr = 1
            else:
                abbr = 0
        except ValueError:
            print('Nicht gueltiger Wert eingegeben. Versuchen Sie erneut.\n')
            abbr = 1
    abbr = 1
    while abbr == 1:
        try:
            dim = int(input('Geben Sie die Raumdimension ein (1, 2 oder 3)\n'))
            if dim not in [1, 2, 3]:
                print('Nicht gueltiger Wert eingegeben. Versuchen Sie erneut.\n')
                abbr = 1
            else:
                abbr = 0
        except ValueError:
            print('Nicht gueltiger Wert eingegeben. Versuchen Sie erneut.\n')
            abbr = 1


    sparse_obj = sparse.Sparse(dim, dis)
    matrix = sparse_obj.return_mat_d()
    print('Es wurden die Dimension {} und die Diskretisierung {} gewaehlt.'.format(dim, dis))

    # Gebe Matrix aus, falls diese nicht groesser als 20x20 ist:
    if matrix.get_shape()[0] <= 20:
        print('Die Koeffizientenmatrix ist:\n', matrix.todense())

    print('Die Anzahl der nicht-Null-Eintraege in der Koeffizientenmatrix ist ' +
          '{}'.format(sparse_obj.anz_nn_abs()))
    print('Die Anzahl der Null-Eintraege in der Koeffizientenmatrix ist ' +
          '{}.'.format(sparse_obj.anz_n_abs()))
    print('Die relative Anzahl der nicht-Null-Eintraege in der Koeffizientenmatrix ist '
          '{}.'.format(sparse_obj.anz_nn_rel()))
    print('Die relative Anzahl der Null-Eintraege in der Koeffizientenmatrix ist '
          '{}.'.format(sparse_obj.anz_n_rel()))

if __name__ == "__main__":
    print(__doc__)
    main()
