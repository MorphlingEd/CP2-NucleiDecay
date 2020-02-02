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
        """takeing random number as """
        rand = random()
        if (rand <= Nuclei.p):
            self.symbol = '0'

    def printSym(self):
        print(self.symbol,end = ' ')