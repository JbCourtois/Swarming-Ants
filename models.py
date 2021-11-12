import random
import numpy as np


class Direction:
    LEFT = np.asarray((-1, 0))
    RIGHT = np.asarray((1, 0))
    UP = np.asarray((0, -1))
    DOWN = np.asarray((0, 1))


class Game:
    RANGE_NB_ROBOTS = (10, 30)
    RANGE_TARGET_HP = (500, 10000)
    RANGE_GRID_H = (30, 300)
    MAX_GRID_X = 700

    ROBOT_COM_RANGE = 5
    ROBOT_FIRE_RANGE = 10

    def __init__(self):
        self.grid_h = random.randint(*self.RANGE_GRID_H)
        self.grid_w = random.randint(self.grid_h, self.MAX_GRID_X)

        self.target_pos = np.asarray((
            random.randrange(self.grid_w),
            random.randrange(self.grid_h),
        ))
        self.target_hp = random.randint(*self.RANGE_TARGET_HP)
