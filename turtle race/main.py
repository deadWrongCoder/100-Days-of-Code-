from turtle import Turtle, Screen

import random

window = Screen()
window.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
turtles = []
steps = [10, 20, 30, 40, 50]
ycor = [-60, -30, 0, 30, 60, 120]
message = Screen()
bet = message.textinput("Make your bet", "Color")
winner = ""

def create_turtles():
    for i in range(0, len(colors)):
        new_turtle = Turtle()
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-150, ycor[i])
        turtles.append(new_turtle)
def move_turtles():
    for i in range(0, len(turtles)):
        turtles[i].forward(random.choice(steps))
def check_xcor():
    for i in range(0, len(turtles)):
        if turtles[i].xcor() >= 230 :
            print(turtles[i].xcor())
            global winner
            winner = turtles[i].pencolor()
            return False
    return True

create_turtles()
while check_xcor() == True:
    move_turtles()
if winner == bet:
    print("You won")
else:
    print(f"You lose. Actual winner is {winner}")

