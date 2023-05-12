# Dans cette vidéo, nous allons écrire un programme qui demande à l'utilisateur de saisir une année et qui vérifie s'elle est bissextile (366 jours) ou non.

# Procedure donner : 

def donner() :
    x = int(input("Donner une annee pour varifier : "))
    while not( x>0) : 
        x = int(input("Donner une annee pour varifier : "))
    return(x)

# fonction bissextille : 

def bissextille(x) : 
    if x % 4 ==0 :
        message = " est bissextille "
    else :
        message = "n'est pas bissextille"
    return(message)

# Procedure affichier :

def affichier() :
    print("L'annee {:d} {:s}".format(anne, bissextille(anne)))

# Algorithme pricipale :

anne = donner()
ms = affichier()