from Tkinter import *
from analysis.Simulation import Simulation
from datastructure.CircleEntity import CircleEntity


class CanvasPlotter(object):
    def __init__(self):
        self.root = Tk()
        self.worldMap = Canvas(self.root, width = 600, height = 400)
        self.worldMap.pack()
        self.root.update()
        self.entities = []
        self.simulator = None

    def createEntities(self, n):
        for i in range(n):
            self.entities.append(CircleEntity(self.worldMap, 10))
        self.worldMap.pack()
        self.simulator = Simulation(self.entities)

    def startAnimation(self):
        self.root.after(0, self.animation)
        self.root.mainloop()

    def animation(self):
        while True:
            if self.simulator is None:
                print("Add entities first: self.createEntities(intNumberOfEntities)")
                break
            self.simulator.run()
            self.worldMap.update()


if __name__ == "__main__":
    plotter = CanvasPlotter()
    plotter.createEntities(300)
    plotter.startAnimation()
