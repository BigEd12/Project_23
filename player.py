from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("chartreuse4")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def forward(self):
        new_y = self.ycor() + 10
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def backward(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 10
            new_x = self.xcor()
            self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)

