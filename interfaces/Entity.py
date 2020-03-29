import numpy as np
from datastructure.SIR import *


class Entity(object):
    def __init__(self, canvas, radius, x = None, y = None):
        self.radius = radius
        self.canvas = canvas
        self.x = self.__getRandomIfNone__(x, canvas.winfo_width())
        self.y = self.__getRandomIfNone__(y, canvas.winfo_height())
        self.status = SIR.Susceptible
        self.body = self.__createBody__()
        self.daysSick = 0

    @staticmethod
    def __getRandomIfNone__(pos, maxValue):
        return pos if pos is not None else np.random.randint(0, maxValue)

    def __createBody__(self):
        return self.canvas.create_oval(self.x, self.y, self.x + self.radius, self.y + self.radius,
                                       outline = 'white', fill = self.status.value)

    def update(self, dx, dy, percentChanceOfInfection, radiusOfInfection, allEntities):
        self.__moveByAmount__(dx, dy)
        self.__infectNearbyEntities_(percentChanceOfInfection, radiusOfInfection, allEntities)

    def __moveByAmount__(self, dx, dy):
        self.x += dx
        self.y += dy
        ddx = self.__forceInsideCanvasBounds__(self.x, self.canvas.winfo_width())
        ddy = self.__forceInsideCanvasBounds__(self.y, self.canvas.winfo_height())
        self.x += ddx
        self.y += ddy
        self.canvas.move(self.body, dx + ddx, dy + ddy)

    def __forceInsideCanvasBounds__(self, pos, maxValue):
        if pos < 0:
            return -pos
        elif pos > maxValue - self.radius:
            return maxValue - pos - self.radius
        else:
            return 0

    def __infectNearbyEntities_(self, percentChanceOfInfection, radiusOfInfection, allEntities):
        if self.status is SIR.Infected:
            for entity in self.__getEntityWithInRadius__(radiusOfInfection, allEntities):
                if np.random.random() <= (percentChanceOfInfection / 100.0):
                    entity.status = SIR.Infected

    def __getEntityWithInRadius__(self, radius, entities):
        return [entity for entity in entities
                if (entity.status is SIR.Susceptible
                    and self.__withinEuclidDistance__(self.x, self.y, entity.x, entity.y, radius))]

    @staticmethod
    def __withinEuclidDistance__(x1, y1, x2, y2, radius):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) <= (radius ** 2)

    def __updateSickDays__(self, maximumDaysSick):
        if self.status is SIR.Infected:
            self.daysSick += 1
        if self.daysSick >= maximumDaysSick:
            self.status = SIR.Removed
