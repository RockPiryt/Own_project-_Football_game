from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0 #Constans for player when he is created
        self.r_score = 0 #Constans for player when he is created
        self.update_scoreboard()#to show initial scoreboard 0-0
    
    def update_scoreboard(self):
        self.clear() #clear previous score before we update scoreboard
        self.goto(-100,200)
        self.write(self.l_score, align='center', font=('Courier', 50, 'normal'))
        self.goto(100,200)
        self.write(self.r_score, align='center', font=('Courier', 50, 'normal'))


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()#to update scoreboard - point for l_player

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()#to update scoreboard - point for r_player