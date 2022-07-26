from tkinter import *
import time
from tkinter.ttk import Separator
import keyboard


class Frog:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def paint(self, w):
        w.create_rectangle(self.x, self.y, self.x+self.width,
                           self.y+self.height, fill="green")


class Car:
    def __init__(self, x, y, w, h, speed=1, color=""):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.speed = speed
        self.color = color

    def move(self):
        self.x += self.speed
       # if self.x > 800:
        #    self.x = 50

    def paint(self, w):
        w.create_rectangle(self.x, self.y, self.x +
                           self.width, self.y+self.height, fill=self.color)
        w.create_line(self.x+self.width*0.75, self.y, self.x +
                      self.width*0.75, self.y+self.height)


tk = Tk()
w = Canvas(tk, width=800, height=400)
w.pack()

start_x = 50
separator_x = 10
frog = Frog(400, 300, 30, 30)
cars = [None]*3
for i in range(len(cars)):
    cars[i] = Car(start_x-(50+separator_x)*i, 50, 50, 30, 3, color="red")


while True:
    for car in cars:
        car.move()

    w.delete("all")

    for car in cars:
        car.paint(w)

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
