import pygame as pg
import time
import copy
import statistics

class Window:
    def __init__(self, size):
        # PARAMETERS
        self.WIDTH = 48 * size + 50 #50px pentru padding
        self.HEIGHT = 24 * size + 50
        self.FPS = 60
        self.CAPTION = "Marian Dimofte Hex"
        self.IMAGE = "images/Favicon.png"

        pg.init()
        pg.display.set_caption(self.CAPTION)
        if self.IMAGE != "": #daca gaseste faviconul il incarca
            icon = pg.image.load(self.IMAGE)
            pg.display.set_icon(icon)

        self.SCREEN = pg.Surface([self.WIDTH, self.HEIGHT]) #canvas-ul
        self.WINDOW = pg.display.set_mode((int(self.WIDTH), int(self.HEIGHT))) #fereastra care se vede
        self.CLOCK = pg.time.Clock()

    def draw(self, tablaJoc):
        hexagonEmpty = pg.image.load("images/hexagonEmpty.png")
        hexagonRed = pg.image.load("images/hexagonRed.png")
        hexagonRed2 = pg.image.load("images/hexagonRed2.png")
        hexagonBlue = pg.image.load("images/hexagonBlue.png")
        hexagonBlue2 = pg.image.load("images/hexagonBlue2.png")
        for i in range(tablaJoc.size):
            for j in range(tablaJoc.size):
                if tablaJoc.map[i][j] == '0':
                    self.SCREEN.blit(hexagonEmpty, (20 + j * 32 + i * 16, 20 + i * 24))
                if tablaJoc.map[i][j] == '1':
                    self.SCREEN.blit(hexagonBlue, (20 + j * 32 + i * 16, 20 + i * 24))
                if tablaJoc.map[i][j] == 'a':
                    self.SCREEN.blit(hexagonBlue2, (20 + j * 32 + i * 16, 20 + i * 24))
                if tablaJoc.map[i][j] == '2':
                    self.SCREEN.blit(hexagonRed, (20 + j * 32 + i * 16, 20 + i * 24))
                if tablaJoc.map[i][j] == 'b':
                    self.SCREEN.blit(hexagonRed2, (20 + j * 32 + i * 16, 20 + i * 24))

    def update(self, tablaJoc):
        self.draw(tablaJoc)
        pg.transform.scale(self.SCREEN, (int(self.WIDTH), int(self.HEIGHT)), self.WINDOW)
        self.CLOCK.tick(self.FPS)
        pg.display.update()

