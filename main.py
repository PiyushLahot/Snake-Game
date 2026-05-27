from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SAAPN KA KHEL")
screen.tracer(0)
my_snake=Snake()
food=Food()
food1=Food()
score=Scoreboard()
screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(key="Down",fun=my_snake.down)
screen.onkey(key="Right",fun=my_snake.right)
screen.onkey(key="Left",fun=my_snake.left)

game_is_on = True
diamond_active = False
diamond_start_time = None
last_diamond_score = -1
food1.hide()

def game_loop():
    global game_is_on, diamond_active, diamond_start_time, last_diamond_score, score, food, food1, my_snake

    my_snake.move()

    if score.score % 10 == 0 and score.score > 0 and not diamond_active and score.score != last_diamond_score:
        diamond_active = True
        diamond_start_time = time.time()
        last_diamond_score = score.score
        food1.diamond()
        food1.refresh()

    if diamond_active:
        if time.time() - diamond_start_time > 5:
            diamond_active = False
            diamond_start_time = None
            food1.hide()

        elif my_snake.my_turtle[0].distance(food1) < 15:
            food1.hide()
            my_snake.extend()
            score.score += 2
            score.destruct()
            diamond_active = False
            diamond_start_time = None
            food.refresh()

    if my_snake.my_turtle[0].distance(food) < 15:
        food.refresh()
        my_snake.extend()
        score.score += 1
        score.destruct()
        food1.hide()
        diamond_active = False
        diamond_start_time = None

    # Wall collision
    if (my_snake.my_turtle[0].xcor() > 280 or my_snake.my_turtle[0].xcor() < -280
            or my_snake.my_turtle[0].ycor() < -280 or my_snake.my_turtle[0].ycor() > 280):
        score.reset_score()
        my_snake.outside()

    # Tail collision
    for turtle in my_snake.my_turtle[1:]:
        if my_snake.my_turtle[0].distance(turtle) < 6:
            score.reset_score()
            my_snake.outside()

    screen.update()
    screen.ontimer(game_loop, 100)  # ← 100ms but doesn't block keys

screen.ontimer(game_loop, 100)  # ← start the loop
screen.mainloop()