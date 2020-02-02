from random import random

class Nuclei(object):
    """Setting important constants of lodine-128 in class fields"""
    lam = 0.02775
    delta_t = 0.01
    p = lam * delta_t


    def __init__(self):
        """Initialize a new nuclei with its state to be undecayed"""
        self.symbol = '1'

    def tryDecay(self):
        """method to determine whether this nuclei will decay in this timestep"""
        rand = random()
        if (rand <= Nuclei.p):
            self.symbol = '0'  # Symbol becoming '0' means the nuclei has decayed


    def printSym(self):
        """method to print the nuclei's state(symbol)"""
        print(self.symbol,end = ' ')
