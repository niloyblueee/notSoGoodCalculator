from tkinter import *

def clear():
    global equation_text
    equation_text=""
    equation.set(equation_text)
    
def percent():
    global equation_text
    if "." in equation_text:
        output=str(float(equation_text)*.1)
        equation.set(output)
        equation_text=output
    else:    
        output=str(int(equation_text)*.1)
        equation.set(output)
        equation_text=output

def button_pressed (num):
    global equation_text
    equation_text+=str(num)
    equation.set(equation_text)

def equal():
    try: 
        global equation_text
        total = str(eval(equation_text))
        equation.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation.set("Error = Divison by Zero")
    except SyntaxError:
        equation.set("Syntax Error")    

window = Tk ()
window.geometry("400x620")
window.title("BLUEEE CALCULATOR")
window.config(bg="black")

equation_text=""
equation = StringVar()
lable = Label(window,textvariable=equation,height=4,width=30,font='impact')
lable.pack()


frame= Frame(window,bg="black")
frame.pack()

button1 = Button(frame,text=1,height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed(1))
button1.grid(column=0,row=3)

button2 = Button(frame,text=2,height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed(2))
button2.grid(column=1,row=3)

button3 = Button(frame,text=3,height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed(3))
button3.grid(column=2,row=3)

button4 = Button(frame,text=4,height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed(4))
button4.grid(column=0,row=2)

button5 = Button(frame,text=5,height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed(5))
button5.grid(column=1,row=2)

button6 = Button(frame,text=6,height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed(6))
button6.grid(column=2,row=2)

button7 = Button(frame,text=7,height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed(7))
button7.grid(column=0,row=1)

button8 = Button(frame,text=8,height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed(8))
button8.grid(column=1,row=1)

button9 = Button(frame,text=9,height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed(9))
button9.grid(column=2,row=1)

dot = Button(frame,text=".",height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed("."))
dot.grid(column=1,row=4)

blank = Button(frame,text=" ",height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed())
blank.grid(column=2,row=4)

button0 = Button(frame,text=0 ,height=4,width=6,font=10,fg="white",bg="#505050",command=lambda: button_pressed(0))
button0.grid(column=0,row=4)

equal = Button(frame,text="=",height=4,width=6,font=10,fg="white",bg="#ff9500",command=equal)
equal.grid(column=3,row=4)

plus = Button(frame,text="+",height=4,width=6,font=10,fg="white",bg="#ff9500",command=lambda: button_pressed("+"))
plus.grid(column=3,row=3)

minus = Button(frame,text="-",height=4,width=6,font=10,fg="white",bg="#ff9500",command=lambda: button_pressed("-"))
minus.grid(column=3,row=2)

multiply = Button(frame,text="X",height=4,width=6,font=10,fg="white",bg="#ff9500",command=lambda: button_pressed("*"))
multiply.grid(column=3,row=1)

divison = Button(frame,text="/",height=4,width=6,font=10,fg="white",bg="#ff9500",command=lambda: button_pressed("/"))
divison.grid(column=3,row=0)

percent = Button(frame,text="%",height=4,width=6,font=10,fg="white",bg="#ff9500",command=percent)
percent.grid(column=2,row=0)

blank = Button(frame,text=" ",height=4,width=6,font=10,fg="white",bg="#ff9500")
blank.grid(column=1,row=0)

ac = Button(frame,text="AC",height=4,width=6,font=10,fg="white",bg="#ff9500",command=clear)
ac.grid(column=0,row=0)


window.mainloop()
