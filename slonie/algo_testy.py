import sys

class Zoo:
    def __init__(self, file_name) -> None:

        self.file = file_name
        self.number = self.read_file(self.file, 0)[0]
        self.wages = self.read_file(self.file, 1)
        self.a = self.read_file(self.file, 2)
        self.b = self.read_file(self.file, 3)

    def read_file(self, file, row):
        with open(file) as f:
            line = f.readlines()
            out = line[row].strip().split(" ")
            return [int(x) for x in out]

    def funkcja(self):

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
                c = 0

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

