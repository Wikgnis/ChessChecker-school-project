## Import

from tkinter import *
import os
import winsound

from Dame import *
from Echec import *

## Class

class ChessCheckerGUI:
    def __init__(self, master, Fullscreen=False, Debug=False, width=800, height=800):
    # configuration des info de la fenetre
        self.master = master
        master.title('- ChessChecker -')
        
        if Fullscreen : 
            master.attributes("-fullscreen", 1)
            self.width = master.winfo_screenwidth()
            self.height = master.winfo_screenheight()
        else:
            self.width = width
            self.height = height
        
        # EspaceDeJeu
        # x1jeu, x2jeu
        # y1jeu, y2jeu

        if self.width > self.height*(6/8):
            self.EspaceDeJeu = self.height*(6/8)
        else:
            self.EspaceDeJeu = self.width
        self.x1jeu = (self.width - self.EspaceDeJeu)/2
        self.y1jeu = (self.height - self.EspaceDeJeu)/2
        self.x2jeu = self.x1jeu + self.EspaceDeJeu
        self.y2jeu = self.y1jeu + self.EspaceDeJeu

        # importation des images
        self.img1 = PhotoImage(file=str(os.path.dirname(__file__))+"\\images\\menu.gif")
        self.img2 = PhotoImage(file=str(os.path.dirname(__file__))+"\\images\\jouer.gif")
        self.img3 = PhotoImage(file=str(os.path.dirname(__file__))+"\\images\\credit.gif")
        self.img4 = PhotoImage(file=str(os.path.dirname(__file__))+"\\images\\quitter.gif")
        self.img5 = PhotoImage(file=str(os.path.dirname(__file__))+"\\images\\go.gif")
        self.img6 = PhotoImage(file=str(os.path.dirname(__file__))+"\\images\\table.gif")
    # Menu toujours visible
        # Création des éléments de ce menu
        self.can = Canvas(self.master, width=self.width, height=self.height, bg='black')
        # Affichage des éléments
        self.can.grid(column=0, row=0, rowspan=4, columnspan=3)
        
        
        # Mise en place du fond d'écran
        self.bg = self.can.create_image(self.width/2, self.height/2, image=self.img1, tags='background')
    # Menu de démarrage
        # Création des éléments de ce menu
        self.jouer = Button(self.master, image=self.img2, command=self.Choix_menu)
        self.credit = Button(self.master, image=self.img3, command=self.Credit)
        self.quitter = Button(self.master, image=self.img4, command=self.master.destroy)
        #Créeation du bouton musique
        self.active = IntVar()
        self.musique = Checkbutton(self.master, text="Musique", height=2, width=10, fill='', variable=self.active, command=self.Musique)
        #Création du titre
        self.titre = self.can.create_text(200,75, text="Chess", font='Aharoni 100', fill="#c3a276", tags='titre')
        self.titre2 = self.can.create_text(300,200, text="Checkers", font='Aharoni 100', fill="#c3a276", tags='titre')
        
        self.MenuStart_Grid()
    # Binding
        self.can.bind('<Button-1>', func=self.PointerPress)
        self.can.bind('<ButtonRelease-1>', func=self.PointerRelease)
        self.can.bind('<Motion>', func=self.PointerMotion)
    # Variables
        # Choix du mode de jeu
        self.Gamemode = "none"
        # Variable tour joueur
        self.PlayerColor = 'white'
        # Variable Jeu
        self.Echec = {}
        self.Echec['white'] = False
        self.Echec['black'] = False
        self.GameEnded = False
        # Variables binding
        self.Selection = False
        self.ObjetCible = ''
        self.cache = object
        # Variables Mouvement objets
        self.start = ()
        # Debug
        if Debug : self.Debug = True
        else: self.Debug = False

