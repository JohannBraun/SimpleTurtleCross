from turtle import Screen
import time
from carmanager import Carmanager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")

NUMBER_OF_CARS = 30
carmanager = Carmanager()
for i in range(NUMBER_OF_CARS):
    carmanager.create_car()

scoreboard = Scoreboard()
scoreboard.refresh(player)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    carmanager.move()
    if carmanager.check_crash(player):
        scoreboard.you_lose(player)
        game_is_on = False
    if player.check_win():
        carmanager.speed_up()
        player.score += 1
        scoreboard.refresh(player)
screen.exitonclick()