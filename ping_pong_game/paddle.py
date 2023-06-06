from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.goto(x_pos, y_pos)
        self.y_dir = 30
    
    def up(self):
        self.y_pos = self.ycor() + self.y_dir
        self.goto(self.xcor(), self.y_pos)
    
    def down(self):
         self.y_pos = self.ycor() - self.y_dir
         self.goto(self.xcor(), self.y_pos)
       
        
       
        
        

