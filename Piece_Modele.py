class Piece:
    """
    Cette classe introduit les différentes actions communes à tous les Pions.
    Elle est une sorte de Classe Modèle pour les Pion.
    """
    def __init__(self, master, coords, RGB, ID='Pion'):
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

    def create(self):
        pass

    def delete(self):
        self.master.delete(self.tag)
        self.Pion = []

    def Moveto(self, x, y):
        xmove = x-self.x
        ymove = y-self.y
        for element in self.Pion:
            self.master.move(element, xmove, ymove)
            self.master.tag_raise(element)
        self.x = x
        self.y = y

        self.x1 += xmove
        self.y1 += ymove
        self.x2 += xmove
        self.y2 += ymove
