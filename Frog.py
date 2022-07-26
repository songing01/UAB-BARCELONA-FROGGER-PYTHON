from tkinter import *
from PIL import ImageTk, Image


class Frog:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        photo = Image.open("frog.png")
        photo = photo.resize((self.width, self.height), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(photo)

    def paint(self, w):
        w.create_image(self.x+self.width/2, self.y +
                       self.height/2, image=self.img)

    def crashes(self, car):
        if car.x <= self.x <= car.x+car.width and car.y <= self.y <= car.y+car.height:
            return True
        elif car.x <= self.x+self.width <= car.x+car.width and car.y <= self.y <= car.y+car.height:
            return True
        elif car.x <= self.x <= car.x + car.width and car.y <= self.y+self.height <= car.y+car.height:
            return True
        elif car.x <= self.x+self.width <= car.x+car.width and car.y <= self.y+self.height <= car.y+car.height:
            return True
        else:
            return False
