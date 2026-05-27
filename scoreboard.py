from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore =self.file_manage_r()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-180, 260)
        self.destruct()
    def diamond_score(self):
        self.destruct()
    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.file_manage_w(str(self.highscore))
        self.score = 0
        self.destruct()
    def destruct(self):
        self.clear()
        self.write(arg=f"Scoreboard:{self.score} | HighScore : {self.highscore}" , font=("Arial", 24, "normal"))
    def end(self):
        self.home()
        self.write(arg=f"GAME OVER", font=("Arial", 50, "bold"), align="center")

    def file_manage_r(self):
        with open("data.txt", "r") as f:
            a = f.read()
            return int(a)
    def file_manage_w(self,text):
        with open("data.txt", "w") as f:
             f.write(text)