class TablaJoc:
    def __init__(self, size):
        self.size = size
        self.map = [['0'for j in range (size)] for i in range (size)]
        self.drumCastigator = []
        self.vizitat = []

    # def MaiSuntLocuri(self):                  #folosit sa verific daca se termina in remiza. am citit pe wikipedia ca nu se poate termina in remiza deci functia nu mai are sens
    #     for l in self.map:
    #         for x in l:
    #             if x == '0':
    #                 return False
    #     return True

    def PozitiePermisa(self, linie, coloana):
        return self.map[linie][coloana] == '0'

    def DfsLinie(self, pozitieCurenta):
        if pozitieCurenta[1] == self.size - 1:
            self.drumCastigator = [pozitieCurenta]
            return True
        self.vizitat.append(pozitieCurenta)

        if pozitieCurenta[0] > 0 and pozitieCurenta[1] != 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] - 1][pozitieCurenta[1]] and (pozitieCurenta[0] - 1, pozitieCurenta[1]) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0] - 1, pozitieCurenta[1])):
                self.drumCastigator.append(pozitieCurenta)
                return True

        if pozitieCurenta[1] > 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0]][pozitieCurenta[1] - 1] and (pozitieCurenta[0], pozitieCurenta[1] - 1) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0], pozitieCurenta[1] - 1)):
                self.drumCastigator.append(pozitieCurenta)
                return True

        if pozitieCurenta[0] < self.size - 1 and pozitieCurenta[1] != 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] + 1][pozitieCurenta[1]] and (pozitieCurenta[0] + 1, pozitieCurenta[1]) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0] + 1, pozitieCurenta[1])):
                self.drumCastigator.append(pozitieCurenta)
                return True

        if pozitieCurenta[1] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0]][pozitieCurenta[1] + 1] and (pozitieCurenta[0], pozitieCurenta[1] + 1) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0], pozitieCurenta[1] + 1)):
                self.drumCastigator.append(pozitieCurenta)
                return True

        if pozitieCurenta[0] > 0 and pozitieCurenta[1] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] - 1][pozitieCurenta[1] + 1] and (pozitieCurenta[0] - 1, pozitieCurenta[1] + 1) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0] - 1, pozitieCurenta[1] + 1)):
                self.drumCastigator.append(pozitieCurenta)
                return True

        if pozitieCurenta[1] > 0 and pozitieCurenta[0] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] + 1][pozitieCurenta[1] - 1] and (pozitieCurenta[0] + 1, pozitieCurenta[1] - 1) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0] + 1, pozitieCurenta[1] - 1)):
                self.drumCastigator.append(pozitieCurenta)
                return True

        return False

    def DfsColoana(self, pozitieCurenta):
        if pozitieCurenta[0] == self.size - 1:
            self.drumCastigator = [pozitieCurenta]
            return True
        self.vizitat.append(pozitieCurenta)

        if pozitieCurenta[0] > 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] - 1][pozitieCurenta[1]] and (pozitieCurenta[0] - 1, pozitieCurenta[1]) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0] - 1, pozitieCurenta[1])):
                self.drumCastigator.append(pozitieCurenta)
                return True

        if pozitieCurenta[1] > 0 and pozitieCurenta[0] != 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0]][pozitieCurenta[1] - 1] and (pozitieCurenta[0], pozitieCurenta[1] - 1) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0], pozitieCurenta[1] - 1)):
                self.drumCastigator.append(pozitieCurenta)
                return True

        if pozitieCurenta[0] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] + 1][pozitieCurenta[1]] and (pozitieCurenta[0] + 1, pozitieCurenta[1]) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0] + 1, pozitieCurenta[1])):
                self.drumCastigator.append(pozitieCurenta)
                return True

        if pozitieCurenta[1] < self.size - 1 and pozitieCurenta[0] != 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0]][pozitieCurenta[1] + 1] and (pozitieCurenta[0], pozitieCurenta[1] + 1) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0], pozitieCurenta[1] + 1)):
                self.drumCastigator.append(pozitieCurenta)
                return True

        if pozitieCurenta[0] > 0 and pozitieCurenta[1] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] - 1][pozitieCurenta[1] + 1] and (pozitieCurenta[0] - 1, pozitieCurenta[1] + 1) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0] - 1, pozitieCurenta[1] + 1)):
                self.drumCastigator.append(pozitieCurenta)
                return True

        if pozitieCurenta[1] > 0 and pozitieCurenta[0] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] + 1][pozitieCurenta[1] - 1] and (pozitieCurenta[0] + 1, pozitieCurenta[1] - 1) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0] + 1, pozitieCurenta[1] - 1)):
                self.drumCastigator.append(pozitieCurenta)
                return True

        return False

    def ColorareDrumCastigator(self, culoare):
        for pozitie in self.drumCastigator:
            self.map[pozitie[0]][pozitie[1]] = culoare

    def Castigator(self):
        if self.drumCastigator != []:
            if self.map[self.drumCastigator[0][0]][self.drumCastigator[0][1]] == 'a':
                return '1'
            if self.map[self.drumCastigator[0][0]][self.drumCastigator[0][1]] == 'b':
                return '2'
        for i in range (self.size):
            if self.map[i][0] == '1': #aici daca conditia este chimbata in !=0 si mai jos lafel atunci si rosul si albastrul pot face fie o linie sau o coloana, din punctul meu de vedere e mai interesant sa poata ambii si liniile si coloanele
                self.vizitat = []
                if self.DfsLinie((i, 0)):
                    if self.map[i][0] == '1':
                        self.ColorareDrumCastigator('a')
                        #oprire stats#################################################################################################################
                        return '1'
                    if self.map[i][0] == '2':
                        self.ColorareDrumCastigator('b')
                        #oprire stats#################################################################################################################
                        return '2'

            if self.map[0][i] == '2': #daca se schimba in !=0 se intampla ce e descris mai sus
                self.vizitat = []
                if self.DfsColoana((0, i)):
                    if self.map[0][i] == '1':
                        self.ColorareDrumCastigator('a')
                        #oprire stats#################################################################################################################
                        return '1'
                    if self.map[0][i] == '2':
                        self.ColorareDrumCastigator('b')
                        #oprire stats#################################################################################################################
                        return '2'
        return 'None'

    def reseteazaTabla(self):
        for i in range(self.size):
            for j in range(self.size):
                self.map[i][j] = '0'

    def __repr__(self):
        sir = ""
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return (sir)

    def __str__(self):
        sir = ""
        for i in range(self.size):
            for j in range(i):
                sir += "  "
            for j in range(self.size):
                sir += self.map[i][j]
                sir += " "
            sir += "\n"
        return sir

