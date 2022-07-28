from tkinter import *
import time
import keyboard

from Car import *
from Frog import *
from Lane import *


WIDTH = 800
HEIGHT = 400

tk = Tk()
w = Canvas(tk, width=WIDTH, height=HEIGHT)
w.pack()

start_x = 50
separator_x = 10
frog = Frog(WIDTH/2, HEIGHT-100, 30, 30)

start_y = 50
separator_y = 20
lanes = [None]*3
numOfCars = [4, 6, 8]
speeds = [-5, 4, 3]
colors = ["red", "blue", "yellow"]
separator_x = [100, 70, 50]
for i in range(len(lanes)):
    lanes[i] = Lane(0, start_y+(50+separator_y) *
                    i, WIDTH, 70,  numOfCars[i], speed=speeds[i], color=colors[i], separator_x=separator_x[i])

t0 = time.time()
isFinished = False

while True:
    if not isFinished:
        for lane in lanes:
            lane.moveVehicles()

        if keyboard.is_pressed("up arrow"):
            if frog.y-5 > 0:
                frog.y -= 5
            else:
                print("Top reached")
                t = time.time()-t0
                reachedTime = int(t*100)/100
                score = 100 - int(t*100)/100
                isFinished = True

        if keyboard.is_pressed("left arrow"):
            if frog.x - 5 > 0:
                frog.x -= 5
        if keyboard.is_pressed("right arrow"):
            if frog.x+5 <= 770:
                frog.x += 5
    for lane in lanes:
        for car in lane.cars:
            if frog.crashes(car):
                isFinished = True
                score = 0

    w.delete("all")

    t = time.time()-t0
    if not isFinished:
        w.create_text(30, 20, text=str(int(t*100)/100),
                      font=("bold", 15))
    else:
        w.create_text(30, 20, text=str(reachedTime),
                      font=("bold", 15))

    for lane in lanes:
        lane.paint(w)

    frog.paint(w)
    if isFinished:
        if score > 0:
            w.create_text(
                700, 30, text=f"record: {str(score)}", font=("bold", 20), fill="red")
        else:
            w.create_text(
                400, 200, text="press 'enter' on your keboard to restart", font=("bold", 20))
            w.create_text(WIDTH/2, HEIGHT/2, fill="white",
                          text=f"YOU LOOSE!!!!")

    if keyboard.is_pressed("enter"):
        print("pressed")
        isFinished = False
        w.update()
        continue

    w.update()
    time.sleep(50/1000)
