from tkinter import *
import time
from tkinter.ttk import Separator
import keyboard
from Car import *
from Frog import *


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


tk = Tk()
w = Canvas(tk, width=800, height=400)
w.pack()

start_x = 50
separator_x = 10
frog = Frog(400, 300, 30, 30)

lane = Lane(0, 50, 800, 70, 5, speed=5, color="red")
# TODO:
# - Add a background color to a lane
# - when a car reaches the last X of the lane, reposition it to the beginning of the lane ( Jest change the X of the car)
# - create 3 lanes and store them in a list( like before the list of cars)
# - move the class Lane to another file -> Lane.py

while True:
    lane.moveVehicles()

    w.delete("all")

    lane.paint(w)

    if keyboard.is_pressed("up arrow"):
        if frog.y-5 > 0:
            frog.y -= 5
        else:
            print("Top reached")
    if keyboard.is_pressed("left arrow"):
        if frog.x - 5 > 0:
            frog.x -= 5
    if keyboard.is_pressed("right arrow"):
        if frog.x+5 <= 770:
            frog.x += 5

    frog.paint(w)

    w.update()  # paints on the screen
    time.sleep(50/1000)
