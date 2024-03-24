from fltk import*
img_dragon = "game_files/media/gengar2.png"
img_knight = "game_files/media/pikachu.png"
fichier = open("parametres.txt", "r", encoding="utf-8")
parametres = fichier.read().splitlines()
largeur, hauteur = int(parametres[0]), int(parametres[1])
moyenne = (largeur + hauteur) // 2
k = moyenne/30
cree_fenetre(largeur, hauteur)
rectangle(0, 0, largeur, hauteur, remplissage="white")


def menu():
    ''' Menu de choix de niveau '''

    efface_tout()
    
    image(largeur//2, hauteur//2, 'game_files/media/fond3.png', hauteur=1500, largeur=2000, tag="fond")
    texte(largeur/2, hauteur/6,
              "Wall Is You", couleur="red", ancrage="center", taille="50")

    rectangle(largeur/3, hauteur*0.4 - 40, largeur-largeur/3, hauteur*0.4 + 40, remplissage="darkred")
    texte(largeur/2, hauteur*0.4, "Map 1", ancrage="center", taille="40")

    rectangle(largeur/3, hauteur*0.5 - 40, largeur-largeur/3, hauteur*0.5 + 40, remplissage="darkred")
    texte(largeur/2, hauteur*0.5, "Map 2", ancrage="center", taille="40")

    rectangle(largeur/3, hauteur*0.6 - 40, largeur-largeur/3, hauteur*0.6 + 40, remplissage="darkred")
    texte(largeur/2, hauteur*0.6, "Map 3", ancrage="center", taille="40")

    rectangle(largeur/3, hauteur*0.7 - 40, largeur-largeur/3, hauteur*0.7 + 40, remplissage="darkred")
    texte(largeur/2, hauteur*0.7, "Map 4", ancrage="center", taille="40")
    
    f = "game_files/maps/map_test.txt"

    while True:
        ev = donne_ev()
        tev = type_ev(ev)

        if tev == "Quitte":
            return ""

        elif tev == "ClicGauche" :
            if abscisse(ev) >= largeur/3 and abscisse(ev) <= largeur-largeur/3 :
                if ordonnee(ev) >= hauteur*0.4 - 40 and ordonnee(ev) <= hauteur*0.4 + 40 :
                    f = "game_files/maps/map1.txt"
                    break
                if ordonnee(ev) >= hauteur*0.5 - 40 and ordonnee(ev) <= hauteur*0.5 + 40 :
                    f = "game_files/maps/map2.txt"
                    break
                if ordonnee(ev) >= hauteur*0.6 - 40 and ordonnee(ev) <= hauteur*0.6 + 40 :
                    f = "game_files/maps/map3.txt"
                    break
                if ordonnee(ev) >= hauteur*0.7 - 40 and ordonnee(ev) <= hauteur*0.7 + 40 :
                    f = "game_files/maps/map4.txt"
                    break

        mise_a_jour()

    efface_tout()
    image(largeur//2, hauteur//2, 'game_files/media/fond3.png', hauteur=1500, largeur=2000, tag="fond")
    return f


def dessine_donjon(donjon, dragons, aventurier):
    ''' Dessine tout le donjon '''
    for i in range(len(donjon)):
        for j in range(len(donjon[i])):
            if donjon[i][j] != []:
                dessine_portes(donjon, (i,j))

def dessine_portes(donjon, position):
    ''' Dessine une salle en fonction des portes salle '''
    (i,j) = position
    x0, y0 = j * (largeur/len(donjon)), i * (hauteur/len(donjon[0]))
    x1, y1 = (j+1) * (largeur/len(donjon)), (i+1) * (hauteur/len(donjon[0]))
    n = 0

    for porte in donjon[i][j]:
        efface("p"+str(n)+str(i)+str(j))
        couleur = "black"

        if porte:
            if n == 0:
                rectangle(x0, y0, x0+k, y0+k, couleur=couleur, remplissage=couleur, tag="p0"+str(i)+str(j))
                rectangle(x1-k, y0, x1, y0+k, couleur=couleur, remplissage=couleur, tag="p0"+str(i)+str(j))
            elif n == 1:
                rectangle(x1-k, y0, x1, y0+k, couleur=couleur, remplissage=couleur, tag="p1"+str(i)+str(j))
                rectangle(x1-k, y1-k, x1, y1, couleur=couleur, remplissage=couleur, tag="p1"+str(i)+str(j))
            elif n == 2:
                rectangle(x0, y1-k, x0+k, y1, couleur=couleur, remplissage=couleur, tag="p2"+str(i)+str(j))
                rectangle(x1-k, y1-k, x1, y1, couleur=couleur, remplissage=couleur, tag="p2"+str(i)+str(j))
            elif n == 3:
                rectangle(x0, y0, x0+k, y0+k, couleur=couleur, remplissage=couleur, tag="p3"+str(i)+str(j))
                rectangle(x0, y1-k, x0+k, y1, couleur=couleur, remplissage=couleur, tag="p3"+str(i)+str(j))

        else:
            if n == 0:
                rectangle(x0, y0, x0+k, y0+k, couleur=couleur, remplissage=couleur, tag="p0"+str(i)+str(j))
                rectangle(x0+k, y0, x1-k, y0+k/2, couleur=couleur, remplissage=couleur, tag="p0"+str(i)+str(j))
                rectangle(x1-k, y0, x1, y0+k, couleur=couleur, remplissage=couleur, tag="p0"+str(i)+str(j))
            elif n == 1:
                rectangle(x1-k, y0, x1, y0+k, couleur=couleur, remplissage=couleur, tag="p1"+str(i)+str(j))
                rectangle(x1-k/2, y0+k, x1, y1-k, couleur=couleur, remplissage=couleur, tag="p1"+str(i)+str(j))
                rectangle(x1-k, y1-k, x1, y1, couleur=couleur, remplissage=couleur, tag="p1"+str(i)+str(j))
            elif n == 2:
                rectangle(x0, y1-k, x0+k, y1, couleur=couleur, remplissage=couleur, tag="p2"+str(i)+str(j))
                rectangle(x0+k, y1-k/2, x1-k, y1, couleur=couleur, remplissage=couleur, tag="p2"+str(i)+str(j))
                rectangle(x1-k, y1-k, x1, y1, couleur=couleur, remplissage=couleur, tag="p2"+str(i)+str(j))
            elif n == 3:
                rectangle(x0, y0, x0+k, y0+k, couleur=couleur, remplissage=couleur, tag="p3"+str(i)+str(j))
                rectangle(x0, y0-k, x0+k/2, y1-k, couleur=couleur, remplissage=couleur, tag="p3"+str(i)+str(j))
                rectangle(x0, y1-k, x0+k, y1, couleur=couleur, remplissage=couleur, tag="p3"+str(i)+str(j))
        n += 1


def dessine_image(donjon, position, path, tag):
    ''' Dessine une image à une position donnée '''
    (i,j) = position
    x0, y0 = j * (largeur/len(donjon)), i * (hauteur/len(donjon[0]))
    x1, y1 = (j+1) * (largeur/len(donjon)), (i+1) * (hauteur/len(donjon[0]))
    image(x0 + (x1 - x0)//2, y0 + (y1 - y0)//2, path, hauteur=int(k*2), largeur=int(k*2), tag=tag)


def dessine_aventurier(donjon, position):
    ''' Dessine l'aventurier '''
    efface("aventurier")
    dessine_image(donjon, position, img_knight, "aventurier")


def dessine_dragons(donjon, dragons):
    ''' Dessine les dragons du donjon '''
    efface("dragon")
    for i in range(len(dragons)):
        for j in range(len(dragons[i])):
            dragon = dragons[i][j]
            if dragon != "":
                position = dragon.position
                dessine_image(donjon, position,
                              "game_files/media/gengar" + str(dragon.niveau) + ".png", "dragon")
#                 dessine_image(donjon, position,
#                               "game_files/media/gengar.png", "dragon")


def dessine_chemin(donjon, chemin):
    ''' Dessine le chemin que veut prendre l'aventurier '''
    efface("chemin")
    if chemin != []:
        n = 0
        while n != len(chemin)-1:
            (i,j) = chemin[n]
            x0, y0 = j * (largeur/len(donjon)), i * (hauteur/len(donjon[0]))
            x1, y1 = (j+1) * (largeur/len(donjon)), (i+1) * (hauteur/len(donjon[0]))
            xf_1, yf_1 = x0 + (x1 - x0)//2, y0 + (y1 - y0)//2
                
            (i,j) = chemin[n+1]
            x0, y0 = j * (largeur/len(donjon)), i * (hauteur/len(donjon[0]))
            x1, y1 = (j+1) * (largeur/len(donjon)), (i+1) * (hauteur/len(donjon[0]))
            xf_2, yf_2 = x0 + (x1 - x0)//2, y0 + (y1 - y0)//2
            
            ligne(xf_1, yf_1, xf_2, yf_2, 'darkred', k/3, tag="chemin")
            n += 1


def donne_position(donjon, abscisse, ordonnee):
    ''' Renvoie la case correspondant au couple de coordonnées abscisse/ordonnée '''
    return int(abscisse // (largeur/len(donjon[0]))), int(ordonnee // (hauteur/len(donjon)))


def dessine_niveau(donjon, dragons, aventurier):
    ''' Dessine tous les composants d'un niveau '''
    dessine_donjon(donjon, dragons, aventurier)
    dessine_aventurier(donjon, aventurier.position)
    dessine_dragons(donjon, dragons)