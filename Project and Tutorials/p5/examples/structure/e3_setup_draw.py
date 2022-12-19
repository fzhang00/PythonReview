from p5 import *

y = 0
# The statement in setup() function
# ececute once when the program begins
def setup():
    global y
    size(640, 360) # size must be the first statement'
    stroke(255) # Set line drawing color to white
    y = 0

# The statements in draw() are executed until the
# program is stopped. Each statement is executed in
# sequence and after the last line is read, the first
# line is executed again.
def draw():
    global y
    background(0) # Clear the screen with a black background
    y = y - 1
    if y < 0:
        y = height
    line((0, y), (width, y))


if __name__ == '__main__':
    run()