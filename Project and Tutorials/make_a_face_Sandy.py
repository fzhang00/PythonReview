from p5 import *

def setup():
    size('400','400')

def draw():
    background(214, 202, 253)
    # grid()
    width=400
    height=400
    ellipse((width/2, height/2), 200, 200)

run()