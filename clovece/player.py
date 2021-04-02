"""
Player class, handles name, strategy and position of player's figures
"""

from strategy import Strategy


class Player:
    """
    Player class
    """
    def __init__(self, name: str, strategy: Strategy):
        self.name = name
        self.strategy = strategy
        self.pos = [[-1, False], [-1, False], [-1, False], [-1, False]]  # pos, completedBoard

    def has_figure(self):
        """
        Check if player has at least one figure on the board
        """
        for figure in self.pos:
            if figure[0] > -1:
                return True
        return False

    def count_figures_on_board(self) -> int:
        """
        Return number of figures on the board
        """
        figures = 0
        for figure in self.pos:
            if figure[0] > -1:
                figures += 1
        return figures

    def figures_on_board(self) -> list:
        """
        Return indexes of figures on the board
        """
        figures = []
        index = 0
        for figure in self.pos:
            if figure[0] > -1:
                figures.append(index)
            index += 1
        return figures

    def get_figure_at_start(self) -> int:
        """
        Return index of first figure at start
        """
        index = 0
        for figure in self.pos:
            if figure[0] == -1:
                return index
            index += 1

    def place_figure(self, game):
        """
        Place figure on the board
        """
        self.pos[self.get_figure_at_start()][0] = game.homes[game.turn] + 1
