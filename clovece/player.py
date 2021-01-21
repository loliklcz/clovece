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

    def CountFiguresOnBoard(self):
        """
        Return number of figures on the board
        """
        figures = 0
        for figure in self.pos:
            if figure[0] > -1:
                figures += 1
        return figures

    def FiguresOnBoard(self):
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

    def GetFigureAtHome(self):
        """
        Return first figure at home
        """
        index = 0
        for figure in self.pos:
            if figure[0] == -1:
                return index
            index += 1

    def PlaceFigure(self, home):
        """
        Place figure on the board
        """
        self.pos[self.GetFigureAtHome()][0] = home + 1