from tkinter import *
import math
from PIL import Image, ImageTk

root = Tk()
root.title("Simple Calculator")

# Defining the e/display box
e = Entry(root, width=50, borderwidth=20)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Global expression to keep track of the current expression
current_expression = ""

#Defining the functions for the buttons
def click(number):
    global current_expression
    current_expression += str(number)
    e.delete(0, END)
    e.insert(0, current_expression)

def ac_clicked():
    global current_expression
    current_expression = ""
    e.delete(0, END)
    
def sqrt_clicked():
    global current_expression
    try:
        result = math.sqrt(float(e.get()))
        current_expression = str(result)
        e.delete(0, END)
        e.insert(0, current_expression)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")
    
def percentage_clicked():
    global current_expression
    try:
        result = float(e.get()) / 100
        current_expression = str(result)
        e.delete(0, END)
        e.insert(0, current_expression)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")

def divide_clicked():
    global current_expression
    current_expression += "/"
    e.delete(0, END)
    e.insert(0, current_expression)

def multiply_clicked():
    global current_expression
    current_expression += "*"
    e.delete(0, END)
    e.insert(0, current_expression)

def minus_clicked():
    global current_expression
    current_expression += "-"
    e.delete(0, END)
    e.insert(0, current_expression)

def plus_clicked():
    global current_expression
    current_expression += "+"
    e.delete(0, END)
    e.insert(0, current_expression)

def equals_clicked():
    global current_expression
    try:
        result = eval(current_expression)
        current_expression = str(result)
        e.delete(0, END)
        e.insert(0, current_expression)
    except ZeroDivisionError:
        e.delete(0, END)
        e.insert(0, "Error")
    except SyntaxError:
        e.delete(0, END)
        e.insert(0, "Error")

def erase_clicked():
    global current_expression
    current_expression = current_expression[:-1]
    e.delete(0, END)
    e.insert(0, current_expression)

def decimalPt_clicked():
    global current_expression
    if "." not in current_expression:
        current_expression += "."
        e.delete(0, END)
        e.insert(0, current_expression)


# Defining the various buttons of the calculator
ac_Btn = Button(root, text="AC", padx=30, bg="#90EE90", pady=20, command=ac_clicked)
sqrt_Btn = Button(root, text="√", padx=30, bg="#ADD8E6", pady=20, command=sqrt_clicked)
percentage_Btn = Button(root, text="%", padx=30, pady=20, bg="#ADD8E6", command=percentage_clicked)
divide_Btn = Button(root, text="/", padx=30, pady=20, bg="#ADD8E6", command=divide_clicked)
one_Btn = Button(root, text="1", padx=30, pady=20, command=lambda: click(1))
two_Btn = Button(root, text="2", padx=30, pady=20, command=lambda: click(2))
three_Btn = Button(root, text="3", padx=30, pady=20, command=lambda: click(3))
four_Btn = Button(root, text="4", padx=30, pady=20, command=lambda: click(4))
five_Btn = Button(root, text="5", padx=30, pady=20, command=lambda: click(5))
six_Btn = Button(root, text="6", padx=30, pady=20, command=lambda: click(6))
seven_Btn = Button(root, text="7", padx=30, pady=20, command=lambda: click(7))
eight_Btn = Button(root, text="8", padx=30, pady=20, command=lambda: click(8))
nine_Btn = Button(root, text="9", padx=30, pady=20, command=lambda: click(9))
zero_Btn = Button(root, text="0", padx=30, pady=20, command=lambda: click(0))
multiply_Btn = Button(root, text="*", padx=30, pady=20, bg="#ADD8E6", command=multiply_clicked)
minus_Btn = Button(root, text="-", padx=30, pady=20, bg="#ADD8E6", command=minus_clicked)
plus_Btn = Button(root, text="+", padx=30, pady=20, bg="#ADD8E6", command=plus_clicked)
equals_Btn = Button(root, text="=", padx=30, pady=20, bg="#ADD8E6", command=equals_clicked)
erase_Btn = Button(root, text="⌫", padx=30, pady=20, command=erase_clicked)
decimalPt_Btn = Button(root, text=".", padx=30, pady=20, command=lambda: click("."))

# Defining the various positions of the Buttons Created
ac_Btn.grid(row=1, column=0)
sqrt_Btn.grid(row=1, column=1)
percentage_Btn.grid(row=1, column=2)
divide_Btn.grid(row=1, column=3)

seven_Btn.grid(row=2, column=0, pady=10)
eight_Btn.grid(row=2, column=1)
nine_Btn.grid(row=2, column=2)
multiply_Btn.grid(row=2, column=3)

four_Btn.grid(row=3, column=0, pady=1)
five_Btn.grid(row=3, column=1)
six_Btn.grid(row=3, column=2)
minus_Btn.grid(row=3, column=3)

one_Btn.grid(row=4, column=0, pady=10)
two_Btn.grid(row=4, column=1)
three_Btn.grid(row=4, column=2)
plus_Btn.grid(row=4, column=3)

zero_Btn.grid(row=5, column=0, pady=1)
decimalPt_Btn.grid(row=5, column=1)
erase_Btn.grid(row=5, column=2)
equals_Btn.grid(row=5, column=3)


root.mainloop()