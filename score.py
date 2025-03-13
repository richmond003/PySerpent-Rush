from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.hideturtle() #hide turtle cursor
        self.show_score()
        
       
    def show_score(self):
             self.clear()
             self.penup()
             self.goto(-280, 230)
             self.write(f"SCORE: {self.current_score}", False, align="left",  font=('Arial', 8, 'bold'))

    def increase_score(self):
          self.current_score += 1
          self.show_score()
    
    def gameover(self):
          self.goto(0,0)
          self.write("GAME OVER.", False, align="center", font=('Arial', 15, 'normal'))