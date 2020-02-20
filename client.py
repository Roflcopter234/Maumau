import pygame
import math
from network import Network
from game import Game
import pickle
pygame.font.init()

width = 900
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.width = 145
        self.height = 250
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("arial", 35)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def show_cards(win, game, p):
    if p == 0:
        if len(game.p1cards) == 1:
            show_cards_u(win, game, p, 1)
        elif len(game.p1cards) == 2:
            show_cards_u(win, game, p, 2)
        elif len(game.p1cards) == 3:
            show_cards_u(win, game, p, 3)
        elif len(game.p1cards) == 4:
            show_cards_u(win, game, p, 4)
        elif len(game.p1cards) == 5:
            show_cards_u(win, game, p, 5)
        elif len(game.p1cards) == 6:
            show_cards_u(win, game, p, 6)
        elif len(game.p1cards) == 7:
            show_cards_o(win, game, p, 7)
        elif len(game.p1cards) == 8:
            show_cards_o(win, game, p, 8)
        elif len(game.p1cards) == 9:
            show_cards_o(win, game, p, 9)
        elif len(game.p1cards) == 10:
            show_cards_o(win, game, p, 10)
        elif len(game.p1cards) == 11:
            show_cards_o(win, game, p, 11)
        elif len(game.p1cards) == 12:
            show_cards_o(win, game, p, 12)
        elif len(game.p1cards) == 13:
            show_cards_o(win, game, p, 13)
        elif len(game.p1cards) == 14:
            show_cards_o(win, game, p, 14)
    elif p == 1:
        if len(game.p2cards) == 1:
            show_cards_uu(win, game, p, 1)
        elif len(game.p2cards) == 2:
            show_cards_uu(win, game, p, 2)
        elif len(game.p2cards) == 3:
            show_cards_uu(win, game, p, 3)
        elif len(game.p2cards) == 4:
            show_cards_uu(win, game, p, 4)
        elif len(game.p2cards) == 5:
            show_cards_uu(win, game, p, 5)
        elif len(game.p2cards) == 6:
            show_cards_uu(win, game, p, 6)
        elif len(game.p2cards) == 7:
            show_cards_oo(win, game, p, 7)
        elif len(game.p2cards) == 8:
            show_cards_oo(win, game, p, 8)
        elif len(game.p2cards) == 9:
            show_cards_oo(win, game, p, 9)
        elif len(game.p2cards) == 10:
            show_cards_oo(win, game, p, 10)
        elif len(game.p2cards) == 11:
            show_cards_oo(win, game, p, 11)
        elif len(game.p2cards) == 12:
            show_cards_oo(win, game, p, 12)
        elif len(game.p2cards) == 13:
            show_cards_oo(win, game, p, 13)
        elif len(game.p2cards) == 14:
            show_cards_oo(win, game, p, 14)


def show_cards_u(win, game, p, anzahl):
    slot = []
    breite = 145 * anzahl
    startpunkt = 450 - breite/anzahl
    for x in range(anzahl):
        slot.append(startpunkt + x*145)

    for x in range(anzahl):
        k1 = pygame.image.load(game.p1cards[x].img)
        k1 = pygame.transform.scale(k1, (145, 250))
        win.blit(k1, (slot[x], 740))

        btns1.append(Button("", slot[x], 740, (255, 255, 255)))
    #450 => 377
    #145*1 = 145 => 377
    #145*2 = 290 =>
    #145*3 = 435 =>


def show_cards_o(win, game, p, anzahl):
    slot = []
    breite = math.floor(755/anzahl-1)
    rest = 755 - breite * anzahl-1
    for x in range(anzahl-1):
        slot.append(rest + x*breite)

    for x in range(anzahl-1):
        k1 = pygame.image.load(game.p1cards[x].img)
        k1 = pygame.transform.scale(k1, (145, 250))
        win.blit(k1, (slot[x], 740))

        btns1.append(Button("", slot[x], 740, (255, 255, 255)))
    #7*145 = 1015 => 870 für 6 =>
    #8*145 = 1160 => 1015 für 7 =>


