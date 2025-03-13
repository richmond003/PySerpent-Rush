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

game_on = True
while game_on:
    playground.update()
    time.sleep(0.1)
    player1.move()

    #Detect food collision
    if player1.head.distance(food) < 15:
        food.random_refresh()
        game_score.increase_score()
        player1.grow_snake()

    # End game if wall collision is detected
    game_on = player1.detect_collision()
    
    if player1.tail_collsion() == False:
        break
    

game_score.gameover()

playground.mainloop()
