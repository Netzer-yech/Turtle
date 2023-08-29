import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Randomly Filled Stars")

# Create a Turtle instance
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.color("white")

# Function to draw a star
def draw_star(turtle , size):

    for _ in range(5):
        turtle.forward(size)  # Move forward by the given size
        turtle.right(144)  # Turn right by 144 degrees


# Draw random stars on the screen within the specified range
for _ in range(10000):  # You can adjust the number of stars
    # Generate random coordinates within the specified range
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)

    size = (random.randint(10, 40))/20  # Adjust the size range of stars

    t.penup()  # Lift the pen to move without drawing
    t.goto(x, y)  # Move the turtle to the random position
    t.pendown()  # Lower the pen to start drawing
    t.fillcolor("white")  # Set fill color to white
    t.begin_fill()  # Begin filling the shape
    draw_star(t, size)  # Call the draw_star function with the chosen size
    t.end_fill()  # End filling the shape

# Close the turtle graphics window when clicked
screen.exitonclick()