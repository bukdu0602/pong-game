from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y = self.y * -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x = self.x * -1
        self.move_speed *= 0.9

    def lose(self):
        self.home()
        self.x *= -1
        self.move_speed = 0.1

