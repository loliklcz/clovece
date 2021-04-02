"""
Strategy class with all implemented strategies
"""

import random


def closest_pos(pos):
    """
    Return figure that is closest to home
    """

    completed_board_list = []  # figures that completed board, but aren't finished yet
    closest_list = []
    closest = None

    # pylint:disable=invalid-name
    for p in pos:
        if p[1] is True and p[0] != -2:
            completed_board_list.append(p)
        else:
            closest_list.append(p)

    if len(completed_board_list) > 0:
        closest = max(completed_board_list)
    else:
        closest = max(closest_list)

    return closest


class Strategy:
    """
    def __init__(self, game, player, roll: int):
        self.game = game
        self.player = player
        self.roll = roll
    """

    def move_place_choice(self, game, player, roll):
        """
        If you roll 6, have at least one figure and at least one figure available at start.
            You will decide to move or place.
        """

    def move_choice(self, game, player, roll):
        """
        If you have more than one figure on board.
            You will decide which figure to move.
        """


class Random(Strategy):
    """
    Strategy: Randomly choose to place a figure or move and randomly choose figure to move.
    """

    def move_place_choice(self, game, player, roll):
        place_or_move = random.randint(0, 1)
        if place_or_move == 0:
            player.place_figure(game)
        else:
            figure = random.choice(player.figures_on_board())
            game.move(player, figure, roll)

    def move_choice(self, game, player, roll):
        figure = random.choice(player.figures_on_board())
        game.move(player, figure, roll)


class MoveCloserToHome(Strategy):
    """
    Strategy: When you roll 6 and there is figure that is close to home then move with it.
        Else, place a new figure.
    """

    def move_place_choice(self, game, player, roll):
        closest = closest_pos(player.pos)

        if game.turn == 0 and closest[0] >= 7:
            figure = player.pos.index(closest)
            game.move(player, figure, roll)
        elif game.turn == 1 and closest[0] >= 2:
            figure = player.pos.index(closest)
            game.move(player, figure, roll)
        else:
            player.place_figure(game)

    def move_choice(self, game, player, roll):
        figure = player.pos.index(closest_pos(player.pos))
        game.move(player, figure, roll)
