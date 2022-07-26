from Car import *


class Lane:
    def __init__(self, x, y, w, h, numOfCars, color="", speed=1, start_x=50, separator_x=10):
        self.cars = [None]*numOfCars
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        car_y = y+h/2-30/2
        for i in range(len(self.cars)):
            self.cars[i] = Car(start_x-(50+separator_x) *
                               i, car_y, 50, 30, speed=speed, color=color)

    def moveVehicles(self):
        for car in self.cars:
            car.move()

    def paint(self, w):
        for car in self.cars:
            car.paint(w)
