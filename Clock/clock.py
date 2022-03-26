from tkinter import *
from time import *
from tkinter import colorchooser

def time_clock():
	time_string = strftime("%H:%M:%S")
	time_label.config(text=time_string)

	date_string = strftime("%d.%m.%Y")
	date_label.config(text=date_string)

	day_string = strftime("%A")
	day_label.config(text=day_string)
	
	time_label.after(1000,time_clock)

def color_choose():
	z = colorchooser.askcolor()[1]
	line_label.config(bg=z)
	line_label2.config(bg=z)
	frame.config(bg=z)

window = Tk()

z = "#448A1C"

frame = Frame(window,bg=z,relief=RAISED,bd=5)
frame.pack()

icon = PhotoImage(file="pic1.png")
options = Button(frame,image=icon,command=color_choose)
options.grid(row=0,column=1)

time_label = Label(frame,font=('Calibri Light',50,'bold'),padx=10,pady=0,relief=RAISED,bd=5)
time_label.grid(row=0,column=0)

line_label = Label(frame,bg=z)
line_label.grid(row=1,column=0,columnspan=2)

day_label = Label(frame,padx=110,font=('Calibri Light',20),relief=RAISED,bd=5)
day_label.grid(row=2,column=0,columnspan=2)

line_label2 = Label(frame,bg=z)
line_label2.grid(row=3,column=0,columnspan=2)

date_label = Label(frame,font=('Calibri Light',20),relief=RAISED,bd=5)
date_label.grid(row=4,column=0,columnspan=2)

time_clock()

window.mainloop()

	