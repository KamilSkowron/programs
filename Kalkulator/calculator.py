from tkinter import *

def button_press(key):
	global equation_text

	equation_text = equation_text + str(key)
	equation_label.set(equation_text)

def equals():
	global equation_text
	try:
		total = str(eval(equation_text))
		equation_label.set(total)
		equation_text = total
		
	except ZeroDivisionError:
		equation_label.set("Arithmetic error")
		equation_text = ""
	
	except SyntaxError:
		equation_label.set("Syntax error")
		equation_text = ""
		
def clear():
	global equation_text

	equation_text = ""
	equation_label.set(equation_text)

window = Tk()
window.title("Calculator")
window.config(relief=RAISED,bd=10)

equation_text = ""
equation_label = StringVar()

view = Label(window,font=("Arial",20),bg="white",width=24,height=2,textvariable=equation_label)
view.pack()

frame = Frame(window)
frame.pack()

button_1 = Button(frame,command=lambda: button_press(1),text="1",height=4,width=9,font=35).grid(row=1,column=0)
button_2 = Button(frame,command=lambda: button_press(2),text="2",height=4,width=9,font=35).grid(row=1,column=1)
button_3 = Button(frame,command=lambda: button_press(3),text="3",height=4,width=9,font=35).grid(row=1,column=2)
button_4 = Button(frame,command=lambda: button_press(4),text="4",height=4,width=9,font=35).grid(row=2,column=0)
button_5 = Button(frame,command=lambda: button_press(5),text="5",height=4,width=9,font=35).grid(row=2,column=1)
button_6 = Button(frame,command=lambda: button_press(6),text="6",height=4,width=9,font=35).grid(row=2,column=2)
button_7 = Button(frame,command=lambda: button_press(7),text="7",height=4,width=9,font=35).grid(row=3,column=0)
button_8 = Button(frame,command=lambda: button_press(8),text="8",height=4,width=9,font=35).grid(row=3,column=1)
button_9 = Button(frame,command=lambda: button_press(9),text="9",height=4,width=9,font=35).grid(row=3,column=2)
button_0 = Button(frame,command=lambda: button_press(0),text="0",height=4,width=9,font=35).grid(row=3,column=3)

button_comma = Button(frame,command=lambda: button_press("."),text=".",height=4,width=9,font=35).grid(row=0,column=0)

multiply = Button(frame,command=lambda: button_press("*"),text="*",height=4,width=9,font=35).grid(row=0,column=1)
devide = Button(frame,command=lambda: button_press("/"),text="/",height=4,width=9,font=35).grid(row=0,column=2)
plus = Button(frame,command=lambda: button_press("+"),text="+",height=4,width=9,font=35).grid(row=1,column=3)
minus = Button(frame,command=lambda: button_press("-"),text="-",height=4,width=9,font=35).grid(row=2,column=3)

button_clear = Button(frame,command=clear,text="C",height=4,width=9,font=35).grid(row=0,column=3)
button_equals = Button(frame,command=equals,text="=",height=4,width=39,font=35).grid(row=4,column=0,columnspan=4)

window.mainloop()