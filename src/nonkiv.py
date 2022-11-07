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

    #Updates ship location and direction data
    def updateShip(self):
        pass
        #check api call for ship location and bearing data
        #assign location on map based on coordinates given
        #gradient of ship determined by bearing
    

    def colourChoice(self):
        pass
        #check api call for ship type, e.g. cargo
        #assign colour of ship based on ship type
    
    def firstUpdate(self):
        updateShip()
        colourChoice()
        pass
