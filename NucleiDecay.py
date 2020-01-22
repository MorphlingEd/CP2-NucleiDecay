from Nuclei import Nuclei
from random import random
def main():
    t = 0
    count = 0
    nucleis = []
    n = 50
    for i in range(0,n):
        nucleis.append([])
        for j in range(0,n):
            new = Nuclei()
            nucleis[i].append(new)
    #         nucleis[i][j].printSym()
    #         if j == n-1:
    #             print()
    # print("Cut!")
    while (count < n*n/2):
        for i in range(0,n):
            for j in range(0,n):
                if nucleis[i][j].symbol == '1':
                    nucleis[i][j].tryDecay(random())
                    if nucleis[i][j].symbol == '0':
                        count += 1
        t += Nuclei.delta_t
    print("The value of the decay constant lambda is 0.02775 per minute, the length of 2D list of nucleis N is 50 and the time step is 0.01 minute.")
    print("After decay, the 2-dimensional list of nucleis is shown below: ")
    for i in range(0,n):
        for j in range(0,n):
            new = Nuclei()
            nucleis[i].append(new)
            nucleis[i][j].printSym()
            if j == n-1:
                print()
    print("The initial number of undecayed nucleis is : " + str(n*n))
    print("The final number of undecayed nucleis is " + str(n*n-count))
    print("The simulated half-life is " + str(t) + " minutes." )
    print("The actual value of the half-life is 24.98 minutes.")
main()