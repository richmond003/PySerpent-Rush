from turtle import Screen
from snake import Snake_Module
import time

playground = Screen()
playground.setup(width=600, height=500)
playground.bgcolor("black")
playground.title("PySerpent-Rush🐍")
playground.tracer(0)


player1 = Snake_Module()

player1.snake_body()

while True:
    playground.update()
    time.sleep(0.1)
    player1.move()
    break

playground.exitonclick()
playground.mainloop()
