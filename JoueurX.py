from Joueur import Joueur


class JoueurX(Joueur):
    def __init__(self, score, nom, symboleX):
        Joueur.__init__(self, score, nom)
        self.symboleX = symboleX

    def joueurXSymboleX(self):
        print(self.nom, "vous avez le symbole :", self.symboleX)

    def saisieJoueurX(self):

        saisieJoueurX = input(f"""Joueur : {self.nom}
        Votre symbole est : {self.symboleX} 
        Veuillez mettre vos coordonnées""")
        return saisieJoueurX


