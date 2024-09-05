from tkinter import *
from snake import Snake

class User_Interface:
    def __init__(self):
        self.window = Tk()

        self.window.title("Shadow the Hedgehog")

        self.window.config(bg="black",width=400,height=400)



        self.Title=Label(text="Shadow the Hedgehog")
        self.Title.pack()

        self.game_on= True
        image = PhotoImage(file="shadow_giff.gif")
        self.label = Label(image=image,width=300,height=300)
        self.label.pack()
        self.button = Button(text="Press Start to play", width=25, height=10, bg='orange', fg='black',
                             activebackground='black',
                             activeforeground='red', command=self.start_game)
        self.button.pack()
        self.window.mainloop()
    def start_game(self):
        self.label.pack()
        self.window.destroy()
        game_on =  True