# --IMPORTS--
from tkinter import *
from pandas import *

import random

# --CONSTANTS--
BACKGROUND_COLOR = "#B1DDC6"
time = 3
current_word = {}
to_learn = {}
window = Tk()

try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient="records")
    

# --FUNCTIONS--

def back_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")


def next_word():
    global current_word, timer
    window.after_cancel(timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    timer = window.after(3000, back_card)


def is_known():
    global current_word, timer
    window.after_cancel(timer)
    to_learn.remove(current_word)
    print(len(to_learn))
    data = DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()
    
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    timer = window.after(3000, back_card)


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
    command=is_known,
)
right_button.grid(column=1, row=1)

next_word()

window.mainloop()
