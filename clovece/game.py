import random
from art import dice
from colorama import init, Fore
from player import Player
from strategy import Random
import time

init(autoreset=True)


class Game:
    def __init__(self, players, size):
        self.players = players
        self.size = size
        self.turn = 0
        self.diceMax = 6
        self.homes = [0, size // 2]

        # !!! REMOVE AFTER TESTING !!!
        p: Player = players[0]
        p.pos[0][0] = 0
        # p.pos[1][0] = 5
        # p.pos[2][0] = 8
        p2: Player = players[1]
        p2.pos[0][0] = 1

        self.start_time = time.time()

        while self.do_turn():
            pass
            # print("Doing turn")

        print("Done")

    def do_turn(self):
        current_player = self.players[self.turn]  # get player that is currently at turn
        print("\n" + Fore.GREEN + f"It's {current_player.name}'s turn!")  # 'It's Test's turn!'
        self.print_pos(current_player)  # '❌ ❌ ❌ | 🏠'

        # Do dice roll
        roll = self.roll_dice()  # get random number as a dice roll
        self.draw_dice(roll)  # draw a dice image
        self.check_roll(roll)  # do action based on roll number

        self.turn += 1
        if self.turn >= len(self.players):  # check if turn is larger or same as player count
            self.turn = 0  # set turn back to 0

        return True

    def check_roll(self, roll: int):
        player: Player = self.players[self.turn]
        strategy = Random(self, player, roll)
        """
        check = at least one figure at start

        if 6 + has figure + check => choice
        elif 6 + check => place figure
        elif not 6 + no figure => "sorry you must roll 6..."
        elif not 6 + more than 1 figure => select figure
        elif not 6 => move
        """

        if roll == 6 and player.has_figure() and player.get_figure_at_start() is not None:
            print("You rolled 6!")
            strategy.move_place_choice()
        elif roll == 6 and player.get_figure_at_start() is not None:
            print("Placing figure!")
            player.place_figure(self)
        elif player.count_figures_on_board() > 1:
            strategy.move_choice()
        elif player.has_figure():
            self.move(player, player.figures_on_board()[0], roll)
        else:
            pass
            print("Sorry, you must roll six to place a figure!")

        """
        if roll == 6 and player.has_figure() and player.get_figure_at_start() is not None:
            print("You rolled 6!")
            choice = random.randint(0, 1)
            if choice == 0:
                player.place_figure(self)
            elif choice == 1:

                self.move(player, choice, roll)
            else:
                self.move(player)

        elif roll == 6 and player.get_figure_at_start() is not None:
            # player.place_figure(self.homes[self.turn])
            player.place_figure(self)
        """

    def print_stats(self, player_object=None):
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
        roll = random.randint(1, self.diceMax)
        print(f"You rolled {roll}")
        return roll

    @staticmethod
    def draw_dice(roll: int):
        print(dice[roll - 1])

    @staticmethod
    def select_figure_dialog(player):
        print("Select a figure you want to move!")
        # index = 0 remove later
        for figure in player.figures_on_board():
            print(figure)

    def move(self, player, figure: int, number: int):
        player.pos[figure][0] += number

        # Game logic
        for plr in self.players:
            for index, pos in enumerate(plr.pos):
                if pos[0] == player.pos[figure][0] and plr != player:
                    plr.pos[index] = [-1, False]
                    print(Fore.RED + f"{player.name} destroyed {plr.name}!")
                    print(plr.pos)

        if player.pos[figure][0] > self.size:
            player.pos[figure][0] -= self.size
            player.pos[figure][1] = True
            if player.pos[figure][0] >= self.homes[self.turn]:
                print("YOU ARE AT HOME!")
                player.pos[figure][0] = -2
                if player.get_figure_at_start() is None and len(player.figures_on_board()) == 0:
                    self.win(player)
                return

        if player.pos[figure][0] >= self.homes[self.turn] and player.pos[figure][1]:
            print("YOU ARE AT HOME!")
            player.pos[figure][0] = -2
            if player.get_figure_at_start() is None and len(player.figures_on_board()) == 0:
                self.win(player)
            return

    def win(self, player):
        print(Fore.CYAN + f"{player.name} won!")
        print("--- %s seconds ---" % (time.time() - self.start_time))
        exit()
