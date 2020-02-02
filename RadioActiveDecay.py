from Nuclei import Nuclei


class radioActiveDecay(object):
    def __init__(self,n = 50):
        """ initialize the 2D list of nucleis, setting default dimension to be 50"""
        self.dim = n
        self.nucleis = []

        """ Using double loop to initialize each place's nucleis"""
        for i in range(0,self.dim):
            self.nucleis.append([])
            for j in range(0,self.dim):
                new = Nuclei()
                self.nucleis[i].append(new)
    
    def decay(self):
        """method used to simulate radioactivedecay and print 2D list and necessary information"""
        t = 0
        count = 0
        n = self.dim

        """usinging tryDecay method of each nuclei with random number as argument 
        to determine whether it decayes """
        while (count < n*n/ 2):
            for i in range(0,n):
                for j in range(0,n):
                    if self.nucleis[i][j].symbol == '1':
                        self.nucleis[i][j].tryDecay()
                        if self.nucleis[i][j].symbol =='0':
                            count += 1
            t += Nuclei.delta_t

        """Print each nuclei's symbol"""
        for i in range(0,n):
            for j in range(0,n):
                self.nucleis[i][j].printSym()
            if j == n-1:
                print()

        """Print important information of this decay process"""
        print("The value of the decay constant lambda is " + str(Nuclei.lam) + " per minute, the length of 2D list of nucleis N is "+str(n)+ " and the time step is " + str(Nuclei.delta_t)+ " minute.")
        print("After decay, the 2-dimensional list of nucleis is shown above: ")
        print("The initial number of undecayed nucleis is : " + str(n*n))
        print("The final number of undecayed nucleis is " + str(n*n-count))
        print("The simulated half-life is " + str(t) + " minutes." )
        print("The actual value of the half-life is 24.98 minutes.")


def main():
    d = radioActiveDecay()
    d.decay()

main()


# def main():
    #     t = 0
#     count = 0
#     nucleis = []
#     n = 50
#     for i in range(0,n):
#         nucleis.append([])
#         for j in range(0,n):
#             new = Nuclei()
#             nucleis[i].append(new)

#     while (count < n*n/2):
#         for i in range(0,n):
#             for j in range(0,n):
#                 if nucleis[i][j].symbol == '1':
#                     nucleis[i][j].tryDecay(random())
#                     if nucleis[i][j].symbol == '0':
#                         count += 1
#         t += Nuclei.delta_t

#     for i in range(0,n):
#         for j in range(0,n):
#             new = Nuclei()
#             nucleis[i].append(new)
#             nucleis[i][j].printSym()
#             if j == n-1:
#                 print()
#     print("The value of the decay constant lambda is " + str(Nuclei.lam) + " per minute, the length of 2D list of nucleis N is "+str(n)+ " and the time step is " + str(Nuclei.delta_t)+ " minute.")
#     print("After decay, the 2-dimensional list of nucleis is shown above: ")
#     print("The initial number of undecayed nucleis is : " + str(n*n))
#     print("The final number of undecayed nucleis is " + str(n*n-count))
#     print("The simulated half-life is " + str(t) + " minutes." )
#     print("The actual value of the half-life is 24.98 minutes.")