from turtle import Turtle

FONT=("Courier",24,"normal")

class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-200,250)
        self.write(f"level: {self.level}", align="center",font=FONT)

    def score_update(self):
        self.level+=1
        self.clear()
        self.write(f"level: {self.level}", align="center",font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center",font=FONT)

    
