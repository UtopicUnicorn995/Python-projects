from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='ashdiasdhasd', fill=THEME_COLOR, font=('Arial 20 italic'),  width=280)
        self.canvas.grid(pady=(20, 50), column=0, row=1, columnspan=2)
        
        true_img = PhotoImage(file='images/true.png')
        self.check_btn = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.check_btn.grid(column=0, row=2)
        
        false_img = PhotoImage(file='images/false.png')
        self.ex_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.ex_btn.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz game")
            self.check_btn.config(state='disabled')
            self.ex_btn.config(state='disabled')
        self.canvas.config(bg="white")
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

        
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

        
    def give_feedback(self, is_right):
        if is_right: 
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red") 

        self.window.after(1000, self.get_next_question)
        