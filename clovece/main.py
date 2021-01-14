from player import Player
from game import Game
import colorama
from colorama import Fore
from art import dice_one

colorama.init(autoreset=True)

player1 = Player("Test", "red")
player2 = Player("Test2", "blue")

players = [player1, player2]
game = Game(players, 10)


while True:
    #game.PrintStats()
    currentPlayer = players[game.turn]
    print("\n" + Fore.GREEN + f"It's {currentPlayer.name}'s turn!")
    #game.PrintStats(currentPlayer)
    game.PrintPos(currentPlayer)

    input("Dice roll...")
    roll = game.RollDice()
    game.DrawDice(roll)

    

    if roll == 6 and currentPlayer.HasFigure():
        choice = input("Do you want to place new figure or make a move? (f/m)")
        if choice == "f":
            currentPlayer.PlaceFigure(game.homes[game.turn])
        else:
            game.Move(currentPlayer, currentPlayer.FiguresInGame()[0], roll)
    
    elif roll == 6:
        currentPlayer.PlaceFigure(game.homes[game.turn])
    
    elif currentPlayer.HasFigure() == False:
        print("Sorry, you must roll six to place a figure!")
    
    elif currentPlayer.CountFiguresInGame() == 1:
        game.Move(currentPlayer, currentPlayer.FiguresInGame()[0], roll)
    
    else:
        print("Select a figure you want to move!")
        index = 0
        for figure in currentPlayer.FiguresInGame():
            print(figure)
        choice = int(input(":"))
        game.Move(currentPlayer, currentPlayer.FiguresInGame()[choice], roll)
        
    





    game.turn += 1
    if game.turn >= len(players):
        game.turn = 0