from turtle import Screen
from player import Player
from ball import Ball
from statics import Static
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('green')
screen.setup(width=800, height=600)
screen.title('Football_game')

#Turn off animation for Player
screen.tracer(0)

#Create 2 players
r_player = Player((320,0), 'red')
l_player = Player((-320,0), 'blue')

#Create ball
ball = Ball()

# Create statics
field_line = Static()
field_line.draw_line()
field_circle = Static()
field_circle.draw_circle()
field_gate = Static()
field_gate.draw_r_gate()
field_gate.draw_l_gate()

#Create scoreboard
scoreboard = Scoreboard()


#Moving player
screen.listen()
screen.onkey(r_player.move_up, "Up")
screen.onkey(r_player.move_down, "Down")
screen.onkey(l_player.move_up, "w")
screen.onkey(l_player.move_down, "s")

#Turn off animation for Player
is_out = False
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)# to slow ball movement - stop for 0.1s iteration
    screen.update()
    
    ball.move() #method to move ball

#########################Bounce from wall####################################
    #Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() #method for ball to bounce from up and down wall in vertical position

#######################Player hits############################################
    #Detect collision with Player
    if ball.distance(r_player) < 50 and ball.xcor() > 290 or ball.distance(l_player) < 50 and ball.xcor() < -290: #and not or !!!!!
        ball.bounce_x() #method for ball to bounce from Player in horizontal position

######################Out section##############################

    #Detect R Player out
    if ball.xcor() > 380 and ball.ycor() > 130 or ball.xcor() > 380 and ball.ycor() < -130:
        ball.out() # in two if_statements for counting score
        scoreboard.l_point() #for changing score when r_player out - point for l_player
        game_is_on = False
        is_out = True

    #Detect R Player out
    if ball.xcor() < -380 and ball.ycor() > 130 or ball.xcor() > 380 and ball.ycor() < -130:
        ball.out() # in two if_statements for counting score
        scoreboard.r_point() #for changing score when r_player out - point for l_player
        game_is_on = False
        is_out = True

################Goal section########################################
    #Detect R Player goal
    if ball.xcor() > 380 and ball.ycor() < 130 and ball.ycor() > -130:
        ball.goal() # in two if_statements for counting score
        scoreboard.l_point() #for changing score when r_player out - point for l_player
        game_is_on = False

    #Detect L Player goal
    if ball.xcor() < -380 and ball.ycor() < 130 and ball.ycor() > -130:
        ball.goal() # in two if_statements for counting score
        scoreboard.r_point() #for changing score when r_player out - point for l_player
        game_is_on = False


# ###############Restart game#####################################
#     # Restart game
#     if is_out == True:
#         screen.onkey(ball.reset_position, "n")
#         game_is_on = True



screen.exitonclick()




