import random
# cannot import name 'Game' from partially initialized module 'game' (most likely due to a circular import)


class Strategy:
    def __init__(self, game, player, roll: int):
        self.game = game
        self.player = player
        self.roll = roll

    def move_place_choice(self):
        pass

    def move_choice(self):
        pass

class Random(Strategy):
    def __init__(self, game, player, roll):
        super().__init__(game, player, roll)

    def move_place_choice(self):
        place_or_move = random.randint(0, 1)
        if place_or_move == 0:
            self.player.place_figure(self.game)
        else:
            figure = random.choice(self.player.figures_on_board())
            # figures = self.player.figures_on_board()
            # print(figures)
            print("Selected figure: " + str(figure) + "*"*30)

            self.game.move(self.player, figure, self.roll)

    def move_choice(self):
        figure = random.choice(self.player.figures_on_board())
        self.game.move(self.player, figure, self.roll)
