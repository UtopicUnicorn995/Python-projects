from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, len(password))
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()

#     if len(email) < 1 or len(password) < 1:
#         messagebox.showwarning(
#             title="Warning!", message="Please complete the all the fields"
#         )
#         return
#     else:
#         is_okay = messagebox.askokcancel(
#             title=website,
#             message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?",
#         )
#         if is_okay:
#             f = open("data.txt", "a")
#             f.write(f"{website} || {email} || {password}\n")
#             f.close()
#             messagebox.showinfo(
#                 title="Success!", message="You have successfully added a user!"
#             )
#     website_entry.delete(0, "end")
#     password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky=(W, E))
website_entry.focus
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky=(W, E))
email_entry.insert(0, "Christian@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky=(W, E))


password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky=(W, E))
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky=(W, E))

window.mainloop()
