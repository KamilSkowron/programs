import sys


class Zoo:
    def __init__(self) -> None:
        self.file = sys.stdin.readlines()
        self.number = int(self.file[0])
        self.wages = [int(x) for x in self.file[1].strip().split()]
        self.a = [int(x) for x in self.file[2].strip().split()]
        self.b = [int(x) for x in self.file[3].strip().split()]

    def function(self):

        p = [None] * self.number
        odw = [False] * self.number
        minimal = min(self.wages)
        score = 0

        # Konstrukcja permutacji p

        for i in range(self.number):
            p[self.b[i]-1] = self.a[i]

        # Rozkład p na cykle proste i wyznaczenie parametrów cykli

        for j in range(self.number):
            p[self.b[j]-1] = self.a[j]
            if not odw[j]:
                minC = float("inf")
                sumC = 0
                elements = []
                x = j

                while (True):
                    elements.append(self.wages[x])
                    minC = min(minC, self.wages[x])
                    x = p[x] - 1
                    odw[x] = True
                    if (x == j):
                        break
                c = len(elements)

                
         # Obliczanie wyniku

                if c >= 2:
                    sumC = sum(elements)
                    score += min((sumC + (c-2) * minC),
                                 (sumC + minC + (c+1) * minimal))

        return score


zoo = Zoo()
zoo.function()
