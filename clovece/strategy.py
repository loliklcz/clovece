import random
# cannot import name 'Game' from partially initialized module 'game' (most likely due to a circular import)


class Strategy:
    """
    def __init__(self, game, player, roll: int):
        self.game = game
        self.player = player
        self.roll = roll
    """

    def move_place_choice(self, game, player, roll):
        pass

    def move_choice(self, game, player, roll):
        pass


class Random(Strategy):
    """
    def __init__(self, game, player, roll):
        super().__init__(game, player, roll)
    """

    def move_place_choice(self, game, player, roll):
        place_or_move = random.randint(0, 1)
        if place_or_move == 0:
            player.place_figure(game)
        else:
            figure = random.choice(player.figures_on_board())
            # figures = self.player.figures_on_board()
            # print(figures)
            print("Selected figure: " + str(figure) + "*"*30)

            game.move(player, figure, roll)

    def move_choice(self, game, player, roll):
        figure = random.choice(player.figures_on_board())
        game.move(player, figure, roll)


class MoveCloserToHome(Strategy):

    def move_place_choice(self, game, player, roll):
        place_or_move = random.randint(0, 1)
        if place_or_move == 0:
            player.place_figure(game)
        else:
            figure = random.choice(player.figures_on_board())
            # figures = self.player.figures_on_board()
            # print(figures)
            print("Selected figure: " + str(figure) + "*"*30)

            game.move(player, figure, roll)

    def move_choice(self, game, player, roll):
        closest_list = []
        figure_index = 0
        for pos in player.pos:
            if 0 <= pos[0] < game.homes[game.turn]:
                closest_list.append([pos, figure_index])
            figure_index += 1

        try:
            closest = max(closest_list[0])
        except:
            closest = [None, random.choice(player.figures_on_board())]

        for figure in player.figures_on_board():
            if figure == closest[1]:
                game.move(player, figure, roll)
                break
