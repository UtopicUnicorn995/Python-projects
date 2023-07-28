from tkinter import *
from tkinter import messsagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # messsagebox.showinfo(title="Title", message="Message")
    t = Toplevel()

    f = open("data.txt", "a")
    f.write(f"{website} || {email} || {password}\n")
    f.close()
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")


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


password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3, sticky=(W, E))
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=(W, E))

window.mainloop()