class Joc:
    JMIN = None
    JMAX = None
    def __init__(self, map):
        self.size = len(map)
        self.map = map
        self.vizitat = []

    def DfsLinie(self, pozitieCurenta):
        if pozitieCurenta[1] == self.size - 1:
            return True
        self.vizitat.append(pozitieCurenta)

        if pozitieCurenta[0] > 0 and pozitieCurenta[1] != 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] - 1][pozitieCurenta[1]] and (pozitieCurenta[0] - 1, pozitieCurenta[1]) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0] - 1, pozitieCurenta[1])):
                return True

        if pozitieCurenta[1] > 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0]][pozitieCurenta[1] - 1] and (pozitieCurenta[0], pozitieCurenta[1] - 1) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0], pozitieCurenta[1] - 1)):
                return True

        if pozitieCurenta[0] < self.size - 1 and pozitieCurenta[1] != 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] + 1][pozitieCurenta[1]] and (pozitieCurenta[0] + 1, pozitieCurenta[1]) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0] + 1, pozitieCurenta[1])):
                return True

        if pozitieCurenta[1] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0]][pozitieCurenta[1] + 1] and (pozitieCurenta[0], pozitieCurenta[1] + 1) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0], pozitieCurenta[1] + 1)):
                return True

        if pozitieCurenta[0] > 0 and pozitieCurenta[1] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] - 1][pozitieCurenta[1] + 1] and (pozitieCurenta[0] - 1, pozitieCurenta[1] + 1) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0] - 1, pozitieCurenta[1] + 1)):
                return True

        if pozitieCurenta[1] > 0 and pozitieCurenta[0] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] + 1][pozitieCurenta[1] - 1] and (pozitieCurenta[0] + 1, pozitieCurenta[1] - 1) not in self.vizitat:
            if self.DfsLinie((pozitieCurenta[0] + 1, pozitieCurenta[1] - 1)):
                return True

        return False

    def DfsColoana(self, pozitieCurenta):
        if pozitieCurenta[0] == self.size - 1:
            return True
        self.vizitat.append(pozitieCurenta)

        if pozitieCurenta[0] > 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] - 1][pozitieCurenta[1]] and (pozitieCurenta[0] - 1, pozitieCurenta[1]) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0] - 1, pozitieCurenta[1])):
                return True

        if pozitieCurenta[1] > 0 and pozitieCurenta[0] != 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0]][pozitieCurenta[1] - 1] and (pozitieCurenta[0], pozitieCurenta[1] - 1) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0], pozitieCurenta[1] - 1)):
                return True

        if pozitieCurenta[0] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] + 1][pozitieCurenta[1]] and (pozitieCurenta[0] + 1, pozitieCurenta[1]) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0] + 1, pozitieCurenta[1])):
                return True

        if pozitieCurenta[1] < self.size - 1 and pozitieCurenta[0] != 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0]][pozitieCurenta[1] + 1] and (pozitieCurenta[0], pozitieCurenta[1] + 1) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0], pozitieCurenta[1] + 1)):
                return True

        if pozitieCurenta[0] > 0 and pozitieCurenta[1] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] - 1][pozitieCurenta[1] + 1] and (pozitieCurenta[0] - 1, pozitieCurenta[1] + 1) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0] - 1, pozitieCurenta[1] + 1)):
                return True

        if pozitieCurenta[1] > 0 and pozitieCurenta[0] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1]] == self.map[pozitieCurenta[0] + 1][pozitieCurenta[1] - 1] and (pozitieCurenta[0] + 1, pozitieCurenta[1] - 1) not in self.vizitat:
            if self.DfsColoana((pozitieCurenta[0] + 1, pozitieCurenta[1] - 1)):
                return True

        return False

    def Umplere(self, pozitieCurenta, culoareVeche, culoareNoua):
        self.map[pozitieCurenta[0]][pozitieCurenta[1]] = culoareNoua

        if pozitieCurenta[0] > 0 and self.map[pozitieCurenta[0] - 1][pozitieCurenta[1]] == culoareVeche:
            self.Umplere((pozitieCurenta[0] - 1, pozitieCurenta[1]), culoareVeche, culoareNoua)

        if pozitieCurenta[1] > 0 and self.map[pozitieCurenta[0]][pozitieCurenta[1] - 1] == culoareVeche:
            self.Umplere((pozitieCurenta[0], pozitieCurenta[1] - 1), culoareVeche, culoareNoua)

        if pozitieCurenta[0] < self.size - 1 and self.map[pozitieCurenta[0] + 1][pozitieCurenta[1]] == culoareVeche:
            self.Umplere((pozitieCurenta[0] + 1, pozitieCurenta[1]), culoareVeche, culoareNoua)

        if pozitieCurenta[1] < self.size - 1 and self.map[pozitieCurenta[0]][pozitieCurenta[1] + 1] == culoareVeche:
            self.Umplere((pozitieCurenta[0], pozitieCurenta[1] + 1), culoareVeche, culoareNoua)

        if pozitieCurenta[0] > 0 and pozitieCurenta[1] < self.size - 1 and self.map[pozitieCurenta[0] - 1][pozitieCurenta[1] + 1] == culoareVeche:
            self.Umplere((pozitieCurenta[0] - 1, pozitieCurenta[1] + 1), culoareVeche, culoareNoua)

        if pozitieCurenta[1] > 0 and pozitieCurenta[0] < self.size - 1 and self.map[pozitieCurenta[0] + 1][pozitieCurenta[1] - 1] == culoareVeche:
            self.Umplere((pozitieCurenta[0] + 1, pozitieCurenta[1] - 1), culoareVeche, culoareNoua)

    def Final(self):
        for i in range (self.size):
            if self.map[i][0] == '1':
                self.vizitat = []
                if self.DfsLinie((i, 0)):
                    return '1'
            if self.map[0][i] == '2':
                self.vizitat = []
                if self.DfsColoana((0, i)):
                    return '2'
        return False

    def Mutari(self, player):                                               # nu verifica daca este si randul playerului in cauza sa mute, se presupune ca este apelata
        mutari = []                                                         # corect(de exemplu daca e 1 hex rosu si unul albastru poate fi randul oricaruia dar daca este 1hex rosu si
        for i in range(self.size):                                          #2hexuri albastre atunci obligatoriu urmeaza randului playerului rosu
            for j in range(self.size):
                if self.map[i][j] == '0':
                    copie = copy.deepcopy(self.map)
                    copie[i][j] = player
                    mutari.append(Joc(copie))
        return mutari

    def inserareStiva(self, stiva, elem):
        i = 0
        while i < len(stiva) and stiva[i][2] > elem[2]: i += 1
        if i == len(stiva): stiva.append(elem)
        else: stiva.insert(i, elem)

    def Bfs(self, stiva, culoareDestinatie, culoarePlayer):
        viz = []
        while len(stiva) > 0:
            elemCurent = stiva.pop()
            viz.append((elemCurent[0], elemCurent[1]))

            if self.map[elemCurent[0]][elemCurent[1]] == culoareDestinatie:
                return elemCurent[2]

            if elemCurent[0] > 0 and (elemCurent[0] - 1, elemCurent[1]) not in viz:
                if self.map[elemCurent[0] - 1][elemCurent[1]] == "0":
                    self.inserareStiva(stiva, (elemCurent[0] - 1, elemCurent[1], elemCurent[2] + 1))
                elif self.map[elemCurent[0] - 1][elemCurent[1]] == culoarePlayer:
                    self.inserareStiva(stiva, (elemCurent[0] - 1, elemCurent[1], elemCurent[2]))
                elif self.map[elemCurent[0] - 1][elemCurent[1]] == culoareDestinatie:
                    return elemCurent[2]

            if elemCurent[1] > 0 and (elemCurent[0], elemCurent[1] - 1) not in viz:
                if self.map[elemCurent[0]][elemCurent[1] - 1] == "0":
                    self.inserareStiva(stiva, (elemCurent[0], elemCurent[1] - 1, elemCurent[2] + 1))
                elif self.map[elemCurent[0]][elemCurent[1] - 1] == culoarePlayer:
                    self.inserareStiva(stiva, (elemCurent[0], elemCurent[1] - 1, elemCurent[2]))
                elif self.map[elemCurent[0]][elemCurent[1] - 1] == culoareDestinatie:
                    return elemCurent[2]

            if elemCurent[0] < self.size - 1 and (elemCurent[0] + 1, elemCurent[1]) not in viz:
                if self.map[elemCurent[0] + 1][elemCurent[1]] == "0":
                    self.inserareStiva(stiva, (elemCurent[0] + 1, elemCurent[1], elemCurent[2] + 1))
                elif self.map[elemCurent[0] + 1][elemCurent[1]] == culoarePlayer:
                    self.inserareStiva(stiva, (elemCurent[0] + 1, elemCurent[1], elemCurent[2]))
                elif self.map[elemCurent[0] + 1][elemCurent[1]] == culoareDestinatie:
                    return elemCurent[2]

            if elemCurent[1] < self.size - 1 and (elemCurent[0], elemCurent[1] + 1) not in viz:
                if self.map[elemCurent[0]][elemCurent[1] + 1] == "0":
                    self.inserareStiva(stiva, (elemCurent[0], elemCurent[1] + 1, elemCurent[2] + 1))
                elif self.map[elemCurent[0]][elemCurent[1] + 1] == culoarePlayer:
                    self.inserareStiva(stiva, (elemCurent[0], elemCurent[1] + 1, elemCurent[2]))
                elif self.map[elemCurent[0]][elemCurent[1] + 1] == culoareDestinatie:
                    return elemCurent[2]

            if elemCurent[0] > 0 and elemCurent[1] < self.size - 1 and (elemCurent[0] - 1, elemCurent[1] + 1) not in viz:
                if self.map[elemCurent[0] - 1][elemCurent[1] + 1] == "0":
                    self.inserareStiva(stiva, (elemCurent[0] - 1, elemCurent[1] + 1, elemCurent[2] + 1))
                elif self.map[elemCurent[0] - 1][elemCurent[1] + 1] == culoarePlayer:
                    self.inserareStiva(stiva, (elemCurent[0] - 1, elemCurent[1] + 1, elemCurent[2]))
                elif self.map[elemCurent[0] - 1][elemCurent[1] + 1] == culoareDestinatie:
                    return elemCurent[2]

            if elemCurent[0] < self.size - 1 and elemCurent[1] > 0 and (elemCurent[0] + 1, elemCurent[1] - 1) not in viz:
                if self.map[elemCurent[0] + 1][elemCurent[1] - 1] == "0":
                    self.inserareStiva(stiva, (elemCurent[0] + 1, elemCurent[1] - 1, elemCurent[2] + 1))
                elif self.map[elemCurent[0] + 1][elemCurent[1] - 1] == culoarePlayer:
                    self.inserareStiva(stiva, (elemCurent[0] + 1, elemCurent[1] - 1, elemCurent[2]))
                elif self.map[elemCurent[0] + 1][elemCurent[1] - 1] == culoareDestinatie:
                    return elemCurent[2]

        return 1000

    def EstimeazaScor(self, adancime):
        tFinal = self.Final()
        if tFinal == Joc.JMAX:
            return (99 + adancime)
        elif tFinal == Joc.JMIN:
            return (-99 - adancime)
        else:
            for i in range(self.size):
                if self.map[i][0] == '1':
                    self.Umplere((i, 0), '1', 'a')
                if self.map[i][self.size - 1] == '1':
                    self.Umplere((i, self.size - 1), '1', 'A')
                if self.map[0][i] == '2':
                    self.Umplere((0, i), '2', 'b')
                if self.map[self.size - 1][i] == '2':
                    self.Umplere((self.size - 1, i), '2', 'B') ###########################################

            stiva1Initiala = []
            stiva2Initiala = []
            for i in range(self.size):
                pos1 = None
                pos2 = None ###################################
                for j in range(self.size):
                    if self.map[i][j] == 'a':
                        pos1 = (i, j, 0)
                    if self.map[j][i] == 'b':
                        pos2 = (j, i, 0)
                if pos1 is not None:
                    stiva1Initiala.insert(0, pos1)
                if pos2 is not None:
                    stiva2Initiala.insert(0, pos2)
            lungime1 = self.Bfs(stiva1Initiala, 'A', '1')
            lungime2 = self.Bfs(stiva2Initiala, 'B', '2')

            for i in range(self.size):
                for j in range(self.size):
                    if self.map[i][j] == 'a' or self.map[i][j] == 'A':
                        self.map[i][j] = '1'
                    elif self.map[i][j] == 'b' or self.map[i][j] == 'B':
                        self.map[i][j] = '2'

            if Joc.JMAX == '1' and Joc.JMIN == '2':
                return - lungime1 + lungime2
            if Joc.JMAX == '2' and Joc.JMIN == '1':
                return - lungime2 + lungime1

            # nrColoane1 = 99
            # nrLinii2 = 99
            # nrLinii1 = 0
            # nrColoane2 = 0
            # for i in range(self.size):
            #     c1 = 0
            #     l2 = 0
            #     l1 = False
            #     c2 = False
            #     for j in range(self.size):
            #         if self.map[j][i] == '1':
            #             c1 += 1
            #         if self.map[i][j] == '2':
            #             l2 += 1
            #
            #         if self.map[i][j] == '1':
            #             l1 = True
            #         if self.map[j][i] == '2':
            #             c2 = True
            #     if l1:
            #         nrLinii1 += 1
            #     if c2:
            #         nrColoane2 += 1
            #
            #     if c1 < nrColoane1:
            #         nrColoane1 = c1
            #     if l2 < nrLinii2:
            #         nrLinii2 = l2
            # if Joc.JMAX == '1' and Joc.JMIN == '2':
            #     return (nrColoane1 - nrLinii1) - (nrLinii2 - nrColoane2)
            # if Joc.JMAX == '2' and Joc.JMIN == '1':
            #     return (nrLinii2 - nrColoane2) - (nrColoane1 - nrLinii1)

