

class Card:
    def __init__(self, zahl, farbe):
        self.zahl = zahl
        self.farbe = farbe
        self.img = "img/" + str(farbe) + str(zahl) + ".png"

    def passt(self, stapel, card):
        if stapel.zahl == card.zahl:
            return True
        elif stapel.farbe == card.farbe:
            return True
        elif card.zahl == 11:
            return True
        else:
            return False