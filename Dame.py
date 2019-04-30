from Piece_Modele import Piece

class Pion_Dame(Piece):
    def __init__(self, master, coords, RGB, ID='Pion'):
        self.master = master
    # liste des différentes parties du pion
        self.Pion = []
    # L'ID correspond au tags du pion sur le canvas(master)
        self.ID = ID
        self.tag = ''
        temp = list(ID)
        for element in temp:
            if element != ' ':
                self.tag += element
    # transformation des variables rgb en str utilisable pour la couleur
        self.color = '#%02x%02x%02x' % (RGB[0], RGB[1], RGB[2])
    # les variables rgb sont conservées pour pouvoir nuancer la couleur
        self.RGB = RGB
    # identification d'un carré dans les coordonnés: il contiendra le pion (n'est vrai que lors de la création)
        if coords[2]-coords[0] >= coords[3]-coords[1]:
            self.size = coords[3]-coords[1]
            self.x1 = coords[0] + (coords[2]-coords[0] - self.size)/2
            self.x2 = coords[2] - (coords[2]-coords[0] - self.size)/2
            self.y1 = coords[1]
            self.y2 = coords[3]
        else:
            self.size = coords[2]-coords[0]
            self.y1 = coords[1] + (coords[3]-coords[1] - self.size)/2
            self.y2 = coords[3] - (coords[3]-coords[1] - self.size)/2
            self.x1 = coords[0]
            self.x2 = coords[2]
    # coordonnés du centre de l'objet
        self.x = (self.x1+self.x2)/2
        self.y = (self.y1+self.y2)/2
    # initialisation
        self.create()
        
    def create(self, Dame=False):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        color = '#%02x%02x%02x' % (self.RGB[0]-10, self.RGB[1]-10, self.RGB[2]-10)
        tag = self.ID+' '+self.tag
        self.Pion += [
            self.master.create_oval(x1, y1, x2, y2, fill=self.color, tags=tag),
            self.master.create_oval(x1+self.size/10, y1+self.size/10, x2-self.size/10,y2-self.size/10, fill=color, tags=tag),
            self.master.create_oval(x1+self.size/4, y1+self.size/4, x2-self.size/4, y2-self.size/4, fill=self.color, tags=tag),
        ]
        if Dame:
            self.Pion += [self.master.create_oval(x1, y1, x2, y2, fill='yellow', tags=tag)]

    def UpgradeToDame(self):
        self.delete()
        temp = list(self.ID)
        self.tag = ''
        self.ID = ''
        temp[:4] = 'Dame'
        for element in temp:
            self.ID += element
            if element != ' ':
                self.tag += element
        self.create(Dame=True)


## Terrain de jeu


class Damier:
    def __init__(self, master, x1, y1, x2, y2):
        self.master = master
    # on decide de la taille de l'echiquier(c'est un carré)
        if x2-x1 >= y2-y1:
            self.size = y2-y1
            self.x1 = x1 + (x2-x1 - self.size)/2
            self.x2 = x2 - (x2-x1 - self.size)/2
            self.y1 = y1
            self.y2 = y2
        else:
            self.size = x2-x1
            self.y1 = y1 + (y2-y1 - self.size)/2
            self.y2 = y2 - (y2-y1 - self.size)/2
            self.x1 = x1
            self.x2 = x2
        self.SizeCase = self.size/10
    # information de chaque cases
        self.Box = {}
    # dictionnaire des différents pions du Damier
        self.PionDic = {}
    # mise en place
        self.create()
        self.Pions()

    def create(self):
        x = self.x1
        y = self.y1
        color = 'black'
    #création des cases
        for i in range(10):
            for n in range(10):
                self.master.create_rectangle(
                    x, y, x+self.SizeCase, y+self.SizeCase, fill=color, tags='Box')
                self.Box[(n, i)] = []
                self.Box[(n, i)].append((x, y, x+self.SizeCase, y+self.SizeCase))
                self.Box[(n, i)].append(color)
                self.Box[(n, i)].append('')
                x += self.SizeCase
                if color == 'black':
                    color = 'white'
                else:
                    color = 'black'
            y += self.SizeCase
            x = self.x1
            if color == 'black':
                color = 'white'
            else:
                color = 'black'
    # Aide
        for i in range(10):
            coord = (((self.Box[(i, 0)][0][0]+self.Box[(i, 0)][0][2])/2),
                     ((self.Box[(i, 0)][0][1]+self.Box[(i, 0)][0][3])/2)-self.SizeCase)
            self.master.create_text(
                coord[0], coord[1], text=str(i), fill='white')
        for i in range(10):
            coord = (((self.Box[(0, i)][0][0]+self.Box[(0, i)][0][2])/2)-self.SizeCase,
                     ((self.Box[(0, i)][0][1]+self.Box[(0, i)][0][3])/2))
            self.master.create_text(
                coord[0], coord[1], text=str(i), fill='white')


    def Pions(self):
        # mise en place des pions blancs
        color = 'white'
        number = 0
        RGB = (255, 255, 255)
        for i in range(3):
            for n in range(10):
                if self.Box[(n, i)][1] == 'black':
                    ID = "Pion "+color+" "+str(number)
                    self.PionDic[ID] = Pion_Dame(
                        self.master, self.Box[(n, i)][0], RGB, ID)
                    self.Box[(n, i)][2] = ID
                    number += 1
    # mise en place des pions noirs
        color = 'black'
        number = 0
        RGB = (55, 55, 55)
        for i in range(7, 10):
            for n in range(10):
                if self.Box[(n, i)][1] == 'black':
                    ID = "Pion "+color+" "+str(number)
                    self.PionDic[ID] = Pion_Dame(
                        self.master, self.Box[(n, i)][0], RGB, ID)
                    self.Box[(n, i)][2] = ID
                    number += 1
