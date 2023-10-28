# Starting this by just writing a simple PvE tictactoe program.
# This should satisfy milestone 1 in the project description.

# In this program, player will move first and be X's, cpu will move second and be O's.
# test comment --Julian

import random
import time
import tkinter

root = tkinter.Tk()
root.title("CSCI-156 Tic Tac Toe")
player1 = True

buttons = []
squaresUsed = [False for _ in range(9)]

def click(i, j):
    global player1
    if (player1 and (squaresUsed[i * 3 + j] == False)):
        buttons[i * 3 + j].config(text='X')
        squaresUsed[i * 3 + j] = True
        player1 = False
    elif ((player1 == False) and (squaresUsed[i * 3 + j] == False)):
        buttons[i * 3 + j].config(text='O')
        squaresUsed[i * 3 + j] = True
        player1 = True

for i in range(3):
    for j in range(3):
        button = tkinter.Button(root, text=str(i) + ', ' + str(j), height=10,width=20, command=lambda i=i, j=j: click(i, j))
        button.grid(row=i,column=j)
        buttons.append(button)

root.mainloop()
