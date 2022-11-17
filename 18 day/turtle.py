import turtle
from turtle import Turtle, Screen
import random

xen = Turtle()
colors = ("green", "blue", "red", "yellow", "black", "violet", "orange")

def draw_square():
    for i in range(0, 4):
        xen.right(90)
        xen.forward(100)


def dashed_line():
    for _ in range(21):
        xen.forward(10)
        xen.penup()
        xen.forward(10)
        xen.pendown()

def dif_shapes(sides):
    for i in range(3, sides):
        angle = 360 / i
        for _ in range(0, i):
            xen.right(angle)
            xen.forward(100)

def random_walk():
    xen.width(5)
    xen.speed(10)
    while True:
        xen.color(random.choice(colors))
        xen.right(random.randint(0, 360))
        xen.forward(100)

def spirograph():
    xen.speed(10)
    for angle in range(0, 361, 5):
        xen.circle(100)
        xen.right(angle)


window = Screen()
window.exitonclick()
