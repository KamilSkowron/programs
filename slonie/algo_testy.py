import sys

class Zoo:
    def __init__(self,file_name) -> None:

        self.file = file_name
        self.number = self.read_file(self.file,0)[0]
        self.wages = self.read_file(self.file,1)
        self.a = self.read_file(self.file,2)
        self.b = self.read_file(self.file,3)

        self.p = {}
        self.odw = [False] * self.number
        self.C = []
        self.pakiet = []

    def read_file(self,file,row):
        with open (file) as f:
            line = f.readlines()
            out = line[row].strip().split(" ")
            return [int(x) for x in out]

    def funkcja(self):
        #Konstrukcja permutacji p
        for i in range(self.number):
            self.p[self.b[i]] = self.a[i]

        #Rozkład p na cykle proste
        for j in range(self.number):
            if not self.odw[j]:
   
                x = j + 1
                while ((not self.odw[x-1]) and self.p[x] != x):
                    self.odw[x-1] = True
                    self.C.append(x)
                    x = self.p[x] 
            if len(self.C) > 1:
                self.pakiet.append(self.C[:])
                self.C.clear()
                    
        #Wyznaczenie parametrów cykli i wynik
        minC = float ("inf")
        metoda = 0
        for k in range(len(self.pakiet)):
            sumaC = 0
            minC = float ("inf")
            for e in self.pakiet[k]:     
                sumaC += self.wages[e-1]
                if minC > self.wages[e-1]:
                    minC = self.wages[e-1]

            metoda += min((sumaC + (len(self.pakiet[k])-2) * minC),(sumaC + minC + (len(self.pakiet[k])+1) * min(self.wages)))

        return(metoda)


#zoo = Zoo()
#zoo.funkcja()