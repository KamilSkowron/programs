class Zoo:
    def __init__(self) -> None:
        self.file = "slo3.in"
        self.number = self.read_file(self.file,0)
        self.wages = self.read_file(self.file,1)
        self.before = self.read_file(self.file,2)
        self.after = self.read_file(self.file,3)
        self.sum = 0

    def read_file(self,file,row):
        with open (file) as f:
            line = f.readlines()
            out = line[row].strip().split(" ")
            return [int(x) for x in out]

    def pair(self):        
        for index_b, value_a in enumerate(zoo.after): 
            index_a = zoo.before.index(value_a)   
            if (zoo.before[index_b] != zoo.after[index_b]):
                yield (index_a,index_b),(zoo.wages[zoo.before[index_b]-1] + zoo.wages[zoo.after[index_b]-1])

    def swapPositions(self,list, pos1, pos2):        
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list

    def found_min(self):
        try:
            lista = list(zoo.pair())
            min_value = min(lista,key=lambda x:x[1]) 
            zoo.swapPositions(self.before,min_value[0][0],min_value[0][1])
            self.sum += min_value[1]
            self.found_min()
        except:
            return print(self.sum)

zoo = Zoo()

zoo.found_min()

        