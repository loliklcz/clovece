class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pos = [[-1, False], [-1, False], [-1, False], [-1, False]] # pos, completedBoard

    def HasFigure(self):
        """
        Check if player has at least one figure on the board
        """
        for figure in self.pos:
            if figure[0] > -1:
                return True
        return False

    def CountFiguresInGame(self): # NOT SURE IF THIS WORKS
        """
        Return number of figures in game
        """
        figures = 0
        for figure in self.pos:
            if figure[0] > -1:
                figures += 1
        return figures

    def GetFigureInHome(self):
        """
        Return first figure at home
        """
        index = 0
        for figure in self.pos:
            if figure[0] == -1:
                return index
            index += 1

    def FiguresInGame(self):
        """
        Return indexes of figures on the board
        """
        figures = []
        index = 0
        for figure in self.pos:
            if figure[0] > -1:
                figures.append(index)
                index += 1
        return figures

    def PlaceFigure(self, home):
        """
        Place figure on the board
        """
        self.pos[self.GetFigureInHome()][0] = home + 1