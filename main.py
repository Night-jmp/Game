#!/usr/bin/python

# Turtle Graphics Game
import turtle
import math
import random
import createScreen
import createPlayer
import createGoals

#Variables
player1pen = turtle.Turtle()
player1pen.pencolor("white")
player1pen.penup()
player1pen.hideturtle()

player2pen = turtle.Turtle()
player2pen.pencolor("white")
player2pen.penup()
player2pen.hideturtle()

# Set up screen
wn = createScreen.createScreen()

# Create Player Turtle
player1 = createPlayer.createPlayer()

# Create a second player
player2 = createPlayer.createPlayer()

# Create goals
maxGoals = 6
goals = []

for count in range(maxGoals):
    goals.append(createGoals.createGoals("red"))

# Determine if there is a collision
def iscollision(t1, t2):
    d = math.sqrt(math.pow(t1.player.xcor() - t2.goal.xcor(), 2) + math.pow(t1.player.ycor() - t2.goal.ycor(), 2))

    if d < 20:
        return True
    else:
        return False


# Set keyboard bindings
turtle.listen()
turtle.onkey(player1.turnleft, "a")
turtle.onkey(player1.turnright, "d")
turtle.onkey(player1.increasespeed, "w")
turtle.onkey(player1.decreasespeed, "s")

turtle.onkey(player2.turnleft, "Left")
turtle.onkey(player2.turnright, "Right")
turtle.onkey(player2.increasespeed, "Up")
turtle.onkey(player2.decreasespeed, "Down")

# Game loop
while True:
    player1.player.forward(player1.speed)
    player2.player.forward(player2.speed)

    # Boundary checking
    player1.boundary_check()

    # Boundary checking
    player2.boundary_check()

    # Goal loop
    for count in range(maxGoals):
        goals[count].goal.forward(3)

#       # Boundary checking
        goals[count].boundary_check()

        # Collision Checking
        if iscollision(player1, goals[count]):
            goals[count].goal.setposition(random.randint(-590, 590), random.randint(-290, 190))
            goals[count].goal.right(random.randint(0, 360))
            player1.score += 1
            player1pen.undo()
            player1pen.setposition(-600, 210)
            scorestr = "Player 1 score: %s" %player1.score
            player1pen.write(scorestr, False, align="left", font=("Ariel", 14, "normal"))

        if iscollision(player2, goals[count]):
            goals[count].goal.setposition(random.randint(-590, 590), random.randint(-290, 190))
            goals[count].goal.right(random.randint(0, 360))
            player2.score += 1
            player2pen.undo()
            player2pen.setposition(500, 210)
            scorestr = "Player 2 score: %s" % player2.score
            player2pen.write(scorestr, False, align="left", font=("Ariel", 14, "normal"))

delay = raw_input("Press Enter To Continue...")
