from Affichage import Affichage
from Joueur import Joueur


#CREER UNE SEUL CLASSE JOUEUR
# VOIR 2 CONSTRUCTEURS
# FAIRE SAISIE AU LIEU DE "JoueurX .."
# COORDONNEES X / Y

#CREATION DE JOUEURS
cpt = 1
joueur1 = input(f"Joueur {cpt} : Veuillez saisir un nom")
cpt=cpt+1
joueur2 = input(f"Joueur {cpt} : Veuillez saisir un nom")

joueurX = Joueur(joueur1,"x")
joueurO = Joueur(joueur2,"o")
jeux = Affichage()


tab = ["x","_","_"],["_","_","_"],["_","_","_"]
jeux.grille(tab)

#INITIALISATION
victoire = 3
matchNul = 3

while victoire == 3:

    saisieX = joueurX.transfoCaseTab(joueurX.saisieJoueur(),joueurX.symbole,tab)

    jeux.grille(tab)
    matchNul = joueurX.matchNul(tab)
    victoire = joueurX.victoire(joueurX.diag(tab),joueurX.verti(tab),joueurX.hori(tab),matchNul)


    if victoire == 3:
        saisieO = joueurO.transfoCaseTab(joueurO.saisieJoueur(), joueurO.symbole, tab)

        jeux.grille(tab)
        matchNul = joueurO.matchNul(tab)
        victoire = joueurO.victoire(joueurO.diag(tab), joueurO.verti(tab), joueurO.hori(tab), matchNul)




