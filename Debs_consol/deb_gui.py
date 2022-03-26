from tkinter import *
from tkinter import ttk
from time import *
import tkinter as tk
import json

PROGRAM_WIDTH = 420
PROGRAM_HEIGHT = 390

total_owed = 0.00

data = {}
js = None
index = 0

def reload():
    global js
    global total_owed
    with open('data.json') as f:
        data = f.read()
    js = json.loads(data)
    print(js)
    for i in range(len(js)):
        i = str(i)
        print(i)
        total_owed += int(js[i][0])

        Label(owed,text=js[i][0]).pack()
        Label(desc,text=js[i][1]).pack()
        Label(date,text=js[i][2]).pack()
        
        text.set(str(total_owed)+" zł owed")
        total.update()

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def submit():
    global total_owed
    global index

    try:

        desp = entry_desp.get()
        money = float(entry_money.get())
        date_string = strftime("%d.%m.%Y")
        
        if len(desp)< 35:  
            total_owed += money
            
            
            with open('data.json', 'a') as fp:
                data[str(len(js)+index)] = js["1"]
                json.dump(data, fp)
            index += 1
            Label(owed,text=money).pack()
            Label(desc,text=desp).pack()
            Label(date,text=date_string).pack()
            
            text.set(str(total_owed)+" zł owed")
            
            entry_money.delete(0, END)
            entry_desp.delete(0, END)
        
        else:
            print("Senstence is too long!")


    except Exception:
        print("This is not a number!")
	
def delete():
	pass

window = Tk()
window.title("Debs program")
#window.resizable(False,False)

text = StringVar()

##--------------# Scrollbar #--------------##

canvas = tk.Canvas(window, borderwidth=0, background="#000000")
frame = tk.Frame(canvas, background="#ffffff")
vsb = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack()
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))


notebook = ttk.Notebook(frame)					# widget that manages a collection of windows/displays

tab1 = Frame(notebook)							# new frame for tab 1
tab2 = Frame(notebook)							# new frame for tab 2

notebook.add(tab1,text="Piskor")
notebook.add(tab2,text="Łukasz")
notebook.pack(expand=False, 					# expand = expand to fill any space not otherwise used
				fill="both")					# fill = fill space on x and y axis


owed = Frame(tab1,relief=RIDGE,bd=2)
owed.grid(row=0,column=0)
desc = Frame(tab1,relief=RIDGE,bd=2)
desc.grid(row=0,column=1)
date = Frame(tab1,relief=RIDGE,bd=2)
date.grid(row=0,column=2)

Label(owed,text="Money owed").pack()
Label(desc,text="                           Description                           ").pack()
Label(date,text="     Date     ").pack()


manage = Frame(window,pady=5)
manage.pack()

##--------------# BUTTONS #--------------##
Label(manage,text="Money_owed").grid(row=0,column=0)
entry_money = Entry(manage,
			        fg="#00FF00",
			        bg="black")
entry_money.grid(row=1,column=0)

Label(manage,text="Description").grid(row=0,column=1)
entry_desp = Entry(manage,
			        fg="#00FF00",
			        bg="black")
entry_desp.grid(row=1,column=1)

Button(manage, text="Submit", command=submit).grid(row=2,column=0,rowspan=2)
Button(manage, text="Clear", command=delete).grid(row=2,column=1,rowspan=20)
total = Label(window,
                textvariable=text,
                fg="#00FF00",
		        bg="black",
                relief=RIDGE,
                bd=3,
                font=('Arial',20))
total.pack()
##--------------# WINDOW SIZE #--------------##

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (PROGRAM_WIDTH/2))
y = int((screen_height/2) - (PROGRAM_HEIGHT/2))
window.geometry(f"{PROGRAM_WIDTH}x{PROGRAM_HEIGHT}+{x}+{y}")

reload()

window.mainloop()