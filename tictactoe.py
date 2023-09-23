#Starting this by just writing a simple PvE tictactoe program

def createBoard():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board;

def drawBoard(board):
    rows = 3
    cols = 3
    for i in range(rows):
        if (i > 0):
            print("- - - - -")
        for j in range(cols):
            if(j == cols - 1):
                print(board[i][j])
                break
            print(board[i][j] + ' | ',end="")

board = createBoard()
drawBoard(board)