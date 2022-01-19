from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Times New Roman', 20, "normal"))
    
    def update_score(self):
        super().__init__()
