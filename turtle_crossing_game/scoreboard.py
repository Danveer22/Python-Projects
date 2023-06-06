from turtle import Turtle
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 260
        self.score = 0
        self.score_board()
   
    def score_board(self):
        self.hideturtle()
        self.penup()
        self.goto(self.x, self.y)
        self.write(arg = f"score-{self.score}",align = 'center',  font = FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.score_board()

    def display_end(self):
        self.goto(0, 0)
        self.write(arg = 'Game-Over', align='center', font= FONT)