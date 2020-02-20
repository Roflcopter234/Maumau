from card import Card
from stapel import Stapel


class Game:
    def __init__(self, id):
        self.p1Played = False
        self.p2Played = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.points = [0, 0]
        self.wins = [0, 0]
        self.p1cards = []
        self.p2cards = []
        self.lastplayer = 2
        self.stapel = Stapel()
        self.ablage = None
        self.rest = []
        self.stapel.shuffle()

    def get_player_move(self, p):
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Played = True
            self.lastplayer = 1
        elif player == 1:
            self.p2Played = True
            self.lastplayer = 2

    def connected(self):
        return self.ready

    def onePlayed(self):
        return self.p1Played or self.p2Played

    def winner(self):
        if len(self.p1cards) == 0:
            return 0
        elif len(self.p2cards) == 0:
            return 1
        else:
            return -1

    def reset(self):
        self.p1Played = False
        self.p2Played = False

    def getStapel(self):
        return self.stapel

    def austeilen(self):
        if len(self.stapel.karten) == 32:
            for x in range(5):
                #self.stapel.karten.gettop()
                self.p1cards.append(self.stapel.karten.pop())
                self.p2cards.append(self.stapel.karten.pop())

            self.ablage = self.stapel.karten.pop()