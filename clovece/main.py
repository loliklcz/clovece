from player import Player
from game import Game
import colorama
from colorama import Fore

colorama.init(autoreset=True)

player1 = Player("Test", "red")
player2 = Player("Abc", "blue")

players = [player1, player2]
# game = Game(players, 10)

for _i in range(1, 20):
    game = Game(players, 10)


while True:
    pass

    # input("Dice roll...")
    # roll = game.roll_dice()
    # game.draw_dice(roll)  # draw art of the dice
    #
    # if roll == 6 and currentPlayer.has_figure() and currentPlayer.get_figure_at_start() is not None:
    #     choice = input("Do you want to place new figure or make a move? (f/m)")
    #     if choice == "f":
    #         currentPlayer.place_figure(game.homes[game.turn])
    #     else:
    #         # ask which figure to move
    #         game.select_figure_dialog(currentPlayer)
    #         choice = int(input(":"))
    #         game.move(currentPlayer, choice, roll)
    #         # game.move(currentPlayer, currentPlayer.figures_on_board()[0], roll)
    #
    # elif roll == 6 and currentPlayer.get_figure_at_start() is not None:
    #     currentPlayer.place_figure(game.homes[game.turn])
    #
    # elif not currentPlayer.has_figure():
    #     print("Sorry, you must roll six to place a figure!")
    #
    # elif currentPlayer.count_figures_on_board() == 1:
    #     game.move(currentPlayer, currentPlayer.figures_on_board()[0], roll)
    #
    # else:
    #     game.select_figure_dialog(currentPlayer)
    #     choice = int(input(":"))
    #     game.move(currentPlayer, choice, roll)
    #
    # game.turn += 1
    # if game.turn >= len(players):  # check if turn is larger or same as player count
    #     game.turn = 0  # set turn back to 0
