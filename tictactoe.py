#Starting this by just writing a simple PvE tictactoe program.
#This should satisfy milestone 1 in the project description.

class TicTacToe:

    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    def drawBoard(self):
        rows = 3
        cols = 3
        for i in range(rows):
            if (i > 0):
                print("- - - - -")
            for j in range(cols):
                if(j == cols - 1):
                    print(self.board[i][j])
                    break
                print(self.board[i][j] + ' | ',end="")


tictactoe = TicTacToe()
tictactoe.drawBoard()