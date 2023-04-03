from turtle import Turtle
from statics import Static

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)#Staring position, not for moving ball!!!
        self.x_move = 10 #distance for ball for one iteration of loop
        self.y_move = 10 
        self.move_speed = 0.05 # for time.sleep method 

    #Ball is moving - write in while loop this method
    def move(self):
        new_x = self.xcor() + self.x_move #move horizontal
        new_y = self.ycor() + self.y_move #move vertical
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 #Reverse direction  multiply by -1!!!
    
    def bounce_x(self):
        self.x_move *= -1 #Reverse direction  multiply by -1!!!
        self.move_speed *= 0.9 # lower number mean fast ball speed - time.sleep()

    def out(self):
        out_text = Static()
        out_text.out()

    def goal(self):
        goal_text = Static()
        goal_text.goal()

    def reset_position(self):
        screen.onkey(ball.reset_position, "n")
        self.game_is_on = True
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x() #change direction for ball in new game



