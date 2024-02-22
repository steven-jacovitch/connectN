from enum import Enum

"""
This is the start of the HW.
If there is any conflict between the doc string and the HW document,
please follow the instruction in the HW document.
Good Luck and have fun !
"""


class Notation(Enum):
    """Enumeration for representing different types of notations in the game.

    Attributes:
        EMPTY (int): Represents an empty cell on the board.
        PLAYER1 (int): Represents a cell occupied by Player 1.
        PLAYER2 (int): Represents a cell occupied by Player 2.
    """

    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2


class Player:
    """Represents a player in the game.

    Attributes:
        __playerName (str): The name of the player.
        __playerNotation (Notation): The notation (symbol) used by the player on the board.
        __curScore (int): The current score of the player.

    Args:
        playerName (str): The name of the player.
        playerNotation (Notation): The notation (symbol) used by the player.
        curScore (int): The initial score of the player.
    """

    def __init__(self, playerName, playerNotation, curScore):
        self.__playerName = playerName
        self.__playerNotation = playerNotation
        self.__curScore = curScore

    def display(self) -> str:
        """Displays the player's details including name, notation, and current score."""
        return f"{self.__playerName} ({self.__playerNotation.name}): {self.__curScore}"

    def addScoreByOne(self):
        """Increments the player's score by one."""
        self.__curScore += 1

    def getScore(self):
        """Returns the current score of the player."""
        return self.__curScore

    def getName(self):
        """Returns the name of the player."""
        return self.__playerName

    def getNotation(self):
        """Returns the notation used by the player."""
        return self.__playerNotation


