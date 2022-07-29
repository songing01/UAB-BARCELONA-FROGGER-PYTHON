from tkinter import *
from PIL import ImageTk, Image, ImageOps


class Car:
    def __init__(self, x, y, w, h, speed=1, color=""):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.speed = speed
        self.color = color
        if self.color == "yellow":
            photo = Image.open("yellowCar.png")
            photo = photo.resize((self.width, self.height), Image.ANTIALIAS)
            if speed < 0:
                photo = ImageOps.mirror(photo)
        elif self.color == "red":
            photo = Image.open("redCar.png")
            photo = photo.resize((self.width, self.height), Image.ANTIALIAS)
            if speed < 0:
                photo = ImageOps.mirror(photo)
        elif self.color == "green":
            photo = Image.open("greenCar.png")
            photo = photo.resize((self.width, self.height), Image.ANTIALIAS)
            if speed < 0:
                photo = ImageOps.mirror(photo)

        self.img = ImageTk.PhotoImage(photo)

    def move(self):
        if self.speed >= 0:
            self.x += self.speed
            if self.x > 800:
                self.x = -70
        else:
            self.x += self.speed
            if self.x < -70:
                self.x = 800

    def paint(self, w):
        w.create_image(self.x+self.width/2, self.y +
                       self.height/2, image=self.img)
