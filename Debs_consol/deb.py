import json
from datetime import datetime

def read_from_file_to_list(file):
	list_of_data = []
	file_readed = open(file)
	while True:
		line =file_readed.readline()
		if not line: break
		line = line.replace("\'", "\"")
		line = json.loads(line)
		list_of_data.append(line)
	file_readed.close()
	return list_of_data

def write_from_list_to_file(data,file):
	myfile = open(file,'w')
	for element in data:
		myfile.write(str(element) + "\n")
	myfile.close()

def add_record(who,data):
	now = datetime.now()
	cash = input("Insert money value: ")
	try:
		cash = float(cash)
		dep = input("Insert depiction: ")
		date_time = now.strftime("%d.%m.%Y")
		table = {who.lower():{"cash":cash, "dep":dep, "date":date_time}}
		data.append(table)
	except:
		print("Wrong input")
		
def show_records(who,data):
	sum_cash_person = 0
	for element in data:
		try:
			print(element[who])
			sum_cash_person += element[who]["cash"] 
		except:
			pass
	print("{} owed {} zł.".format(who.capitalize(),sum_cash_person))

welcome_tekst = "Welcome in debt system."

menu = """
What do you want to?(Press "0" to leave): 
1. add debt
2. view debts
"""
D = read_from_file_to_list("deb_file.txt")

def program():
	
	print(menu)
	choice = None
	while (choice not in [0,1,2]):
		try:	
			choice = int(input("Choice: "))
		except:
			print("It's not a number")
		if choice not in [0,1,2]:
			print("Avaible option [0,1,2]")
	
	if choice == 1:
		person = input("Who owes?: ")
		add_record(person,D)
		program()
		
	elif choice == 2:
		person = input("Who owes?: ").lower()
		show_records(person,D)
		program()
	elif choice == 0:
		write_from_list_to_file(D,"deb_file.txt")

print(welcome_tekst)
program()
