from Piece_Modele import Piece


class Pion_Echec(Piece):
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
    # identification d'un carré dans les coordonnés: il contiendra le pion
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
    # Variables utilisée pour le 1er déplacement du Pion
        self.Moved = False
    # initialisation
        self.create()

    def create(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
    #deux valeurs utiles pour la création du polygon
        size6 = self.size/6  # represente 1/6 de la taille maximum possible
        size12 = self.size/12  # represente 1/12 de la taille maximum possible
    #xstart et ystart points de départ du tracé du polygon
        xstart = x1+2*size6
        ystart = y1+3*size6
    #liste des differents points du polygon
        pts = [
            (xstart, ystart),
            (xstart, ystart+size12),
            (xstart+size12, ystart+size6),
            (xstart, y2-size6),
            (xstart-size12, y2-size6),
            (x1+size6, y2),
            (x2-size6, y2),
            (x2-size6-size12, y2-size6),
            (x2-2*size6, y2-size6),
            (xstart+size6+size12, ystart+size6),
            (xstart+2*size6, ystart+size12),
            (xstart+2*size6, ystart)
        ]
    #création des partie du pion
        darkcolor = '#%02x%02x%02x' % (self.RGB[0]-25, self.RGB[1]-25, self.RGB[2]-25)
        tag = self.ID+' '+self.tag
        self.Pion += [
            self.master.create_polygon(pts, fill=self.color, tags=tag, outline='black'),
            self.master.create_polygon((xstart+size12, ystart+size6), (xstart, y2-size6), (x2-2*size6, y2-size6),(xstart+size6+size12, ystart+size6), fill=darkcolor, tags=tag, outline='black'),
            self.master.create_oval(x1+2*size6, y1+size6, x2-2*size6, y1+3*size6, fill=self.color, tags=tag, outline='black'),
        ]


class Tour_Echec(Piece):
    def __init__(self, master, coords, RGB, ID='Tour'):
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
    # identification d'un carré dans les coordonnés: il contiendra le pion
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

    def create(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
    #deux valeurs utiles pour la création du polygon
        size6 = self.size/6  # represente 1/6 de la taille maximum possible
        size12 = self.size/12  # represente 1/12 de la taille maximum possible
    #liste des differents points du polygon
        pts = [
            (x1+size6, y2),
            (x1+size6+size12, y2-size6),
            (x1+2*size6, y2-size6),
            (x1+2*size6+size12, y1+2*size6+size12),
            (x1+size6+(3/2)*size12, y1+2*size6),
            (x1+size6+(3/2)*size12, y1+size6+(3/2)*size12),
            (x1+2*size6, y1+size6+(3/2)*size12),
            (x1+2*size6, y1+size6+size12),
            (x1+size6+(3/2)*size12, y1+size6+size12),
            (x1+size6+(3/2)*size12, y1+size6),
            (x2-size6-(3/2)*size12, y1+size6),
            (x2-size6-(3/2)*size12, y1+size6+size12),
            (x2-2*size6, y1+size6+size12),
            (x2-2*size6, y1+size6+(3/2)*size12),
            (x2-size6-(3/2)*size12, y1+size6+(3/2)*size12),
            (x2-size6-(3/2)*size12, y1+2*size6),
            (x2-2*size6-size12, y1+2*size6+size12),
            (x2-2*size6, y2-size6),
            (x2-size6-size12, y2-size6),
            (x2-size6, y2),
        ]

        darkcolor = '#%02x%02x%02x' % (self.RGB[0]-25, self.RGB[1]-25, self.RGB[2]-25)
        tag = self.ID+' '+self.tag
        self.Pion += [
            self.master.create_polygon(pts, fill=self.color, tags=tag, outline='black'),
            self.master.create_polygon((x1+2*size6, y2-size6), (x1+2*size6+size12, y1+2*size6+size12), (x2 - 2*size6-size12, y1+2*size6+size12), (x2-2*size6, y2-size6), tags=tag, fill=darkcolor, outline='black'),
            self.master.create_polygon((x1+2*size6, y1+size6+(3/2)*size12), (x1+2*size6, y1+size6+size12), (x2 - 2*size6, y1+size6+size12), (x2-2*size6, y1+size6+(3/2)*size12), tags=tag, fill=darkcolor, outline='black'),
        ]


class Fou_Echec(Piece):
    def __init__(self, master, coords, RGB, ID='Fou'):
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
    # identification d'un carré dans les coordonnés: il contiendra le pion
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

    def create(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
    #deux valeurs utiles pour la création du polygon
        size6 = self.size/6  # represente 1/6 de la taille maximum possible
        size12 = self.size/12  # represente 1/12 de la taille maximum possible
    #liste des differents points du polygon
        pts = [
            (x1+size6+size12, y2),
            (x1+size6+size12, y2-size12),
            (x1+2*size6, y2-size12),
            (x1+2*size6+size12, y2-2*size6-size12),
            (x1+2*size6, (y1+y2)/2),
            (x1+2*size6, y1+2*size6+size12),
            (x2-2*size6, y1+2*size6+size12),
            (x2-2*size6, (y1+y2)/2),
            (x2-2*size6-size12, y2-2*size6-size12),
            (x2-2*size6, y2-size12),
            (x2-size6-size12, y2-size12),
            (x2-size6-size12, y2),
        ]
    #création des partie du pion
        darkcolor = '#%02x%02x%02x' % (self.RGB[0]-25, self.RGB[1]-25, self.RGB[2]-25)
        tag = self.ID+' '+self.tag
        self.Pion += [
            self.master.create_polygon(pts, fill=self.color, tags=tag, outline='black'),
            self.master.create_oval(x1+2*size6+(3/2)*size12, y1+size12, x2-2*size6-(3/2)*size12, y1+size6, fill=self.color, tags=tag, outline='black'),
            self.master.create_oval(x1+2*size6+(1/2)*size12, y1+size6, x2-2*size6-(1/2)*size12, y1+2*size6+size12, fill=self.color, tags=tag, outline='black'),
            self.master.create_polygon((x1+2*size6, (y1+y2)/2), (x1+2*size6, (y1+y2)/2-(1/2)*size12), (x2-2*size6,(y1+y2)/2-(1/2)*size12), (x2-2*size6, (y1+y2)/2), fill=darkcolor, tags=tag, outline='black'),
            self.master.create_polygon((x1+2*size6, y2-size12), (x1+2*size6+size12, y2-2*size6-size12), (x2 - 2*size6-size12, y2-2*size6-size12), (x2-2*size6, y2-size12), fill=darkcolor, tags=tag, outline='black'),
        ]


class Cavalier_Echec(Piece):
    def __init__(self, master, coords, RGB, ID='Cavalier'):
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
    # identification d'un carré dans les coordonnés: il contiendra le pion
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

    def create(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
    #deux valeurs utiles pour la création du polygon
        size6 = self.size/6  # represente 1/6 de la taille maximum possible
        size12 = self.size/12  # represente 1/12 de la taille maximum possible
    #liste des differents points du polygon
        pts = [
            (x1+size6+size12, y2),
            (x1+size6+size12, y2-size6),

            (x1+2*size6+size12, y2-2*size6-size12),
            (x1+2*size6, y1+3*size6),

            (x1+2*size6, y1+size6+size12),
            (x1+3*size6, y1+size6),
            (x1+3*size6+size12, y1+size12),
            (x1+3*size6+size12, y1+size6),
            (x1+4*size6, y1+size6),
            (x2-size6, y1+2*size6+size12),
            (x2-size6-size12, y1+3*size6),
            (x2-2*size6-size12, y1+3*size6),
            (x2-2*size6, y2-2*size6-size12),
            (x2-size6-size12, y2-size6),
            (x2-size6-size12, y2),
        ]
    #création des partie du pion
        darkcolor = '#%02x%02x%02x' % (self.RGB[0]-25, self.RGB[1]-25, self.RGB[2]-25)
        tag = self.ID+' '+self.tag
        self.Pion += [
            self.master.create_polygon(pts, fill=self.color, tags=tag, outline='black'),
            self.master.create_polygon((x1+size6+size12, y2), (x1+size6+size12, y2-size6), (x2-size6-size12, y2-size6), (x2-size6-size12, y2), fill=darkcolor, tags=tag, outline='black'),
            self.master.create_polygon((x1+2*size6+size12, y2-2*size6-size12), (x1+2*size6, y1+3*size6), (x1+2*size6, y1 + size6+size12),(x1+3*size6, y1+size6), (x1+2*size6+size12, y1+size6+size12), fill=darkcolor, tags=tag, outline='black'),
        ]


class Roi_Echec(Piece):
    def __init__(self, master, coords, RGB, ID='Roi'):
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
    # identification d'un carré dans les coordonnés: il contiendra le pion
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

    def create(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
    #deux valeurs utiles pour la création du polygon
        size6 = self.size/6  # represente 1/6 de la taille maximum possible
        size12 = self.size/12  # represente 1/12 de la taille maximum possible
    #liste des differents points du polygon
        pts = [
            (x1+size6+size12, y2),
            (x1+size6+size12, y2-size12),
            (x1+2*size6, y2-size12),
            (x1+2*size6+size12, y2-2*size6-size12),
            (x1+2*size6, (y1+y2)/2),
            (x1+2*size6, y1+2*size6+size12),
            (x1+2*size6+size12, y1+2*size6+size12),
            (x1+2*size6, y1+2*size6),
            (x1+2*size6+1.5*size12, y1+2*size6),
            (x1+2*size6+1.5*size12, y1+size6+size12),
            (x1+2*size6+0.5*size12, y1+size6+size12),
            (x1+2*size6+0.5*size12, y1+size6),
            (x1+2*size6+1.5*size12, y1+size6),
            (x1+2*size6+1.5*size12, y1+size12),
            (x1+3*size6+0.5*size12, y1+size12),
            (x1+3*size6+0.5*size12, y1+size6),
            (x1+3*size6+1.5*size12, y1+size6),
            (x1+3*size6+1.5*size12, y1+size6+size12),
            (x1+3*size6+0.5*size12, y1+size6+size12),
            (x1+3*size6+0.5*size12, y1+2*size6),
            (x1+4*size6, y1+2*size6),
            (x1+3*size6+size12, y1+2*size6+size12),
            (x2-2*size6, y1+2*size6+size12),
            (x2-2*size6, (y1+y2)/2),
            (x2-2*size6-size12, y2-2*size6-size12),
            (x2-2*size6, y2-size12),
            (x2-size6-size12, y2-size12),
            (x2-size6-size12, y2),
        ]
    #création des partie du pion
        darkcolor = '#%02x%02x%02x' % (
            self.RGB[0]-25, self.RGB[1]-25, self.RGB[2]-25)
        tag = self.ID+' '+self.tag
        self.Pion += [
            self.master.create_polygon(pts, fill=self.color, tags=tag, outline='black'),
            self.master.create_polygon((x1+2*size6, (y1+y2)/2), (x1+2*size6, (y1+y2)/2-(1/2)*size12), (x2-2*size6,(y1+y2)/2-(1/2)*size12), (x2-2*size6, (y1+y2)/2), fill=darkcolor, tags=tag, outline='black'),
            self.master.create_polygon((x1+2*size6, y2-size12), (x1+2*size6+size12, y2-2*size6-size12), (x2 - 2*size6-size12, y2-2*size6-size12), (x2-2*size6, y2-size12), fill=darkcolor, tags=tag, outline='black'),
        ]


class Dame_Echec(Piece):
    def __init__(self, master, coords, RGB, ID='Roi'):
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
    # identification d'un carré dans les coordonnés: il contiendra le pion
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

    def create(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
    #deux valeurs utiles pour la création du polygon
        size6 = self.size/6  # represente 1/6 de la taille maximum possible
        size12 = self.size/12  # represente 1/12 de la taille maximum possible
    #liste des differents points du polygon
        pts = [
            (x1+size6+size12, y2),
            (x1+size6+size12, y2-size12),
            (x1+2*size6, y2-size12),
            (x1+2*size6+size12, y2-2*size6-size12),
            (x1+2*size6, (y1+y2)/2),
            (x1+2*size6, y1+2*size6+size12),
            (x1+2*size6+size12, y1+2*size6+size12),
            (x1+2*size6, y1+2*size6),
            (x1+2*size6, y1+size6+0.5*size12),
            (x1+2*size6+size12, y1+size6+size12),
            (x2-2*size6-size12, y1+size6+size12),
            (x2-2*size6, y1+size6+0.5*size12),
            (x2-2*size6, y1+2*size6),
            (x2-2*size6-size12, y1+2*size6+size12),
            (x2-2*size6, y1+2*size6+size12),
            (x2-2*size6, (y1+y2)/2),
            (x2-2*size6-size12, y2-2*size6-size12),
            (x2-2*size6, y2-size12),
            (x2-size6-size12, y2-size12),
            (x2-size6-size12, y2),
        ]
    #création des partie du pion
        darkcolor = '#%02x%02x%02x' % (self.RGB[0]-25, self.RGB[1]-25, self.RGB[2]-25)
        tag = self.ID+' '+self.tag
        self.Pion += [
            self.master.create_polygon(pts, fill=self.color, tags=tag, outline='black'),
            self.master.create_oval(x1+2*size6+(3/2)*size12, y1+size6, x2-2*size6-(3/2)*size12, y1+size6+size12, outline='black', fill=self.color, tags=tag),
            self.master.create_polygon((x1+2*size6, (y1+y2)/2), (x1+2*size6, (y1+y2)/2-(1/2)*size12), (x2-2*size6,(y1+y2)/2-(1/2)*size12), (x2-2*size6, (y1+y2)/2), fill=darkcolor, tags=tag, outline='black'),
            self.master.create_polygon((x1+2*size6, y2-size12), (x1+2*size6+size12, y2-2*size6-size12), (x2 - 2*size6-size12, y2-2*size6-size12), (x2-2*size6, y2-size12), fill=darkcolor, tags=tag, outline='black'),
        ]


## Terrain de jeu


class Echiquier:
    def __init__(self, master, x1, y1, x2, y2):
        self.master = master
    #on decide de la taille de l'echiquier(c'est un carré)
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
        self.SizeCase = self.size/8
    # information de chaque cases
        self.Box = {}
    # liste des différents pions du Damier
        self.PionDic = {}
    # mise en place
        self.create()
        self.Pion()

    def create(self):
        #self.master.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='pink')
        x = self.x1
        y = self.y1
        color = 'black'
    #création des cases
        for i in range(8):
            for n in range(8):
                self.master.create_rectangle(
                    x, y, x+self.SizeCase, y+self.SizeCase, fill=color)
                self.Box[(n, i)] = []
                self.Box[(n, i)].append(
                    (x, y, x+self.SizeCase, y+self.SizeCase))
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
    #Aide
        for i in range(8):
            coord = (((self.Box[(i, 0)][0][0]+self.Box[(i, 0)][0][2])/2),
                     ((self.Box[(i, 0)][0][1]+self.Box[(i, 0)][0][3])/2)-self.SizeCase)
            self.master.create_text(
                coord[0], coord[1], text=str(i), fill='white')
        for i in range(8):
            coord = (((self.Box[(0, i)][0][0]+self.Box[(0, i)][0][2])/2)-self.SizeCase,
                     ((self.Box[(0, i)][0][1]+self.Box[(0, i)][0][3])/2))
            self.master.create_text(
                coord[0], coord[1], text=str(i), fill='white')

    def Pion(self):
    # mise en place des pions blancs
        # Pions
        color = 'white'
        RGB = (225, 225, 225)
        for n in range(8):
            ID = "Pion "+color+" "+str(n)
            self.PionDic[ID] = Pion_Echec(
                self.master, self.Box[(n, 1)][0], RGB, ID)
            self.Box[(n, 1)][1] = ID
        # Tours
        position = [0, 7]
        for n in range(len(position)):
            ID = "Tour "+color+" "+str(n)
            self.PionDic[ID] = Tour_Echec(
                self.master, self.Box[(position[n], 0)][0], RGB, ID)
            self.Box[(position[n], 0)][1] = ID
        # Fou
        position = [1, 6]
        for n in range(len(position)):
            ID = "Fou "+color+" "+str(n)
            self.PionDic[ID] = Fou_Echec(
                self.master, self.Box[(position[n], 0)][0], RGB, ID)
            self.Box[(position[n], 0)][1] = ID
        # Cavalier
        position = [2, 5]
        for n in range(len(position)):
            ID = "Cavalier "+color+" "+str(n)
            self.PionDic[ID] = Cavalier_Echec(
                self.master, self.Box[(position[n], 0)][0], RGB, ID)
            self.Box[(position[n], 0)][1] = ID
        # Reine
        ID = "Reine "+color+' 0'
        self.PionDic[ID] = Dame_Echec(
            self.master, self.Box[(3, 0)][0], RGB, ID)
        self.Box[(3, 0)][1] = ID
        # Roi
        ID = "Roi "+color+' 0'
        self.PionDic[ID] = Roi_Echec(self.master, self.Box[(4, 0)][0], RGB, ID)
        self.Box[(4, 0)][1] = ID
    # mise en place des pions noirs
        color = 'black'
        RGB = (55, 55, 55)
        # Pion
        for n in range(8):
            ID = "Pion "+color+" "+str(n)
            self.PionDic[ID] = Pion_Echec(
                self.master, self.Box[(n, 6)][0], RGB, ID)
            self.Box[(n, 6)][1] = ID
        # Tour
        position = [0, 7]
        for n in range(len(position)):
            ID = "Tour "+color+" "+str(n)
            self.PionDic[ID] = Tour_Echec(
                self.master, self.Box[(position[n], 7)][0], RGB, ID)
            self.Box[(position[n], 7)][1] = ID
        # Fou
        position = [1, 6]
        for n in range(len(position)):
            ID = "Fou "+color+" "+str(n)
            self.PionDic[ID] = Fou_Echec(
                self.master, self.Box[(position[n], 7)][0], RGB, ID)
            self.Box[(position[n], 7)][1] = ID
        # Cavalier
        position = [2, 5]
        for n in range(len(position)):
            ID = "Cavalier "+color+" "+str(n)
            self.PionDic[ID] = Cavalier_Echec(
                self.master, self.Box[(position[n], 7)][0], RGB, ID)
            self.Box[(position[n], 7)][1] = ID
        # Reine
        ID = "Reine "+color+' 0'
        self.PionDic[ID] = Dame_Echec(
            self.master, self.Box[(3, 7)][0], RGB, ID)
        self.Box[(3, 7)][1] = ID
        # Roi
        ID = "Roi "+color+' 0'
        self.PionDic[ID] = Roi_Echec(self.master, self.Box[(4, 7)][0], RGB, ID)
        self.Box[(4, 7)][1] = ID
