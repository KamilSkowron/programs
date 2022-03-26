import sys

class Zoo:
    def __init__(self) -> None:
        self.file = sys.stdin.readlines()
        self.number = int(self.file[0])
        self.wages = [int(x) for x in self.file[1].strip().split()]
        self.a = [int(x) for x in self.file[2].strip().split()]
        self.b = [int(x) for x in self.file[3].strip().split()]

        self.p = {}
        self.odw = [False] * self.number
        self.C = []
        self.pakiet = []


    def funkcja(self):
        #Konstrukcja permutacji p
        for i in range(zoo.number):
            zoo.p[zoo.b[i]] = zoo.a[i]

        #Rozkład p na cykle proste
        for j in range(zoo.number):
            if not zoo.odw[j]:
   
                x = j + 1
                while ((not zoo.odw[x-1]) and zoo.p[x] != x):
                    zoo.odw[x-1] = True
                    zoo.C.append(x)
                    x = zoo.p[x] 
            if len(zoo.C) > 1:
                zoo.pakiet.append(zoo.C[:])
                zoo.C.clear()
                    
        #Wyznaczenie parametrów cykli i wynik
        minC = float ("inf")
        metoda = 0
        for k in range(len(zoo.pakiet)):
            sumaC = 0
            minC = float ("inf")
            for e in zoo.pakiet[k]:     
                sumaC += zoo.wages[e-1]
                if minC > zoo.wages[e-1]:
                    minC = zoo.wages[e-1]

            metoda += min((sumaC + (len(zoo.pakiet[k])-2) * minC),(sumaC + minC + (len(zoo.pakiet[k])+1) * min(zoo.wages)))
        print(metoda)


zoo = Zoo()
zoo.funkcja()