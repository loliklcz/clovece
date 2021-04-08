"""
Main file
"""

from time import time
import matplotlib.pyplot as plt
import numpy as np
from player import Player
from game import Game
from strategy import MoveCloserToHome, MoveCloserToEnemy
# from strategy import Random, MoveCloserToHome, MoveCloserToEnemy

DEBUG = False
GAMES = 1000


wins = [0, 0]
total_turns = [[0], [0]]

start_time = time()
for i in range(0, GAMES):
    player1 = Player("Test", MoveCloserToEnemy())
    player2 = Player("Abc", MoveCloserToHome())
    players = [player1, player2]

    game = Game(players, 10, DEBUG)
    # wins.append(game.player_won)
    if game.player_won == player1.name:
        wins[0] += 1
        total_turns[0].append(game.total_turns)
    else:
        wins[1] += 1
        total_turns[1].append(game.total_turns)

mean_turns = [sum(total_turns[0]) / len(total_turns[0]), sum(total_turns[1]) / len(total_turns[1])]

print("---Wins---")
print(f"{player1.name} - {wins[0]}")
print(f"{player2.name} - {wins[1]}")

print(f"Finished {GAMES} games in {time() - start_time} seconds")


labels = ['Wins', 'Turns']
# player1_data = [wins.count(player1.name)]
# player2_data = [wins.count(player2.name)]
player1_data = [wins[0], round(mean_turns[0])]
player2_data = [wins[1], round(mean_turns[1])]

x = np.arange(len(labels))  # the label locations
WIDTH = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - WIDTH / 2, player1_data, WIDTH, label=players[0].strategy.__class__.__name__)
rects2 = ax.bar(x + WIDTH / 2, player2_data, WIDTH, label=players[1].strategy.__class__.__name__)

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Wins')
ax.set_title('Scores')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.savefig('graph.png')
plt.show()
