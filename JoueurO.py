from Joueur import Joueur


class JoueurO(Joueur):
    def __init__(self,score,nom,symboleO):
        Joueur.__init__(self,score,nom)
        self.symboleO = symboleO


    def joueurOSymboleO(self):
        print(self.nom,"vous avez le symbole :",self.symboleO)

    def saisieJoueurO(self):

        saisieJoueurO = input(f"""Joueur : {self.nom}
        Votre symbole est : {self.symboleO} 
        Veuillez mettre vos coordonnées""")
        return saisieJoueurO
