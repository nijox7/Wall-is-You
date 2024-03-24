from modele import*
from vue import*

#INITIALISATION
f = "game_files/maps/map_test.txt"
f = menu() #Ouvre le menu du choix de niveaux
if f != "":
    donjon, position, dragons = charge_fichier(f)
    aventurier = Aventurier(position, 1)
    chemin = []
    dessine_niveau(donjon, dragons, aventurier)


while f!= "" and not gagne(dragons):
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "Quitte":
        break

    elif tev == "ClicGauche": 
        # Pivote la case sur laquelle on clique
        j, i = donne_position(donjon, abscisse(ev), ordonnee(ev))
        pivoter(donjon, (i, j))
        efface("chemin")
        dessine_portes(donjon, (i, j))

    elif tev == "ClicDroit":
        # Cherche le chemin vers le dragon le plus haut niveau
        chemin = intention(donjon, aventurier.position, dragons)
        dessine_chemin(donjon, chemin)

    elif tev == "Touche":
        nom_touche = touche(ev)
        
        if nom_touche == "space":
            print("oui")
            # L'aventurier affronte le dragon
            if chemin != []:
                if not combat(dragons, aventurier, chemin):
                    print("PERDU")
                    break
                dessine_niveau(donjon, dragons, aventurier)
                chemin = []
                efface("chemin")

        elif nom_touche == "Escape":
            # REVIENS AU MENU
            f = menu()
            if f == "":
                break
            donjon, position, dragons = charge_fichier(f)
            aventurier = Aventurier(position, 1)
            dessine_niveau(donjon, dragons, aventurier)
            chemin = []

        elif nom_touche == "r":
            # REINITIALISE LA SALLE
            donjon, position, dragons = charge_fichier(f)
            aventurier = Aventurier(position, 1)
            chemin = []
            dessine_niveau(donjon, dragons, aventurier)

    mise_a_jour()

ferme_fenetre()