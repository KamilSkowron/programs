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
            if not odw[j]:
                minC = float("inf")
                sumC = 0
                x = j
                c = 0

                while True:
                    sumC += self.wages[x]
                    minC = min(minC, self.wages[x])
                    x = p[x] - 1
                    odw[x] = True
                    c += 1
                    if (x == j):
                        break


         # Obliczanie wyniku
                score += min((sumC + (c-2) * minC),
                             (sumC + minC + (c+1) * minimal))
        print(score)
        return score

zoo = Zoo()
zoo.function()

