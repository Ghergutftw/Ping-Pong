import time
from ball import *
from paddle import *
from scoreboard import *

with open('art_pong.txt', 'r') as f:
    for line in f:
        print(line.rstrip())


screen = Screen()
screen.setup(height=600 , width=800)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350 , 0)
l_paddle = Paddle(-350 , 0)
ball = Ball()
score = 0
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_the_ball()
        scoreboard.l_point()

    #Detect L paddle misses
    if ball.xcor () < -380 :
        ball.reset_the_ball ()
        scoreboard.r_point()


screen.exitonclick()