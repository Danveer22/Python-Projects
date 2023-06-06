import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title('Turtle-race')

screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, 'Up')

car_manager = CarManager()
score_board = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.crate_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.display_end()
            game_is_on = False
    
    if player.ycor() > 280:
        score_board.increase()
        player.reset()
        car_manager.speed_up()

screen.exitonclick()
