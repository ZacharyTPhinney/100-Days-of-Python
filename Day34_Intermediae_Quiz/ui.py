
from quiz_brain import QuizBrain
from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()


        self.window.title("Quizzler")
        self.button1 = Button( text='button 1', width=25,height=10, bg='green', fg='black', activebackground='black',
                              activeforeground='green')

        self.game_score=0
        self.score_label=Label(text=f"score:{self.game_score}",bg= THEME_COLOR,fg="black",font=("Arial",15,"italic"))
        self.score_label.grid(column=2,row = 0)
        self.canvas=Canvas(height=300,width=300)


        self.window.config(bg=THEME_COLOR)


        self.window.config(padx=20,pady=20)
        self.question_text = self.canvas.create_text(150,125,width=280,text="Question goes here",font=("Arial",20,"italic"))
        self.canvas.grid(column=1,row=1,columnspan=2)
        true = PhotoImage( file="images/false.png")
        false = PhotoImage(file="images/true.png")
        self.button1 = Button( width=75, height=75,image=false,command=self.is_true)
        self.button2 = Button( width=75, height=75 ,
                              image=true,command= self.is_false)
        self.button2.grid(column=2, row=4)
        self.button1.grid(column=1,row=4)
        self.get_next_question()
        self.window.mainloop()



    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
            self.score_label.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.canvas.config(bg="white")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        is_right = self.give_feedback(self.quiz.check_answer("True"))




    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
