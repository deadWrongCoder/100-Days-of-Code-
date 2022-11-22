from tkinter import *

window = Tk()
window.title("Km to Mile Converter")
window.minsize(width=100, height=100)

input = Entry(width=10)
input.grid(row=0, column=0)

km = Label(width=10, text="Km")
km.grid(row=0, column=1)

miles_number = Label(width=10)
miles_number.grid(row=1, column=0)

miles = Label(width=10, text="Miles")
miles.grid(row=1, column=1)

def km_to_miles():
    result = int(input.get()) * 0.62137119
    miles_number.config(text= str(round(result, 2)))
convert_button = Button(text="Convert", command=km_to_miles)
convert_button.grid(row=2, column=0)


window.mainloop()
