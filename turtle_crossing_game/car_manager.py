import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.speed_increment = MOVE_INCREMENT
        
    def crate_car(self):  
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            self.car = Turtle('square')
            self.car.penup()
            self.car.shapesize(1, 2)
            self.car.color(random.choice(COLORS))
            self.x_position = 300
            self.y_position = random.randint(-250, 250)
            self.car.goto(self.x_position, self.y_position)
            self.all_cars.append(self.car)

    def move_cars(self):
        for self.car in self.all_cars:
            self.car.setheading(180)
            self.car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += self.speed_increment
        
        

   



 


