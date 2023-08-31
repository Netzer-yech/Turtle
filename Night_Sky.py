import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Randomly Filled Stars")

# Create a Turtle instance
t1 = turtle.Turtle()
t1.hideturtle()
t1.speed(0)  # Fastest drawing speed
t1.color("white")

# t2 = turtle.Turtle()
# t2.speed(0)
# t2.color("white")
#
# t3 = turtle.Turtle()
# t3.speed(0)
# t3.color("white")
#
# t4 = turtle.Turtle()
# t4.speed(0)
# t4.color("white")


# Function to draw a star
def draw_star(turtle, size):

    for _ in range(10):
        turtle.hideturtle()
        turtle.circle(size)


# Draw random stars on the screen within the specified range
for _ in range(10000):  # You can adjust the number of stars
    # Generate random coordinates within the specified range
    x1 = random.randint(-370, 370)
    y1 = random.randint(-350, 350)
    # x2 = random.randint(-370, 370)
    # y2 = random.randint(-350, 350)
    # x3 = random.randint(-370, 370)
    # y3 = random.randint(-350, 350)
    # x4 = random.randint(-370, 370)
    # y4 = random.randint(-350, 350)

    size1 = (random.randint(10, 20))/30  # Adjust the size range of stars
    # size2 = (random.randint(10, 20))/30  # Adjust the size range of stars
    # size3 = (random.randint(10, 20))/30  # Adjust the size range of stars
    # size4 = (random.randint(10, 20))/30  # Adjust the size range of stars


    t1.penup()  # Lift the pen to move without drawing
    t1.goto(x1, y1)  # Move the turtle to the random position
    t1.pendown()  # Lower the pen to start drawing
    t1.fillcolor("white")  # Set fill color to white
    t1.begin_fill()  # Begin filling the shape
    draw_star(t1, size1)  # Call the draw_star function with the chosen size
    t1.end_fill()  # End filling the shape
    # t2.penup()  # Lift the pen to move without drawing
    # t2.goto(x2, y2)  # Move the turtle to the random position
    # t2.pendown()  # Lower the pen to start drawing
    # t2.fillcolor("white")  # Set fill color to white
    # t2.begin_fill()  # Begin filling the shape
    # draw_star(t2, size2)  # Call the draw_star function with the chosen size
    # t2.end_fill()  # End filling the shape
    # t3.penup()  # Lift the pen to move without drawing
    # t3.goto(x3, y3)  # Move the turtle to the random position
    # t3.pendown()  # Lower the pen to start drawing
    # t3.fillcolor("white")  # Set fill color to white
    # t3.begin_fill()  # Begin filling the shape
    # draw_star(t3, size3)  # Call the draw_star function with the chosen size
    # t3.end_fill()  # End filling the shape
    # t4.penup()  # Lift the pen to move without drawing
    # t4.goto(x4, y4)  # Move the turtle to the random position
    # t4.pendown()  # Lower the pen to start drawing
    # t4.fillcolor("white")  # Set fill color to white
    # t4.begin_fill()  # Begin filling the shape
    # draw_star(t4, size4)  # Call the draw_star function with the chosen size
    # t4.end_fill()  # End filling the shape


# Close the turtle graphics window when clicked
screen.exitonclick()