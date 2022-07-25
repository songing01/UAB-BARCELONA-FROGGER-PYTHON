from tkinter import *
import time
import keyboard

tk =Tk()
w=Canvas(tk,width=800,height=400)
w.pack()

x=50
frog_x=400
frog_y=300
frog_width=30
frog_height=30

while True:
  x+=1
  w.delete("all")
  w.create_rectangle(x,50,x+50,100)
  if keyboard.is_pressed("up arrow"):
      frog_y -=5
  if keyboard.is_pressed("left arrow"):
      frog_x -=5
  if keyboard.is_pressed("right arrow"):
      frog_x +=5

  w.create_rectangle(frog_x,frog_y,frog_x+frog_width,frog_y+frog_height,fill="green")
  w.update() #paints on the screen
  time.sleep(50/1000)