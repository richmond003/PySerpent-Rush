from turtle import Screen
from snake import Snake_Module
import time

# screen setup
playground = Screen()
playground.setup(width=600, height=500)
playground.bgcolor("black")
playground.title("PySerpent-Rush🐍")
playground.tracer(0)


# Player 1 object
player1 = Snake_Module()

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
    

playground.exitonclick()
playground.mainloop()