class Stare:
    def __init__(self, jocCurent, playerCurent, adancime, parinte = None, estimare = None):
        self.jocCurent = jocCurent
        self.playerCurent = playerCurent
        self.adancime = adancime
        self.parinte = parinte
        self.estimare = estimare
        self.mutariPosibile = []
        self.stareAleasa = None

    def Mutari(self):
        listaMutari = self.jocCurent.Mutari(self.playerCurent)
        opusPlayer = '1' if currentPlayer == '2' else '2'
        listaStariMutari = [Stare(mutare, opusPlayer, self.adancime - 1, parinte = self) for mutare in listaMutari]
        listaStariMutari.sort(key = lambda x: x.jocCurent.EstimeazaScor(self.adancime - 1))
        return listaStariMutari

    def __repr__(self):
        sir = ""
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return (sir)

def MinMax(stare):
    Stats.numarNoduriMinMax += 1

    if stare.adancime == 0 or stare.jocCurent.Final():
        stare.estimare = stare.jocCurent.EstimeazaScor(stare.adancime)
        return stare

    stare.mutariPosibile = stare.Mutari()

    mutariCuEstimare = [MinMax(x) for x in stare.mutariPosibile]

    if stare.playerCurent == Joc.JMAX:
        stare.stareAleasa = max(mutariCuEstimare, key = lambda x: x.estimare)
    else:
        stare.stareAleasa = min(mutariCuEstimare, key = lambda x: x.estimare)

    stare.estimare = stare.stareAleasa.estimare
    return stare

