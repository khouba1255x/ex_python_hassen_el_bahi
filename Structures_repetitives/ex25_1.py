# Dans cette vidéo, nous allons écrire un programme qui demande un nombre de départ, et qui ensuite affiche les dix nombres suivants en utilisant la boucle for. 
# Par exemple, si l'utilisateur entre le nombre 33, le programme affichera les nombres de 34 à 43.

# Procedure saisier : 

def saisie() :
    x = int(input("Donner un nombre  :  "))
    return(x)
    
# Fonction repeter :

def repeter(x) : 
    for i in range (10) : 
        x = x+1
        print(str(i+1)," =",x)

# Algorithme pricipale :

nb = saisie()
repeter(nb)