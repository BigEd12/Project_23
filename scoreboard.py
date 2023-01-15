from turtle import Turtle, Screen
FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 20, "bold")
screen = Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-270, 255)
        self.write(f"Level: {self.level}", font=FONT)


    def level_up(self):
        self.clear()
        self.level += 1
        self.penup()
        self.goto(-270, 255)
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(-80, -10)
        self.write(f"Game Over\nFinal level: {self.level}", font=GAME_OVER_FONT)
