

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


# defining global initial values to be used in multiple functions
pa = 1e5
t = np.linspace(0, 0.1, 100)
y0 = [0, pa, pa, 0]


def plotter(lines):
    """
    Plots lines using matplotlib
    :param lines: the solutions to the functions you would like to plot
    :return: the plots for xdot, p1, and p2 all as functions of time
    """
    # plotting xdot as a function of time.
    plt.figure(1)
    plt.plot(t, lines[:, 0], 'k-')  # made xdot black, : = all
    plt.xlabel("Time (seconds)")  # label
    plt.ylabel(r"$\dot{x}$")  # label
    plt.title(r"$\dot{x}$ as a function of time plot")  # label
    plt.show()

    # plotting p1 and p2 as a function of time on a new graph
    plt.figure(1)
    plt.ticklabel_format(style='plain')
    plt.subplots_adjust(left=0.2)  # default values kept cutting off my axis labels, thanks to bing copilot for the idea
    plt.plot(t, lines[:, 1], 'r-', label="p1")  # made p1 red
    plt.plot(t, lines[:, 2], 'b-', label="p2")  # made p2 blue
    plt.xlabel("Time (seconds)")  # label
    plt.ylabel("Pressure (pa)")  # label
    plt.title("p1 & p2 as a function of time plot")  # label
    plt.legend()  # show legend for p1 and p2
    plt.show()


def odesyst(y, t):
    """
    Sets the ODE system and returns them in equation form
    :param y: variable
    :param t: time
    :return: xdot function, p1dot function, p2dot function
    """
    # defining parameters for the ode system
    area = 4.909e-4
    Cd = 0.6
    ps = 1.4e7
    pa = 1e5
    v = 1.473e-4
    B = 2e9
    rho = 850
    Kvalve = 2e-5
    m = 30
    yy = 0.002

    # Definitions for readability, not to be uncommented
    # y[0] = xdot
    # y[1] = p1
    # y[2] = p2
    # f1 = xdot = (p1-p2) * A/m
    # f2 = p1dot = (y * Kvalve * (ps - p1) - rho * A * xdot) * beta / (V * rho)
    # f3 = p2dot = (y * Kvalve * (p2 - pa) - rho * A * xdot) * beta / (V * rho)

    f = [(area / m) * (y[1] - y[2]), (B / (rho * v)) * (yy * Kvalve * (ps - y[1]) - rho * area * y[0]),
         (B / (rho * v)) * (rho * area * y[0] - yy * Kvalve * (y[2] - pa)), y[0]]

    return f  # returning all three equations


def main():
    """
    Main function :return: plots ẋ as a function of time, with nice title and labels. Plots p1 and p2 together as
    functions of time, on a new graph, with nice title and labels and legend.
    """
    # calls odeint to solve using our function odesyst as an argument, then calls plotter to plot the results
    plotter(odeint(odesyst, y0, t))


if __name__ == "__main__":
    main()
