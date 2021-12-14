from canvas import Canvas
from shapes import Square, Rectangle

# CLI Ask the user for the Canvas dimensions
canvas_width = int(input("Please enter the width of the canvas: "))
canvas_height = int(input("Please enter the height of the canvas: "))

# Create a dictionary of color codes and ask the user for a color
colors = {"white": [255, 255, 255], "black": [0, 0, 0]}
canvas_color = input("Choose a canvas color (white or black): ")

# Create a canvas with the user input
canvas = Canvas(width=canvas_width, height=canvas_height, color=colors[canvas_color])


while True:
    shape_type = input("What would you like to draw? Type quit to quit.")
#   if rectangle ask for rectangle data
    if shape_type.lower()== "rectangle":
        rect_x = int(input("Enter an x value for the rectangle: "))
        rect_y = int(input("Enter a y  value for the rectangle: "))
        rect_width = int(input("Enter the width of the rectangle: "))
        rect_height = int(input("Enter the height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green should the rectangle have? "))
        blue = int(input("How much blue should the rectangle have? "))
        # Create rectangle instance and draw
        rect = Rectangle(x=rect_x,  y=rect_y, width=rect_width, height=rect_height, color=[red, green, blue])
        rect.draw(canvas=canvas)

# if square ask user for square data
    if shape_type.lower()== "square":
        sq_x = int(input("Enter an x value for the square: "))
        sq_y = int(input("Enter a y value for the square: "))
        sq_side = int(input("Enter a side length for the square: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green should the rectangle have? "))
        blue = int(input("How much blue should the rectangle have? "))
#       Create square instance and draw
        sq = Square(x=sq_x, y=sq_y, side=sq_side, color=[red, green, blue])
        sq.draw(canvas=canvas)

    if shape_type.lower()== "quit":
        break

canvas.make("canvas.png")


