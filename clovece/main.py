from player import Player
from game import Game
import colorama
from colorama import Fore

colorama.init(autoreset=True)

player1 = Player("Test", "red")
player2 = Player("Test2", "blue")

players = [player1, player2]
game = Game(players, 10)


while True:
    currentPlayer = players[game.turn] # get player that is currently at turn
    print("\n" + Fore.GREEN + f"It's {currentPlayer.name}'s turn!")
    game.PrintPos(currentPlayer)
    print(currentPlayer.FiguresOnBoard())

    input("Dice roll...")
    roll = game.RollDice()
    game.DrawDice(roll) # draw art of the dice

    

    if roll == 6 and currentPlayer.HasFigure(): # todo check if player figures at START is higher than 0
        choice = input("Do you want to place new figure or make a move? (f/m)")
        if choice == "f":
            currentPlayer.PlaceFigure(game.homes[game.turn])
        else:
            # ask which figure to move
            game.Move(currentPlayer, currentPlayer.FiguresOnBoard()[0], roll)
    
    elif roll == 6:
        currentPlayer.PlaceFigure(game.homes[game.turn])
    
    elif currentPlayer.HasFigure() == False:
        print("Sorry, you must roll six to place a figure!")
    
    elif currentPlayer.CountFiguresOnBoard() == 1:
        game.Move(currentPlayer, currentPlayer.FiguresOnBoard()[0], roll)
    
    else:
        game.SelectFigureDialog(currentPlayer)
        choice = int(input(":"))
        game.Move(currentPlayer, choice, roll)

        # print("Select a figure you want to move!")
        # index = 0
        # for figure in currentPlayer.FiguresOnBoard():
        #     print(figure)
        # choice = int(input(":"))
        # game.Move(currentPlayer, choice, roll)
        
    





    game.turn += 1
    if game.turn >= len(players):
        game.turn = 0