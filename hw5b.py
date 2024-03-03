# region imports
import hw5a as pta
import random as rnd
from matplotlib import pyplot as plt
import numpy as np

# endregion

# region Functions
def ffPoint(Re, rr):
    """
    This function takes Re and rr as parameters and outputs a friction factor according to the following:
    1.  if Re>4000 use Colebrook Equation
    2.  if Re<2000 use f=64/Re
    3.  else calculate a probabilistic friction factor where the distribution has a mean midway between the prediction
        of the f=64/Re and Colebrook Equations and a standard deviation of 20% of this mean
    :param Re:  the Reynolds number
    :param rr:  the relative roughness
    :return:  the friction factor
    """
    if Re >= 4000:  # Check if Reynolds number is above 4000 to use CBEQN
        return pta.ff(Re, rr, CBEQN=True)
    if Re <= 2000:  # Check if Reynolds number is below 2000 to use laminar flow equation
        return pta.ff(Re, rr)

    CBff = pta.ff(Re, rr, CBEQN=True)  # prediction of Colebrook Equation in Transition region
    Lamff = pta.ff(Re, rr, CBEQN=False)  # prediction of Laminar Equation in Transistion region
    mean = Lamff + ((CBff + Lamff) * ((Re-2000)/2000))  # equation from hw5 sheet
    sig = 0.2 * mean  # from HW5 sheet
    result = np.random.normal(mean, sig, size=None)  # choosing a random value from the normal distribution
    print(result)  # print result to CLI
    return result  # return resulting guess at friction factor


def PlotPoint(Re, f):
    if 2000 <= Re <= 4000:
        pta.plotMoody(pt=(Re, f), plotPoint=True, tri=True)
    else:
        pta.plotMoody(pt=(Re, f), plotPoint=True, tri=False)


def main():
    Re = float(input("Enter the Reynolds number: "))
    rr = float(input("Enter the relative roughness: "))
    f = ffPoint(Re, rr)
    PlotPoint(Re, f)


# endregion

# region Function Calls
if __name__ == "__main__":
    main()
# endregion
