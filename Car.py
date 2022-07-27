class Car:
    def __init__(self, x, y, w, h, speed=1, color=""):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.speed = speed
        self.color = color

    def move(self):
        if self.speed >= 0:
            self.x += self.speed
            if self.x > 800:
                self.x = -50
        else:
            self.x += self.speed
            if self.x < -50:
                self.x = 800

    def paint(self, w):
        w.create_rectangle(self.x, self.y, self.x +
                           self.width, self.y+self.height, fill=self.color)
        if self.speed >= 0:
            w.create_line(self.x+self.width*0.75, self.y, self.x +
                          self.width*0.75, self.y+self.height)
        else:
            w.create_line(self.x+self.width*0.25, self.y, self.x +
                          self.width*0.25, self.y+self.height)
