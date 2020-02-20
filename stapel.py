from card import Card
import random


class Stapel:
    def __init__(self):
        self.karten = []
        self.farben = ["herz", "eichel", "blatt", "schellen"]

        for i in self.farben:
            for x in range(7, 15):
                self.karten.append(Card(x, i))

        #self.top = self.karten[-1]

    def shuffle(self):
        return random.shuffle(self.karten)

    def gettop(self):
        return self.karten[-1]