def AlphaBeta(alpha, beta, stare):
    Stats.numarNoduriAlphaBeta += 1

    if stare.adancime == 0 or stare.jocCurent.Final():
        stare.estimare = stare.jocCurent.EstimeazaScor(stare.adancime)
        return stare

    if alpha > beta:
        return stare

    stare.mutariPosibile = stare.Mutari()

    if stare.playerCurent == Joc.JMAX:
        estimareCurenta = float('-inf')
        for mutare in stare.mutariPosibile:
            stareNoua = AlphaBeta(alpha, beta, mutare)

            if estimareCurenta < stareNoua.estimare:
                stare.stareAleasa = stareNoua
                estimareCurenta = stareNoua.estimare

            if alpha < stareNoua.estimare:
                alpha = stareNoua.estimare
                if alpha >= beta:
                    break
    elif stare.playerCurent == Joc.JMIN:
        estimareCurenta = float('inf')
        for mutare in stare.mutariPosibile:
            stareNoua = AlphaBeta(alpha, beta, mutare)

            if estimareCurenta > stareNoua.estimare:
                stare.stareAleasa = stareNoua
                estimareCurenta = stareNoua.estimare

            if beta > stareNoua.estimare:
                beta = stareNoua.estimare
                if alpha >= beta:
                    break
    stare.estimare = stare.stareAleasa.estimare
    return stare

class Human:
    def __init__(self, color):
        self.color = color # 1 blue ; 2 red
        self.esteComputer = False

    def turn(self, tablaJoc):
        if e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                pos = pg.mouse.get_pos()
                linieHexagon = (pos[1] - 20) // 24
                coloanaHexagon = (pos[0] - 20 - linieHexagon * 16) // 32
                if tablaJoc.PozitiePermisa(linieHexagon, coloanaHexagon) and tablaJoc.Castigator() == 'None':
                    tablaJoc.map[linieHexagon][coloanaHexagon] = self.color
                    return True
                # if tablaJoc.Castigator() != 'None':
                #     print(repr(tablaJoc))
        return False

class Computer:
    def __init__(self, color, algoritm, dificultate):
        self.color = color
        self.algoritm = algoritm
        self.ultimaEstimare = -1000
        self.esteComputer = True

        if dificultate == "Incepator":
            self.adancime = 1
        elif dificultate == "Mediu":
            self.adancime = 2
        elif dificultate == "Avansat":
            self.adancime = 3

    def turn(self, tablaJoc):
        if self.color == "1":
            Joc.JMAX = "1"
            Joc.JMIN = "2"
        elif self.color == "2":
            Joc.JMAX = "2"
            Joc.JMIN = "1"

        if tablaJoc.Castigator() == "None":
            stareActualizata = None
            stareCurenta = Stare(Joc(tablaJoc.map), self.color, self.adancime)
            if self.algoritm == "Min-Max":
                stareActualizata = MinMax(stareCurenta)
            elif self.algoritm == "Alpha-Beta":
                stareActualizata = AlphaBeta(-500, 500, stareCurenta)
            tablaJoc.map = stareActualizata.stareAleasa.jocCurent.map
            self.ultimaEstimare = stareActualizata.stareAleasa.estimare
            return True
        return False

