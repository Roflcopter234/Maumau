

class Card:
    def __init__(self, zahl, farbe):
        self.zahl = zahl
        self.farbe = farbe
        self.img = "img/" + str(farbe) + str(zahl) + ".png"

    def passt(self, card):
        if self.zahl == card.zahl:
            return True
        elif self.farbe == card.farbe:
            return True
        elif self.zahl == 11:
            return True
        else:
            return False
