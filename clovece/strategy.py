import random
# cannot import name 'Game' from partially initialized module 'game' (most likely due to a circular import)


def closest_pos(pos):
    completed_board_list = []
    closest_list = []
    closest = None

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
            print("Selected figure: " + str(figure) + "*"*30)  # TODO: REMOVE

            game.move(player, figure, roll)

    def move_choice(self, game, player, roll):
        figure = random.choice(player.figures_on_board())
        game.move(player, figure, roll)


class MoveCloserToHome(Strategy):

    def move_place_choice(self, game, player, roll):  # TODO
        place_or_move = random.randint(0, 1)
        if place_or_move == 0:
            player.place_figure(game)
        else:
            figure = random.choice(player.figures_on_board())
            # figures = self.player.figures_on_board()
            # print(figures)
            print("Selected figure: " + str(figure) + "*"*30)  # TODO: REMOVE

            game.move(player, figure, roll)

    def move_choice(self, game, player, roll):

        """
        closest_list = []
        figure_index = 0
        for pos in player.pos:
            if pos[0] < game.homes[game.turn]:  # if 0 <= pos[0] < game.homes[game.turn]

                closest_list.append([pos, figure_index])
            figure_index += 1
        """

        """
        for pos in player.pos:
            if abs(pos[0] - game.homes[game.turn]):
                final_value = pos[0]
                print("Found closest figure at " + abs(pos[0] - game.homes[game.turn]))
        """

        """
        try:
            closest = max(closest_list[0])
        except:
            closest = [None, random.choice(player.figures_on_board())]
        """

        print("Closest pos found!")
        print(player.pos)
        print(closest_pos(player.pos))

        for figure in player.figures_on_board():
            if figure == closest_pos(player.pos)[0]:
                game.move(player, figure, roll)
                break

        figure = player.pos.index(closest_pos(player.pos))
        game.move(player, figure, roll)
