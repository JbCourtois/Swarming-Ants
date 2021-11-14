from unittest import TestCase
from itertools import combinations

from ..models import Game


class PositionTestCase(TestCase):
    game = Game()

    def test_distance(self):
        pos_a = self.game.Position(0, 3)
        pos_b = self.game.Position(1, 1)

        self.assertEqual(pos_a.distance(pos_b), 3)

    def test_distance_cyclic(self):
        pos_a = self.game.Position(0, 2)
        pos_b = self.game.Position(self.game.grid_w - 1, self.game.grid_h - 1)

        self.assertEqual(pos_a.distance(pos_b), 4)

    def test_move(self):
        pos = self.game.Position(0, 0)

        pos.move(1, 2)
        self.assertEqual(pos.x, 1)
        self.assertEqual(pos.y, 2)

        pos.move(-1, -2)
        self.assertEqual(pos.x, 0)
        self.assertEqual(pos.y, 0)

        pos.move(-1, -2)
        self.assertEqual(pos.x, self.game.grid_w - 1)
        self.assertEqual(pos.y, self.game.grid_h - 2)


class GameTestCase(TestCase):
    def setUp(self):
        self.game = Game()
        self.game.spawn_robots()

    def assertBetween(self, value, low, high):
        self.assertTrue(low <= value <= high)

    def test_spawn(self):
        self.assertBetween(len(self.game.robots), *Game.RANGE_NB_ROBOTS)

        for robot in self.game.robots:
            self.assertGreaterEqual(
                self.game.target_pos.distance(robot.position),
                Game.ROBOT_SPAWN_GAP)

        for r1, r2 in combinations(self.game.robots, 2):
            self.assertGreaterEqual(
                r1.position.distance(r2.position),
                Game.ROBOT_SPAWN_GAP)
