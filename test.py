# tab = ['0','1','2','3','4','5','6','7','8']

# NEW !

tab = ["x","_","_"],["_","_","_"],["_","_","_"]

def saisie():
    return int(input("Saisir vos coordonées"))

def transfoCoordonée( nombre, symbole,tab):
    # Transforme les cases du tableau de facon plus userfriendly

        while nombre >= 9:
            nombre = int(input("Erreur dans la saisie. Refaire une saisie"))


        if nombre == 0 and tab[0][0] == '_':
            tab[0][0] = symbole
            print("Saisie prise en compte")
            return 1

        elif nombre == 1 and tab[0][1] == '_':
            tab[0][1] = symbole
            print("Saisie prise en compte")
            return 1

        elif nombre == 2 and tab[0][2] == '_':
            tab[0][2] = symbole
            print("Saisie prise en compte")
            return 1

        elif nombre == 3 and tab[1][0] == '_':
            tab[1][0] = symbole
            print("Saisie prise en compte")
            return 1

        elif nombre == 4 and tab[1][1] == '_':
            tab[1][1] = symbole
            print("Saisie prise en compte")
            return 1

        elif nombre == 5 and tab[1][2] == '_':
            tab[1][2] = symbole
            print("Saisie prise en compte")
            return 1

        elif nombre == 6 and tab[2][0] == '_':
            tab[2][0] = symbole
            print("Saisie prise en compte")
            return 1

        elif nombre == 7 and tab[2][1] == '_':
            tab[2][1] = symbole
            print("Saisie prise en compte")
            return 1

        elif nombre == 8 and tab[2][2] == '_':
            tab[2][2] = symbole
            print("Saisie prise en compte")
            return 1
        else:
            return 0
# def verfiSaisie(nb):
#
#     if nb ==1:
#         print("Saisie prise en compte")
#     elif nb == 9:
#         saisie = input("Pas dans la fourchette")
#         return saisie
#
#     elif nb == 0:
#         saisie = input("Case deja prise")
#         return saisie

valeur = transfoCoordonée(9,"x",tab)
# verfiSaisie(valeur)