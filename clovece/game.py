import random
from art import dice
from colorama import init, Fore

init(autoreset=True)

class Game:
    def __init__(self, players, size):
        self.players = players
        self.size = size
        self.turn = 0
        self.diceMax = 6
        self.homes = [0, size // 2]

    def PrintStats(self, playerObject="all"):
        if playerObject == "all":
            for player in self.players:
                print(f"{player.name} ({player.color})")
                print(f"Position: {player.pos}")
                print(f"HasFigure: {player.HasFigure()}")
        else:
            print(f"{playerObject.name} ({playerObject.color})")
            print(f"Position: {playerObject.pos}")
            print(f"HasFigure: {playerObject.HasFigure()}")

    def PrintPos(self, player):
        atHome = []
        atStart = []
        onBoard = []
        for pos in player.pos:
            if pos[0] == -2:
                atHome.append("🏠")
            if pos[0] == -1:
                atStart.append("❌")
            if pos[0] > -1:
                if pos[1] == True:
                    onBoard.append(Fore.YELLOW + f"♟️ ({pos[0]})" + Fore.RESET)
                else:
                    onBoard.append(f"♟️ ({pos[0]})")

        print(" ".join(onBoard) + "\n" + " ".join(atStart) + " | " + " ".join(atHome))

    
    def RollDice(self) -> int:
        roll = random.randint(1, self.diceMax)
        print(f"You rolled {roll}")
        return roll

    def DrawDice(self, roll: int):
        print(dice[roll - 1])

    def SelectFigureDialog(self, player):
        print("Select a figure you want to move!")
        index = 0
        for figure in player.FiguresOnBoard():
            print(figure)

    def Move(self, player, figure:int, number:int):
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
                return

        if player.pos[figure][0] >= self.homes[self.turn] and player.pos[figure][1]:
            print("YOU ARE AT HOME!")
            player.pos[figure][0] = -2
            return