from datetime import datetime

def read_from_file(file):
        D = [line.rstrip() for line in open(file)]                                #wczytanie pliku do zmiennej 
        B = [dane.split(",") for dane in D]                                       #rozdzielenie pakietu danych
        return B

def add_data(file):
        now = datetime.now()
        try:
                name = input("Insert name: ").lower()
                money = float(input("Insert money value: "))
                dep = input("Insert depiction: ")
                date_time = now.strftime("%d.%m.%Y")
                data = "{},{},{},{}".format(name,money,dep,date_time)
 
                myfile = open(file,'a')
                myfile.write("\n"+str(data))
                myfile.close()
        except:
                print("Wrong data.")

def look_person(variable):
        person = str(input("Person: ")).lower()
        Z = [data for data in variable if data[0] == person]
        if Z == []: return (print("There is not user as: {}".format(person.capitalize())))
        suma = 0
        for data in Z: 
                print(data)
                suma += float(data[1])
        print("{} owes {} zł".format(data[0].capitalize(),suma))

menu = """
What do you want to?(Press "0" to leave): 
1. add debt
2. view debts
"""

def program(file):
        print("Welcome in debt system.")
        while True:
                data_of_file = read_from_file(file)
                print(menu)

                choice = None
                while (choice not in [0,1,2]):
                        try:	
                                choice = int(input("Choice: "))
                        except:
                                print("It's not a number")
                        if choice not in [0,1,2]:
                                print("Avaible option [0,1,2]")
                
                if choice == 1: add_data(file)
                elif choice == 2: look_person(data_of_file)
                else: break

program("test.txt")