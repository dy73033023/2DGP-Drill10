from pico2d import *
import game_framework

PIXEL_PER_METER = (1.0 / 0.03) # 1pixel = 3cm, 1m = 33.33 pixel
flip = ' '

# Boy Run Speed
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
            idx * 180,  168 * 2,   # left, bottom (맨 윗줄)
            180, 168,         # width, height
            0, flip,            # 회전 없음, 플립 없음
            self.x, self.y,   # 화면 중심
            200, 200          # 출력 크기 (잘림 방지)
        )

    def update(self):
        global flip

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if self.x > 1400:
            self.x -= self.velocity
            flip = 'h'
        else:
            self.x += self.velocity