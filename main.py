from turtle import Screen
from snake import Snake_Module
from food import Snake_food
from score import Score
import time

# Screen setup
playground = Screen()
playground.setup(width=600, height=500)
playground.bgcolor("black")
playground.title("PySerpent-Rush🐍")
playground.tracer(0)

# Initialize game objects
game_score = Score()
player1 = Snake_Module()
food = Snake_food()

restart = False

def play_again():
    """Sets the restart flag to True when the space key is pressed."""
    global restart
    restart = True

# Game event handlers
playground.listen()
playground.onkey(player1.turn_right, "Right")
playground.onkey(player1.turn_left, "Left")
playground.onkey(player1.turn_up, "Up")
playground.onkey(player1.turn_down, "Down")
playground.onkey(play_again, "space")  # Space key to restart the game

# Main game loop
while True:
    game_on = True
    while game_on:
        playground.update()
        time.sleep(0.1)
        player1.move()

        # Detect food collision
        if player1.head.distance(food) < 15:
            food.random_refresh()
            game_score.increase_score()
            player1.grow_snake()

        # Detect collision with wall or tail
        if player1.detect_collision() or player1.tail_collsion():
            game_on = False

    # Game over handling
    game_score.gameover()
    game_score.new_user = False

    # Check high score
    game_score.check_highscore()

    # Wait for the player to press space to restart
    print("Press SPACE to restart...")
    restart = False
    while not restart:
        playground.update()  # Keeps the screen responsive

    # Reset the game state
    player1.reset_snake()
    game_score.show_score()
