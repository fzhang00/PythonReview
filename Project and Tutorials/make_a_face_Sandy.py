from p5 import *

def setup():
    size('400','400')

def draw():
    background(214, 202, 253)
    # grid()
    width=400
    height=400
    ellipse((width/2, height/2), 200, 200)
    stroke(0)
    fill(255, 226, 208)
    fill(0, 0, 0)
    eye_size = 50
    ellipse((160, 180), eye_size, eye_size)
    ellipse((240, 180), eye_size, eye_size)

run()