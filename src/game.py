from dataclasses import dataclass
from random import randrange

import numpy as np

debug = print  # TODO: remove


class PositionArray(np.ndarray):
	@property
	def x(self):
		return self[0]

	@x.setter
	def x(self, value):
		self[0] = value
	
	@property
	def y(self):
		return self[1]

	@y.setter
	def y(self, value):
		self[1] = value
	
	def distance(self, other):
		return sum(abs(self - other))


def Position(x, y):
	return np.array([x, y]).view(PositionArray)


class Bot:
	ATTACK_RANGE = 2
	VISION = 5

	def __init__(self, *args):
		self.pos = Position(0, 0)

		# Strategic parameters
		self.move_counter = 0
		self.shift_line = False

	def move(self, info: 'BotInput'):
		if info.target is not None:
			if info.target.pos.distance(0) <= self.ATTACK_RANGE:
				return 'A'
			if info.target.pos.x < 0:
				return 'L'
			if info.target.pos.x > 0:
				return 'R'
			if info.target.pos.y < 0:
				return 'D'
			if info.target.pos.y > 0:
				return 'U'


		if not self.shift_line:
			if self.move_counter <= Game.SIZE_X - self.VISION:
				self.move_counter += 1
				return 'L'
			self.shift_line = True
			self.move_counter = 0
			return 'D'

		# Continue switching line
		if self.move_counter <= 2 * self.VISION:
			self.move_counter += 1
			return 'D'

		# Go back to explore line
		self.shift_line = False
		self.move_counter = 0
		return 'L'


@dataclass
class Target:
	MAX_HP = 10000

	pos: Position
	hp: int = MAX_HP


class FakeTarget(Target):
	pos: PositionArray['Relative to bot position']


@dataclass
class BotInput:
	allies: list[Bot]
	target: FakeTarget | None


class Game:
	SIZE_X = 5000
	SIZE_Y = 5000
	NB_BOTS = 50

	def __init__(self):
		self.target = Target(Position(
			randrange(self.SIZE_X),
			randrange(self.SIZE_Y)))
		self.bots = [Bot() for _ in range(self.NB_BOTS)]
		self.bot_positions = [
			Position(randrange(self.SIZE_X), randrange(self.SIZE_Y))
			for _ in range(self.NB_BOTS)
		]
		self.turn = 0

	def get_connected_bots(self):
		# TODO: Union-find
		return {}

	def parse_bot_action(self, bot_index, action):
		bot_pos = self.bot_positions[bot_index]
		match action:
			case 'L':
				bot_pos.x -= 1
				bot_pos.x %= self.SIZE_X
			case 'R':
				bot_pos.x += 1
				bot_pos.x %= self.SIZE_X
			case 'U':
				bot_pos.y += 1
				bot_pos.y %= self.SIZE_Y
			case 'D':
				bot_pos.y -= 1
				bot_pos.y %= self.SIZE_Y
			case 'A':
				if bot_pos.distance(self.target.pos) <= Bot.ATTACK_RANGE:
					self.target.hp -= 1

	def move(self):
		chains = self.get_connected_bots()
		for bot_index, bot in enumerate(self.bots):
			bot_pos = self.bot_positions[bot_index]
			info = BotInput(
				allies=chains.get(bot_index, []),  # TODO: compute, and see target if any connected bot sees target
				target=FakeTarget(
					hp=self.target.hp,
					pos=self.target.pos - bot_pos
				) if bot_pos.distance(self.target.pos) <= Bot.VISION else None,
			)
			action = bot.move(info)
			self.parse_bot_action(bot_index, action)

	def run(self):
		while self.target.hp > 0:
			self.move()
			self.turn += 1
			if not self.turn % 100:
				debug(f'Turn {self.turn}: {self.target.hp} HP')


if __name__ == "__main__":
	TOLERANCE = 50
	def generate_game():
		while True:
			game = Game()
			ty = game.target.pos.y
			for pos in game.bot_positions:
				if ty - TOLERANCE <= pos.y <= ty + TOLERANCE:
					print('Shift', abs(pos.y - ty))
					return game
			print('game aborted')
	generate_game().run()
