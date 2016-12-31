import turtle
import createPlayer

class createScreen():
    '''Creates the player screen'''

    def __init__(self):
        self.bgimage = "mars.gif"
        wn = turtle.Screen()
        wn.screensize(600, 600)
        wn.setup(width=1.0, height=1.0, startx=None, starty=None)
        wn.bgpic(self.bgimage)
        wn.addshape("rover.gif")
        wn.addshape("battery.gif")
        wn.tracer(3)
        mypen = turtle.Turtle()
        mypen.penup()
        mypen.setposition(-600, -300)
        mypen.pensize(3)
        mypen.pencolor("white")
        mypen.pendown()
        for side in range(2):
            mypen.forward(1200)
            mypen.left(90)
            mypen.forward(500)
            mypen.left(90)
        mypen.hideturtle()