# Regles    
    def ReglesRespect(self, Game, CoordsObj, CoordsCase):
        self.Echec['white'] = False
        self.Echec['black'] = False
    # Echec
        if Game == 'Chess':
            if 'Pion' in self.ObjetCible:
                Coup, Elimination = self.DeplacementPionEchec(CoordsObj)[0], self.DeplacementPionEchec(CoordsObj)[1]
            elif 'Tour' in self.ObjetCible:
                Coup, Elimination = self.DeplacementTour(CoordsObj)[0], self.DeplacementTour(CoordsObj)[1]
            elif 'Fou' in self.ObjetCible:
                Coup, Elimination = self.DeplacementFou(CoordsObj)[0], self.DeplacementFou(CoordsObj)[1]
            elif 'Cavalier' in self.ObjetCible:
                Coup, Elimination = self.DeplacementCavalier(CoordsObj)[0], self.DeplacementCavalier(CoordsObj)[1]
            elif 'Reine' in self.ObjetCible:
                Coup = self.DeplacementTour(CoordsObj)[0]+self.DeplacementFou(CoordsObj)[0]
                Elimination = self.DeplacementTour(CoordsObj)[1]+self.DeplacementFou(CoordsObj)[1]
            elif 'Roi' in self.ObjetCible:
                Coup, Elimination = self.DeplacementRoi(CoordsObj)[0], self.DeplacementRoi(CoordsObj)[1]
    # Dame
        elif Game == 'Checker':
            if 'Pion' in self.ObjetCible:
                if self.Damier.Box[CoordsCase][1] == 'black':
                    Coup, Elimination = self.DeplacementPion(CoordsObj)[0], self.DeplacementPion(CoordsObj)[1]
            elif 'Dame' in self.ObjetCible:
                if self.Damier.Box[CoordsCase][1] == 'black':
                    Coup, Elimination = self.DeplacementDame(CoordsObj)[0], self.DeplacementDame(CoordsObj)[1]
    # test si le coup est valide
        print('\n\nTest coup valide: \nCoup: ', Coup,', Case: ', CoordsCase)
        if CoordsCase in Coup:
            if self.Debug : print('Case in Coup')
        # Dame
            if Game == 'Checker':
                index  = Coup.index(CoordsCase)
                self.Damier.Box[CoordsObj][2] = ''
                self.Damier.Box[CoordsCase][2] = self.ObjetCible
                if Elimination[index] != '':
                    ID = self.Damier.Box[Elimination[index]][2]
                    self.Damier.Box[CoordsCase][2] = ''
                    self.Damier.Box[Elimination[index]][2] = ''
                    self.Damier.PionDic[ID].delete()       
        # Echec
            else:
                if 'Pion' in self.ObjetCible:
                    if not self.Echiquier.PionDic[self.ObjetCible].Moved:
                        self.Echiquier.PionDic[self.ObjetCible].Moved = True
                        if self.Debug:print(self.ObjetCible,'deplacé: ', self.Echiquier.PionDic[self.ObjetCible].Moved)
                if self.Debug:print('Coup possibles: ', Coup,', Eliminations disponibles: ', Elimination)
                index = Coup.index(CoordsCase)
                if Elimination[index] != '':
                    self.Echiquier.PionDic[self.Echiquier.Box[CoordsCase][1]].delete()
        #return True    
            return True
        
    def DetectionEchec(self):
        if self.Debug : print('\n\nFunc : DetectionEchec\nCoordsObj: ')
    # Variables
        Echecs = []
        Roi = ('Roi white 0', 'Roi black 0')
        if self.PlayerColor == 'white':
            Roi = Roi[0]
        else:
            Roi = Roi[1]
        x = (self.Echiquier.PionDic[Roi].x  -self.x1jeu)
        y = (self.Echiquier.PionDic[Roi].y - self.y1jeu)
        coordx = x//self.Echiquier.SizeCase
        coordy = y//self.Echiquier.SizeCase
        coords = (coordx, coordy)
        if self.Debug : print('Coords: ', coords)
        Echec.append(self.DeplacementCavalier[0])
        Echec.append(self.DeplacementFou[0])
        Echec.append(self.DeplacementTour[0])


    # Detection
