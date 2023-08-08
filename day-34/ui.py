from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.canvas.create_text(150, 125, text='ashdiasdhasd', fill=THEME_COLOR, font=('Arial 20 italic'))
        self.canvas.grid(pady=20, column=0, row=1, columnspan=2)
        
        check_btnImage = PhotoImage(file='images/true.png')
        self.check_btn = Button(image=check_btnImage, highlightthickness=0)
        self.check_btn.grid(column=0, row=2)
        
        x_btnImage = PhotoImage(file='images/false.png')
        self.check_btn = Button(image=x_btnImage, highlightthickness=0)
        self.check_btn.grid(column=1, row=2)
        
        self.window.mainloop()