def show_cards_uu(win, game, p, anzahl):
    slot = []
    breite = 145 * anzahl
    startpunkt = 450 - breite / anzahl
    for x in range(anzahl):
        slot.append(startpunkt + x * 145)

    for x in range(anzahl):
        k1 = pygame.image.load(game.p2cards[x].img)
        k1 = pygame.transform.scale(k1, (145, 250))
        win.blit(k1, (slot[x], 740))

        btns2.append(Button("", slot[x], 740, (255, 255, 255)))
    # 450 => 377
    # 145*1 = 145 => 377
    # 145*2 = 290 =>
    # 145*3 = 435 =>


def show_cards_oo(win, game, p, anzahl):
    slot = []
    breite = math.floor(755 / anzahl - 1)
    rest = 755 - breite * anzahl - 1
    for x in range(anzahl - 1):
        slot.append(rest + x * breite)

    for x in range(anzahl - 1):
        k1 = pygame.image.load(game.p2cards[x].img)
        k1 = pygame.transform.scale(k1, (145, 250))
        win.blit(k1, (slot[x], 740))

        btns2.append(Button("", slot[x], 740, (255, 255, 255)))
    # 7*145 = 1015 => 870 für 6 =>
    # 8*145 = 1160 => 1015 für 7 =>


def redrawWindow(win, game, p):
    win.fill((128, 128, 128))

    if not (game.connected()):
        font = pygame.font.SysFont("arial", 40)
        text = font.render("Waiting for Players", 1, (255, 0, 0))
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("arial", 40)
        text = font.render("Player1", 1, (255, 0, 0))
        win.blit(text, (180, 600))

        text = font.render("Player2", 1, (255, 0, 0))
        win.blit(text, (680, 100))

        for btnn in btns:
            btnn.draw(win)

        rueckseite = pygame.image.load('img/back.png')
        rueckseite = pygame.transform.scale(rueckseite, (145, 250))
        win.blit(rueckseite, (290, 340))

        ablage = pygame.image.load(game.ablage.img)
        #ablage = pygame.image.load('img/eichel7.png')
        ablage = pygame.transform.scale(ablage, (145, 250))
        win.blit(ablage, (460, 340))

        #karten anzeigen
        show_cards(win, game, p)


    pygame.display.update()


