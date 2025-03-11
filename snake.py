from turtle import Turtle

class Snake_Module:
    def __init__(self):
        self.serpent = []
        self.cordinates = [(0,0), (-20, 0), (-40, 0), (-60, 0)]
        self.colors = ["red", "yellow", "green", "white"]
        self.color_index = 0 

    def move(self):
        for seg in range(len(self.serpent) - 1, 0, -1):
            prev_xcor = self.serpent[seg - 1].xcor()
            prev_ycor = self.serpent[seg - 1].ycor()
            self.serpent[seg].goto(prev_xcor, prev_ycor)
        self.serpent[0].forward(20)
        self.serpent[0].right(80)

    def snake_body(self):
        for pos in self.cordinates:
            snake_seg = Turtle(shape="square")
            snake_seg.color(self.colors[self.color_index])
            self.color_index += 1
            snake_seg.penup()
            snake_seg.goto(pos)
            self.serpent.append(snake_seg)