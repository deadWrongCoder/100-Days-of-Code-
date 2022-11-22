from tkinter import *


def timer():
    count_down(25)
def count_down(count):
    if count > 0:
        canvas.itemconfig(timer_text, text=str(count))
        window.after(1000, count_down, count - 1)



window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30)
text = Label(text="Timer", fg="green",font=("Courier", 30, "bold"))
text.grid(row=0, column=1)
canvas = Canvas(width=200, height=224)
image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=image)
timer_text = canvas.create_text(100,140, text="00:00", fill="white", font=("Courier", 30, "bold") )
canvas.grid(row=1, column=1)
start_button = Button(text="Start", fg="green", command=timer)
start_button.grid(row=2, column=0)
tomato_count = Label(text="✔", fg="green", pady=20, font=("Courier", 30, "bold"))
tomato_count.grid(row=2, column=1)
reset_button = Button(text="Reset", fg="green")
reset_button.grid(row=2, column=2)
window.mainloop()
