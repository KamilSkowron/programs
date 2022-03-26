class Join_csv:

    def __init__(self,file1,file2,column) -> None:              #Creates an object
        self.file1 = self.open_csv(file1)
        self.file2 = self.open_csv(file2)
        self.column = column

    def open_csv(self,file):                                    #Open csv
        with open(file) as f:
            list_of_records = []
            while True:
                line = f.readline().strip()
                if not line:
                    return list_of_records 
                line_record = line.split(',')
                list_of_records.append(line_record)

    def column_check(self):                                     #check number of joined column
        for x1, v1 in enumerate(self.file1[0]):
            if (v1 == self.column):
                set_column1 = x1

        for x2, v2 in enumerate(self.file2[0]):
            if (v2 == self.column):
                set_column2 = x2
        return(set_column1,set_column2)

    def inner(self):                                            # INNER JOIN
        for index1 in range(len(self.file1)):
            for index2 in range(len(self.file2)):
                if (self.file1[index1][self.column_check()[0]] == self.file2[index2][self.column_check()[1]]):
                    yield self.file1[index1] + self.file2[index2]

    def left(self):                                             # LEFT JOIN
        for index1 in range(len(self.file1)):
            value = True
            for index2 in range(len(self.file2)):
                if (self.file1[index1][self.column_check()[0]] == self.file2[index2][self.column_check()[1]]):
                    value = False
                    yield self.file1[index1] + self.file2[index2]
            if (value):
                value = False
                yield self.file1[index1] + ["NaN"]*len(self.file2[0])

    def right(self):                                            # RIGHT JOIN
        for index2 in range(len(self.file2)):
            value = True
            for index1 in range(len(self.file1)):
                if (self.file1[index1][self.column_check()[0]] == self.file2[index2][self.column_check()[1]]):
                    value = False
                    yield self.file1[index1] + self.file2[index2]
            if (value):
                value = False
                yield ["NaN"]*len(self.file1[0]) + self.file2[index2]
                
    def save_new_csv(self,name_of_new_file,function):           # save new csv
        with open(name_of_new_file,"w") as out:
            for x in list(function):                           
                out.write(','.join(x))                          
                out.write("\n")                                 

    def console_print(self,function):                           # console print only
        for x in list(function):
            print(x)

Conv = Join_csv("employee.csv", "branch.csv","emp_id")          # ("file_path","file_path","column_name")


Conv.save_new_csv("inner.csv",Conv.inner())                     # INNER.CSV         ("name_of_new_file", method)
Conv.console_print(Conv.inner())                                # INNER PRINT

Conv.save_new_csv("left.csv",Conv.left())                       # LEFT.CSV          ("name_of_new_file", method)
Conv.console_print(Conv.left())                                 # LEFT PRINT

Conv.save_new_csv("right.csv",Conv.right())                     # RIGHT.CSV         ("name_of_new_file", method)
Conv.console_print(Conv.right())                                # RIGHT PRINT


# If you run this script, will be create three files CSV