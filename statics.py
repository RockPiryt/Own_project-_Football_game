from turtle import Turtle
FONT = ("Courier", 30, 'normal')

class Static(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')

    def out(self):
        self.write('OUT', move=False, align='center', font=FONT)
        self.hideturtle()
    
    def goal(self):
        self.write('GOAL', move=False, align='center', font=FONT)
        self.hideturtle()
    
    def draw_line(self):
        self.shape('square')
        self.shapesize(stretch_len=0.1, stretch_wid=50)
    
    def draw_circle(self):
        self.goto(0,-25)
        self.circle(50)
        self.hideturtle()

    def draw_r_gate(self):
        self.penup()
        self.goto(340,130)
        self.pendown()
        self.forward(40)
        self.right(90)
        self.forward(250)
        self.right(90)
        self.forward(40)
        self.hideturtle()

    def draw_l_gate(self):
        self.penup()
        self.goto(-340,-130)
        self.pendown()
        self.forward(40)
        self.right(90)
        self.forward(250)
        self.right(90)
        self.forward(40)
        self.hideturtle()