import socket
import sys
import random
import time

address = ''
port = int(sys.argv[1])

client_list = []
current_player = 0

def manageGame():
    current_player = 0                              #this will handle the starting move logic for player 1 and 2
    client = client_list[0]
    client.send("client1_first".encode('utf-8'))
    client = client_list[1]
    client.send("client2_second".encode('utf-8'))
    try:
        while True:
            client = client_list[current_player]
            move = client.recv(1024).decode('utf-8')
            current_player = (current_player + 1) % len(client_list)
            client = client_list[current_player]
            client.send(move.encode('utf-8'))
    except: 
        print("An opponent has left the game.")
        for client in client_list:
            client.close()
    return      

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket creates on port: ' + str(port))
server.bind((address, port))
server.listen()
print('Listening...')

while True:
    print("Current client count: " + str(len(client_list)))
    if len(client_list) < 2:
        client, addr = server.accept()
        client_list.append(client)
        print('Connection from ' + str(addr))
        #client.send(tictactoe.drawBoard().encode('utf-8'))
    else:
        manageGame()
        for client in client_list:
            client.close()
        #client_list = []  # Reset the client list for the next game
