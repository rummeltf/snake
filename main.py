from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=650)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
game_over = Turtle()

game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)
game_over.color("white")


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_pos()
        snake.extend()
        score.clear()
        score.score += 1
        score.write(arg=f"Score: {score.score}", move=False, align="center", font=('Times New Roman', 20, "normal"))
    
    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        game_over.write(arg="Game Over", move=False, align="center", font=('Times New Roman', 30, "normal"))

    # detect collision with self
    for segment in snake.segments:
        if snake.head.distance(segment) < 20:
            if snake.head.distance(segment) < 5:
                continue
            else:
                game_is_on = False
                game_over.write(arg="Game Over", move=False, align="center", font=('Times New Roman', 30, "normal"))

screen.exitonclick()
