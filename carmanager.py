from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 1


class Carmanager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.setheading(180)
        rand_x = float(random.randrange(320, 880, 40))
        rand_y = float(random.randrange(-250, 280, 30))
        new_car.goto(rand_x, rand_y)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            if car.xcor() <= -320:
                rand_x = float(random.randrange(320, 880, 40))
                rand_y = float(random.randrange(-250, 280, 30))
                car.goto(rand_x, rand_y)
            car.forward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT

    def check_crash(self, player):
        for car in self.all_cars:
            if car.ycor() == int(player.ycor()) and car.distance(player) < 39 or player.ycor() == 0 and player.distance(
                    car) < 39 and 5 > car.ycor() > -5:
                return True


