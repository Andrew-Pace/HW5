# During the completion of this code, assistance was received from ChatGPT

# region Imports
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as pyplot
from math import floor, ceil
# endregion

# region Functions

def RSquared(x,y,coeff):
    """
    To calculate the R**2 value for a set of x,y data and a LeastSquares fit with polynomial having coefficients a
    :param x:
    :param y:
    :param a:
    :return:
    """
    AvgY=np.mean(y) #calculates the average value of y
    SSTot=0
    SSRes=0
    ymodel=Poly(x,*coeff)
    for i in range(len(y)):
        SSTot+=(y[i]-AvgY)**2
        SSRes+=(y[i]-ymodel[i])**2
    RSq= 1 - SSRes / SSTot

    return RSq

def Poly(xdata, *a):
    """
    Calculate the value for a polynomial given xdata and the coefficients of the polynomial.
    :param xdata: An array of x values for computing corresponding y values.
    :param a: Coefficients of the polynomial.
    :return: The array of y values corresponding to xdata.
    """
    y = np.zeros_like(xdata)
    power = len(a) - 1
    for i in range(power + 1):
        for j in range(len(xdata)):
            x = xdata[j]
            c = a[i]
            y[j] += c * x ** i
    return y

def PlotLeastSquares(x, y, coeff, showpoints=True, npoints=500):
    """
    Make a single formatted plot for a polynomial fit to the x,y data.
    :param x: The x data as a numpy array.
    :param y: The y data as a numpy array.
    :param coeff: The coefficients for the polynomial fit.
    :param showpoints: Boolean indicating if we should show points or not.
    :param npoints: Number of points in the curve fit to plot.
    :return: List of xvals and yvals for the plot.
    """
    Xmin, Xmax = min(x), max(x)
    Ymin, Ymax = min(y), max(y)
    xvals = np.linspace(Xmin, Xmax, npoints)
    yvals = Poly(xvals, *coeff)
    RSq = RSquared(x, y, coeff)
    pyplot.plot(xvals, yvals, linestyle='dashed', color='black', linewidth='2')
    pyplot.title(r'$R^2={:0.3f}$'.format(RSq))
    pyplot.xlim(floor(Xmin * 10) / 10, ceil(Xmax * 10) / 10)
    pyplot.ylim(floor(Ymin), ceil(Ymax * 10) / 10)
    if showpoints:
        pyplot.plot(x, y, linestyle='none', marker='o', markerfacecolor='white', markeredgecolor='black', markersize=10)
    pyplot.xlabel('X values')
    pyplot.ylabel('Y values')
    pyplot.gca().tick_params(axis='both', top=True, right=True, direction='in', grid_linewidth=1, grid_linestyle='dashed', grid_alpha=0.5)
    pyplot.show()
    return xvals, yvals


def LeastSquaresFit(x, y, power=1):
    """
    Fit x, y data with a polynomial of specified degree and return the coefficients.
    :param x: The x-values of data points.
    :param y: The y-values of data points.
    :param power: The degree of the polynomial.
    :return: The coefficients for the polynomial fit.
    """
    a = np.ones(power + 1)
    coeff, _ = curve_fit(Poly, x, y, p0=a)
    return coeff

def main():
    """
    Test and plot curve_fit functionalities.
    """
    x = np.array([0.05, 0.11, 0.15, 0.31, 0.46, 0.52, 0.70, 0.74, 0.82, 0.98, 1.17])
    y = np.array([0.956, 1.09, 1.332, 0.717, 0.771, 0.539, 0.378, 0.370, 0.306, 0.242, 0.104])
    coeff1 = LeastSquaresFit(x, y, power=1)
    linx, liny = PlotLeastSquares(x, y, coeff1, showpoints=True)
    coeff2 = LeastSquaresFit(x, y, power=3)
    cubx, cuby = PlotLeastSquares(x, y, coeff2, showpoints=True)
    pyplot.plot(linx, liny, linewidth=2, linestyle='dashed', color='black', label='Linear fit')
    pyplot.plot(cubx, cuby, linewidth=2, linestyle='dotted', color='black', label='Cubic fit')
    pyplot.plot(x, y, linestyle='none', marker='o', markersize=10, markerfacecolor='white', markeredgecolor='black', label='Data')
    pyplot.xlabel('X values')
    pyplot.ylabel('Y values')
    pyplot.legend()
    pyplot.tick_params(axis='both', top=True, right=True, direction='in', grid_linewidth=1, grid_linestyle='dashed', grid_alpha=0.5)
    pyplot.show()

# endregion

# region Function Calls
if __name__ == "__main__":
    main()
# endregion
