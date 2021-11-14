from unittest import TestCase

from ..models import Game

game = Game()


class PositionTest(TestCase):
    def test_distance(self):
        pos_a = game.Position(0, 3)
        pos_b = game.Position(1, 1)

        self.assertEqual(pos_a.distance(pos_b), 3)

    def test_distance_cyclic(self):
        pos_a = game.Position(0, 2)
        pos_b = game.Position(game.grid_w - 1, game.grid_h - 1)

        self.assertEqual(pos_a.distance(pos_b), 4)

    def test_move(self):
        pos = game.Position(0, 0)

        pos.move(1, 2)
        self.assertEqual(pos.x, 1)
        self.assertEqual(pos.y, 2)

        pos.move(-1, -2)
        self.assertEqual(pos.x, 0)
        self.assertEqual(pos.y, 0)

        pos.move(-1, -2)
        self.assertEqual(pos.x, game.grid_w - 1)
        self.assertEqual(pos.y, game.grid_h - 2)
