from turtle import Turtle

class Snake_Module:
    #snake constants
    UP = 90
    DOWN = 270
    RIGHT = 0
    LEFT = 180
    MOVE_DISTANCE = 20

    def __init__(self):
        self.serpent = []
        self.cordinates = [(0,0), (-20, 0), (-40, 0), (-60, 0)]
        self.colors = ["red", "yellow", "green", "white"]
        self.color_index = 0 
        self.create_snake()
        self.head = self.serpent[0]
      
    def move(self):
        for seg in range(len(self.serpent) - 1, 0, -1):
            prev_xcor = self.serpent[seg - 1].xcor()
            prev_ycor = self.serpent[seg - 1].ycor()
            self.serpent[seg].goto(prev_xcor, prev_ycor)
        self.head.forward(self.MOVE_DISTANCE)
        
        

    def create_snake(self):
        """ 
            Create snake body
           """
        for pos in self.cordinates:
            snake_seg = Turtle(shape="square")
            snake_seg.color(self.colors[self.color_index])
            self.color_index += 1
            snake_seg.penup()
            snake_seg.goto(pos)
            self.serpent.append(snake_seg)
    
    def turn_right(self):
        """ 
         Turn snake right if snake is not heading left
           """
        if self.head.heading() != self.LEFT:
            self.head.setheading(0)

    def turn_left(self):
        """ 
         Turn snake left if snake is not heading right
           """
        if self.head.heading() != self.RIGHT:
            self.head.setheading(180)
    
    def turn_up(self):
        """ 
         Turn snake up if snake is not heading down
           """
        if self.head.heading() != self.DOWN:
            self.head.setheading(90)
    
    def turn_down(self):
        """ 
         Turn snake down if snake is not heading up
           """
        if self.head.heading() != self.UP:
            self.head.setheading(270)