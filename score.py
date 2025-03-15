from turtle import Turtle

class Score(Turtle):
    new_user = True
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.highscore = 0
        self.color("white")
        self.hideturtle() #hide turtle cursor
        self.show_score()
    
        
       
    def show_score(self):
        self.clear()
        self.penup()
        self.goto(-280, 230)

        if self.new_user:
            self.write(f"SCORE: {self.current_score}", False, align="left",  font=('Arial', 8, 'bold'))
        else:
            self.write(f"HIGH SCORE: {self.highscore}    SCORE {self.current_score}", False, align="left",  font=('Arial', 8, 'bold'))


    def increase_score(self):
          self.current_score += 1
          self.show_score()
    
    def check_highscore(self):
        if self.current_score > self.highscore:
              self.highscore = self.current_score
              self.current_score = 0
        else:
             self.current_score = 0
    
    def reset_score(self):
         pass
    
    def gameover(self):
          self.goto(0,0)
          self.write(f"{"GAME OVER":>16}.\nPress Space to Play Again", False, align="center", font=('Arial', 15, 'normal'))
    
  


# if __name__ == "__main__":
#     # read from file
#     with open('file.txt') as file:
#         content = file.read()
#         print(content)
    
#     # write to file
#     with open('file1.txt', mode='w') as file:
#          file.write("New content")

#     #append to file
#     with open('file2.txt', mode='a') as file:
#          file.write("\n New line")

