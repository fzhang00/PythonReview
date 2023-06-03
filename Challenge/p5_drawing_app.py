from p5 import *

pen = None


def setup():
    global pen
    size(100, 100)

    no_stroke()
    fill(255, 102)
    pen = Pen()

def draw():
    global pen
    background(0)
    pen.draw()
    pen.display()


class Pen:
    def __init__(self):
        self.pos=[]
        self.size=10
        self.color=(255, 255, 255)
    
    def draw(self):
        if mouse_is_pressed:
            self.pos.append((mouse_x, mouse_y))
        
    def display(self):
        for (x, y) in self.pos:
            ellipse(x, y, self.size, self.size)

if __name__ == '__main__':
    run()