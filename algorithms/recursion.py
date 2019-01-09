"""
Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems
until you get to a small enough problem that it can be solved trivially. Usually recursion involves a function calling
itself. While it may not seem like much on the surface, recursion allows us to write elegant solutions to problems that
may otherwise be very difficult to program.

laws of recursion
- A recursive algorithm must have a base case.
- A recursive algorithm must change its state and move toward the base case.
- A recursive algorithm must call itself, recursively.
"""

import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()


def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


draw_spiral(my_turtle, 200)
my_win.exitonclick()

