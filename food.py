from turtle import Screen,Turtle
import random as rnd

screen = Screen()
DIAMOND = ((0, 20), (20, 0), (0, -20), (-20, 0))
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.refresh()
        self.apple()
    def apple(self):
        self.shape("circle")
        self.color("green")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def diamond(self):
        self.screen=Screen()
        self.screen.register_shape("diamond", DIAMOND)
        self.shape("diamond")
        self.penup()
        self.color("blue")
        self.speed("fastest")

    def hide(self):
        self.goto(1000,1000)

    def refresh(self):
        x_cor=rnd.randint(-280,280)
        y_cor= rnd.randint(-280,280)
        self.goto(x_cor,y_cor)



