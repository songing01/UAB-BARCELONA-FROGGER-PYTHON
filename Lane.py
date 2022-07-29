from Car import *


class Lane:
    def __init__(self, x, y, w, h, numOfCars, color="", speed=1, start_x=70, separator_x=10):
        self.cars = [None]*numOfCars
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        car_y = y+h/2-40/2
        if speed < 0:
            start_x = 800
            for i in range(len(self.cars)):
                self.cars[i] = Car(start_x+(70+separator_x) *
                                   i, car_y, 70, 40, speed=speed, color=color)
        else:
            for i in range(len(self.cars)):
                self.cars[i] = Car(start_x-(50+separator_x) *
                                   i, car_y, 70, 40, speed=speed, color=color)

    def moveVehicles(self):
        for car in self.cars:
            car.move()

    def paint(self, w):
        w.create_rectangle(self.x, self.y, self.x+self.width,
                           self.y+self.height, fill="#A9A9A9")

        for car in self.cars:
            car.paint(w)
