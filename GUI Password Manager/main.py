from tkinter import *

window = Tk()

def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    string = website + " | " + username + " | " + password + "\n"
    with open("passwords.txt", "a") as file:
        file.write(string)
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)



window.config(padx=20, pady=20)
window.title("Password Manager")
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="Website: ")
website.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username = Label(text="Username/email: ")
username.grid(row=2, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "email@gmail.com")

password = Label(text="Password: ")
password.grid(row=3, column=0)
password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)
generate_button = Button(text="Generate")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()


