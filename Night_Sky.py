import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Randomly Filled Stars")

# Create a Turtle instance
t1 = turtle.Turtle()
# t2 = turtle.Turtle()
t1.speed(0)  # Fastest drawing speed
# t2.speed(0)
t1.color("white")
# t2.color("white")


# Function to draw a star
def draw_star(turtle, size):

    for _ in range(10):
        t1.hideturtle()
        turtle.circle(size)  # Move forward by the given size


# Draw random stars on the screen within the specified range
for _ in range(10000):  # You can adjust the number of stars
    # Generate random coordinates within the specified range
    x = random.randint(-370, 370)
    y = random.randint(-350, 350)

    size1 = (random.randint(10, 20))/30  # Adjust the size range of stars

    t1.penup()  # Lift the pen to move without drawing
    t1.goto(x, y)  # Move the turtle to the random position
    t1.pendown()  # Lower the pen to start drawing
    t1.fillcolor("white")  # Set fill color to white
    t1.begin_fill()  # Begin filling the shape
    draw_star(t1, size1)  # Call the draw_star function with the chosen size
    t1.end_fill()  # End filling the shape

# for _ in range(10000):  # You can adjust the number of stars
#     # Generate random coordinates within the specified range
#     x1 = random.randint(-400, 400)
#     y1 = random.randint(-400, 400)
#
#     size2 = (random.randint(10, 40))/20  # Adjust the size range of stars
#
#     t1.penup()  # Lift the pen to move without drawing
#     t1.goto(x1, y1)  # Move the turtle to the random position
#     t1.pendown()  # Lower the pen to start drawing
#     t1.fillcolor("white")  # Set fill color to white
#     t1.begin_fill()  # Begin filling the shape
#     draw_star(t1, size2)  # Call the draw_star function with the chosen size
#     t1.end_fill()  # End filling the shape

# Close the turtle graphics window when clicked
screen.exitonclick()