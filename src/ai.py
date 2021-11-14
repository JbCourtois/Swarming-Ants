import random

import numpy as np

from .models import DIRECTIONS, Game


class AI:
    """Robot strategy.

    Each turn, run() will be called with the turn input,
    and should return an order.
    """
    BASE_MESSAGE_DELAY = 15
    MIN_KNOW = 7

    def __init__(self):
        self.target = None
        self.pos = np.asarray((0, 0))

        self.message_delay = 0
        self.alerted = set()

    def run(self, data: '.models.RobotInput'):
        self.message_delay -= 1
        if data.on_target:
            self.target = np.asarray((0, 0))

        for neighbour in data.neighbours:
            self._process_neighbour(neighbour)

        if self.target is None:
            return self._order_random_move()

        if self.alerted >= self.MIN_KNOW:
            # Rush to the target!
            return self._order_target_move()

        # Inform other robots
        if any(n.in_range for n in data.neighbours) and self.message_delay <= 0:
            self.message_delay = self.BASE_MESSAGE_DELAY
            return self._order_message()

        return self._order_random_move()

    def _process_neighbour(self, neighbour):
        distance = sum(abs(coord) for coord in neighbour.pos)
        neighbour.in_range = (distance < Game.ROBOT_COM_RANGE)

        if neighbour.message is None:
            return

        if self.target is None:
            self.target = neighbour.message.target + neighbour.pos

        origin = neighbour.pos + neighbour.message.origin
        self.alerted.add(origin)
        for relative_alerted in neighbour.message.alerted:
            self.alerted.add(origin + relative_alerted)

    def _order_random_move(self):
        """Move in a random direction."""
        key, shift = random.choice(DIRECTIONS.items())
        shift = np.asarray(shift)

        self.pos -= shift
        if self.target_x is not None:
            self.target -= shift

        return f'MOVE {key}'

    def _order_target_move(self):
        """Move toward target, or fire if already on it."""
        if self.target[0] < 0:
            return 'MOVE W'
        if self.target[0] > 0:
            return 'MOVE E'
        if self.target[1] < 0:
            return 'MOVE N'
        if self.target[1] > 0:
            return 'MOVE S'
        return 'FIRE 0 0'

    def _order_message(self):
        """Send a message."""
        positions = [self.pos, self.target, *self.alerted]
        message = ','.join(
            '-'.join(map(str, pos))
            for pos in positions)

        return f'MESSAGE {message}'
