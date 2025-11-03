from pico2d import *
import game_framework
import random

PIXEL_PER_METER = (1.0 / 0.03) # 1pixel = 3cm, 1m = 33.33 pixel
flip = ' '

# Bird fly Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    image = None

    def __init__(self, x=400, y=300, velocity = 1):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0.0

    def draw(self):
        idx = int(self.frame) % 5
        self.image.clip_composite_draw(
            idx * 180,  168 * 2,   # left, bottom
            180, 168,         # width, height
            0, flip,            # 회전 없음, 플립 없음
            self.x, self.y,   # 화면 중심
            PIXEL_PER_METER / 3 * 2, PIXEL_PER_METER / 3 * 2 # 비둘기 크기 66cm -> 22~24 pixel
        )

    def update(self):
        global flip

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if flip == ' ':
            self.x += self.velocity
        elif flip == 'h':
            self.x -= self.velocity

        if self.x > 1500:
            flip = 'h'
        elif self.x < 100:
            flip = ' '