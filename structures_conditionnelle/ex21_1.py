# Dans cette vidéo, nous allons écrire un programme qui demande à l’utilisateur de saisir un nombre puis qui en fonction du nombre saisi :
# – 6 : affiche « le personnage va à droite ».
# – 4 : affiche « le personnage va à gauche ».
# – 8 : affiche « le personnage va en haut ».
# – 2 : affiche « le personnage va en bas ».
# – dans le cas d’un autre caractère, affiche : « erreur de saisie, le personnage ne bouge pas ».

# procedure saisie :

def saisie() :
    nb = int(input("Donner just un chiffre :  "))
    while not(len(str(nb)) == 1) :
        nb = int(input("Donner just un chiffre :  "))
    return(nb)

# fonction message : 

def message (nb) : 
    if nb == 6 :
        print("Le presonnage va à droite")
    elif nb == 4 :
        print("Le presonnage va à gauche")
    elif nb == 8 :
        print("Le presonnage va en haut")
    elif nb == 2 :
        print("Le presonnage va en bas")
    else : 
        print("errur de saisie, le personnege ne bouge pas")

# Procedure afficha
# Algorithme pricipale : 

nb = saisie()
ms = message(nb)