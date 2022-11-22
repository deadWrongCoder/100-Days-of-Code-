from tkinter import *

window = Tk()

window.minsize(width=300, height=300)

label = Label(text="Text")
label.pack()
def change_label():
    label.config(text="I clicked!")

button = Button(text="Click me", command =change_label)
button.pack()
window.mainloop()
