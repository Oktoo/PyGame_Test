from settings import *

class Player_Fight:
    def __init__(self, x, y, width, height, name, image):
        self.type = "player"
        self.alive = True
        self.name = name
        self.image = image
        self.x = x
        self.y = y - (height-32)
        self.xx = x/grid_size
        self.yy = y/grid_size
        self. width = width
        self.height = height
        self.health = 100
        self.attack = 20
        self.maxmove = 5
        self.move = self.maxmove
        self.tura = 0
        self.pos = [0, 0]
        self.maxenergy = 2
        self.energy = self.maxenergy

    def main(self, display):
        #pygame.draw.rect(display, (25, 220, 0), (self.x + P_scroll[0], self.y - P_scroll[1] , self.width, self.height))
        display.blit(self.image, (self.x + self.pos[0], self.y + self.pos[1]))

class Enemy_Fight:
    def __init__(self, x, y, width, height, IMAGE, name):
        self.type = "enemy"
        self.alive = True
        self.name = name
        self.image = IMAGE
        self.xx = x/grid_size
        self.yy = y/grid_size
        self.x = x
        self.y = y - (height-32)
        self. width = width
        self.height = height
        self.health = 100
        self.attack = 20
        self.pos = [0, 0]
        self.tura = 0
        self.maxmove = 2
        self.move = self.maxmove
        self.maxenergy = 2
        self.energy = self.maxenergy

    def main(self, display):
        display.blit(self.image, (self.x+self.pos[0], self.y+self.pos[1]))


class Wall_Fight(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y - (height-32)
        self.width = width
        self.height = height
        self.pos = [0, 0]

    def main(self, display):
        pygame.draw.rect(display, (0, 0, 0), (self.x, self.y, self.width, self.height))

class Cel:
    def __init__(self, x, y, IMAGE):
        self.image = IMAGE
        self.x = x
        self.y = y
        self.pos = [0, 0]

    def main(self, display):
        display.blit(self.image, (self.x, self.y))

