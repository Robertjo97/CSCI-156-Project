import random
import time
import socket
import sys

address = str(sys.argv[1])
port = int(sys.argv[2])
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((address,port))
res = client_socket.recv(1024).decode('utf-8')          # receives welcome message from server
print(res)
choice = input()
client_socket.send(choice.encode('utf-8'))
res2 = client_socket.recv(1024).decode('utf-8')         # receives confirmation message from serv
print(res2)


class TicTacToe:

    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    
    moveCount = 0 #keeps track of number of moves for tie game scenario
    winner = False
    isPlayer1 = False
    
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

    def playerMove(self, x): #takes in player move, prints it to the board, and increments moveCount

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

    def player2Move(self, oppMove): #prints other player's move to the board and increments moveCount
        x = oppMove

        if(x == "1"):
            if (self.board[0][0] != " "):
                print("error")
            else:
                self.board[0][0] = "O"
                self.moveCount += 1
        elif(x == "2"):
            if (self.board[0][1] != " "):
                print("error")
            else:
                self.board[0][1] = "O"
                self.moveCount += 1
        elif(x == "3"):
            if (self.board[0][2] != " "):
                print("error")
            else:
                self.board[0][2] = "O"
                self.moveCount += 1
        elif(x == "4"):
            if (self.board[1][0] != " "):
                print("error")
            else:
                self.board[1][0] = "O"
                self.moveCount += 1
        elif(x == "5"):
            if (self.board[1][1] != " "):
                print("error")
            else:
                self.board[1][1] = "O"
                self.moveCount += 1
        elif(x == "6"):
            if (self.board[1][2] != " "):
                print("error")
            else:
                self.board[1][2] = "O"
                self.moveCount += 1
        elif(x == "7"):
            if (self.board[2][0] != " "):
                print("error")
            else:
                self.board[2][0] = "O"
                self.moveCount += 1
        elif(x == "8"):
            if (self.board[2][1] != " "):
                print("error")
            else:
                self.board[2][1] = "O"
                self.moveCount += 1
        elif(x == "9"):
            if (self.board[2][2] != " "):
                print("error")
            else:
                self.board[2][2] = "O"
                self.moveCount += 1

    def cpuMove(self): #Dumb Cpu. It just randomly picks an available move. It doesnt take into account player moves.
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

    def winScan(self): #Scans the game board for a win.
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
            
    def vsPlayer(self):                     #handles logic for Player vs. Player
        msg = client_socket.recv(1024).decode('utf-8')          #recieves message for whose turn it is first
        if(msg == 'client1_first'):
            self.isPlayer1 = True
            while True:                     # player 1 move loop
                self.drawBoard()
                tictactoe.winScan()
                if(self.winner == True):
                    break
                elif(self.winner == False and self.moveCount == 9):
                    print("Game Over: Tie Game!")
                    break
                x = input("Enter a move: ")
                tictactoe.playerMove(x)
                tictactoe.drawBoard()
                tictactoe.winScan()
                if(self.winner == True):
                    client_socket.send(x.encode('utf-8'))
                    break
                elif(self.winner == False and self.moveCount == 9):
                    print("Game Over: Tie Game!")
                    client_socket.send(x.encode('utf-8'))
                    break
                client_socket.send(x.encode('utf-8'))
                tictactoe.wait_for_opp_move()
        else:
            while True:                      # player 2 move loop
                tictactoe.wait_for_opp_move()
                self.drawBoard()
                tictactoe.winScan()
                if(self.winner == True):
                    client_socket.send(x.encode('utf-8'))
                    break
                elif(self.winner == False and self.moveCount == 9):
                    print("Game Over: Tie Game!")
                    client_socket.send(x.encode('utf-8'))
                    break
                x = input("Enter a move: ")
                tictactoe.player2Move(x)
                tictactoe.drawBoard()
                tictactoe.winScan()
                if(self.winner == True):
                    break
                elif(self.winner == False and self.moveCount == 9):
                    print("Game Over: Tie Game!")
                    break
                client_socket.send(x.encode('utf-8'))
    
    def init(self): #Main game loop for Player vs. CPU
        self.drawBoard()
        while True:
            x = input("Enter a move: ")
            tictactoe.playerMove(x)
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
    
    def wait_for_opp_move(self):            # waits for move from other player and redraws the board with their selected move
        if(self.isPlayer1 == True):
            print("Waiting for other player's move...")
            oppMove = client_socket.recv(1024).decode('utf-8')      # receives move from other player
            tictactoe.player2Move(oppMove)
            return
        else:
            print("Waiting for other player's move...")
            oppMove = client_socket.recv(1024).decode('utf-8')      # receives move from other player
            tictactoe.playerMove(oppMove)
            return


if(choice == '1'):          # starts game with CPU if choice is 1   
    tictactoe = TicTacToe()
    tictactoe.init()        # starts game with CPU if choice is 1
else:                       # starts game with player if choice is 2
    tictactoe = TicTacToe()
    tictactoe.vsPlayer()

