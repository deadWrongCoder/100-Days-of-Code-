from turtle import Turtle, Screen

window = Screen()
xen = Turtle()

def move_forwards():
    xen.forward(10)

def move_backwards():
    xen.backward(10)

def turn_left():
    xen.left(10)

def turn_right():
    xen.right(10)

def clear():
    xen.penup()
    xen.clear()
    xen.home()
    xen.pendown()

window.listen()

window.onkey(key="W", fun=move_forwards)
window.onkey(key="S", fun=move_backwards)
window.onkey(key="A", fun=turn_left)
window.onkey(key="D", fun=turn_right)
window.onkey(key="C", fun=clear)

window.exitonclick()
