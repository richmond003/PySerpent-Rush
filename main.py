from turtle import Turtle, Screen

playground = Screen()
playground.setup(width=600, height=500)
playground.bgcolor("black")
playground.title("PySerpent-Rush🐍")


serpent = Turtle(shape="square")
serpent.color("white")

playground.exitonclick()
playground.mainloop()