class Stats:
    numarNoduriGenerateMinMax = []
    numarNoduriMinMax = 0

    numarNoduriGenerateAlphaBeta = []
    numarNoduriAlphaBeta = 0

    def __init__(self):
        self.timpiGandire = []
        self.start = 0

    def startGandire(self):
        self.start = time.time()

    def oprireGandire(self):
        self.timpiGandire.append(time.time() - self.start)

    def resetGandire(self):
        self.start = 0
        self.timpiGandire = []

    @classmethod
    def updateNoduriGenerateMinMax(cls):
        cls.numarNoduriGenerateMinMax.append(cls.numarNoduriMinMax)
        cls.numarNoduriMinMax = 0

    @classmethod
    def resetNoduriGenerateMinMax(cls):
        cls.numarNoduriGenerateMinMax = []
        cls.numarNoduriMinMax = 0

    @classmethod
    def updateNoduriGenerateAlphaBeta(cls):
        cls.numarNoduriGenerateAlphaBeta.append(cls.numarNoduriAlphaBeta)
        cls.numarNoduriAlphaBeta = 0

    @classmethod
    def resetNoduriGenerateAlphaBeta(cls):
        cls.numarNoduriGenerateAlphaBeta = []
        cls.numarNoduriAlphaBeta = 0

marimeTabla = 11
dificultate = ""
algoritm = ""
print("Cat de mare sa fie tabla?")
print("Numar, de la 3 la 20.")
print("-----------------")
iesire = False
while not iesire:
    x = input("Numar = ")
    nr = int(x)
    if nr > 2 and nr < 21:
        marimeTabla = nr
        iesire = True
    else:
        print("Input gresit.")

tablaJoc = TablaJoc(marimeTabla)
WINDOW = Window(marimeTabla)
firstPlayer = None
secondPlayer = None
stats1 = Stats()
stats2 = Stats()

print("Ce mod doresti sa joci?")
print("-----------------")
print("1.PvP")
print("2.EvE")
print("3.PvE")

iesire = False
while not iesire:
    x = input("Mod = ")
    if x == '1':
        firstPlayer = Human('1')
        secondPlayer = Human('2')
        iesire = True
        print("==================")
    elif x == '2':
        print("==================")

        print("\n")
        print("Ce dificultate alegi?")
        print("-----------------")
        print("1.Incepator")
        print("2.Mediu")
        print("3.Avansat")

        while not iesire:
            x = input("Dificultate = ")
            if x == '1':
                dificultate = "Incepator"
                print("==================")
                iesire = True
            elif x == '2':
                dificultate = "Mediu"
                print("==================")
                iesire = True
            elif x == '3':
                dificultate = "Avansat"
                print("==================")
                iesire = True
            else:
                print("Input gresit.")

        firstPlayer = Computer('1', "Alpha-Beta", dificultate)
        secondPlayer = Computer('2', "Min-Max", dificultate)



    elif x == '3':

        print("==================")
        print("\n")
        print("Ce dificultate alegi?")
        print("-----------------")
        print("1.Incepator")
        print("2.Mediu")
        print("3.Avansat")

        while not iesire:
            x = input("Dificultate = ")
            if x == '1':
                dificultate = "Incepator"
                print("==================")
                iesire = True
            elif x == '2':
                dificultate = "Mediu"
                print("==================")
                iesire = True
            elif x == '3':
                dificultate = "Avansat"
                print("==================")
                iesire = True
            else:
                print("Input gresit.")

        print("\n")
        print("Ce algoritm alegi?")
        print("-----------------")
        print("1.Alpha-Beta")
        print("2.Min-Max")

        iesire = False
        while not iesire:
            x = input("Algoritm = ")
            if x == '1':
                algoritm = "Alpha-Beta"
                iesire = True
            elif x == '2':
                algoritm = "Min-Max"
                iesire = True
            else:
                print("Input gresit.")

        h = None
        c = None
        print("\n")
        print("Ce culoare alegi?")
        print("Albastrul castiga conectand latura de sus cu cea de jos si rosul latura din stanga cu cea din dreapta.")
        print("-----------------")
        print("1.Albastru")
        print("2.Rosu")
        iesire = False
        while not iesire:
            x = input("Culoare = ")
            if x == '1':
                h = Human('1')
                c = Computer('2', algoritm, dificultate)
                iesire = True
                print("==================")
            elif x == '2':
                h = Human('2')
                c = Computer('1', algoritm, dificultate)
                iesire = True
                print("==================")
            else:
                print("Input gresit.")

        print("\n")
        print("Doriti sa incepeti?")
        print("-----------------")
        print("1.Da")
        print("2.Nu")
        iesire = False
        while not iesire:
            x = input("Raspuns = ")
            if x == '1':
                firstPlayer = h
                secondPlayer = c
                iesire = True
                print("==================")
            elif x == '2':
                firstPlayer = c
                secondPlayer = h
                iesire = True
                print("==================")
            else:
                print("Input gresit.")
    else:
        print("Input gresit.")

currentPlayer = firstPlayer
stats1.startGandire()

sir = "Acum muta "
if currentPlayer.color == '1':
    sir += "Albastru."
if currentPlayer.color == '2':
    sir += "Rosu."

print("\n\n\nTabla initiala:")
print("------------------")
print(str(tablaJoc))
print("==================")
print(sir)

