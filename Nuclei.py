class Nuclei(object):
    lam = 0.02775
    delta_t = 0.01
    p = lam * delta_t
    def __init__(self):
        self.symbol = '1'
    def tryDecay(self,rand):
        if (rand <= Nuclei.p):
            self.symbol = '0'
    def printSym(self):
        print(self.symbol,end = ' ')