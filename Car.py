class Car:
    def __init__(self, x, y, w, h, speed=1, color=""):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.speed = speed
        self.color = color

    def move(self):
        self.x += self.speed
       # if self.x > 800:
        #    self.x = 50

    def paint(self, w):
        w.create_rectangle(self.x, self.y, self.x +
                           self.width, self.y+self.height, fill=self.color)
        w.create_line(self.x+self.width*0.75, self.y, self.x +
                      self.width*0.75, self.y+self.height)
