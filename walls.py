from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=10)
        self.color("white")
        self.speed("fastest")
        self.draw_walls()

    def draw_walls():
        pass