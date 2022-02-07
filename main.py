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
        score.update_score()
    
    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
        score.update_score()

    # detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()
            score.update_score()




screen.exitonclick()
