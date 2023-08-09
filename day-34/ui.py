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
        self.canvas.grid(pady=(20, 50), column=0, row=1, columnspan=2)
        
        true_img = PhotoImage(file='images/true.png')
        self.check_btn = Button(image=true_img, highlightthickness=0)
        self.check_btn.grid(column=0, row=2)
        
        false_img = PhotoImage(file='images/false.png')
        self.check_btn = Button(image=false_img, highlightthickness=0)
        self.check_btn.grid(column=1, row=2)
        
        self.window.mainloop()