import turtle


def drawSquare(size, rapide):
    turtle.speed(rapide)
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def drawPentagone(size, speed, angle):
    turtle.speed(speed)
    for i in range(5):
        turtle.forward(size)
        turtle.left(angle)

# drawSquare(200, 5)

# turtle.clear()
# turtle.reset()

# drawPentagone(200, 5, 72)

# turtle.clear()
# turtle.reset()



turtle.right(45)
turtle.forward(280)
turtle.right(135)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.left(135)
turtle.forward(280)
turtle.left(135)
turtle.forward(200)

turtle.penup()
turtle.goto(0, -210)
turtle.pendown()

turtle.forward(200)
turtle.right(135)
turtle.forward(80)
turtle.right(45)
turtle.forward(280)
turtle.right(45)
turtle.forward(80)
turtle.right(135)
turtle.forward(200)

turtle.done()

