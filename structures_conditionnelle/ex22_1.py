# Dans cette vidéo, nous allons écrire un programme qui vérifie si un nombre est pair ou impair.

# Procedure saisie : 

def saisie() :
    nb = int(input("Donner un positive nombre :  "))
    while not(nb > 0) :
        nb = int(input("Avec plaisir Donner un positive nombre :  "))
    return(nb)

# fonction test : 

def test(nb) : 
    if nb % 2 == 0 :
        print("Le nombre est pair ")
    else : 
        print("Le nombre est impair")

# procedure affichier : 

# def affichier(nb) :
    

# Algorithme pricipale :

nb = saisie()
ms = test(nb)