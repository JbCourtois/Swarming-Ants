from dataclasses import dataclass
import random


DIRECTIONS = {
    'W': (-1, 0),
    'E': (1, 0),
    'N': (0, -1,),
    'S': (0, 1),
}


class RobotCommandError(ValueError):
    """Exception used when a robot receives an invalid command."""


class Game:
    RANGE_NB_ROBOTS = (10, 30)
    RANGE_TARGET_HP = (500, 10000)
    RANGE_GRID_H = (30, 300)
    MAX_GRID_X = 700

    ROBOT_SPAWN_GAP = 3
    ROBOT_COM_RANGE = 5
    ROBOT_FIRE_RANGE = 10

    def __init__(self):
        self.grid_h = random.randint(*self.RANGE_GRID_H)
        self.grid_w = random.randint(self.grid_h, self.MAX_GRID_X)

        self._generate_classes()

        self.target_pos = self.generate_position()
        self.target_hp = random.randint(*self.RANGE_TARGET_HP)

        self.robots = []

    def generate_position(self):
        """Generate a random position on the game grid."""
        return self.Position(
            x=random.randrange(self.grid_w),
            y=random.randrange(self.grid_h),
        )

    def generate_robot(self):
        """Generate a robot at a random position.

        It must be at distance at least {ROBOT_SPAWN_GAP} from all other entities.
        """
        forbidden_positions = []
        forbidden_positions.extend(robot.position for robot in self.robots)

        while True:
            spawn_position = self.generate_position()
            if any(
                    spawn_position.distance(pos) < self.ROBOT_SPAWN_GAP
                    for pos in forbidden_positions):
                continue

            return self.Robot(position=spawn_position)

    def spawn_robots(self):
        nb_robots = random.randint(*self.RANGE_NB_ROBOTS)
        self.robots.extend(
            self.generate_robot()
            for _ in range(nb_robots))

    def _generate_classes(game):
        @dataclass
        class Position:
            x: int
            y: int

            def shift(self, shift_x, shift_y, in_place=True):
                new_x = (self.x + shift_x) % game.grid_w
                new_y = (self.y + shift_y) % game.grid_h

                if not in_place:
                    return self.__class__(x=new_x, y=new_y)

                self.x = new_x
                self.y = new_y
                return self

            def distance(self, other):
                """Compute the Manhattan distance between two points.

                Recall that the grid is cyclic."""
                diff_x = self.x - other.x
                diff_x = min(diff_x % game.grid_w, -diff_x % game.grid_w)

                diff_y = self.y - other.y
                diff_y = min(diff_y % game.grid_h, -diff_y % game.grid_h)

                return diff_x + diff_y

        @dataclass
        class Robot:
            position: Position
            message: str = ""
            lol = 3

            def reset(self):
                self.message = ""

            def hold(self):
                """Do nothing. This is the default order."""

            def move(self, direction):
                if (shift := DIRECTIONS.get(direction)) is None:
                    raise RobotCommandError('Invalid direction')
                self.position.shift(*shift)

            def fire(self, target):
                if game.target_pos != target:
                    return

            def send_message(self, message):
                """Send a message.

                At the start of the next turn,
                all other robots in communication range
                will receive that message.
                """
                self.message = message

        game.Robot = Robot
        game.Position = Position
