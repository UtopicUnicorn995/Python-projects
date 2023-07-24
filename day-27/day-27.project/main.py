from tkinter import *
import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width=180, height=100)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)


miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

text = Label(text="is equal to")
text.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)


def calculate():
    result.config(text=int(input.get()) * 1.609)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)
window.mainloop()
