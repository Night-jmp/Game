import turtle

class createPlayer():

    def __init__(self):
        self.speed = 4
        self.score = 0
        self.player = turtle.Turtle()
        self.player.shape("rover.gif")
        self.player.penup()
        self.player.speed(0)

    def turnleft(self):
        self.player.left(30)

    def turnright(self):
        self.player.right(30)

    def increasespeed(self):
        if self.speed < 10:
            self.speed += 1

    def decreasespeed(self):
        if self.speed > 0:
            self.speed -= 1

    def boundary_check(self):
        if self.player.xcor() > 600 or self.player.xcor() < -600:
            self.player.right(180)

        if self.player.ycor() > 200 or self.player.ycor() < -300:
            self.player.right(180)
