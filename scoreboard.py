from turtle import Turtle
SCORE_FONT = ('Times New Roman', 16, "normal")
GAME_OVER_FONT = ('Times New Roman', 30, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align="center", font=SCORE_FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
