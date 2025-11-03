from pico2d import *
import game_world
import game_framework
import random

PIXEL_PER_METER = (1.0 / 0.03) # 1pixel = 3cm, 1m = 33.33 pixel

class Bird:
    image = None
    def __init__(self, x = 400, y = 300):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0

    def draw(self):

    def update(self):


