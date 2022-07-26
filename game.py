from tkinter import *
import time
from tkinter.ttk import Separator
import keyboard
from Car import *
from Frog import *

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
