from tkinter import *
import time
from tkinter.ttk import Separator
import keyboard
from Car import *
from Frog import *
from Lane import *

tk = Tk()
w = Canvas(tk, width=800, height=400)
w.pack()

start_x = 50
separator_x = 10
frog = Frog(400, 300, 30, 30)


# TODO:
# - Add a background color to a lane #444444
# - when a car reaches the last X of the lane, reposition it to the beginning of the lane ( Jest change the X of the car) : done
# - create 3 lanes and store them in a list( like before the list of cars) : done
# - move the class Lane to another file -> Lane.py
start_y = 50
separator_y = 10
lanes = [None]*3
for i in range(len(lanes)):
    lanes[i] = Lane(0, start_y+(50+separator_y) *
                    i, 800, 70, 5, speed=5, color="red")

while True:
    for lane in lanes:
        lane.moveVehicles()

    w.delete("all")

    for lane in lanes:
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
