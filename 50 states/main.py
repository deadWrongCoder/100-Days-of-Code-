from turtle import Turtle, Screen
import pandas

window = Screen()
window.title("50 States")
image = "image.gif"
window.addshape(image)
xen = Turtle()
xen.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = 0
guessed_list = []
default_title = "Guess the State"
while guessed_states < 50:
    answer = window.textinput(title=default_title, prompt="What's another state's name?").title()
    if answer in states:
        state_data = data[data.state == answer]
        new_text = Turtle()
        new_text.penup()
        new_text.hideturtle()
        new_text.goto(int(state_data.x), int(state_data.y))
        new_text.write(answer)
        guessed_list.append(answer)
        guessed_states += 1
        default_title = f"{guessed_states}/50 States"
window.exitonclick()
