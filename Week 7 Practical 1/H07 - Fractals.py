import turtle

trtl = turtle.Turtle()

def korch_curve(turtle, length, degree):
    if degree == 0:
    #turtle must draw a segment of size length
        turtle.forward(length)
    else:
        length = length / 3
        degree = degree-1

        korch_curve(turtle, length, degree) # First segment
        turtle.left(60)
        korch_curve(turtle, length, degree) # Second segment
        turtle.right(120)
        korch_curve(turtle, length, degree) # Third segment
        turtle.left(60)
        korch_curve(turtle, length, degree) # Fourth segment

korch_curve(trtl, 5000, 5)
