from turtle import Turtle

class Player(Turtle):

    def __init__(self, position, body_color):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color(body_color)
        self.penup()
        self.goto(position)

    #Move Player
    def move_up(self):
        new_y =  self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y =  self.ycor() - 20
        self.goto(self.xcor(), new_y)
