from turtle import Screen
from snake import Snake_Module
from food import Snake_food
from score import Score
import time


# screen setup
playground = Screen()
playground.setup(width=600, height=500)
playground.bgcolor("black")
playground.title("PySerpent-Rush🐍")
playground.tracer(0)

game_score = Score()

# Player 1 object
player1 = Snake_Module()
food = Snake_food()

# Game event handlers
playground.listen()
playground.onkey(player1.turn_right, "Right")
playground.onkey(player1.turn_left, "Left")
playground.onkey(player1.turn_up, "Up")
playground.onkey(player1.turn_down, "Down")

while True:
    playground.update()
    time.sleep(0.2)
    player1.move()


    #Detect food collsion
    if player1.head.distance(food) < 10:
        food.random_refresh()
        game_score.increase_score()

playground.exitonclick()
playground.mainloop()
