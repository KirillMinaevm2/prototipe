from tkinter import *
from tkinter import ttk
from math import *

def calculate():
    example = entry.get()
    answer = eval(example)
    output.config(text="Результат: " + str(answer))

root = Tk()
root.title('Calculator python')
root.geometry('500x300')
root["bg"] = "white"

entry = Entry(font=("arial", 24), fg="black", bg="white")
entry.pack()

button = Button(root, text="Вычислить",width=50, height=3, command=calculate)
button.pack()

output = Label(font=("arial", 24), fg="black", bg="white")
output.pack()

osn = Label (text="Встроенный Python", fg = "black",bg = "white",font = ("Arial Bold", 24) ).pack (side = TOP)
summa = Label (text="Математическое сложение : a+b ", fg = "black",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
minus = Label (text="Математическое вычитание : a-b ", fg = "black",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
multiply = Label (text="Математическое умножение : a*b ", fg = "black",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
delit = Label (text="Математическое деление : a/b ", fg = "black",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
delit1 = Label (text="Целочисленное деление : a//b ", fg = "black",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
delit2 = Label (text="Деление по модулю : a%b ", fg = "black",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
doubleply = Label (text="Возведение в степень : a**b ", fg = "black",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
kmath = Label (text="Библиотека math ", fg = "grey",bg = "white",font = ("Arial Bold", 24) ).pack (side = TOP)
sqrty = Label (text="Квадратный корень : sqrt(a) ", fg = "grey",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
supfactorial = Label (text="Математический факториал : factorial(a) ", fg = "grey",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
loga = Label (text="Логарифм : log(x[, base]) ", fg = "grey",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
sinus = Label (text="Синус: sin(a) ", fg = "grey",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
cosin = Label (text="Косинус : cos(a) ", fg = "grey",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)
pyth = Label (text="Для 3.11 ", fg = "red",bg = "white",font = ("Arial Bold", 24) ).pack (side = TOP)
cubsqwrt =  Label (text="Кубический корень : cbrt(a) ", fg = "red",bg = "white",font = ("Arial Bold", 15) ).pack (side = TOP)


root.mainloop()


