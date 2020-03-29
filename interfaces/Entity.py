import numpy as np
from datastructure.SIR import *

class Entity(object):
    def __init__(self, canvas, radius, x = None, y = None):
        self.radius = radius
        self.canvas = canvas
        self.x = self.getRandomIfNone(x, canvas.winfo_width())
        self.y = self.getRandomIfNone(y, canvas.winfo_height())
        self.status = SIR.Susceptible
        self.body = self.createBody()

    @staticmethod
    def getRandomIfNone(pos, maxValue):
        return pos if pos is not None else np.random.randint(0, maxValue)

    def createBody(self):
        return self.canvas.create_oval(self.x, self.y, self.x + self.radius, self.y + self.radius,
                                       outline = 'white', fill = self.status.value)

    def moveByAmount(self, dx, dy):
        self.x += dx
        self.y += dy
        ddx = self.forceInsideCanvasBounds(self.x, self.canvas.winfo_width())
        ddy = self.forceInsideCanvasBounds(self.y, self.canvas.winfo_height())
        self.x += ddx
        self.y += ddy
        self.canvas.move(self.body, dx + ddx, dy + ddy)

    def forceInsideCanvasBounds(self, pos, maxValue):
        if pos < 0:
            return -pos
        elif pos > maxValue - self.radius:
            return maxValue - pos - self.radius
        else:
            return 0
