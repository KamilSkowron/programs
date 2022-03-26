
class Zoo:
    def __init__(self) -> None:
        self.file = "slo4.in"
        self.number = self.read_file(self.file,0)
        self.wages = self.read_file(self.file,1)
        self.before = self.read_file(self.file,2)
        self.after = self.read_file(self.file,3)
        self.sum = 0
        self.lista = []
        self.total = 0
        

    def read_file(self,file,row):
        with open (file) as f:
            line = f.readlines()
            out = line[row].strip().split(" ")
            return [int(x) for x in out]

    def calculate(self):
        for index in self.lista:                #suma mas cyklu
            self.sum += self.wages[index-1]
        if (len(self.lista)-2) >= 0:
            min_elefant = min([self.wages[self.lista[i]-1]] for i in range(len(self.lista)))[0]
            self.total += self.sum + (len(self.lista)-2) * min_elefant
            self.sum = 0
            return self.total


    def search(self,look_value):
        if look_value in zoo.lista:
            self.calculate()
            zoo.lista.clear()
            return zoo.lista
        else:
            index_element = zoo.after.index(look_value)
            found_value = zoo.before[index_element]
            zoo.lista.append(look_value)    
            zoo.before.pop(index_element)
            zoo.after.remove(look_value)
            return zoo.search(found_value)


zoo = Zoo()


while (any(zoo.before)):
    zoo.search(zoo.before[0])
print(zoo.total)
