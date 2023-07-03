from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1.05

    def bounce2(self):
        self.x_move *= -1.05

    def reset_posn(self):
        self.goto(0, 0)
        self.bounce2()
