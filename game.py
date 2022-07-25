from tkinter import *

tk =Tk()
w=Canvas(tk,width=800,height=400)
w.pack()
w.create_rectangle(50,50,100,100)
while True:
    w.update()