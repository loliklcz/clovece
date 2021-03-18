from player import Player
from game import Game
from strategy import *
from time import time


debug = False
games = 10000

player1 = None
player2 = None

wins = []

start_time = time()
for i in range(0, games):
    player1 = Player("Test", MoveCloserToHome())
    player2 = Player("Abc", Random())
    players = [player1, player2]

    game = Game(players, 10, debug)
    wins.append(game.player_won)

print("---Wins---")
print(f"{player1.name} - {wins.count(player1.name)}")
print(f"{player2.name} - {wins.count(player2.name)}")

print(f"Finished {games} games in {time() - start_time} seconds")