# Deplacements
    def DeplacementPionEchec(self, CoordsObj):
        if self.Debug : print('\n\nFunc : DeplacementPionEchec\nCoordsObj: ', CoordsObj)
    # Variables
        CoupDeplacement = []
        CoupAttaque = []
        Elimination = ()
    # Creation des coups possibles sans manger de Pion
        if not self.Echiquier.PionDic[self.ObjetCible].Moved:
            if self.Debug:print('Premier déplacement de: ', self.ObjetCible)
            for i in range(1,3):
                if self.PlayerColor == 'white':
                    CoupDeplacement.append((CoordsObj[0], CoordsObj[1]+i))
                else:
                    CoupDeplacement.append((CoordsObj[0], CoordsObj[1]-i))
        else:
            if self.Debug:print('Déplacement normal de: ', self.ObjetCible)
            if self.PlayerColor == 'white':
                CoupDeplacement.append((CoordsObj[0], CoordsObj[1]+1))
            else:
                CoupDeplacement.append((CoordsObj[0], CoordsObj[1]-1))
        if self.Debug: print('Coup Déplacement sans Obsatcle: ', CoupDeplacement)
        i = 0
        Obstacle = False
        while i < len(CoupDeplacement) and not Obstacle:
            if self.Echiquier.Box[CoupDeplacement[i]][1] != '':
                if self.Debug:print('Obstacle sur ', CoupDeplacement[i], ': ', self.Echiquier.Box[CoupDeplacement[i]][1])
                CoupDeplacement = CoupDeplacement[:i]
                Obstacle = True
            i += 1
        if self.Debug:print('Coup Déplacement avec Obsatcle: ', CoupDeplacement)
    # Deplacement en fonction des pieces adverses
        if CoordsObj[0] > 0 and CoordsObj[1] > 0 and CoordsObj[1] < 7:
            if self.PlayerColor == 'white':
                temp = 1
            else:
                temp = -1
            CoupAttaque.append((CoordsObj[0]-1, CoordsObj[1]+temp))     
        if CoordsObj[0] < 7 and CoordsObj[1] > 0 and CoordsObj[1] < 7:
            if self.PlayerColor == 'white':
                temp = 1
            else:
                temp = -1
            CoupAttaque.append((CoordsObj[0]+1, CoordsObj[1]+temp))
        
        if self.Debug:print('CoupAttaque possibles avant check: ', CoupAttaque)
        
        popindex = []
        for i in range(len(CoupAttaque)):
            if self.Echiquier.Box[CoupAttaque[i]][1] == "" or self.PlayerColor in self.Echiquier.Box[CoupAttaque[i]][1]:
                if self.Debug : print('Impossible sur ', CoupAttaque[i], ': ', self.Echiquier.Box[CoupAttaque[i]][1],'( temp: ', temp,')')
                popindex.append(i)
        
        temp = 0
        for index in popindex:
            CoupAttaque.pop(index-temp)
            temp += 1
    # Retourne les Coup possibles ainsi que si il y en a les coordonnés des pièces à détruire
        
        Coup = CoupAttaque + CoupDeplacement
        Elimination = CoupAttaque[:] + ['']*len(CoupDeplacement)
        
        if self.Debug:print('CoupAttaque possibles réels: ', CoupAttaque,' Il y a donc Elimination sur: ', Elimination)
        
        return [Coup, Elimination]
        
    def DeplacementTour(self, CoordsObj):
        if self.Debug:print('\n\nFunc : DeplacementTour\nCoordsObj: ', CoordsObj)
    # Variables
        Coup = [[], [], [], []]
        Elimination = [[], [], [], []]
    # Création des Coups possibles de la Tour sans manger de Pion
        for i in range(1, int(CoordsObj[0]+1)):
            Coup[0].append((CoordsObj[0]-i, CoordsObj[1]))
        if self.Debug : print('Coup0: ', Coup[0])
        for i in range(1, int(8-CoordsObj[0])):
            Coup[1].append((CoordsObj[0]+i, CoordsObj[1]))
        if self.Debug : print('Coup1: ', Coup[1])
        for i in range(1, int(CoordsObj[1]+1)):
            Coup[2].append((CoordsObj[0], CoordsObj[1]-i))
        if self.Debug : print('Coup2: ', Coup[2])
        for i in range(1, int(8-CoordsObj[1])):
            Coup[3].append((CoordsObj[0], CoordsObj[1]+i))
        if self.Debug : print('Coup3: ', Coup[3])
    # Deplacement en fonction des pieces adverses
        for i in range(len(Coup)):
            n = 0
            end = False
            while n < len(Coup[i]) and not end:
                if self.Echiquier.Box[Coup[i][n]][1] != '':
                    if self.PlayerColor in self.Echiquier.Box[Coup[i][n]][1]:
                        Coup[i] = Coup[i][:n]
                    else:
                        Coup[i] = Coup[i][:n+1] 
                        Elimination[i].append(Coup[i][n])
                    end = True
                if not end:
                    Elimination[i].append('')
                n += 1
            if self.Debug:print('Coup', i, ' avec Obstacle: ',Coup[i], ', Elimination', i, ': ', Elimination[i])
    # Retourne les Coup possibles ainsi que si il y en a les coordonnés des pièces à détruire
        Coup = Coup[0] + Coup[1] + Coup[2] + Coup[3]
        Elimination = Elimination[0] + Elimination[1] + Elimination[2] + Elimination[3]
        return [Coup, Elimination]

    def DeplacementFou(self, CoordsObj):
        if self.Debug : print('\n\nFunc : DeplacementFou\nCoordsObj: ', CoordsObj)
    # Variables
        Coup = [[], [], [], []]
        Elimination = [[], [], [], []]
    # Création des Coups possibles du Fou sans manger de Pion
        temp = list(CoordsObj)
        while temp[0] > 0 and temp[1] > 0:
            temp[0] -= 1
            temp[1] -= 1
            Coup[0].append((temp[0], temp[1]))
        if self.Debug : print('Coup0: ', Coup[0])
        temp = list(CoordsObj)
        while temp[0] > 0 and temp[1] < 7:
            temp[0] -= 1
            temp[1] += 1
            Coup[1].append((temp[0], temp[1]))
        if self.Debug : print('Coup1: ', Coup[1])
        temp = list(CoordsObj)
        while temp[0] < 7 and temp[1] > 0:
            temp[0] += 1
            temp[1] -= 1
            Coup[2].append((temp[0], temp[1]))
        if self.Debug : print('Coup3: ', Coup[2])
        temp = list(CoordsObj)
        while temp[0] < 7 and temp[1] < 7:
            temp[0] += 1
            temp[1] += 1
            Coup[3].append((temp[0], temp[1]))
        if self.Debug : print('Coup3: ', Coup[3])
    # Deplacement en fonction des pieces adverses
        for i in range(len(Coup)):
            n = 0
            end = False
            while n < len(Coup[i]) and not end:
                if self.Echiquier.Box[Coup[i][n]][1] != '':
                    if self.PlayerColor in self.Echiquier.Box[Coup[i][n]][1]:
                        Coup[i] = Coup[i][:n]
                    else:
                        Coup[i] = Coup[i][:n+1] 
                        Elimination[i].append(Coup[i][n])
                    end = True
                if not end:
                    Elimination[i].append('')
                n += 1
            if self.Debug : print('Coup', i, ' avec Obstacle: ', Coup[i], ', Elimination', i, ': ', Elimination[i])
    # Retourne les Coup possibles ainsi que si il y en a les coordonnés des pièces à détruire
        Coup = Coup[0] + Coup[1] + Coup[2] + Coup[3]
        Elimination = Elimination[0] + Elimination[1] + Elimination[2] + Elimination[3]
        return [Coup, Elimination]

    def DeplacementCavalier(self, CoordsObj):
        if self.Debug:print('\n\nFunc : DeplacementCavalier\nCoordsObj: ', CoordsObj)
    # Variables
        Coup = []
        Elimination = []
    # Création des Coups possibles du Cavalier sans manger de Pion
        if CoordsObj[0] > 1:
            if CoordsObj[1] > 0:
                Coup.append((CoordsObj[0]-2, CoordsObj[1]-1))
            if CoordsObj[1] < 7:
                Coup.append((CoordsObj[0]-2, CoordsObj[1]+1))
        print('Coup: ', Coup)
        if CoordsObj[0]<6:
            if CoordsObj[1] > 0:
                Coup.append((CoordsObj[0]+2, CoordsObj[1]-1))
            if CoordsObj[1] < 7:
                Coup.append((CoordsObj[0]+2, CoordsObj[1]+1))
        print('Coup: ', Coup)
        if CoordsObj[1] > 1:
            if CoordsObj[0] > 0:
                Coup.append((CoordsObj[0]-1, CoordsObj[1]-2))
            if CoordsObj[0] < 7:
                Coup.append((CoordsObj[0]+1, CoordsObj[1]-2))
        print('Coup: ', Coup)
        if CoordsObj[1] < 6:
            if CoordsObj[0] > 0:
                Coup.append((CoordsObj[0]-1, CoordsObj[1]+2))
            if CoordsObj[0] < 7:
                Coup.append((CoordsObj[0]+1, CoordsObj[1]+2))
        print('Coup: ', Coup)
        if self.Debug : print('Coup: ', Coup)
    # Deplacement en fonction des pieces adverses
        popindex = []
        for i in range(len(Coup)):
            if self.Echiquier.Box[Coup[i]][1] == '':
                Elimination.append('')
            elif self.PlayerColor in self.Echiquier.Box[Coup[i]][1]:
                popindex.append(i)
            else:
                Elimination.append(Coup[i][:])
        temp = 0
        for index in popindex:
            Coup.pop(index-temp)
            temp += 1
        if self.Debug : print('Coup: ', Coup, ', Elimination: ', Elimination)
    # Retourne les Coup possibles ainsi que si il y en a les coordonnés des pièces à détruire
        return [Coup, Elimination]
    
    def DeplacementRoi(self, CoordsObj):
        if self.Debug:print('\n\nFunc : DeplacementRoi\nCoordsObj: ', CoordsObj)
    # Variables
        Coup = []
        Elimination = []
    # Création des Coups possibles du Roi sans manger de Pion
        if CoordsObj[0] > 0:
            Coup.append((CoordsObj[0]-1, CoordsObj[1]))
            if CoordsObj[1] > 0:    
                Coup.append((CoordsObj[0]-1, CoordsObj[1]-1))
            if CoordsObj[1] < 7:    
                Coup.append((CoordsObj[0]-1, CoordsObj[1]+1))
        if CoordsObj[0] < 7:
            Coup.append((CoordsObj[0]+1, CoordsObj[1]))
            if CoordsObj[1] > 0:
                Coup.append((CoordsObj[0]+1, CoordsObj[1]-1))
            if CoordsObj[1] < 7:
                Coup.append((CoordsObj[0]+1, CoordsObj[1]+1))
        if CoordsObj[1] < 7:
            Coup.append((CoordsObj[0], CoordsObj[1]+1))
        if CoordsObj[1] > 0:
            Coup.append((CoordsObj[0], CoordsObj[1]-1))
    # Deplacement en fonction des pieces adverses
        popindex = []
        for i in range(len(Coup)):
            if self.Echiquier.Box[Coup[i]][1] == '':
                Elimination.append('')
            elif self.PlayerColor in self.Echiquier.Box[Coup[i]][1]:
                popindex.append(i)
            else:
                Elimination.append(Coup[i][:])
        temp = 0
        for index in popindex:
            Coup.pop(index-temp)
            temp += 1
        if self.Debug : print('Coup: ', Coup, ', Elimination: ', Elimination)
    # Retourne les Coup possibles ainsi que si il y en a les coordonnés des pièces à détruire
        return [Coup, Elimination]

    def DeplacementPion(self, CoordsObj, CoordsInterdits=()):
        if self.Debug:print('\n\nFunc : DeplacementPion\nCoordsObj: ', CoordsObj)
    # Variables    
        Coup = []
        Elimination = ['']*4
    # Creation des 4 déplacement possibles
        if CoordsObj[1] > 0:
            if CoordsObj[0] > 0 and (CoordsObj[0]-1, CoordsObj[1]-1) != CoordsInterdits:
                Coup.append((CoordsObj[0]-1, CoordsObj[1]-1))
            else:
                Coup.append(())
            if CoordsObj[0] < 9 and (CoordsObj[0]+1, CoordsObj[1]-1) != CoordsInterdits:
                Coup.append((CoordsObj[0]+1, CoordsObj[1]-1))
            else:
                Coup.append(())
        else:
            for i in range(2) : Coup.append(())
        if CoordsObj[1] < 9:
            if CoordsObj[0] > 0 and (CoordsObj[0]-1, CoordsObj[1]+1) != CoordsInterdits:
                Coup.append((CoordsObj[0]-1, CoordsObj[1]+1))
            else:
                Coup.append(())
            if CoordsObj[0] < 9 and (CoordsObj[0]+1, CoordsObj[1]+1) != CoordsInterdits:
                Coup.append((CoordsObj[0]+1, CoordsObj[1]+1))
            else:
                Coup.append(())
        else:
            for i in range(2) : Coup.append(())       
    # Correction deplacement en fonction du reste des pièces
        if self.Debug : print('liste de depart: ', Coup)

        for i in range(len(Coup)):

            if self.Debug : print('Coup depart: ', Coup[i])

            if Coup[i] != ():
                if self.Damier.Box[Coup[i]][2] != '':
                    temp = ()

                    if self.Debug : print('In Box: ', self.Damier.Box[Coup[i]][2])

                    if self.PlayerColor in self.Damier.Box[Coup[i]][2]:
                        Coup[i] = ()

                    elif i == 0 and Coup[i][0] > 0 and Coup[i][1] > 0:
                        temp = (Coup[:][i][0]-1, Coup[:][i][1]-1)
                        if self.Damier.Box[temp][2] == '':
                            Elimination[i] = Coup[i]
                            Coup[i] = temp[:]

                    elif i == 1 and Coup[i][0] < 9 and Coup[i][1] > 0:
                        temp = (Coup[:][i][0]+1, Coup[:][i][1]-1)
                        if self.Damier.Box[temp][2] == '':
                            Elimination[i] = Coup[i]
                            Coup[i] = temp[:]

                    elif i == 2 and Coup[i][0] > 0 and Coup[i][1] < 9:
                        temp = (Coup[:][i][0]-1, Coup[:][i][1]+1)
                        if self.Damier.Box[temp][2] == '':
                            Elimination[i] = Coup[i]
                            Coup[i] = temp[:]

                    elif Coup[i][0] < 9 and Coup[i][1] < 9:
                        temp = (Coup[:][i][0]+1, Coup[:][i][1]+1)
                        if self.Damier.Box[temp][2] == '':
                            Elimination[i] = Coup[i]
                            Coup[i] = temp[:]

                    if self.Debug : print('Coup arrivée: ', Coup[i],', Temp: ', temp)

        if self.Debug : print('Coup: ', Coup, '\n Elimination: ', Elimination)
    # Empecher le retour en arriere pour les Pions
        if self.PlayerColor == 'white':
            if Elimination[0] == '':
                Coup[0] = ()
            if Elimination[1] == '':
                Coup[1] = ()
        else:
            if Elimination[2] == '':
                Coup[2] = ()
            if Elimination[3] == '':
                Coup[3] = ()
        if self.Debug : print('Coup arrivée sans retour arriere: ', Coup[i])
    # Retourne les Coup possibles ainsi que si il y en a les coordonnés des pièces à détruire
        return [Coup, Elimination]

    def DeplacementDame(self, CoordsObj, CoordsInterdits=()):  
        if self.Debug : print('\n\nFunc : DeplacementDame\n')
    # Variables    
        Coup = []
        Coord1, Coord2, Coord3, Coord4 = [], [], [], []
        Elimination = ['']*4
    # Creation des 4 déplacement possibles
        temp = list(CoordsObj)
        while temp[0] > 0 and temp[1] > 0:
            temp[0] -= 1
            temp[1] -= 1
            Coord1.append((temp[0], temp[1]))
        temp = list(CoordsObj)
        while temp[0] > 0 and temp[1] < 9:
            temp[0] -= 1
            temp[1] += 1
            Coord2.append((temp[0], temp[1]))
        temp = list(CoordsObj)
        while temp[0] < 9 and temp[1] > 0:
            temp[0] += 1
            temp[1] -= 1
            Coord3.append((temp[0], temp[1]))
        temp = list(CoordsObj)
        while temp[0] < 9 and temp[1] < 9:
            temp[0] += 1
            temp[1] += 1
            Coord4.append((temp[0], temp[1]))
    # Correction deplacement en fonction du reste des pièces
        Coup = [Coord1] + [Coord2] + [Coord3] + [Coord4]
        Elimination = [[""]*len(Coord1)] + [[""]*len(Coord2)] + [[""]*len(Coord3)] + [[""]*len(Coord4)]
        if self.Debug : print('Coup départ: ', Coup, ', Elimination depart: ', Elimination)
        temp = 0
        for i in range(4):
            n = 0
            stop = False
            while n < len(Coup[i]) and not stop:

                if self.Debug:print('Coup: ', Coup[i][n], ', In: ',self.Damier.Box[Coup[i][n]][2])

                if self.Damier.Box[Coup[i][n]][2] != '':
                    if self.PlayerColor in self.Damier.Box[Coup[i][n]][2]:
                        Coup[i] = Coup[i][:n]
                        Elimination[i] = Elimination[i][:n]
                        stop = True
                    elif n+1 < len(Coup[i]) and self.Damier.Box[Coup[i][n+1]][2] == '':
                        Coup[i] = Coup[i][:n+2]
                        Elimination[i] = Elimination[i][:n]
                        Elimination[i].append(Coup[i].pop(n))
                        print('Elimination: ', Coup[i][n])
                        stop = True
                    else:
                        Coup[i] = Coup[i][:n]
                        Elimination[i] = Elimination[i][:n]
                        stop = True
                print(Elimination[i])
                n+=1
        Coup = Coup[0] + Coup[1] + Coup[2] + Coup[3] 
        Elimination = Elimination[0] + Elimination[1] + Elimination[2] + Elimination[3]
        if self.Debug : print('Coup fin: ', Coup,', Elimination Fin: ', Elimination)
    # Retourne les Coup possibles ainsi que si il y en a les coordonnés des pièces à détruire
        return [Coup, Elimination]
