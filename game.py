from tkinter import *
import time
from tkinter.ttk import Separator
import keyboard
from Car import *
from Frog import *
from Lane import *
# TODO: When frog reaches to of the screen, display a record on top-right, calculated from 100-time needed to reach the top of the screen
# In case the seepd parameter of the lane is negative,
# cars should move from right to left.Make the appropiate changes(small number) in order to make the cars moving left- right,
#  detect when cars reach the left side of the screen ( reposition) and draw the cars so the vertical line is on the left side of the car

tk = Tk()
w = Canvas(tk, width=800, height=400)
w.pack()

start_x = 50
separator_x = 10
frog = Frog(400, 300, 30, 30)

start_y = 50
separator_y = 20
lanes = [None]*3
numOfCars = [4, 6, 8]
speeds = [-5, 4, 3]
colors = ["red", "blue", "yellow"]
separator_x = [100, 70, 50]
for i in range(len(lanes)):
    lanes[i] = Lane(0, start_y+(50+separator_y) *
                    i, 800, 70,  numOfCars[i], speed=speeds[i], color=colors[i], separator_x=separator_x[i])

t0 = time.time()
isFinished = False
while True:
    if not isFinished:
        for lane in lanes:
            lane.moveVehicles()

        w.delete("all")
        t = time.time()-t0
        w.create_text(30, 20, text=str(int(t*100)/100),
                      font=("bold", 15))

        for lane in lanes:
            lane.paint(w)

        if keyboard.is_pressed("up arrow"):
            if frog.y-5 > 0:
                frog.y -= 5
            else:
                print("Top reached")
                t = time.time()-t0
                isFinished = True
                w.create_text(
                    700, 30, text=f"record: {str(100 - int(t*100)/100)}", font=("bold", 20), fill="red")
                # w.create_text(
                #    400, 200, text="press 'enter' on your keboard to restart", font=("bold", 20))
                # if keyboard.is_pressed("enter"):
                #    isFinished = False

        if keyboard.is_pressed("left arrow"):
            if frog.x - 5 > 0:
                frog.x -= 5
        if keyboard.is_pressed("right arrow"):
            if frog.x+5 <= 770:
                frog.x += 5

    frog.paint(w)

    w.update()
    time.sleep(50/1000)
