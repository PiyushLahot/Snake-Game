# from turtle import Turtle
# CORD = [(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
# UP=90
# DOWN=270
# LEFT=180
# RIGHT=0
#
# class Snake:
#     def __init__(self):
#         self.my_turtle = []
#         self.create()
#
#     def create(self):
#         for pos in CORD:
#             self.add_segment(pos)
#
#     def add_segment(self,pos):
#         lex = Turtle()
#         lex.shape("square")
#         lex.color("white")
#         lex.penup()
#         lex.goto(pos)
#         self.my_turtle.append(lex)
#
#     def extend(self):
#         self.add_segment(self.my_turtle[-1].position())
#     def move(self):
#         for turtle in range(len(self.my_turtle) - 1, 0, -1):
#             x_cor=self.my_turtle[turtle-1].xcor()
#             y_cor=self.my_turtle[turtle-1].ycor()
#             self.my_turtle[turtle].goto(x_cor,y_cor)
#         self.my_turtle[0].forward(MOVE_DISTANCE)
#
#     def up(self):
#         if self.my_turtle[0].heading() != DOWN:
#             self.my_turtle[0].setheading(UP)
#     def down(self):
#         if self.my_turtle[0].heading() != UP:
#             self.my_turtle[0].setheading(DOWN)
#     def left(self):
#         if self.my_turtle[0].heading() != RIGHT:
#             self.my_turtle[0].setheading(LEFT)
#     def right(self):
#         if self.my_turtle[0].heading() != LEFT:
#             self.my_turtle[0].setheading(RIGHT)

# snake.py
from turtle import Turtle

CORD = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.my_turtle = []
        self.pending_heading = RIGHT  # ← track buffered direction
        self.create()

    def create(self):
        for pos in CORD:
            self.add_segment(pos)

    def add_segment(self, pos):
        lex = Turtle()
        lex.shape("square")
        lex.color("white")
        lex.penup()
        lex.goto(pos)
        self.my_turtle.append(lex)

    def extend(self):
        self.add_segment(self.my_turtle[-1].position())

    def move(self):
        # Apply the buffered heading ONCE per tick, right before moving
        self.my_turtle[0].setheading(self.pending_heading)

        for turtle in range(len(self.my_turtle) - 1, 0, -1):
            x_cor = self.my_turtle[turtle - 1].xcor()
            y_cor = self.my_turtle[turtle - 1].ycor()
            self.my_turtle[turtle].goto(x_cor, y_cor)
        self.my_turtle[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.my_turtle[0].heading() != DOWN:
            self.pending_heading = UP

    def down(self):
        if self.my_turtle[0].heading() != UP:
            self.pending_heading = DOWN

    def left(self):
        if self.my_turtle[0].heading() != RIGHT:
            self.pending_heading = LEFT

    def right(self):
        if self.my_turtle[0].heading() != LEFT:
            self.pending_heading = RIGHT
    def outside(self):
        for turtle in self.my_turtle:
            turtle.goto(1000, 1000)
        self.my_turtle.clear()
        self.pending_heading = RIGHT
        self.create()