btns = [Button("", 290, 340, (255, 255, 255)), Button("", 460, 340, (255, 255, 255))]
btns1 = []
btns2 = []

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldnt get game")
            break

        if game.winner() != -1:
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldnt get game")
                break

            font = pygame.font.SysFont("arial", 60)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You won!", 1, (255, 0, 0))
            elif game.winner == -1:
                pass
            else:
                text = font.render("You lost!", 1, (255, 0, 0))

            win.blit(text, (300, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if game.lastplayer == 2:
                                n.send(btn.text)            #send the move that the server needs to do
                        else:
                            if game.lastplayer == 1:
                                n.send(btn.text)
        redrawWindow(win, game, player)

        game.p1Played = False
        game.p2Played = False


main()


"""def show_cards(win, game, p):
    if p == 0:
        if len(game.p1cards) == 1:
            k1 = pygame.image.load(game.p1cards[0].img)
            k1 = pygame.transform.scale(k1, (145, 250))
            win.blit(k1, (377, 740))

            btns1.append(Button("", 377, 740, (255, 255, 255)))
        elif len(game.p1cards) == 2:
            k1 = pygame.image.load(game.p1cards[0].img)
            k1 = pygame.transform.scale(k1, (145, 250))
            win.blit(k1, (305, 740))
            k2 = pygame.image.load(game.p1cards[1].img)
            k2 = pygame.transform.scale(k2, (145, 250))
            win.blit(k2, (450, 740))

            btns1.append(Button("", 305, 740, (255, 255, 255)))
            btns1.append(Button("", 450, 740, (255, 255, 255)))
        elif len(game.p1cards) == 3:
            k1 = pygame.image.load(game.p1cards[0].img)
            k1 = pygame.transform.scale(k1, (145, 250))
            win.blit(k1, (232, 740))
            k2 = pygame.image.load(game.p1cards[1].img)
            k2 = pygame.transform.scale(k2, (145, 250))
            win.blit(k2, (377, 740))
            k3 = pygame.image.load(game.p1cards[2].img)
            k3 = pygame.transform.scale(k3, (145, 250))
            win.blit(k3, (522, 740))

            btns1.append(Button("", 232, 740, (255, 255, 255)))
            btns1.append(Button("", 377, 740, (255, 255, 255)))
            btns1.append(Button("", 522, 740, (255, 255, 255)))
        elif len(game.p1cards) == 4:
            k1 = pygame.image.load(game.p1cards[0].img)
            k1 = pygame.transform.scale(k1, (145, 250))
            win.blit(k1, (160, 740))
            k2 = pygame.image.load(game.p1cards[1].img)
            k2 = pygame.transform.scale(k2, (145, 250))
            win.blit(k2, (305, 740))
            k3 = pygame.image.load(game.p1cards[2].img)
            k3 = pygame.transform.scale(k3, (145, 250))
            win.blit(k3, (450, 740))
            k4 = pygame.image.load(game.p1cards[3].img)
            k4 = pygame.transform.scale(k4, (145, 250))
            win.blit(k4, (595, 740))

            btns1.append(Button("", 160, 740, (255, 255, 255)))
            btns1.append(Button("", 305, 740, (255, 255, 255)))
            btns1.append(Button("", 450, 740, (255, 255, 255)))
            btns1.append(Button("", 595, 740, (255, 255, 255)))
        elif len(game.p1cards) == 5:
            k1 = pygame.image.load(game.p1cards[0].img)
            k1 = pygame.transform.scale(k1, (145, 250))
            win.blit(k1, (87, 740))
            k2 = pygame.image.load(game.p1cards[1].img)
            k2 = pygame.transform.scale(k2, (145, 250))
            win.blit(k2, (232, 740))
            k3 = pygame.image.load(game.p1cards[2].img)
            k3 = pygame.transform.scale(k3, (145, 250))
            win.blit(k3, (377, 740))
            k4 = pygame.image.load(game.p1cards[3].img)
            k4 = pygame.transform.scale(k4, (145, 250))
            win.blit(k4, (522, 740))
            k5 = pygame.image.load(game.p1cards[4].img)
            k5 = pygame.transform.scale(k5, (145, 250))
            win.blit(k5, (667, 740))

            btns1.append(Button("", 87, 740, (255, 255, 255)))
            btns1.append(Button("", 232, 740, (255, 255, 255)))
            btns1.append(Button("", 377, 740, (255, 255, 255)))
            btns1.append(Button("", 522, 740, (255, 255, 255)))
            btns1.append(Button("", 667, 740, (255, 255, 255)))
        elif len(game.p1cards) == 6:

        elif len(game.p1cards) == 7:

        elif len(game.p1cards) == 8:"""


def show_cards(win, game, p):
    if p == 0:
        if len(game.p1cards) == 1:
            show_cards_u(win, game, p, 1)
        elif len(game.p1cards) == 2:
            show_cards_u(win, game, p, 2)
        elif len(game.p1cards) == 3:
            show_cards_u(win, game, p, 3)
        elif len(game.p1cards) == 4:
            show_cards_u(win, game, p, 4)
        elif len(game.p1cards) == 5:
            show_cards_u(win, game, p, 5)
        elif len(game.p1cards) == 6:
            show_cards_u(win, game, p, 6)
        elif len(game.p1cards) == 7:
            show_cards_o(win, game, p, 7)
        elif len(game.p1cards) == 8:
            show_cards_o(win, game, p, 8)
        elif len(game.p1cards) == 9:
            show_cards_o(win, game, p, 9)
        elif len(game.p1cards) == 10:
            show_cards_o(win, game, p, 10)
        elif len(game.p1cards) == 11:
            show_cards_o(win, game, p, 11)
        elif len(game.p1cards) == 12:
            show_cards_o(win, game, p, 12)
        elif len(game.p1cards) == 13:
            show_cards_o(win, game, p, 13)
        elif len(game.p1cards) == 14:
            show_cards_o(win, game, p, 14)
    elif p == 1:
        if len(game.p2cards) == 1:
            show_cards_uu(win, game, p, 1)
        elif len(game.p2cards) == 2:
            show_cards_uu(win, game, p, 2)
        elif len(game.p2cards) == 3:
            show_cards_uu(win, game, p, 3)
        elif len(game.p2cards) == 4:
            show_cards_uu(win, game, p, 4)
        elif len(game.p2cards) == 5:
            show_cards_uu(win, game, p, 5)
        elif len(game.p2cards) == 6:
            show_cards_uu(win, game, p, 6)
        elif len(game.p2cards) == 7:
            show_cards_oo(win, game, p, 7)
        elif len(game.p2cards) == 8:
            show_cards_oo(win, game, p, 8)
        elif len(game.p2cards) == 9:
            show_cards_oo(win, game, p, 9)
        elif len(game.p2cards) == 10:
            show_cards_oo(win, game, p, 10)
        elif len(game.p2cards) == 11:
            show_cards_oo(win, game, p, 11)
        elif len(game.p2cards) == 12:
            show_cards_oo(win, game, p, 12)
        elif len(game.p2cards) == 13:
            show_cards_oo(win, game, p, 13)
        elif len(game.p2cards) == 14:
            show_cards_oo(win, game, p, 14)


def show_cards_u(win, game, p, anzahl):
    slot = []
    breite = 145 * anzahl
    startpunkt = 450 - breite/anzahl
    for x in range(anzahl):
        slot.append(startpunkt + x*145)

    for x in range(anzahl):
        k1 = pygame.image.load(game.p1cards[x].img)
        k1 = pygame.transform.scale(k1, (145, 250))
        win.blit(k1, (slot[x], 740))

        btns1.append(Button("", slot[x], 740, (255, 255, 255)))
    #450 => 377
    #145*1 = 145 => 377
    #145*2 = 290 =>
    #145*3 = 435 =>


def show_cards_o(win, game, p, anzahl):
    slot = []
    breite = math.floor(755/anzahl-1)
    rest = 755 - breite * anzahl-1
    for x in range(anzahl-1):
        slot.append(rest + x*breite)

    for x in range(anzahl-1):
        k1 = pygame.image.load(game.p1cards[x].img)
        k1 = pygame.transform.scale(k1, (145, 250))
        win.blit(k1, (slot[x], 740))

        btns1.append(Button("", slot[x], 740, (255, 255, 255)))
    #7*145 = 1015 => 870 für 6 =>
    #8*145 = 1160 => 1015 für 7 =>


def show_cards_uu(win, game, p, anzahl):
    slot = []
    breite = 145 * anzahl
    startpunkt = 450 - breite / anzahl
    for x in range(anzahl):
        slot.append(startpunkt + x * 145)

    for x in range(anzahl):
        k1 = pygame.image.load(game.p1cards[x].img)
        k1 = pygame.transform.scale(k1, (145, 250))
        win.blit(k1, (slot[x], 740))

        btns2.append(Button("", slot[x], 740, (255, 255, 255)))
    # 450 => 377
    # 145*1 = 145 => 377
    # 145*2 = 290 =>
    # 145*3 = 435 =>


def show_cards_oo(win, game, p, anzahl):
    slot = []
    breite = math.floor(755 / anzahl - 1)
    rest = 755 - breite * anzahl - 1
    for x in range(anzahl - 1):
        slot.append(rest + x * breite)

    for x in range(anzahl - 1):
        k1 = pygame.image.load(game.p1cards[x].img)
        k1 = pygame.transform.scale(k1, (145, 250))
        win.blit(k1, (slot[x], 740))

        btns2.append(Button("", slot[x], 740, (255, 255, 255)))
    # 7*145 = 1015 => 870 für 6 =>
    # 8*145 = 1160 => 1015 für 7 =>