import socket
from _thread import *
from game import Game
from card import Card
from stapel import Stapel
import pickle

server = "192.168.56.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for connection")

connected = set()
games = {}
idCount = 0
stapel = Stapel


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(pickle.dumps(p))                                  #conn.send(str.encode(str(p)))


    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096*2))            #data = conn.recv(4096*2).decode()

            if gameId in games:             #check if game still exists
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset()
                    elif data != "get":
                        game.play(p, data)          #executing the move that got sent

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost Connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to", addr)

    idCount += 1
    p = 0
    gameId = (idCount-1)//2     #number of games
    if idCount % 2 == 1:        #if you are first create new game
        games[gameId] = Game(gameId)
        print("Creating a new game..")
    else:
        games[gameId].ready = True
        p=1

    if games[gameId].ready:
        games[gameId].austeilen()

    start_new_thread(threaded_client, (conn, p, gameId))