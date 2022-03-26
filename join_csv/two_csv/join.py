class Join_csv:

    def __init__(self,file1,file2) -> None:
        self.file1 = self.open_csv(file1)
        self.file2 = self.open_csv(file2)
        self.type = 3

    def open_csv(self,file):
        with open(file) as f:
            f_lines = f.readlines()
            return f_lines

    def connect(self,index):
        merge = self.file1[index].strip() + "," + self.file2[index].strip() + "\n"
        return merge

    def save_new_csv(self,name_of_new_file):
        with open(name_of_new_file,"w") as out:
            for index in range(len(self.file1)):
                out.write(self.connect(index))

Conv = Join_csv("loans3.csv", "add.csv")

Conv.save_new_csv("new.csv")