iesire = False
afisatCastigator = False
skippedFirstPrint = False
while not iesire:
    events = pg.event.get()
    for e in events:
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_r:
                tablaJoc.reseteazaTabla()

                stats1.resetGandire()
                stats2.resetGandire()
                Stats.resetNoduriGenerateAlphaBeta()
                Stats.resetNoduriGenerateMinMax()

                stats1.startGandire()
                currentPlayer = firstPlayer
                afisatCastigator = False

                sir = "Acum muta "
                if currentPlayer.color == '1':
                    sir += "Albastru."
                if currentPlayer.color == '2':
                    sir += "Rosu."

                print("\n\n\nTabla initiala:")
                print("------------------")
                print(str(tablaJoc))
                print("==================")
                print(sir)

        if e.type == pg.QUIT:
            if not afisatCastigator:
                print("#####################################################")
                print("First Player")
                if firstPlayer.esteComputer:
                    print("=>Computer")
                    print("=>Numar mutari: " + str(len(stats1.timpiGandire)))
                    print("=>Timp total de gandire: {:.2f}".format(sum(stats1.timpiGandire)))
                    print("=>Timp minim de gandire: {:.2f}".format(min(stats1.timpiGandire)))
                    print("=>Timp maxim de gandire: {:.2f}".format(max(stats1.timpiGandire)))
                    print("=>Timp mediu de gandire: {:.2f}".format(sum(stats1.timpiGandire) / len(stats1.timpiGandire)))
                    print("=>Mediana timpilor de gandire: {:.2f}".format(statistics.median(stats1.timpiGandire)))
                else:
                    print("=>Human")
                    print("=>Numar mutari: " + str(len(stats1.timpiGandire)))
                    print("=>Timp total de gandire: {:.2f}".format(sum(stats1.timpiGandire)))

                print("==================")
                print("Second Player")
                if secondPlayer.esteComputer:
                    print("=>Computer")
                    print("=>Numar mutari: " + str(len(stats2.timpiGandire)))
                    print("=>Timp total de gandire: {:.2f}".format(sum(stats2.timpiGandire)))
                    print("=>Timp minim de gandire: {:.2f}".format(min(stats2.timpiGandire)))
                    print("=>Timp maxim de gandire: {:.2f}".format(max(stats2.timpiGandire)))
                    print("=>Timp mediu de gandire: {:.2f}".format(sum(stats2.timpiGandire) / len(stats2.timpiGandire)))
                    print("=>Mediana timpilor de gandire: {:.2f}".format(statistics.median(stats2.timpiGandire)))
                else:
                    print("=>Human")
                    print("=>Numar mutari: " + str(len(stats2.timpiGandire)))
                    print("=>Timp total de gandire: {:.2f}".format(sum(stats2.timpiGandire)))

                    print("#####################################################")
                    if Stats.numarNoduriGenerateMinMax != []:
                        print("Min-Max:")
                        print("=>Numar total noduri: " + str(sum(Stats.numarNoduriGenerateMinMax)))
                        print("=>Minim noduri: {}".format(min(Stats.numarNoduriGenerateMinMax)))
                        print("=>Maxim noduri: {}".format(max(Stats.numarNoduriGenerateMinMax)))
                        print("=>Medie noduri: {:.2f}".format(sum(Stats.numarNoduriGenerateMinMax) / len(Stats.numarNoduriGenerateMinMax)))
                        print("=>Mediana noduri: {}".format(statistics.median(Stats.numarNoduriGenerateMinMax)))

                        print("==================")
                    if Stats.numarNoduriGenerateAlphaBeta != []:          ######################
                        print("Alpha-Beta:")
                        print("=>Numar total noduri: " + str(sum(Stats.numarNoduriGenerateAlphaBeta)))
                        print("=>Minim noduri: {}".format(min(Stats.numarNoduriGenerateAlphaBeta)))
                        print("=>Maxim noduri: {}".format(max(Stats.numarNoduriGenerateAlphaBeta)))
                        print("=>Medie noduri: {:.2f}".format(sum(Stats.numarNoduriGenerateAlphaBeta) / len(Stats.numarNoduriGenerateAlphaBeta)))
                        print("=>Mediana noduri: {}".format(statistics.median(Stats.numarNoduriGenerateAlphaBeta)))

            iesire = True
        if currentPlayer.turn(tablaJoc):
            if currentPlayer == firstPlayer:
                stats1.oprireGandire()
                stats2.startGandire()
                currentPlayer = secondPlayer
            else:
                stats2.oprireGandire()
                stats1.startGandire()
                currentPlayer = firstPlayer

            if tablaJoc.Castigator() == 'None':
                sir = "A mutat "
                sir2 = "Acum muta "
                if currentPlayer.color == '1':
                    sir2 += "Albastru."
                    sir += "Rosu."
                if currentPlayer.color == '2':
                    sir2 += "Rosu."
                    sir += "Albastru."
                print(sir)
                print("------------------")
                print(str(tablaJoc))
                if currentPlayer == secondPlayer:
                    print("Timp gandire: {:.2f}".format(stats1.timpiGandire[len(stats1.timpiGandire) - 1]))
                elif currentPlayer == firstPlayer:
                    print("Timp gandire: {:.2f}".format(stats1.timpiGandire[len(stats2.timpiGandire) - 1]))
                if currentPlayer == firstPlayer:
                    if secondPlayer.esteComputer:
                        if secondPlayer.algoritm == "Min-Max":
                            print("Numar noduri generate:" + str(Stats.numarNoduriMinMax))
                            Stats.updateNoduriGenerateMinMax()
                        elif secondPlayer.algoritm == "Alpha-Beta":
                            print("Numar noduri generate:" + str(Stats.numarNoduriAlphaBeta))
                            Stats.updateNoduriGenerateAlphaBeta()

                        print("Estimare arbore: " + str(secondPlayer.ultimaEstimare))
                elif currentPlayer == secondPlayer:
                    if firstPlayer.esteComputer:
                        if firstPlayer.algoritm == "Min-Max":
                            print("Numar noduri generate:" + str(Stats.numarNoduriMinMax))
                            Stats.updateNoduriGenerateMinMax()
                        elif firstPlayer.algoritm == "Alpha-Beta":
                            print("Numar noduri generate:" + str(Stats.numarNoduriAlphaBeta))
                            Stats.updateNoduriGenerateAlphaBeta()

                        print("Estimare arbore: " + str(firstPlayer.ultimaEstimare))
                print("==================")
                print(sir2)

    if tablaJoc.Castigator() != 'None' and not afisatCastigator:
        culoareCastigator = tablaJoc.Castigator()
        if culoareCastigator == '1':
            stats1.oprireGandire()
            print("A mutat Albastru.")
            print("------------------")
            print(str(tablaJoc))
            print("Timp gandire: {:.2f}".format(stats1.timpiGandire[len(stats2.timpiGandire) - 1]))
            if firstPlayer.esteComputer:
                if firstPlayer.algoritm == "Min-Max":
                    print("Numar noduri generate:" + str(Stats.numarNoduriMinMax))
                    Stats.updateNoduriGenerateMinMax()
                elif firstPlayer.algoritm == "Alpha-Beta":
                    print("Numar noduri generate:" + str(Stats.numarNoduriAlphaBeta))
                    Stats.updateNoduriGenerateAlphaBeta()

                print("Estimare arbore: " + str(firstPlayer.ultimaEstimare))
        if culoareCastigator == '2':
            stats2.oprireGandire()
            print("A mutat Rosu.")
            print("------------------")
            print(str(tablaJoc))
            print("Timp gandire: {:.2f}".format(stats1.timpiGandire[len(stats1.timpiGandire) - 1]))
            if secondPlayer.esteComputer:
                if secondPlayer.algoritm == "Min-Max":
                    print("Numar noduri generate:" + str(Stats.numarNoduriMinMax))
                    Stats.updateNoduriGenerateMinMax()
                elif secondPlayer.algoritm == "Alpha-Beta":
                    print("Numar noduri generate:" + str(Stats.numarNoduriAlphaBeta))
                    Stats.updateNoduriGenerateAlphaBeta()

                print("Estimare arbore: " + str(secondPlayer.ultimaEstimare))
        print("==================")
        if culoareCastigator == '1':
            print("A castigat Albastru!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if culoareCastigator == '2':
            print("A castigat Rosu!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        print("#####################################################")
        print("First Player")
        if firstPlayer.esteComputer:
            print("=>Computer")
            print("=>Numar mutari: " + str(len(stats1.timpiGandire)))
            print("=>Timp total de gandire: {:.2f}".format(sum(stats1.timpiGandire)))
            print("=>Timp minim de gandire: {:.2f}".format(min(stats1.timpiGandire)))
            print("=>Timp maxim de gandire: {:.2f}".format(max(stats1.timpiGandire)))
            print("=>Timp mediu de gandire: {:.2f}".format(sum(stats1.timpiGandire) / len(stats1.timpiGandire)))
            print("=>Mediana timpilor de gandire: {:.2f}".format(statistics.median(stats1.timpiGandire)))
        else:
            print("=>Human")
            print("=>Numar mutari: " + str(len(stats1.timpiGandire)))
            print("=>Timp total de gandire: {:.2f}".format(sum(stats1.timpiGandire)))

        print("==================")
        print("Second Player")
        if secondPlayer.esteComputer:
            print("=>Computer")
            print("=>Numar mutari: " + str(len(stats2.timpiGandire)))
            print("=>Timp total de gandire: {:.2f}".format(sum(stats2.timpiGandire)))
            print("=>Timp minim de gandire: {:.2f}".format(min(stats2.timpiGandire)))
            print("=>Timp maxim de gandire: {:.2f}".format(max(stats2.timpiGandire)))
            print("=>Timp mediu de gandire: {:.2f}".format(sum(stats2.timpiGandire) / len(stats2.timpiGandire)))
            print("=>Mediana timpilor de gandire: {:.2f}".format(statistics.median(stats2.timpiGandire)))
        else:
            print("=>Human")
            print("=>Numar mutari: " + str(len(stats2.timpiGandire)))
            print("=>Timp total de gandire: {:.2f}".format(sum(stats2.timpiGandire)))

        print("#####################################################")
        if Stats.numarNoduriGenerateMinMax != []:
            print("Min-Max:")
            print("=>Numar total noduri: " + str(sum(Stats.numarNoduriGenerateMinMax)))
            print("=>Minim noduri: {}".format(min(Stats.numarNoduriGenerateMinMax)))
            print("=>Maxim noduri: {}".format(max(Stats.numarNoduriGenerateMinMax)))
            print("=>Medie noduri: {:.2f}".format(sum(Stats.numarNoduriGenerateMinMax) / len(Stats.numarNoduriGenerateMinMax)))
            print("=>Mediana noduri: {}".format(statistics.median(Stats.numarNoduriGenerateMinMax)))

            print("==================")
        if Stats.numarNoduriGenerateAlphaBeta != []:  ######################
            print("Alpha-Beta:")
            print("=>Numar total noduri: " + str(sum(Stats.numarNoduriGenerateAlphaBeta)))
            print("=>Minim noduri: {}".format(min(Stats.numarNoduriGenerateAlphaBeta)))
            print("=>Maxim noduri: {}".format(max(Stats.numarNoduriGenerateAlphaBeta)))
            print("=>Medie noduri: {:.2f}".format(sum(Stats.numarNoduriGenerateAlphaBeta) / len(Stats.numarNoduriGenerateAlphaBeta)))
            print("=>Mediana noduri: {}".format(statistics.median(Stats.numarNoduriGenerateAlphaBeta)))

        afisatCastigator = True

    WINDOW.update(tablaJoc)

