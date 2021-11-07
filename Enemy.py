from settings import *
class Enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def main(self, display):
        pygame.draw.rect(display, (0, 0, 0), (self.x-display_scroll[0], self.y-display_scroll[1], self.width, self.height))