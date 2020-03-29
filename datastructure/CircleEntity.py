from interfaces.Entity import Entity


class CircleEntity(Entity):
    def __init__(self, canvas, radius, x = None, y = None):
        super(CircleEntity, self).__init__(canvas, radius, x, y)