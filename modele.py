#CLASSES
class Aventurier():
    def __init__(self, position, niveau):
        self.position = position
        self.niveau = niveau

class Dragon():
    def __init__(self, position, niveau):
        self.position = position
        self.niveau = niveau


#FONCTIONS
def connecte(donjon, p1, p2):
    ''' Vérifie si deux salles sont connectées ou pas '''
    portes1, portes2 = donjon[p1[0]][p1[1]], donjon[p2[0]][p2[1]]
    if p1[0] == p2[0]:
        if p1[1] < p2[1]:
            return portes1[1] and portes2[3]
        else:
            return portes1[3] and portes2[1]
    elif p1[1] == p2[1]:
        if p1[0] < p2[0]:
            return portes1[2] and portes2[0]
        else:
            return portes1[0] and portes2[2]
    return False


def pivoter(donjon, position):
    ''' Pivote une case '''
    t = donjon[position[0]][position[1]].copy()
    t[0], t[1], t[2], t[3] = t[3], t[0], t[1], t[2]
    donjon[position[0]][position[1]] = t.copy()


def Voisines(donjon, position):
    ''' Renvoie les voisines disponibles '''
    voisines = []
    if position[0] > 0:
        voisine = (position[0] - 1, position[1])
        if connecte(donjon, position, voisine):
            voisines.append(voisine)
    if position[1] < len(donjon[position[0]]) - 1:
        voisine = (position[0], position[1] + 1)
        if connecte(donjon, position, voisine):
            voisines.append(voisine)
    if position[0] < len(donjon) - 1:
        voisine = (position[0] + 1, position[1])
        if connecte(donjon, position, voisine):
            voisines.append(voisine)
    if position[1] > 0:
        voisine = (position[0], position[1] - 1)
        if connecte(donjon, position, voisine):
            voisines.append(voisine)
    return voisines


def donne_dragon(dragons, position):
    ''' Renvoie l'objet dragon correspondant à la position '''
    (xy) = position
    return dragons[x][y]


def position_dragons(dragons):
    ''' Renvoie la position de tous les dragons '''
    positions = []
    for i in range(len(dragons)):
        for j in range(len(dragons[i])):
            dragon = dragons[i][j]
            if dragon != "":
                positions.append(dragon.position)
    return positions


# def trouve_dragon(donjon, position, dragons, visite=[]):
#     ''' Renvoie un chemin possible de l'aventurier jusqu'au dragon '''
#     visite.append(position)
#     chemin = []
#     if position in position_dragons(dragons):
#         return [position]
#     voisines = Voisines(donjon, position)
#     for voisine in voisines:
#         if voisine not in visite:
#             if connecte(donjon, position, voisine):
#                 chemin = trouve_dragon(donjon, voisine, dragons, visite)
#                 if chemin != []:
#                     return [position] + chemin
#     return chemin


def trouve_dragon(donjon, position, dragons, visite=[]):
    ''' Renvoie le plus court chemin pour affronter un dragon '''
    voisines = []
    file = []
    file.append([position])
    while file != []:
        lenF = len(file)
        for i in range(lenF):
            voisines = Voisines(donjon, file[0][len(file[0])-1])
            for voisine in voisines:
                if voisine not in visite:
                    file.append(file[0] + [voisine])
            visite += file.pop(0)
        for chemin in file:
            (x,y) = chemin[len(chemin)-1]
            if dragons[x][y] != "":
                return chemin
    return []

def intention(donjon, position, dragons):
    ''' Renvoie le chemin que l'aventurier veut faire '''
    visite, chemin, chemin_f = [], [], []
    nMax = 0
    for i in range(len(dragons)):
        chemin = trouve_dragon(donjon, position, dragons, visite.copy())
        if chemin != []:
            (x,y) = chemin[len(chemin)-1]
            dragon = dragons[x][y]
            visite.append(dragon.position)
            if dragon.niveau > nMax:
                nMax = dragon.niveau
                chemin_f = chemin.copy()
    return chemin_f


def deplace_aventurier(aventurier, dragons, position):
    ''' Déplace l'aventurier et met à jour le donjon '''
    aventurier.position = position
    aventurier.niveau += 1
    (x,y) = position


def combat(dragons, aventurier, chemin):
    ''' Renvoie True si l'aventurier gagne, false sinon '''
    (x,y) = chemin[len(chemin)-1]
    dragon = dragons[x][y]
    if aventurier.niveau < dragon.niveau:
        return False
    dragons[x][y] = ""
    deplace_aventurier(aventurier, dragons, dragon.position)
    return True


def charge_grille(fichier):
    ''' Charge la grille du donjon '''
    grille = []
    salles = {'═': [False, True, False, True], '║': [True, False, True, False],
              '╔': [False, True, True, False], '╗': [False, False, True, True],
              '╚': [True, True, False, False], '╝': [True, False, False, True],
              '╠': [True, True, True, False], '╣': [True, False, True, True],
              '╦': [False, True, True, True], '╩': [True, True, False, True],
              '╨': [True, False, False, False], '╡': [False, False, False, True],
              '╥': [False, False, True, False], '╞': [False, True, False, False],
              '╬': [True, True, True, True]}
    i = 0
    for ligne in fichier:
        if ligne[0] == 'A':
            break
        grille.append([])
        for elem in ligne:
            if elem in salles:
                grille[i].append(salles[elem])
        i += 1 #numéro de ligne augmente
    return grille


def charge_aventurier(fichier):
    ''' Charge la position de l'aventurier '''
    for ligne in fichier:
        if ligne[0] == 'A':
            ligne = ligne.split(" ")
            x, y = int(ligne[1]), int(ligne[2])
            break
    return (x, y)


def charge_dragons(fichier, donjon):
    ''' Charge la liste des dragons '''
    dragons = [["" for _ in range(len(donjon[i]))] for i in range(len(donjon))]
    for ligne in fichier:
        if ligne[0] == 'D':
            ligne = ligne.split(" ")
            x, y, niv = int(ligne[1]), int(ligne[2]), int(ligne[3])
            dragons[x][y] = Dragon((x, y), niv)
    return dragons


def charge_fichier(fichier):
    ''' Charge les données d'une map '''
    #                                                 #
    ## AMELIORATION DE LA GESTION D'ERREURS POSSIBLE ##
    #                                                 #
    fichier = open(fichier, "r", encoding="utf-8")
    fichier = fichier.read().splitlines()
    donjon = charge_grille(fichier)
    position = charge_aventurier(fichier)
    dragons = charge_dragons(fichier, donjon)
    return donjon, position, dragons


def gagne(dragons):
    ''' Vérifie si l'aventurier a gagné en tuant tous les dragons '''
    for ligne in dragons:
        for dragon in ligne:
            if dragon != "":
                return False
    return True