""" This module serves as an example on how to draw multiple plots in a single
    figure.
"""


import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def plot_quadratic_polynom(lin_coef, const_coef, axis):
    """ Adds a plot of the polynom q(x) = a*x + b to the current figure handle.

    Inputs:
        lin_coef (float): the linear coefficient `a` of the polynom
        const_coef (float): the constant coefficient `b` of the polynom
        axis (matplotlib.axis): the axis object that the polynom will be plottet to
    """

    x_values = np.linspace(-10, 10)
    y_values = lin_coef*x_values + const_coef

    axis.plot(x_values, y_values)



def main():
    """ The main function of this module, which executes the example.
    """

    # first create a new figure and get the axis object therein
    plt.figure()
    ax1 = plt.gca()
    # plot some functions to this axis
    plot_quadratic_polynom(0, 2, ax1)
    plot_quadratic_polynom(1, 0.5, ax1)


    # create a second figure and again get the axis handle of this figure
    plt.figure()
    ax2 = plt.gca()
    # plot some other functions to this plot
    plot_quadratic_polynom(1, 0, ax2)
    plot_quadratic_polynom(2, 0, ax2)


    # now also plot a zero function to both axis
    plot_quadratic_polynom(0, 0, ax1)
    plot_quadratic_polynom(0, 0, ax2)

    # finally plot all figures
    plt.show()



if __name__ == "__main__":
    main()
