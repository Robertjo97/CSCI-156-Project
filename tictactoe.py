# Starting this by just writing a simple PvE tictactoe program.
# This should satisfy milestone 1 in the project description.

# In this program, player will move first and be X's, cpu will move second and be O's.
# test comment --Julian

import random
import time
import tkinter

root = tkinter.Tk() #Create root gui object
root.title("CSCI-156 Tic Tac Toe") #Title the window
player1 = True #Keeps track of X's and O's. Player 1 is X's.

buttons = [] #Array that holds the buttons
squaresUsed = [False for _ in range(9)] #Array that keeps track if a move has been made in a tile.

def restart_game(): #Function to restart the game
    global player1, squaresUsed #Global variables to be reset
    for button in buttons: #Change button text back to " "
        button.config(text=" ")
    squaresUsed = [False for _ in range(9)] #Set all squares back to unused (false)
    player1 = True  #Set starting player back to X's

playAgain = tkinter.Button(root, text="Restart", width=20, height=10, command=restart_game)  #Creates button to restart game
playAgain.grid(row=3, column=0) #Places button on grid

end = tkinter.Button(root, text="Exit", width=20, height=10, command=root.quit) #Creates button to end game
end.grid(row=3, column=2)   #Places button on grid

'''def cpuMove(self): #Dumb Cpu. For now it just randomly picks an available move. It doesnt take into account player moves yet.
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
                return'''
def cpuMove():
    print('undefined')
    #make cpu logic
    #use time.sleep(0.5)

def winScan():  #Function to scan the grid for win conditions
    
    if ( #Check if three squares in a row have the same value
        buttons[0].cget("text") != " "                              #Top Horizontal
        and buttons[0].cget("text") == buttons[1].cget("text")
        and buttons[0].cget("text") == buttons[2].cget("text")
        
        or buttons[3].cget("text") != " "                           #Mid Horizontal
        and buttons[3].cget("text") == buttons[4].cget("text")
        and buttons[3].cget("text") == buttons[5].cget("text")
        
        or buttons[6].cget("text") != " "                           #Bot Horizontal
        and buttons[6].cget("text") == buttons[7].cget("text")
        and buttons[6].cget("text") == buttons[8].cget("text")

        or buttons[0].cget("text") != " "                           #Left Verical
        and buttons[0].cget("text") == buttons[3].cget("text")
        and buttons[0].cget("text") == buttons[6].cget("text")

        or buttons[1].cget("text") != " "                           #Mid Vertical
        and buttons[1].cget("text") == buttons[4].cget("text")
        and buttons[1].cget("text") == buttons[7].cget("text")

        or buttons[2].cget("text") != " "                           #Right Vertical
        and buttons[2].cget("text") == buttons[5].cget("text")
        and buttons[2].cget("text") == buttons[8].cget("text")

        or buttons[0].cget("text") != " "                           #Left->Right Diagonal
        and buttons[0].cget("text") == buttons[4].cget("text")
        and buttons[0].cget("text") == buttons[8].cget("text")

        or buttons[2].cget("text") != " "                           #Right->Left Diagonal
        and buttons[2].cget("text") == buttons[4].cget("text")
        and buttons[2].cget("text") == buttons[6].cget("text")
    ):
        print("winner") #Print winner
          
    if(all(squaresUsed)):   #Check if all squares are true (indicating used)
        print("Tie Game")   #Print Tie Game


def click(index):    #Function to handle click event
    global player1  #Global player1 variable (Keeps track of which player is making a move)
    if player1 and (squaresUsed[index] == False):   #If player is player 1 and the square clicked hasn't been used: 
        buttons[index].config(text="X")    #set the clicked button to X
        squaresUsed[index] = True   #Mark off the tile as being used
        player1 = False #Set to player 2
    elif (player1 == False) and (squaresUsed[index] == False):  #Same logic but if its player2's turn
        buttons[index].config(text="O")
        squaresUsed[index] = True
        player1 = True
    winScan()   #Check for a winner by calling the winScan function
    cpuMove()


for i in range(3):  #Loops to create buttons
    for j in range(3):
        button = tkinter.Button(
            root, text=" ", height=10, width=20, command=lambda i=i, j=j: click((i * 3 + j))   #On click, calls the click function. Passes in an index value resulting from the conversion of the i and j coordinates to a 1d array.
        )
        button.grid(row=i, column=j) #Places button on grid to its respctive i and j coordinates.
        buttons.append(button)  #Adds button to the buttons array


root.mainloop() #Start main loop
