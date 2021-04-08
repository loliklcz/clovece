"""
Game file, see Game class
"""

from random import randint
from time import time
from colorama import init, Fore
from player import Player
from art import dice
# from strategy import Strategy


init(autoreset=True)


class Game:
    """
    Game class, handles all players, board, turns, homes
    """

    # pylint: disable=too-many-instance-attributes
    def __init__(self, players, size, debug=False):
        self.players = players
        self.size = size
        self.debug = debug
        self.turn = 0
        self.dice_max = 6
        self.homes = [0, size // 2]
        self.game_end = False

        self.player_won = None
        self.total_turns = 0

        self.start_time = time()

        while self.game_end is not True:
            self.total_turns += 1
            self.do_turn()

        if self.debug:
            print(Fore.CYAN + f"{self.player_won} won!")
            print("--- %s seconds ---" % (time() - self.start_time))

    def do_turn(self):
        """
        Called every turn, rolls a dice, checks dice roll
        """
        current_player = self.players[self.turn]  # get player that is currently at turn

        if self.debug:
            print("\n" + Fore.GREEN + f"It's {current_player.name}'s turn!")  # 'It's Test's turn!'
            self.print_pos(current_player)  # '❌ ❌ ❌ | 🏠'

        # Do dice roll
        roll = self.roll_dice()  # get random number as a dice roll

        if self.debug:
            print(f"You rolled {roll}")
        # self.draw_dice(roll)  # draw a dice image
        #  (or delete it completely)

        self.check_roll(roll)  # do action based on roll number

        self.turn += 1
        if self.turn >= len(self.players):  # check if 'turn' is larger or same as player count
            self.turn = 0  # set 'turn' back to 0

        return True

    def check_roll(self, roll: int):
        """
        Run function from strategy depending on dice roll
            and count of figures at home, start or board
        """
        player: Player = self.players[self.turn]
        # strategy = player.strategy(self, player, roll)
        strategy = player.strategy

        # pylint:disable=pointless-string-statement
        """
        check = at least one figure at start

        if 6 + has figure + check => choice
        elif 6 + check => place figure
        elif not 6 + no figure => "sorry you must roll 6..."
        elif not 6 + more than 1 figure => select figure
        elif not 6 => move
        """

        if roll == 6 and player.has_figure() and player.get_figure_at_start() is not None:
            if self.debug:
                print("Calling move_place_choice")
            strategy.move_place_choice(self, player, roll)
        elif roll == 6 and player.get_figure_at_start() is not None:
            if self.debug:
                print("Placing figure!")
            player.place_figure(self)
        elif player.count_figures_on_board() > 1:
            if self.debug:
                print("Calling move_choice")
            strategy.move_choice(self, player, roll)
        elif player.has_figure():
            self.move(player, player.figures_on_board()[0], roll)
        else:
            if self.debug:
                print("Sorry, you must roll six to place a figure!")

    def print_stats(self, player_object=None):
        """
        Prints information about player (used for debugging)
        """
        if player_object is None:
            for player in self.players:
                print(f"{player.name} ({player.color})")
                print(f"Position: {player.pos}")
                print(f"HasFigure: {player.has_figure()}")
        else:
            print(f"{player_object.name} ({player_object.color})")
            print(f"Position: {player_object.pos}")
            print(f"HasFigure: {player_object.HasFigure()}")

    @staticmethod
    def print_pos(player):
        """
        Print information about player's figures
        """
        at_home = []
        at_start = []
        on_board = []
        for pos in player.pos:
            if pos[0] == -2:
                at_home.append("🏠")
            if pos[0] == -1:
                at_start.append("❌")
            if pos[0] > -1:
                if pos[1] is True:
                    on_board.append(Fore.YELLOW + f"♟️ ({pos[0]})" + Fore.RESET)
                else:
                    on_board.append(f"♟️ ({pos[0]})")

        print(" ".join(on_board) + "\n" + " ".join(at_start) + " | " + " ".join(at_home))

    def roll_dice(self) -> int:
        """
        Returns random number as dice roll
        """
        roll = randint(1, self.dice_max)
        return roll

    @staticmethod
    def draw_dice(roll: int):
        """
        Draw dice image
        """
        print(dice[roll - 1])

    @staticmethod
    def select_figure_dialog(player):
        """
        TODO: remove this function later, it only displays available
            figures to user (not needed while using strategies)
        """
        print("Select a figure you want to move!")
        # index = 0 remove later
        for figure in player.figures_on_board():
            print(figure)

    def move(self, player, figure: int, number: int):  # TOD\O: simplify this function ------- later
        """
        Move player's figure by x and handle destroying figures and wins
        """
        player.pos[figure][0] += number

        # Game logic
        for plr in self.players:
            for index, pos in enumerate(plr.pos):
                if pos[0] == player.pos[figure][0] and plr != player:
                    plr.pos[index] = [-1, False]
                    if self.debug:
                        print(Fore.RED + f"{player.name} destroyed {plr.name}!")
                    # print(plr.pos)

        if player.pos[figure][0] > self.size:
            player.pos[figure][0] -= self.size
            player.pos[figure][1] = True
            if player.pos[figure][0] >= self.homes[self.turn]:
                if self.debug:
                    print("YOU ARE AT HOME!")
                player.pos[figure][0] = -2
                if player.get_figure_at_start() is None and len(player.figures_on_board()) == 0:
                    self.win(player)
                return

        if player.pos[figure][0] >= self.homes[self.turn] and player.pos[figure][1]:
            if self.debug:
                print("YOU ARE AT HOME!")
            player.pos[figure][0] = -2
            if player.get_figure_at_start() is None and len(player.figures_on_board()) == 0:
                self.win(player)
            return

    def win(self, player):
        """
        Set game_end to true and set the player who won
        """
        self.game_end = True
        self.player_won = player.name
