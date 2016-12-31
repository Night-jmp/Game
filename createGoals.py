import turtle
import random

class createGoals():

    def __init__(self, color):
        self.goal = turtle.Turtle()
        self.goal.color(color)
        self.goal.shape("battery.gif")
        self.goal.penup()
        self.goal.speed(0)
        self.goal.setposition(random.randint(-590, 590), random.randint(-290, 190))

    def boundary_check(self):
        if self.goal.xcor() > 590 or self.goal.xcor() < -590:
            self.goal.right(180)

        if self.goal.ycor() > 190 or self.goal.ycor() < -290:
            self.goal.right(180)