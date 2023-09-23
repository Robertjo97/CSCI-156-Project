#Starting this by just writing a simple PvE tictactoe program.
#This should satisfy milestone 1 in the project description.

#In this program, player will move first and be X's, cpu will move second and be O's.

import random
import time

class TicTacToe:

    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    
    moveCount = 0 #keeps track of number of moves for tie game scenario
    winner = False
    
    def drawBoard(self): #Draws a 3x3 grid
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

    def playerMove(self): #I know there's a better way to do this but I'll figure it out later lol
        
        x = input("Enter a move: ")

        if(x == "1"):
            if (self.board[0][0] != " "):
                print("error")
            else:
                self.board[0][0] = "X"
                self.moveCount += 1
        elif(x == "2"):
            if (self.board[0][1] != " "):
                print("error")
            else:
                self.board[0][1] = "X"
                self.moveCount += 1
        elif(x == "3"):
            if (self.board[0][2] != " "):
                print("error")
            else:
                self.board[0][2] = "X"
                self.moveCount += 1
        elif(x == "4"):
            if (self.board[1][0] != " "):
                print("error")
            else:
                self.board[1][0] = "X"
                self.moveCount += 1
        elif(x == "5"):
            if (self.board[1][1] != " "):
                print("error")
            else:
                self.board[1][1] = "X"
                self.moveCount += 1
        elif(x == "6"):
            if (self.board[1][2] != " "):
                print("error")
            else:
                self.board[1][2] = "X"
                self.moveCount += 1
        elif(x == "7"):
            if (self.board[2][0] != " "):
                print("error")
            else:
                self.board[2][0] = "X"
                self.moveCount += 1
        elif(x == "8"):
            if (self.board[2][1] != " "):
                print("error")
            else:
                self.board[2][1] = "X"
                self.moveCount += 1
        elif(x == "9"):
            if (self.board[2][2] != " "):
                print("error")
            else:
                self.board[2][2] = "X"
                self.moveCount += 1

    def cpuMove(self): #Dumb Cpu. For now it just randomly picks an available move. It doesnt take into account player moves yet.
        possRows = [0,1,2]
        possCols = [0,1,2]
        moveMade = False

        while(moveMade == False):
            moveRow = random.choice(possRows)
            movCol = random.choice(possCols)
            if(self.board[moveRow][movCol] == " "):
                self.board[moveRow][movCol] = "O"
                moveMade = True
                self.moveCount += 1
                return

    def winScan(self): #Scans the game board for a win. Again, there's prob a better way to do this.
        for i in range (3):

            #Horizontal win condition
            if(self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] != " "):
                winner = self.board[i][0]
                print("Game Over: " + winner + " Wins!")
                self.winner = True
                return
            
            #Vertical win condition
            if(self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] != " "):
                winner = self.board[0][i]
                print("Game Over: " + winner + " Wins!")
                self.winner = True
                return
            
            #Diagonal win condition
            if(self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != " "):
                winner = self.board[0][0]
                print("Game Over: " + winner + " Wins!")
                self.winner = True
                return
            if(self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != " "):
                winner = self.board[0][2]
                print("Game Over: " + winner + " Wins!")
                self.winner = True
                return
    
    def init(self): #Main game loop
        print("Welcome to TicTacToe")
        self.drawBoard()
        while True:
            tictactoe.playerMove()
            tictactoe.drawBoard()
            tictactoe.winScan()
            if(self.winner == True):
                break
            elif(self.winner == False and self.moveCount == 9):
                print("Game Over: Tie Game!")
                break
            tictactoe.cpuMove()
            time.sleep(0.5)
            tictactoe.drawBoard()
            tictactoe.winScan()
            if(self.winner == True):
                break
            elif(self.winner == False and self.moveCount == 9):
                print("Game Over: Tie Game!")
                break
            
tictactoe = TicTacToe()
tictactoe.init()

