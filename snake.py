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
        self.create_snake()
        self.head = self.serpent[0]
        self.head.color("red")
      
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
            # snake_seg = Turtle(shape="square")
            # snake_seg.color("white")
            # snake_seg.penup()
            # snake_seg.goto(pos)
            # self.serpent.append(snake_seg)
            self._add_segment(pos)

    def _add_segment(self, pos):
        """ 
         Add new segment 
           """

        snake_seg = Turtle(shape="square")
        snake_seg.color("white")
        snake_seg.penup()
        snake_seg.goto(pos)
        self.serpent.append(snake_seg)

    def grow_snake(self):
        """ Grow snake length """
        print(self.serpent[-1].position())
        self._add_segment(self.serpent[-1].position())
        

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
    
    def detect_collision(self):
        """ 
        Detect if snake head has contact with gamee wall 
         """
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 250 or self.head.ycor() < -250:
            return False
        else:
            return True
    
    def tail_collsion(self):
        """ 
            Detect collision with wall 
         """
        
        for seg in self.serpent:
            if seg == self.head:
                pass
            elif self.head.distance(seg) < 10:
                print(self.head.distance(seg))
                return False
            else:
                return True