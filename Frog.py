class Frog:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
    #self.img = PhotoImage(file="frog.jpg")

    def paint(self, w):
        w.create_rectangle(self.x, self.y, self.x+self.width,
                           self.y+self.height, fill="green")
        #w.create_image(self.x,self.y, image=self.img)

    def crashes(self, car):
        if car.x <= self.x <= car.x+car.width and car.y <= self.y <= car.y+car.height:
            return True
        elif car.x <= self.x+self.width <= car.x+car.width and car.y <= self.y <= car.y+car.height:
            return True
        elif car.x <= self.x <= car.x + car.width and car.y <= self.y+self.height <= car.y+car.height:
            return True
        elif car.x <= self.x <= car.x+car.width and car.y <= self.y+self.height <= car.y+car.height:
            return True
        else:
            return False
