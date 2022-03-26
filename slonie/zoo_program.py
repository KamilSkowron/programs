import sys

class Zoo:
    def __init__(self) -> None:
        self.file = sys.argv[1]
        self.number = self.read_file(self.file,0)
        self.wages = self.read_file(self.file,1)
        self.before = self.read_file(self.file,2)
        self.after = self.read_file(self.file,3)
        self.sum = 0
        self.lista = []
        self.total = 0
        self.look = self.before[0]

    def read_file(self,file,row):
        with open (file) as f:
            line = f.readlines()
            out = line[row].strip().split(" ")
            return [int(x) for x in out]

    def calculate(self):
        if (len(self.lista)-2) >= 0:
            min_elefant = self.wages[self.lista[0]-1]
            for index in self.lista:                
                self.sum += self.wages[index-1]
                if min_elefant > self.wages[index-1]:
                    min_elefant = self.wages[index-1]

            add = self.sum + (len(self.lista)-2) * min_elefant
            self.total += add
            self.sum = 0
            return self.total

    def search(self):
        if zoo.after[0] == zoo.before[0]:           #same element
            zoo.before.pop(0)                           #remove     
            zoo.after.pop(0)                            #remove
            if zoo.before == []:                        #if last element is the same
                return None                                     #remove
            self.look = zoo.before[0]

        #finding elements in cycle
        index_element = zoo.after.index(self.look)  
        found_value = zoo.before[index_element]

        #adding elements to lists and remove from available 
        zoo.lista.append(self.look)    
        zoo.before.pop(index_element)
        zoo.after.remove(self.look)

        #return next pointer
        return found_value

zoo = Zoo()

while(True):
    if zoo.look == None:                    #last element was already in right place
        print(zoo.total)     
        break
    elif zoo.look in zoo.lista:             #close cycle   
        zoo.calculate()
        zoo.lista.clear()
        if zoo.before == []:                #when there is no more elements, break
            print(zoo.total)
            break
        zoo.look = zoo.before[0]            #else look new cycle
    else:
        zoo.look = zoo.search()             #if not close cycle yet repeat

