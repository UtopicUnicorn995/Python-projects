# https://tcl.tk/man/tcl8.6.13/TkCmd/entry.htm
import tkinter
from tkinter import *

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

# LABEL
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "normal"))
my_label.grid(column=0, row=0)
# - my_label.pack(expand=True)

# Update particular component
my_label["text"] = "New Text"
# another option
# - my_label.config(text="New Text")


# BUTTON
def button_clicked():
    my_label["text"] = input.get()


button = tkinter.Button(text="Click Me!", command=button_clicked)
button2 = tkinter.Button(text="New Button", command=button_clicked)
# command=button_clicked -- No (), Name of the function not calling the function
# - button = Button()
button.grid(column=1, row=2)
button2.grid(column=2, row=0)


# ENTRY
input = Entry(width=10)
input.grid(column=4, row=3)
print(input.get())

window.mainloop()
