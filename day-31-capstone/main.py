# --IMPORTS--
from tkinter import *
from pandas import *

import random

# --CONSTANTS--
BACKGROUND_COLOR = "#B1DDC6"
time = 3

window = Tk()


data_storage = []

try:
    with open("data/words_to_learn.csv") as new_data:
        data_to_use = read_csv(new_data).to_dict(orient="records")
        data_storage = data_to_use
except FileNotFoundError:
    with open("data/french_words.csv") as data_file:
        data_to_use = read_csv(data_file).to_dict(orient="records")
        DataFrame(data_to_use).to_csv("data/words_to_learn.csv", index=False)
else:
    with open("data/french_words.csv") as data_file:
        data_to_use = read_csv(data_file).to_dict(orient="records")
        data_storage = data_to_use
   
# --FUNCTIONS--
print(data_storage)

def back_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=word_user["English"], fill="white")


def next_word():
    global word_user, timer
    window.after_cancel(timer)
    word_user = random.choice(data_to_use)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=word_user["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    timer = window.after(3000, back_card)


def next_word2():
    global word_user, timer
    window.after_cancel(timer)
    try:
        word_user = random.choice(data_storage)
    except: 
        canvas.itemconfig(language, text="Title", fill="black")
        canvas.itemconfig(word, text="Word", fill="black")
        canvas.itemconfig(language, text="Title", fill="white")
        canvas.itemconfig(word, text="Word", fill="white")
    else:
        word_user = random.choice(data_to_use)

    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=word_user["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    timer = window.after(3000, back_card)
    data_storage.remove(word_user)
    DataFrame(data_storage).to_csv("data/words_to_learn.csv", index=False)


# --UI--

window.title("Flashy Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, back_card)

# -IMAGES-
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
wrong_btnImage = PhotoImage(file="images/wrong.png")
right_btnImage = PhotoImage(file="images/right.png")

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))


wrong_button = Button(
    image=wrong_btnImage,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0,
    command=next_word,
)
wrong_button.grid(column=0, row=1)
right_button = Button(
    image=right_btnImage,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0,
    command=next_word2,
)
right_button.grid(column=1, row=1)

next_word()

window.mainloop()
