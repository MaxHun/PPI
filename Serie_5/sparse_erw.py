"""
sparse.py stellt die Klasse Sparse zur Verfuegung, mit der die Matrix A^(d) fuer d=1,2,3
bestimmt und analysiert werden kann.
"""
import numpy as np
import scipy.sparse as sp
from scipy.sparse import linalg as sp_lina
from scipy import linalg as lina


class Sparse(object):
    """
    Diese Klasse erlaubt das Erstellen der Matrizen A^(d) fuer d in [1,2,3]. Diese Matrizen werden
    z. B. fuer die Berechnung der DGL u''(x)=-f(x) verwendet. Es handelt sich bei diesen Matrizen
    um sehr duenn besetzte Block-Band-Matrizen, was die Verwendung von sog. sparse-Matrizen
    in der numerischen Umsetzung nahelegt.

    Attribute:

        dim (int):
            Raumdimension des zu untersuchenden Gebietes.
        dis (numpy.ndarray aus floats):
            Mass fuer die Diskretisierung des zu untersuchenden Gebietes.
        matr (scipy.dok_matrix-Objekt):
            A^(d) mit Diskretisierung dis.
    """
    def __init__(self, dim, dis, r_s=None, ex_lsg=None):
        """
        Initialisiert ein neues Sparse-Objekt.

        Input:

            dim (int):
                Raumdimension des zu untersuchenden Gebietes.
            dis (int):
                Bestimmt die Feinheit der Diskretisierung.
            r_s (np.ndarray oder None (Standard)):
                Rechte Seite des zu loesenden Gleichungssystems.
            ex_lsg (function oder None (Standard)):
                Exakte Loesung des zu loesenden Gliechungssystems.

        Return: -
        """
        self.dim = dim
        self.dis = dis
        self.matr = self.constr_mat_l_k(dim, dim, dis)
        self.r_s = r_s
        self.ex_lsg = ex_lsg

    def cg_meth(self, los1, vekb, eps):
        """
        Diese Methode approximiert die Loesung eines Gleichungssystems mithilfe des CG-Verfahrens,
        bis auf eine vogegebene Genauigkeit.

        Input:

            los0 (numpy.ndarray aus floats):
                Die erste Loesung, die in der Iteration benutzt wird
            vekb (numpy.ndarray aus floats):
                Der b Vektor des zu loesendes Gleichungssystems
            eps (float):
                Die Genauigkeit, bei welcher die Iteration abgebrochen wird

        Return:

            los (Liste aus numpy.ndarray aus floats):
                Liste mit den berechneten Loesungen nach jedem Iterationsschitt
        """
        rplus = vekb - self.matr.dot(los1)
        dplus = rplus
        los = []
        norm = 1000000000
        #In dieser Schleife wird die Iteration durchgeführt
        while norm > eps:
            rminus = rplus
            dminus = dplus
            los0 = los1
            zet = self.matr.dot(dminus)
            alpha = np.dot(rminus, rminus)/np.dot(dminus, zet)
            los1 = los0 + np.dot(alpha, dminus)
            rplus = rminus - np.dot(alpha, zet)
            beta = np.dot(rplus, rplus)/np.dot(rminus, rminus)
            dplus = rplus + np.dot(beta, dminus)
            los.append(los1)
            norm = lina.norm(rplus, ord=np.inf)
        return los

    def constr_mat_l_k(self, k, dim, dis):
        """
        Konstruiert die Matrix A_l(k) mit der gewuenschten Diskretisierung.

        Input:

            k (float):
                Bestimmt den Wert auf der Hauptdiagonalen der untersuchten Matrix (=2*k)
            dim (int, moegliche Werte: 1, 2, 3):
                Raumdimension des betrachteten Gebietes.
            dis (int):
                Diskretisierung des Gebietes.

        Return:
            (scipy.sparse.dok_matrix-Objekt):
                A_l(k) mit der gewuenschten Diskretisierung.
        """
        if dim == 1:

            # Im Falle dim==1 werden die 3 mittleren Diagonalen gemaess Definition befuellt:

            mat = sp.dok_matrix((dis-1, dis-1))
            mat.setdiag(2*k)
            mat.setdiag(-1, 1)
            mat.setdiag(-1, -1)
            return mat

        elif dim == 2 or dim == 3:

            # Anlegen der Matrix:

            mat = sp.dok_matrix(((dis-1)**dim, (dis-1)**dim))

            # Per for-Schleife wird auf die (n-1)^(d-1)-dimensionale Diagonale
            # die Matrix A^(d-1) mit gleichem k gelegt (Rekursion):

            for min_ind in (dis-1)**(dim-1)*np.arange(dis-1):
                max_ind = min_ind + (dis-1)**(dim-1)
                if dim == 2:

                    # Der Fall d==2 wird gesondert behandelt, um einen rekursiven Aufruf der
                    # Methode nur fuer d==3 ausfuehren zu muessen. Dies dient der Verbesserung
                    # der Geschwindigkeit dieser Methode. Da setdiag nicht auf Teilmatrizen
                    # anwendbar ist, werden numpy-arrays zur Indexierung verwendet. Die
                    # folgenden drei Zeilen sind dabei analog zum Fall d==1, werden
                    # hier aber auf Teilmatrizen einer groesseren Matrix angewendet.

                    mat[np.arange(min_ind, max_ind), np.arange(min_ind, max_ind)] = 2*k
                    mat[np.arange(min_ind, max_ind)[:-1], np.arange(min_ind, max_ind)[1:]] = -1
                    mat[np.arange(min_ind, max_ind)[1:], np.arange(min_ind, max_ind)[:-1]] = -1
                else:
                    mat[min_ind:max_ind, min_ind:max_ind] = self.constr_mat_l_k(k, dim-1, dis)

            # Zudem werden die beiden (n-1)**(l-1)-ten Nebendiagonalen mit -1 befuellt:

            mat.setdiag(-1, (dis-1)**(dim-1))
            mat.setdiag(-1, -(dis-1)**(dim-1))

            return mat

        # Ausgabe bei fehlerhaftem l:
        print("Der Methode constr_A_k_l wurde ein falscher Wert fuer l " +
              "uebergeben. Moeglich sind l=1,2,3")
        return None

    def return_mat_d(self):
        """
        Diese Methode gibt die Matrix A^(d) as sparse-Matrix zurueck.

        Input: -

        Return:
            (scipy.sparse.dok_matrix-Objekt):
                Die Matrix A^(d) als sparse-Matrix.
        """
        return self.matr

    def return_mat_d_inv(self):
        """
        Gibt die numerisch berechnete Inverse von A^(d) zurueck.

        Input: -

        Return:
            (scipy.sparse.dok_matrix-Objekt):
                Inverse von A^(d).
        """
        return sp_lina.inv(self.matr)

    def return_mat_d_csc(self):
        """
        Gibt A^(d) als scipy.sparse.csc_matrix-Objekt zurueck.

        Input: -

        Return:
            (scipy.sparse.csc_matrix-Objekt)
                Die Matrix A^(d)
        """
        return self.matr.tocsc()

    def anz_nn_abs(self):
        """
        Gibt die Anzahl von Eintraegen von A^(d) zurueck, die ungleich 0 sind.

        Input: -

        Return:
            (int):
                Anzahl von Nicht-Nulleintraegen von A^(d).
        """

        # Array mit Indizes aller Nichtnull-Eintraege von A^(d):

        nn_arr = self.matr.nonzero()[0]

        return len(nn_arr)

    def anz_n_abs(self):
        """
        Gibt die Anzahl von Eintraegen von A^(d) zurueck, die gleich 0 sind.

        Input: -

        Return:
            (int):
                Anzahl von Nulleintraegen von A^(d).
        """

        # Array mit Indizes aller Nichtnull-Eintraege von A^(d):

        nn_arr = self.matr.nonzero()[0]

        # Dimension (Groesse) von A:

        matr_dim = self.matr.get_shape()[0]**2

        return matr_dim - len(nn_arr)

    def anz_nn_rel(self):
        """
        Gibt die relative Anzahl von Eintraegen von A^(d) zurueck, die ungleich 0 sind.

        Input: -

        Return:
            (int):
                Relative Anzahl von Nulleintraegen von A^(d).
        """

        # Array mit Indizes aller Nichtnull-Eintraege von A^(d):

        nn_arr = self.matr.nonzero()[0]

        # Dimension (Groesse) von A:

        matr_dim = self.matr.get_shape()[0]**2

        return len(nn_arr)/matr_dim

    def anz_n_rel(self):
        """
        Gibt die relative Anzahl von Eintraegen von A^(d) zurueck, die gleich 0 sind.

        Input: -

        Return:
            (int):
                Relative Anzahl von Nulleintraegen von A^(d).
        """

        # Array mit Indizes aller Nichtnull-Eintraege von A^(d):

        nn_arr = self.matr.nonzero()[0]

        # Dimension (Groesse) von A:

        matr_dim = self.matr.get_shape()[0]**2

        return 1 - len(nn_arr)/matr_dim

    def kond_a_d_zs(self):
        """
        Gibt die Kondition der Matrix A^(d) bezueglich der Zeilensummennorm zurueck.

        Input: -

        Return:
            (float):
                Kondition von A^(d) bzgl. Zeilennorm.
        """
        norm_matr = sp_lina.norm(self.matr, ord=np.inf)
        norm_matr_inv = sp_lina.norm(self.return_mat_d_inv(), ord=np.inf)
        return norm_matr * norm_matr_inv

    def l_u_zerl(self):
        """
        Errechnet die L-U-Zerlegung von A^(d)=P_r^T*L*U*P_c^T

        Input: -

        Return:
            (list):
                Nullter Eintrag: das mit der Zerlegung korrespondierende scipy.SuperLU-Objekt.
                Erster Eintrag: Tripel aus den Matrizen P_r, P_c, L, U.
        """
        zerl = sp_lina.splu(self.matr)
        matr_dim = self.matr.get_shape()[0]
        pr_matr = sp.csc_matrix((matr_dim, matr_dim))
        pr_matr[zerl.perm_r, np.arange(matr_dim)] = 1
        pc_matr = sp.csc_matrix((matr_dim, matr_dim))
        pc_matr[np.arange(matr_dim), zerl.perm_c] = 1
        l_matr = zerl.L.A
        u_matr = zerl.U.A
        #print( "JHFHGFKHGFKHGTFKHTF", lina.norm(self.matr-(pr_matr.T * (l_matr * u_matr) * pc_matr.T).A))
        return [zerl, [pr_matr, pc_matr, l_matr, u_matr]]

    def lgs_lsg(self, r_s=None):
        """
        Loest das Gleichungssystem Ax=r_s fuer eine vorgebene rechte Seite unter Ausnutzung der
        Dreieckszerlegung.

        Input:

            r_s (numpy.ndarray):
                rechte Seite b des zu loesenden Gleichungssystems A^(d)*x=b.

       Return:
           (numpy.ndarray):
               Loesungsvektor.
        """
        if r_s is None and self.r_s is not None:
            r_s = self.r_s
        elif r_s is  None and self.r_s is  None:
            print("Bitte uebergeben Sie eine gueltige rechte Seite!")
            return True
        pr_matr, pc_matr, l_matr, u_matr = self.l_u_zerl()[1]

        # Berechnen der permutierten rechten Seite:

        r_s_perm = pr_matr*r_s

        # Berechne z:

        zw_erg1 = sp_lina.spsolve_triangular(l_matr, r_s_perm, lower=True)

        # Berechne permutierte Loesung:

        zw_erg2 = sp_lina.spsolve_triangular(u_matr, zw_erg1, lower=False)

        # Berechne Loesung durch Permutation:

        lsg = pc_matr*zw_erg2

        return lsg
        #return self.l_u_zerl()[0].solve(r_s)

    def anz_nn_lu_abs(self):
        """
        Gibt die Anzahl von Eintraegen von L bzw. U zurueck, die ungleich 0 sind.

        Input: -

        Return:
            (int-Tupel):
                Anzahl von Nicht-Nulleintraegen von L und U.
        """

        # Array mit Indizes aller Nichtnull-Eintraege der Matrizen:

        nn_arr_l = self.l_u_zerl()[1][2].nonzero()[0]
        nn_arr_u = self.l_u_zerl()[1][3].nonzero()[0]

        return len(nn_arr_l), len(nn_arr_u)

    def anz_n_lu_abs(self):
        """
        Gibt die Anzahl von Eintraegen von L bzw. U zurueck, die gleich 0 sind.

        Input: -

        Return:
            (int-Tupel):
                Anzahl von Nulleintraegen von L und U.
        """

        # Array mit Indizes aller Nichtnull-Eintraege der Matrizen:

        nn_arr_l = self.l_u_zerl()[1][2].nonzero()[0]
        nn_arr_u = self.l_u_zerl()[1][3].nonzero()[0]

        # Dimension (Groesse) von A, L und U:

        matr_dim = self.matr.get_shape()[0]**2

        return matr_dim - len(nn_arr_l), matr_dim - len(nn_arr_u)

    def anz_nn_lu_rel(self):
        """
        Gibt die relative Anzahl von Eintraegen von L bzw. U zurueck, die ungleich 0 sind.

        Input: -

        Return:
            (int-Tupel):
                Relative Anzahl von Nulleintraegen von L und U.
        """

        # Array mit Indizes aller Nichtnull-Eintraege der Matrizen:

        nn_arr_l = self.l_u_zerl()[1][2].nonzero()[0]
        nn_arr_u = self.l_u_zerl()[1][3].nonzero()[0]

        # Dimension (Groesse) von A, L und U:

        matr_dim = self.matr.get_shape()[0]**2

        return len(nn_arr_l)/matr_dim, len(nn_arr_u)/matr_dim

    def anz_n_lu_rel(self):
        """
        Gibt die relative Anzahl von Eintraegen von L bzw. U zurueck, die gleich 0 sind.

        Input: -

        Return:
            (int-Tupel):
                Relative Anzahl von Nulleintraegen von L und U.
        """

        # Array mit Indizes aller Nichtnull-Eintraege von A^(d):

        nn_arr_l = self.l_u_zerl()[1][2].nonzero()[0]
        nn_arr_u = self.l_u_zerl()[1][3].nonzero()[0]

        # Dimension (Groesse) von A, L und U:

        matr_dim = self.matr.get_shape()[0]**2

        return 1 - len(nn_arr_l)/matr_dim, 1 - len(nn_arr_u)/matr_dim





if __name__ == "__main__":
    # Moeglichkeit zu Testen der Klasse:
    TEST = Sparse(2, 4)
    A = TEST.return_mat_d_csc()
    # print(A.todense(),"\n", TEST.l_u_zerl()[1][2], "\n", TEST.l_u_zerl()[1][2]
    # , np.sum(TEST.anz_nn_lu_abs()))
    # print(TEST.anz_nn_lu_abs())
    #print(TEST.anz_n_rel(), TEST.anz_n_abs(), TEST.anz_nn_abs())