class Board:
    """Represents the game board.

    Attributes:
        __rowNum (int): Number of rows in the board.
        __colNum (int): Number of columns in the board.
        __grid (list): 2D list representing the game board.

    Args:
        rowNum (int): Number of rows in the board.
        colNum (int): Number of columns in the board.
    """

    def __init__(self, rowNum, colNum) -> None:
        """
        For example:
            If temp = Board(2,2)
            temp. __grid is
            [[EMPTY Notation,EMPTY Notation ],
            [EMPTY Notation, EMPTY Notation]]
            The empty notation is what you define in the Notation Class."""
        self.__rowNum = rowNum
        self.__colNum = colNum
        self.__grid = [[Notation.EMPTY for _ in range(colNum)] for _ in range(rowNum)]

    def initGrid(self):
        """Initializes the game board with empty cells."""
        self.__grid = [
            [Notation.EMPTY for _ in range(self.__colNum)] for _ in range(self.__rowNum)
        ]

    def getColNum(self):
        """Returns the number of columns in the board."""
        return self.__colNum

    def placeMark(self, colNum, mark):
        """Attempts to place a mark on the board at the specified column.

        Args:
            colNum (int): The column number where the mark is to be placed.
            mark (Notation): The mark to be placed on the board.

        Returns:
            bool: True if the mark was successfully placed, False otherwise.
        """
        try:
            if colNum < 0 or colNum >= self.__colNum:  # check if the column number is valid
                print("Invalid column number")
                return False
            if mark == Notation.EMPTY:  # check if the mark is valid
                print("Invalid marker")
                return False
            for row in range(self.__rowNum - 1, -1, -1):  # loop from the bottom to the top
                if self.__grid[row][colNum] == Notation.EMPTY:
                    self.__grid[row][colNum] = mark
                    return True
            print("Column is full")  # if the column is full (no empty cells), return False
            return False
        except:
            return False

    def checkFull(self):
        """Checks if the board is completely filled.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        for row in range(self.__rowNum):
            for col in range(self.__colNum):
                if self.__grid[row][col] == Notation.EMPTY:
                    return False
        return True

    def display(self):
        """Displays the current state of the board."""

        boardStr = ""
        for row in range(self.__rowNum):  # loop through each row of the board
            for col in range(self.__colNum):  # for each cell in the row
                if (
                    self.__grid[row][col] == Notation.EMPTY
                ):  # append 'O' to boardStr if the cell contains Notation.EMPTY
                    boardStr += "O"
                elif (
                    self.__grid[row][col] == Notation.PLAYER1
                ):  # append 'R' to boardStr if the cell contains Notation.PLAYER1
                    boardStr += "R"
                else:  # append 'Y' to boardStr if the cell contains Notation.PLAYER2
                    boardStr += "Y"
            boardStr += "\n"
        print("Current Board is\n" + boardStr)

    # Private methods for internal use
    def __checkWinHorizontal(self, target):
        """
        This method is used to check if there is a win condition in the horizontal direction.
        Args:
            target (int): The number of consecutive marks needed for a win.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        try:
            for row in self.__grid:
                marks_in_a_row = 0
                previous_mark = Notation.EMPTY
                for mark in row:
                    if mark != Notation.EMPTY:
                        if mark == previous_mark:
                            marks_in_a_row += 1
                        else:
                            marks_in_a_row = 1
                        if marks_in_a_row == target:
                            return mark
                    else:
                        marks_in_a_row = 0
                    previous_mark = mark
            return None
        except:
            return None

    def __checkWinVertical(self, target):
        """
        This method is used to check if there is a win condition in the vertical direction.
        Args:
            target (int): The number of consecutive marks needed for a win.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        try:
            for col in range(len(self.__grid[0])):
                marks_in_a_row = 0
                previous_mark = Notation.EMPTY
                for row in range(len(self.__grid)):
                    mark = self.__grid[row][col]
                    if mark != Notation.EMPTY:
                        if mark == previous_mark:
                            marks_in_a_row += 1
                        else:
                            marks_in_a_row = 1
                        if marks_in_a_row == target:
                            return mark
                    else:
                        marks_in_a_row = 0
                    previous_mark = mark
            return None
        except:
            return None

    def __checkWinOneDiag(self, target, rowNum, colNum):
        """
        This method is used to check if there is a win condition in the diagonal direction. (from top left to bottom right)
        Uses specified row and column to start checking from.

        Args:
            target (int): The number of consecutive marks needed for a win.
            rowNum (int): The row number of the cell to start checking from.
            colNum (int): The column number of the cell to start checking from.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        try:
            if rowNum <= len(self.__grid) - target and colNum <= len(self.__grid[0]) - target:
                if self.__grid[rowNum][colNum] != Notation.EMPTY:
                    win = True
                    for i in range(1, target):
                        if self.__grid[rowNum][colNum] != self.__grid[rowNum + i][colNum + i]:
                            win = False
                            break
                    if win:
                        return self.__grid[rowNum][colNum]
            return None
        except:
            return None

    def __checkWinAntiOneDiag(self, target, rowNum, colNum):
        """
        This method is used to check if there is a win condition in the diagonal direction. (from bottom left to top right)
        Uses specified row and column number to start checking from.

        Args:
            target (int): The number of consecutive marks needed for a win.
            rowNum (int): The row number of the cell to start checking from.
            colNum (int): The column number of the cell to start checking from.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        try:
            if rowNum >= target - 1 and colNum <= len(self.__grid[0]) - target:
                if self.__grid[rowNum][colNum] != Notation.EMPTY:
                    win = True
                    for i in range(1, target):
                        if self.__grid[rowNum][colNum] != self.__grid[rowNum - i][colNum + i]:
                            win = False
                            break
                    if win:
                        return self.__grid[rowNum][colNum]
            return None
        except:
            return None

    def __checkWinDiagonal(self, target):
        """
        This method is used to check if there is a win condition in the diagonal direction.
        Args:
            target (int): The number of consecutive marks needed for a win.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        try:
            for row in range(self.__rowNum):
                for col in range(self.__colNum):
                    if self.__checkWinOneDiag(target, row, col) != None:
                        return self.__checkWinOneDiag(target, row, col)
                    elif self.__checkWinAntiOneDiag(target, row, col) != None:
                        return self.__checkWinAntiOneDiag(target, row, col)
            return None
        except:
            return None

    def checkWin(self, target):
        """Checks if there is a winning condition on the board.

        Args:
            target (int): The number of consecutive marks needed for a win.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        try:
            if self.__checkWinDiagonal(target) != None:
                return self.__checkWinDiagonal(target)
            elif self.__checkWinHorizontal(target) != None:
                return self.__checkWinHorizontal(target)
            elif self.__checkWinVertical(target) != None:
                return self.__checkWinVertical(target)
            else:
                return None
        except:
            return None

class Game:
    """Represents the game logic and flow.

    Args:
        rowNum (int): Number of rows in the game board.
        colNum (int): Number of columns in the game board.
        connectN (int): Number of consecutive marks needed for a win.
        targetScore (int): The score a player needs to reach to win the game.
        playerName1 (str): Name of the first player.
        playerName2 (str): Name of the second player.
    """

    def __init__(
        self, rowNum, colNum, connectN, targetScore, playerName1, playerName2
    ) -> None:
        self.__board = Board(rowNum, colNum)
        self.__player1 = Player(playerName1, Notation.PLAYER1, 0)
        self.__player2 = Player(playerName2, Notation.PLAYER2, 0)
        self.__playerList = [self.__player1, self.__player2]
        self.__curPlayer = self.__playerList[0]
        self.__connectN = connectN
        self.__targetScore = targetScore

    def __playBoard(self, curPlayer):
        """Handles the process of a player making a move on the board.

        Args:
            curPlayer (Player): The current player who is making the move.
        """

        isPlaced = False
        while not isPlaced:
            colNum = input(
                f"{curPlayer.getName()} ({curPlayer.getNotation().name}), please enter a column number: "
            )
            if colNum.isdigit() and int(colNum) < self.__board.getColNum():
                isPlaced = self.__board.placeMark(int(colNum), curPlayer.getNotation())
            else:
                print("Invalid input.")

    def __changeTurn(self):
        """Switches the turn to the other player."""
        if self.__curPlayer == self.__player1:
            self.__curPlayer = self.__player2
        else:
            self.__curPlayer = self.__player1

    def playRound(self):
        """Plays a single round of the game."""

        curWinnerNotation = None
        self.__board.initGrid()
        self.__curPlayer = self.__player1
        print("Starting a new round")
        while curWinnerNotation == None:
            self.__curPlayer.display()
            self.__board.display()
            self.__playBoard(self.__curPlayer)
            if self.__board.checkWin(self.__connectN) != None:
                curWinnerNotation = self.__board.checkWin(self.__connectN)
                print(f"{self.__curPlayer.getName()} wins!")
                self.__board.display()
                self.__curPlayer.addScoreByOne()
                break
            elif self.__board.checkFull():
                print("The board is full. It's a tie!")
                break
            self.__changeTurn()

    def play(self):
        """Starts and manages the game play until a player wins."""

        while self.__player1.getScore() < self.__targetScore and self.__player2.getScore() < self.__targetScore:
            self.playRound()
        print("Game Over")
        print(self.__player1.display())
        print(self.__player2.display())



def main():
    """Main function to start the game."""
    game = Game(4, 4, 3, 2, "P1", "P2")
    game.play()


if __name__ == "__main__":
    main()
