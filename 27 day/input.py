from tkinter import *

window = Tk()

window.minsize(width=300, height=300)

label = Label(text="Text")
label.pack()
input = Entry(width=20)
input.pack()
def change_label():
    text= input.get()
    label.config(text=text)

button = Button(text="Click me", command =change_label)
button.pack()

window.mainloop()
