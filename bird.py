from pico2d import load_image, get_time, load_font

import game_world
import game_framework
from state_machine import StateMachine

# Bird의 fly Speed 계산
pixels_per_meter = (10.0 / 0.3)  # 10 pixel 30 cm
run_speed_kmph = 20.0  # Km / Hour
run_speed_mpm = (run_speed_kmph * 1000.0 / 60.0)
run_speed_mps = (run_speed_mpm / 60.0)
run_speed_pps = (run_speed_mps * pixels_per_meter)

# Bird fly Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8