from pico2d import *
import game_framework
import random

# Bird의 fly Speed 계산
pixels_per_meter = (10.0 / 0.3)  # 10 pixel 30 cm
fly_speed_kmph = 60  # Km / Hour 비둘기의 시속 반영 -> 60km/h
fly_speed_mpm = (fly_speed_kmph * 1000.0 / 60.0)
fly_speed_mps = (fly_speed_mpm / 60.0)
fly_speed_pps = (fly_speed_mps * pixels_per_meter) # 초당 픽셀 이동 거리 초속 17 ~ 22미터 정도

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    image = None

    def __init__(self):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = (random.randint(100, 1500),random.randint(100, 500))
        self.flip = ' '
        self.frame = 0.0

    def draw(self):
        idx = int(self.frame) % 5
        self.image.clip_composite_draw(
            idx * 180,  168 * 2,   # left, bottom
            180, 168,         # width, height
            0, self.flip,            # 회전 없음, 플립 없음
            self.x, self.y,   # 화면 중심
            pixels_per_meter / 3 * 2, pixels_per_meter / 3 * 2 # 날개 핀 크기 약 66cm 반영 -> 22~24 pixel
        )

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if self.flip == ' ':
            self.x += fly_speed_pps * game_framework.frame_time
        elif self.flip == 'h':
            self.x -= fly_speed_pps * game_framework.frame_time

        if self.x > 1500:
            self.flip = 'h'
        elif self.x < 100:
            self.flip = ' '