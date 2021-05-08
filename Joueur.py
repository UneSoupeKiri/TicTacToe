class Joueur:

    def __init__(self, nom, symbole):

        self.nom = nom
        self.symbole = symbole

    def saisieNom(self):
        saisieNom = input("Saisir un nom de Joueur")
        return  saisieNom

    #NEW !
    def transfoCaseTab(self,nombre, symbole, tab):
        # Transforme les cases du tableau de facon plus userfriendly
        while nombre >= 9:
            print("ERREUR DANS LA SAISIE ! Je n'accepte que les nombres entre 0 et 8 inclus")
            nombre = int(input("Veuillez mettre vos coordonnées"))

        if nombre == 0 and tab[0][0] == '_':
            tab[0][0] = symbole
            return tab

        if nombre == 1 and tab[0][1] == '_':
            tab[0][1] = symbole
            return tab

        if nombre == 2 and tab[0][2] == '_':
            tab[0][2] = symbole
            return tab

        if nombre == 3 and tab[1][0] == '_':
            tab[1][0] = symbole
            return tab

        if nombre == 4 and tab[1][1] == '_':
            tab[1][1] = symbole
            return tab

        if nombre == 5 and tab[1][2] == '_':
            tab[1][2] = symbole
            return tab

        if nombre == 6 and tab[2][0] == '_':
            tab[2][0] = symbole
            return tab

        if nombre == 7 and tab[2][1] == '_':
            tab[2][1] = symbole
            return tab

        if nombre == 8 and tab[2][2] == '_':
            tab[2][2] = symbole
            return tab


    def saisieJoueur(self):

        saisieJoueur= int(input(f"""Joueur : {self.nom}
        Votre symbole est : {self.symbole} 
        Veuillez mettre vos coordonnées"""))
        return saisieJoueur


    def victoire(self, score1,score2,score3,matchNul):
        if score1== 1 or score2== 1 or score3== 1:
            print("Joueur 2 vous avez gagné")
            return  1
        elif score1== 0 or score2== 0 or score3== 0:
            print("Joueur 1 vous avez gagné")
            return  2
        elif matchNul==4:
            print("Match NUL !")
            return 4
        else:
            return 3

    def matchNul(self,tab):
        i = 0
        while i < len(tab) - 1:
            if tab[i]=="_":
                i += 1
            else:
                return 3
        return 4

    # ! NEW
    def diag(self,tab):
        # 02 11 20
        # ['.', '.', 'o'] 02
        # ['.', 'o', '.'] 11
        # ['o', '.', '.'] 20
        tab1 = []
        ii = 3
        for i in range(3):
            ii = ii - 1
            tab1.extend(tab[i][ii])
            if tab1.count("o") == 3:
                return 1
            elif tab1.count("x") == 3:
                return 0
            else:
                # 00 11 22
                # ['o', '.', '.'] 00
                # ['.', 'o', '.'] 11
                # ['.', '.', 'o'] 22
                tab2 = []
                for i in range(3):
                    tab2.extend(tab[i][i])
                    if tab2.count("o") == 3:
                        return 1
                    elif tab2.count("x") == 3:
                        return 0
                else:
                    return 3

    # NEW !
    def hori(self,tab):
        # ['o', 'o', 'o'] 00 01 02
        # ['.', '.', '.'] 10 11 12
        # ['.', '.', '.'] 20 21 22

        def scan(tab, index):
            if tab[index].count("o") == 3:
                return 1
            elif tab[index].count("x") == 3:
                return 0

        for i in range(3):
            returnVal = scan(tab, i)
            return returnVal

        return 3
    # NEW !
    def verti(self,tab):
        # ['o', '.', '.'] 00 01 02
        # ['o', '.', '.'] 10 11 12
        # ['o', '.', '.'] 20 21 22
        tab1 = []
        for ii in range(3):
            for i in range(3):
                tab1.extend(tab[i][ii])
                if tab1.count("o") == 3:
                    return 1
                elif tab1.count("x") == 3:
                    return 0
        return 3


