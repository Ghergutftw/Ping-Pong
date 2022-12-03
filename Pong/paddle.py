from turtle import *

UP = 90
DOWN = 270
MOVING_DISTANCE = 20

class Paddle ( Turtle  ) :
    def __init__(self, x_position , y_position) :
        super ().__init__ ()
        self.color ( "white" )
        self.shape ( "square" )
        self.penup ()
        self.shapesize ( stretch_wid=5, stretch_len=1 )
        self.goto ( x_position, y_position )


    def go_up(self) :
         new_y = self.ycor () + MOVING_DISTANCE
         self.goto ( self.xcor (), new_y )

    def go_down(self) :
        new_y =self.ycor () - MOVING_DISTANCE
        self.goto ( self.xcor (), new_y )
