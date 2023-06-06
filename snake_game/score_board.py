from turtle import Turtle

with open('data.txt') as data:
    contents = data.read()


class Scoreboard(Turtle):
    
    def __init__(self) :
        super().__init__()
        self.score = 0
        self.highscore = int(contents)
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}, Highsore: {self.highscore}", align='center', font = ('Arial', 20, 'normal'))
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open('data.txt', mode='w') as data:
            data.write(str(self.highscore))
        self.score = 0
        self.update_score_board()
    
    def increase_score(self):
        self.score += 1
        self.update_score_board()

   

    
    