from unittest import TestCase
from unittest.mock import patch

from .. import game


class TestPosition(TestCase):
    def test_creation(self):
        pos = game.Position(3, 4)
        self.assertEqual(pos.x, 3)
        self.assertEqual(pos.y, 4)
        self.assertIsInstance(pos, game.PositionArray)

    def test_modification(self):
        pos = game.Position(3, 4)
        pos.x = 5
        pos.y = 6
        self.assertEqual(pos.x, 5)
        self.assertEqual(pos.y, 6)

    def test_distance(self):
        pos = game.Position(3, 6)
        other_pos = game.Position(-2, 11)
        self.assertEqual(pos.distance(other_pos), 10)
        self.assertEqual(pos.distance(0), 9)


class TestGame(TestCase):
    @patch.object(game, 'randrange', side_effect=range(5000))
    @patch.object(game.Game, 'NB_BOTS', 5)
    def setUp(self, *_mocks):
        self.game = game.Game()

    def test_game(self):
        self.assertEqual(self.game.target.hp, game.Target.MAX_HP)
        self.assertEqual(self.game.turn, 0)
