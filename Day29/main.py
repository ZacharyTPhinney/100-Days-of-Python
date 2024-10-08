from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    from random import choice,randint,shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']





    password_letters = [choice(letters) for char in range(randint(8, 10))]

    symbol_list = [choice(symbols) for char in range(randint(2, 4))]


    number_list = [choice(numbers) for char in range(randint(2, 4))]

    passwordlist = password_letters + symbol_list + number_list

    shuffle(passwordlist)

    password = "".join(passwordlist)

    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    password = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()



    if len(password) == 0 or len(email) == 0 or len(website) == 0:
        show_warning = messagebox.showwarning(title="Warning", message="There needs to be text here.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPasswod: {password} \nIs it ok to save?")


        if is_ok:

            f = open("passwordsfile.txt", "a")
            f.write(f"Website:{website} | Email:{email} | Password:{password}\n")

            f.close()
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            website_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------dddd------------- #*
from tkinter import *

window = Tk()

#create and place image in window
window.title("Password Manager")
window.config(padx = 50 ,pady=50)
canvas = Canvas(height=200,width = 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row = 0,column = 1)



#labels
website_label = Label(text = "Website:")
website_label.grid(row = 1,column = 0)
email_label = Label(text = "Email/Username:")
email_label.grid(row = 2 ,column = 0)
password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)


#Entries
website_entry = Entry(width = 55)
website_entry.grid(row = 1,column=1,columnspan=2)
email_entry = Entry(width = 55)
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3,column =1)



#Buttons


generate_password_button = Button(text="Generate Password",command=password_generator)
generate_password_button.grid(row = 3,column = 2)
add_button = Button(text = "Add",width = 46,command=save)
add_button.grid(row = 4,column =1,columnspan=2)




window.mainloop()