import time

class Ship():
    #Class properties defined
    gradient = 0.0
    x_pos = 0.0
    y_pos = 0.0

    def __init__(self, gradient, x_pos, y_pos):
        #initialise Ship object properties
        self.gradient = gradient
        self.x_pos = x_pos
        self.y_pos = y_pos

    #Updates ship location and gradient data
    def updateShip(self):
        pass

    def 