# Binding Action

    def PointerPress(self, evt):
        if self.Gamemode != 'none':
            if self.Debug:
                print('\n\nFunc: PointerPress\n')
        # Detecte les elements présents sous le pointeur apres avoir appuyer sur le bouton droit
            TagOrID = self.can.find_overlapping(
                evt.x-1, evt.y-1, evt.x+1, evt.y+1)
            if self.Debug:
                print('All TagOrID', TagOrID)
                print(self.Selection)
        # Detecte si les elements présents sous le pointeur sont des piéces pour jouer
            for element in TagOrID:
                Tag = self.can.gettags(element)
                if self.Debug:print('Tags: ', Tag)
                if len(Tag) > 0 and Tag[0] not in ['', 'current', 'background', 'Box', 'Title'] and not self.Selection:
                    if self.PlayerColor in Tag:
                        if self.Debug : print('\nSelection valide\n')
                        self.ObjetCible = Tag[0]+' '+Tag[1]+' '+Tag[2]
                        if self.Debug:print('Objet Cible: ', self.ObjetCible)
                        self.start = (evt.x, evt.y)
                        self.Selection = True
                        if self.Gamemode == 'Chess':
                            coordsObj = [self.Echiquier.PionDic[self.ObjetCible].x,
                                         self.Echiquier.PionDic[self.ObjetCible].y]
                        else:
                            coordsObj = [self.Damier.PionDic[self.ObjetCible].x,
                                         self.Damier.PionDic[self.ObjetCible].y]
                        self.cache = self.can.create_rectangle(evt.x-self.width/4, evt.y-self.height/4, evt.x+self.width/4, evt.y+self.height/4, outline="")

    def PointerRelease(self, evt):
        if self.Debug:
            print('\n\nFunc: PointerRelease\nSelection: ', self.Selection)

        if self.Selection:
            # Variables
            Game = self.Gamemode
            if Game == 'Chess':
                SizeCase = self.Echiquier.SizeCase
            elif Game == 'Checker':
                SizeCase = self.Damier.SizeCase
            CoordsObj = ((self.start[0]-self.x1jeu)//SizeCase,
                         (self.start[1]-self.y1jeu)//SizeCase)
            SurTerrain = False
            Possible = False
            Deplacement = False
        # Test si le Pion est sur la zone de jeu
            if (evt.x > self.x1jeu
                    and evt.y > self.y1jeu
                    and evt.x < self.x2jeu
                    and evt.y < self.y2jeu
                ):
                SurTerrain = True
                CoordsTest = ((evt.x-self.x1jeu)//SizeCase,
                              (evt.y-self.y1jeu)//SizeCase)
        # Mouvement vers la case valide
            if SurTerrain and self.ReglesRespect(Game, CoordsObj, CoordsTest):
                coords = CoordsTest
                if Game == 'Chess':
                    self.Echiquier.Box[CoordsObj][1] = ''
                    self.Echiquier.Box[coords][1] = self.ObjetCible
                elif Game == 'Checker':
                    self.Damier.Box[CoordsObj][2] = ''
                    self.Damier.Box[coords][2] = self.ObjetCible
                Deplacement = True
        # Sinon retour à la case de départ
            else:
                coords = CoordsObj
        # Mouvement de l'objet
            if Game == 'Chess':
                CoordBox = self.Echiquier.Box[coords][0]
                self.Echiquier.PionDic[self.ObjetCible].Moveto(
                    (CoordBox[0]+CoordBox[2])/2, (CoordBox[1]+CoordBox[3])/2)
            elif Game == 'Checker':
                CoordBox = self.Damier.Box[coords][0]
                self.Damier.PionDic[self.ObjetCible].Moveto(
                    (CoordBox[0]+CoordBox[2])/2, (CoordBox[1]+CoordBox[3])/2)
            # Réinitialisation des variables necessaires au mouvement de l'objet
            self.Selection = False

            if Game == 'Checker':
                if self.PlayerColor == 'white':
                    if coords[1] == 9:
                        self.Damier.PionDic[self.ObjetCible].UpgradeToDame()
                        self.Damier.PionDic[self.Damier.PionDic[self.ObjetCible]
                                            .ID] = self.Damier.PionDic[self.ObjetCible]
                        self.Damier.Box[coords][2] = self.Damier.PionDic[self.Damier.PionDic[self.ObjetCible].ID].ID

                elif coords[1] == 0:
                    self.Damier.PionDic[self.ObjetCible].UpgradeToDame()
                    temp = self.Damier.PionDic[self.ObjetCible].ID
                    self.Damier.PionDic[self.Damier.PionDic[self.ObjetCible]
                                        .ID] = self.Damier.PionDic[self.ObjetCible]
                    self.Damier.Box[coords][2] = self.Damier.PionDic[self.Damier.PionDic[self.ObjetCible].ID].ID

            self.ObjetCible = ''
            # Changement de joueur
            if self.PlayerColor == 'white' and Deplacement:
                self.PlayerColor = 'black'
            elif Deplacement:
                self.PlayerColor = 'white'
    
    def PointerMotion(self, evt):
        if self.Selection:
            if self.Gamemode =='Chess':
                self.Echiquier.PionDic[self.ObjetCible].Moveto(evt.x, evt.y)
            else:
                self.Damier.PionDic[self.ObjetCible].Moveto(evt.x, evt.y)
            coords = self.can.coords(self.cache)
            self.can.move(self.cache, evt.x-coords[0]-self.width/4, evt.y-coords[1]-self.height/4)
# Grid
    def MenuStart_Grid(self):
        
        self.jouer.grid(column=0, row=1, pady=0, sticky='w')
        self.credit.grid(column=0, row=2, sticky='w')
        self.quitter.grid(column=0, row=3, sticky='w')
        self.musique.grid(column=2, row=3, sticky='se')

    def Choix_menu(self):
        
        self.jouer.grid_forget()
        self.quitter.grid_forget()
        self.credit.grid_forget()
        
        self.quitter = Button(self.master, text='Quitter', height=3, width=20, command=self.master.destroy)
        
        
        # Les deux boutons radio pour le choix du mode de jeu
        # self.ChoixJeu est la variable permettant de savoir quel mode de jeu est choisi
        # valeur par defaut self.ChoixJeu est ""
        self.ChoixJeu = StringVar()
        self.Chess = Radiobutton(self.master, text='Chess', font='Aharoni', height=2, width=10, indicatoron=0, variable=self.ChoixJeu, value='Chess')
        self.Checker = Radiobutton(self.master, text='Checker', font='Aharoni', height=2, width=10, indicatoron=0, variable=self.ChoixJeu, value='Checker')
        
        self.ChoixJeu.set('none')

        self.Chess.grid(column=1, row=2)
        self.Checker.grid(column=2, row=2)
        self.quitter.grid(column=1, row=3, sticky='s')
    
        #bouton pour lancer le mode de jeu
        self.go = Button(self.master, image=self.img5, command=self.Play)
        self.go.grid(column=0, row=2, pady=50, sticky='w')
        
    def MenuStart_GridForget(self):
        self.can.delete('background')
        self.can.delete('titre')
        self.go.grid_forget()
        self.Chess.grid_forget()
        self.Checker.grid_forget()
        self.bg = self.can.create_image(self.width/2, self.height/2, image=self.img6, tags='background')
        
    def Musique(self):
        état = self.active.get()
        if état==1:
            winsound.PlaySound(os.path.dirname(__file__)+"\\images\\Musique.wav", winsound.SND_ASYNC)
        else:
            winsound.PlaySound(os.path.dirname(__file__)+"\\images\\Clic.wav", winsound.SND_ASYNC)
            
    def Credit(self):
        self.can.delete('background')
        self.can.delete('titre')
        self.jouer.grid_forget()
        self.credit.grid_forget()
        self.musique.grid_forget()
        
        self.can.create_text(900,75, text="Bruit du clic: https://www.youtube.com/watch?v=2Hywp100_xU", font='Aharoni 25', fill="white")
        self.can.create_text(950,200, text="Musique : https://www.youtube.com/watch?v=ksdnLi8b5Cs&t=9s", font='Aharoni 25', fill="white")
        self.can.create_text(900,325, text="Table en bois : http://www.lesperlesdelunivers.fr/texture-bois/", font='Aharoni 25', fill="white")
        self.can.create_text(950,450, text="Plateau d'échec : https://dzbc.org/chess-wallpaper-for-android.html/3?lang=fr", font='Aharoni 25', fill="white")
        self.can.create_text(950,575, text="Code : LEBOCQ Titouan et HERVIEU Valentin", font='Aharoni 25', fill="white")
        
        
# Action in GUI
    def Play(self):
        Game = self.ChoixJeu.get()
        if Game != "none":
            if Game == "Chess":
                self.MenuStart_GridForget()
                self.Echiquier = Echiquier(self.can, self.x1jeu, self.y1jeu, self.x2jeu, self.y2jeu)
                if self.Debug :
                    print('\n\nTerrain de Jeu:\n')
                    for keyBox in self.Echiquier.Box:                       
                        print(self.Echiquier.Box[keyBox])
                    print('\n')
                    for keyPion in self.Echiquier.PionDic:
                        print(keyPion, ': ', self.Echiquier.PionDic[keyPion])
                    print('\n\n')
            elif Game == "Checker":
                self.MenuStart_GridForget()
                self.Damier = Damier(self.can, self.x1jeu, self.y1jeu, self.x2jeu, self.y2jeu) 
                if self.Debug :
                    print('\n\nTerrain de Jeu:\n')
                    for keyBox in self.Damier.Box:                       
                        print(self.Damier.Box[keyBox])
                    print('\n')
                    for keyPion in self.Damier.PionDic:
                        print(keyPion, ': ', self.Damier.PionDic[keyPion])
                    print('\n\n')
            self.Gamemode = Game
            if self.Debug : print('\n\nMode de Jeu: ', Game,'\n\n')

## Main

Window = Tk()

Game = ChessCheckerGUI(Window, Fullscreen=True, Debug=True)

Window.mainloop()
